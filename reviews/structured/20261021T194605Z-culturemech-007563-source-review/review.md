# Source and formulation review: anaerobic_alkaline_ye_medium (CultureMech:007563)

- Review: 20261021T194605Z-culturemech-007563-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:39:57Z
- Finished UTC: 2026-10-21T19:46:05Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated record combines two distinct JCM formulations: JCM993 identity and supplement doses with JCM1076 salt and water amounts. Both maintained contributors remain identifiable. Liquid units, resazurin scale, source-stage preparation and the scoped trace stock also require curation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 355; batch 036 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-five task batches contain 350 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 353 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007563 | data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml | generated | anaerobic_alkaline_ye_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007563 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007563 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch036/355/strict.tsv |
| validate-terms | passed | True | CultureMech:007563 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007563 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007563 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ993api | unavailable | False | CultureMech:007563 | The current optional J993 MediaDive API and its preserved retry returned503. Exact JCM993 and TOGO source content are available, so current recipe differences can be assessed without historical byte-equivalence claims. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007563.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007563.

77 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "950",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 10; Distilled water / 900.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q2",
    "ingredient": "NaCl",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 0; NaCl / 2.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q3",
    "ingredient": "KH2PO4",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 2; KH 2 PO 4 / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q4",
    "ingredient": "NH4Cl",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 1; NH 4 Cl / 1.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q5",
    "ingredient": "K2HPO4",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 3; K 2 HPO 4 / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q6",
    "ingredient": "Resazurin",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 9; Resazurin / 1.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q7",
    "ingredient": "MgCl2・6H2O",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 5; MgCl 2 ·6H 2 O / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q8",
    "ingredient": "KCl",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 4; KCl / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q9",
    "ingredient": "Tris base",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 6; Tris base / 3.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Tris base                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Tris base\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q10",
    "ingredient": "Na2S2O3・5H2O",
    "decision": "correct",
    "stage": "JCM993 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal batch; raw HTML row 7; Na 2 S 2 O 3 ·5H 2 O / 3.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;S&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;3&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2S2O3・5H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q11",
    "ingredient": "Trace stock receiving dose",
    "decision": "correct",
    "stage": "JCM993 basal trace addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 basal trace dose; raw HTML row 8; Trace element solution (see Medium No. 439 ) / 1.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M439])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "The source adds 1 ml of the named JCM439 stock; the existing G_PER_L unit is wrong. Preserve trace composition at stock scope."
  },
  {
    "decision_id": "q12",
    "ingredient": "8% NaHCO3 solution",
    "decision": "correct",
    "stage": "JCM993 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "claim_present": true
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 post-cooling stock dose; raw HTML row 12; 8% NaHCO 3 solution / 30.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q13",
    "ingredient": "8% NaHCO3 solution strength",
    "decision": "add",
    "stage": "JCM993 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 post-cooling stock dose; raw HTML row 12; 8% NaHCO 3 solution / 30.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q14",
    "ingredient": "10% (w/v) Yeast extract solution",
    "decision": "correct",
    "stage": "JCM993 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "claim_present": true
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 post-cooling stock dose; raw HTML row 11; 10% (w/v) Yeast extract solution / 20.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 10% (w/v) Yeast extract solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Yeast extract solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q15",
    "ingredient": "10% (w/v) Yeast extract solution strength",
    "decision": "add",
    "stage": "JCM993 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 post-cooling stock dose; raw HTML row 11; 10% (w/v) Yeast extract solution / 20.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 10% (w/v) Yeast extract solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Yeast extract solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q16",
    "ingredient": "5% Na2S・9H2O solution",
    "decision": "correct",
    "stage": "JCM993 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "claim_present": true
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 post-cooling stock dose; raw HTML row 13; 5% Na 2 S·9H 2 O solution / 8.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q17",
    "ingredient": "5% Na2S・9H2O solution strength",
    "decision": "add",
    "stage": "JCM993 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 post-cooling stock dose; raw HTML row 13; 5% Na 2 S·9H 2 O solution / 8.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a"
      },
      {
        "source_key": "togoM1047original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q18",
    "ingredient": "NaOH quantity and concentration",
    "decision": "not_quantified",
    "stage": "JCM993 initial pH adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 initial pH adjustment; NaOH quantity and concentration",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "VARIABLE preserves the unquantified dose; stock concentration is also unspecified. Add source evidence without an invented amount."
  },
  {
    "decision_id": "q19",
    "ingredient": "Initial pH",
    "decision": "add",
    "stage": "JCM993 before autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 before autoclaving; Initial pH",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "This is an initial adjustment, not the measured final pH. For JCM1076 retain the separate final target around8.2."
  },
  {
    "decision_id": "q20",
    "ingredient": "CO2 post-cooling gas ratio",
    "decision": "correct",
    "stage": "JCM993 after cooling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 after cooling; CO2 post-cooling gas ratio",
        "exact_source_quote": "replace the gas phase with a N 2 -CO 2 (4:1, v/v) gas mixture.",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "Represent the explicit4:1 v/v mixture at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer pressure or whole-medium gas dose."
  },
  {
    "decision_id": "q21",
    "ingredient": "N2 post-cooling gas ratio",
    "decision": "correct",
    "stage": "JCM993 after cooling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 after cooling; N2 post-cooling gas ratio",
        "exact_source_quote": "replace the gas phase with a N 2 -CO 2 (4:1, v/v) gas mixture.",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "Represent the explicit4:1 v/v mixture at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer pressure or whole-medium gas dose."
  },
  {
    "decision_id": "q22",
    "ingredient": "Initial and stock-storage N2 fraction",
    "decision": "not_quantified",
    "stage": "JCM993 sterilization and sterile-stock storage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 sterilization and sterile-stock storage; Initial and stock-storage N2 fraction",
        "exact_source_quote": "autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "N2 is named without a percentage. This differs from the explicitly proportioned post-cooling gas replacement."
  },
  {
    "decision_id": "q23",
    "ingredient": "Source default autoclave cycle",
    "decision": "add",
    "stage": "JCM993 stated default",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 stated default; Source default autoclave cycle",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "Record121 C for15 min only for the exact source autoclaved stages; pressure and stock storage duration are unspecified."
  },
  {
    "decision_id": "q24",
    "ingredient": "Stock handling and order",
    "decision": "add",
    "stage": "JCM993 after cooling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 after cooling; Stock handling and order",
        "exact_source_quote": "Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N 2 atmosphere):",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "Retain the source-specific supplementation after gas replacement and the distinct stock preparation/storage scope."
  },
  {
    "decision_id": "q25",
    "ingredient": "Final measured medium volume",
    "decision": "not_quantified",
    "stage": "JCM993 complete receiving batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 complete receiving batch; Final measured medium volume",
        "exact_source_quote": "Distilled water 900.0 ml",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "Source water and liquid additions are explicit; a measured final volume or make-up instruction is not. Do not normalize batch grams silently or add entire stock preparation volumes."
  },
  {
    "decision_id": "q26",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "950",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "950",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 10; Distilled water / 950.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;950.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 950,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q27",
    "ingredient": "NaCl",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 0; NaCl / 20.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q28",
    "ingredient": "KH2PO4",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 2; KH 2 PO 4 / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q29",
    "ingredient": "NH4Cl",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 1; NH 4 Cl / 1.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q30",
    "ingredient": "K2HPO4",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 3; K 2 HPO 4 / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q31",
    "ingredient": "Resazurin",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 9; Resazurin / 1.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q32",
    "ingredient": "MgCl2・6H2O",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 5; MgCl 2 ·6H 2 O / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q33",
    "ingredient": "KCl",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 4; KCl / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q34",
    "ingredient": "Tris base",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 6; Tris base / 3.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Tris base                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Tris base\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q35",
    "ingredient": "Na2S2O3・5H2O",
    "decision": "correct",
    "stage": "JCM1076 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal batch; raw HTML row 7; Na 2 S 2 O 3 ·5H 2 O / 3.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;S&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;3&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2S2O3・5H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve the exact source batch amount and unit, with no inferred measured final volume. Water is ml and resazurin is mg. The target salt/water values follow JCM1076 despite its JCM993 identity; matching numbers elsewhere do not authenticate G_PER_L or merge equivalence."
  },
  {
    "decision_id": "q36",
    "ingredient": "Trace stock receiving dose",
    "decision": "correct",
    "stage": "JCM1076 basal trace addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 basal trace dose; raw HTML row 8; Trace element solution (see Medium No. 439 ) / 1.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M439])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "The source adds 1 ml of the named JCM439 stock; the existing G_PER_L unit is wrong. Preserve trace composition at stock scope."
  },
  {
    "decision_id": "q37",
    "ingredient": "8% Na2CO3 solution",
    "decision": "correct",
    "stage": "JCM1076 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Trace element solution (see Medium [M439])",
            "composition": [],
            "notes": "Cross-reference to Medium M439",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "8% NaHCO3 solution",
            "composition": [],
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "notes": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "10% (w/v) Yeast extract solution",
            "composition": [],
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "notes": "Role: Nutrient source; Properties: Undefined component",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "5% Na2S・9H2O solution",
            "composition": [],
            "concentration": {
              "value": "8",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          }
        ],
        "claim_present": false
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 13; 8% Na 2 CO 3 solution / 20.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt; solution                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"8% Na2CO3 solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q38",
    "ingredient": "8% Na2CO3 solution strength",
    "decision": "add",
    "stage": "JCM1076 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Trace element solution (see Medium [M439])",
            "composition": [],
            "notes": "Cross-reference to Medium M439",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "8% NaHCO3 solution",
            "composition": [],
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "notes": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "10% (w/v) Yeast extract solution",
            "composition": [],
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "notes": "Role: Nutrient source; Properties: Undefined component",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "5% Na2S・9H2O solution",
            "composition": [],
            "concentration": {
              "value": "8",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 13; 8% Na 2 CO 3 solution / 20.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt; solution                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"8% Na2CO3 solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q39",
    "ingredient": "10% (w/v) Yeast extract solution",
    "decision": "correct",
    "stage": "JCM1076 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "claim_present": true
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 11; 10% (w/v) Yeast extract solution / 10.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 10% (w/v) Yeast extract solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Yeast extract solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q40",
    "ingredient": "10% (w/v) Yeast extract solution strength",
    "decision": "add",
    "stage": "JCM1076 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 11; 10% (w/v) Yeast extract solution / 10.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 10% (w/v) Yeast extract solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Yeast extract solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q41",
    "ingredient": "5% Na2S・9H2O solution",
    "decision": "correct",
    "stage": "JCM1076 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "claim_present": true
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 14; 5% Na 2 S·9H 2 O solution / 6.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 6,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q42",
    "ingredient": "5% Na2S・9H2O solution strength",
    "decision": "add",
    "stage": "JCM1076 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 14; 5% Na 2 S·9H 2 O solution / 6.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 6,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q43",
    "ingredient": "0.5 M Maltose solution",
    "decision": "correct",
    "stage": "JCM1076 post-cooling stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Trace element solution (see Medium [M439])",
            "composition": [],
            "notes": "Cross-reference to Medium M439",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "8% NaHCO3 solution",
            "composition": [],
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "notes": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "10% (w/v) Yeast extract solution",
            "composition": [],
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "notes": "Role: Nutrient source; Properties: Undefined component",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "5% Na2S・9H2O solution",
            "composition": [],
            "concentration": {
              "value": "8",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          }
        ],
        "claim_present": false
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "claim_present": true
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 12; 0.5 M Maltose solution / 20.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 0.5 M Maltose solution                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"0.5 M Maltose solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.5,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Preserve this source-specific ml dose, distinct from the other contributor. Missing target branch constituents require resolving the merged identity; do not add mutually different recipes together. Existing G_PER_L doses are wrong."
  },
  {
    "decision_id": "q44",
    "ingredient": "0.5 M Maltose solution strength",
    "decision": "add",
    "stage": "JCM1076 stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Trace element solution (see Medium [M439])",
            "composition": [],
            "notes": "Cross-reference to Medium M439",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "8% NaHCO3 solution",
            "composition": [],
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "notes": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "10% (w/v) Yeast extract solution",
            "composition": [],
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "notes": "Role: Nutrient source; Properties: Undefined component",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "5% Na2S・9H2O solution",
            "composition": [],
            "concentration": {
              "value": "8",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling stock dose; raw HTML row 12; 0.5 M Maltose solution / 20.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 0.5 M Maltose solution                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2"
      },
      {
        "source_key": "togoM1145original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"0.5 M Maltose solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.5,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f"
      }
    ],
    "interpretation": "Keep stock strength separate from its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies 0.5 M. No mass conversion or final-medium concentration is invented."
  },
  {
    "decision_id": "q45",
    "ingredient": "NaOH quantity and concentration",
    "decision": "not_quantified",
    "stage": "JCM1076 initial pH adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 initial pH adjustment; NaOH quantity and concentration",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "VARIABLE preserves the unquantified dose; stock concentration is also unspecified. Add source evidence without an invented amount."
  },
  {
    "decision_id": "q46",
    "ingredient": "Initial pH",
    "decision": "add",
    "stage": "JCM1076 before autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 before autoclaving; Initial pH",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "This is an initial adjustment, not the measured final pH. For JCM1076 retain the separate final target around8.2."
  },
  {
    "decision_id": "q47",
    "ingredient": "CO2 post-cooling gas ratio",
    "decision": "correct",
    "stage": "JCM1076 after cooling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 after cooling; CO2 post-cooling gas ratio",
        "exact_source_quote": "replace the gas phase with a N 2 -CO 2 (4:1, v/v) gas mixture.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "Represent the explicit4:1 v/v mixture at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer pressure or whole-medium gas dose."
  },
  {
    "decision_id": "q48",
    "ingredient": "N2 post-cooling gas ratio",
    "decision": "correct",
    "stage": "JCM1076 after cooling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 after cooling; N2 post-cooling gas ratio",
        "exact_source_quote": "replace the gas phase with a N 2 -CO 2 (4:1, v/v) gas mixture.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "Represent the explicit4:1 v/v mixture at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer pressure or whole-medium gas dose."
  },
  {
    "decision_id": "q49",
    "ingredient": "Initial and stock-storage N2 fraction",
    "decision": "not_quantified",
    "stage": "JCM1076 sterilization and sterile-stock storage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 sterilization and sterile-stock storage; Initial and stock-storage N2 fraction",
        "exact_source_quote": "autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "N2 is named without a percentage. This differs from the explicitly proportioned post-cooling gas replacement."
  },
  {
    "decision_id": "q50",
    "ingredient": "Source default autoclave cycle",
    "decision": "add",
    "stage": "JCM1076 stated default",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 stated default; Source default autoclave cycle",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "Record121 C for15 min only for the exact source autoclaved stages; pressure and stock storage duration are unspecified."
  },
  {
    "decision_id": "q51",
    "ingredient": "Stock handling and order",
    "decision": "add",
    "stage": "JCM1076 after cooling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 after cooling; Stock handling and order",
        "exact_source_quote": "Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N 2 atmosphere):",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "Retain the source-specific supplementation after gas replacement and the distinct stock preparation/storage scope."
  },
  {
    "decision_id": "q52",
    "ingredient": "Final measured medium volume",
    "decision": "not_quantified",
    "stage": "JCM1076 complete receiving batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 complete receiving batch; Final measured medium volume",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "Source water and liquid additions are explicit; a measured final volume or make-up instruction is not. Do not normalize batch grams silently or add entire stock preparation volumes."
  },
  {
    "decision_id": "q53",
    "ingredient": "JCM1076 final target pH",
    "decision": "add",
    "stage": "JCM1076 after its specific supplementation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 after its specific supplementation; JCM1076 final target pH",
        "exact_source_quote": "Check final pH be around 8.2.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "interpretation": "This final target belongs only to JCM1076. JCM993 does not state a final pH; no transfer between recipes."
  },
  {
    "decision_id": "q54",
    "ingredient": "JCM993 final pH",
    "decision": "not_quantified",
    "stage": "JCM993 after supplementation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm993",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993",
        "source_locator": "JCM993 after supplementation; JCM993 final pH",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a",
        "parsed_text_sha256": "4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d"
      }
    ],
    "interpretation": "Only the pre-autoclave adjustment is given; do not convert it into a final measured value or import JCM1076 final pH."
  },
  {
    "decision_id": "q55",
    "ingredient": "HCl (25%)",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 18; HCl (25%) / 12.5 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; HCl (25%)                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;12.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"HCl (25%)\",\n          \"volume\": 12.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q56",
    "ingredient": "HCl (25%)",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 18; HCl (25%) / 12.5 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; HCl (25%)                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;12.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"HCl (25%)\",\n          \"volume\": 12.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q57",
    "ingredient": "Distilled water",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 27; Distilled water / 987.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;987.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q58",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "988.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 27; Distilled water / 987.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;987.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 987,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q59",
    "ingredient": "Na2MoO4・2H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 26; Na 2 MoO 4 ·2H 2 O / 36.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q60",
    "ingredient": "Na2MoO4・2H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 26; Na 2 MoO 4 ·2H 2 O / 36.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q61",
    "ingredient": "H3BO3",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 20; H 3 BO 3 / 30.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 30,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q62",
    "ingredient": "H3BO3",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 20; H 3 BO 3 / 30.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 30,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q63",
    "ingredient": "FeSO4・7H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 19; FeSO 4 ·7H 2 O / 2.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 2.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q64",
    "ingredient": "FeSO4・7H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 19; FeSO 4 ·7H 2 O / 2.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 2.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q65",
    "ingredient": "MnCl2・4H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 21; MnCl 2 ·4H 2 O / 100.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q66",
    "ingredient": "MnCl2・4H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 21; MnCl 2 ·4H 2 O / 100.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q67",
    "ingredient": "CoCl2・6H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 22; CoCl 2 ·6H 2 O / 190.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q68",
    "ingredient": "CoCl2・6H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 22; CoCl 2 ·6H 2 O / 190.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q69",
    "ingredient": "NiCl2・6H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 23; NiCl 2 ·6H 2 O / 24.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q70",
    "ingredient": "NiCl2・6H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 23; NiCl 2 ·6H 2 O / 24.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q71",
    "ingredient": "ZnSO4・7H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 25; ZnSO 4 ·7H 2 O / 144.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;144.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q72",
    "ingredient": "ZnSO4・7H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "144",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 25; ZnSO 4 ·7H 2 O / 144.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;144.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q73",
    "ingredient": "CuCl2・2H2O",
    "decision": "add",
    "stage": "Receiving trace composition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 24; CuCl 2 ·2H 2 O / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "Represent only the named JCM439 trace-stock constituent and batch amount; no parent basal medium or other referenced stock transfers."
  },
  {
    "decision_id": "q74",
    "ingredient": "CuCl2・2H2O",
    "decision": "correct",
    "stage": "Existing M439 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; raw HTML row 24; CuCl 2 ·2H 2 O / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda"
      },
      {
        "source_key": "togoM439original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c"
      }
    ],
    "interpretation": "The local parent flattens stock batch mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml. Its water also combines separate parent stages. Preserve the exact source basis, not an assumed one-liter concentration."
  },
  {
    "decision_id": "q75",
    "ingredient": "Trace acid strength",
    "decision": "add",
    "stage": "JCM439 trace stock only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; Trace acid strength",
        "exact_source_quote": "HCl (25%) 12.5 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      }
    ],
    "interpretation": "Retain25% and12.5 ml separately; source percentage basis and density are unqualified."
  },
  {
    "decision_id": "q76",
    "ingredient": "Trace final measured volume",
    "decision": "not_quantified",
    "stage": "JCM439 trace stock only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 trace stock only; Trace final measured volume",
        "exact_source_quote": "Distilled water 987.0 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      }
    ],
    "interpretation": "Listed water987 ml plus acid12.5 ml totals999.5 ml, not a measured final volume. The API separately declares1000 ml; retain this provider normalization without rewriting the primary."
  },
  {
    "decision_id": "q77",
    "ingredient": "Provider-declared normalization volumes",
    "decision": "not_quantified",
    "stage": "J1076 main and trace API normalizations",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1007",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "interpretation": "The provider explicitly declares these denominators. They are not independent experimental measurements or an instruction to modify primary batch amounts. Trace input liquids total999.5 ml; main liquids total1007 ml."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:007563.

13 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 13/13 primary and 9/13 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 13: primary 100.00%; secondary 69.23%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Distinct contributor recipes incorrectly merged

identity: concern. Targets: CultureMech:007563.

JCM993/M1047 and JCM1076/M1145 are both exact contributors, not interchangeable synonyms: NaCl2 versus20 g, water900 versus950 ml, bicarbonate versus carbonate, different yeast/sulfide doses and maltose only in JCM1076. The target combines JCM1076 basal values with JCM993 identity/supplements. The specialized namesake is excluded by stable ID and import provenance.

### Named stock scope and API normalization

representation: concern. Targets: CultureMech:007563.

Only JCM439 trace stock transfers, not its parent basal medium, pH7, vessel example, vitamins, lactate or receiving doses. Empty trace stubs and incorrect volume units lose that distinction. Provider normalization volumes remain separate from primary amounts.

### Main and transferred chemical forms

grounding: concern. Targets: CultureMech:007563.

Main hydrate terms and generic resazurin match the source specificity; no unsupported resazurin salt claim is introduced. Transferred M439 cobalt and nickel hexahydrates are grounded to anhydrous CHEBI35696 and34887. Other parent groundings are excluded.

### Preparation, pH stages and gas ratios

completeness: concern. Targets: CultureMech:007563.

All three layers omit initial pH9, exact default autoclave cycle, post-cooling4:1 v/v N2/CO2 and stock handling. JCM1076 final pH around8.2 belongs only to that contributor.

### Mixture classification and growth claims

scope: supported. Targets: CultureMech:007563.

COMPLEX/UNDEFINED and LIQUID fit the yeast-containing sources. Names and generic microbial-cultivation applications do not establish strain growth, taxonomy or interchangeability.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007563.

35 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Two maintained contributors and regeneration

ownership: concern. Targets: CultureMech:007563.

The complete merge event and merged_from resolve two exact maintained inputs with distinct formulations. The generated identity must be resolved without overwriting either source recipe or adopting the excluded namesake.

### Source support and attachment

evidence: concern. Targets: CultureMech:007563.

Current primary/TOGO evidence is available, but target and both owners lack attached amount/preparation evidence. A current source match does not prove historical byte equivalence.

## Findings

### f1: Two distinct recipes form a mixed generated identity

blocker / open / confirmed; issue key: culturemech.007563.distinct-recipes-merged.

Target JCM993 identity/supplementation carries JCM1076 water and salt values; its synonym field implies equivalence unsupported by the exact recipes.

### f2: Liquid units and resazurin scale are wrong

major / open / confirmed; issue key: culturemech.007563.units-and-stage-basis.

All local volume doses are G_PER_L, resazurin1 mg is stored1 G_PER_L, and batch amounts and trace stock fields lack source-stage basis.

### f3: Distinct preparation and gas stages are missing

major / open / confirmed; issue key: culturemech.007563.preparation-ph-gas.

Initial pH9, source default121 C/15 min, post-cooling4:1 v/v gas and JCM1076-only final pH8.2 are absent.

### f4: Transferred trace hydrates use anhydrous identities

major / open / confirmed; issue key: culturemech.007563.trace-hydrate-grounding.

The M439 cobalt and nickel source names are hexahydrates, while the stored primary terms35696 and34887 are anhydrous.

### f5: Claims lack attached source evidence

minor / open / confirmed; issue key: culturemech.007563.claim-evidence.

Accessions and merge histories do not attach exact amounts, stages or preparation support.

## Recommended Actions And Acceptance Checks

### a1

Resolve the merge boundary and retain separate source recipes/variants with exact ownership; then regenerate after source-specific comparisons.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct units and exact batch/stock basis within each separate owner; retain strengths and doses without invented final concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add exact source-scoped handling and gas proportions, preserving unknown pressure, NaOH dose and JCM993 final pH.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Independently resolve hydrate identities before copying parent grounding into receiving trace stocks; preserve source mass amounts.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach narrow literal snippets and exact source locators/hash/times after curation; retain append-only history and distinct contributor sources.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch036/355/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch036/355/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml:1:id: CultureMech:007563<br>./data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml:1:id: CultureMech:007563<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch036/source-preflight-bound/355/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 35 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| jcm993 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993; Complete exact primary formulation and preparation | supports | The source is a distinct recipe and must retain its own quantities and conditions. |
| jcm1076 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076; Complete exact primary formulation and preparation | supports | The source is a distinct recipe and must retain its own quantities and conditions. |
| trace | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439; Trace element solution subsection only | supports | Only this stock transfers; parent basal medium, gas handling, pH, dose timing and other stocks are excluded. |
| togoM1047original | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047; $.meta and complete components/comments | supports | Exact TOGO-to-JCM accession correspondence; these are separate recipes. |
| togoM1145original | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145; $.meta and complete components/comments | supports | Exact TOGO-to-JCM accession correspondence; these are separate recipes. |
| md1076 | https://mediadive.dsmz.de/rest/medium/J1076; $.medium and solutions[*] complete composition/steps | supports | Provider declares main1007 ml and trace1000 ml; normalized g_l values are distinct from original batch amounts. No measured-volume or historical-revision equivalence inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch036/355/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:9754 resolves to tris. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754": [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| scoped-grounding | /private/tmp/culturemech-review-work-batch036/355/grounding-inventory.json; Every asserted target/owner and transferred-stock primary/secondary slot | context_only | All exact labels resolved. Source form correspondence remains separate. |
| chebi35696-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact formula/structure | supports | The asserted term is anhydrous dichloride, whereas the transferred stock source names a hexahydrate. |
| chebi34887-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact formula/structure | supports | The asserted term is anhydrous dichloride, whereas the transferred stock source names a hexahydrate. |
| history-metadata | data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml; data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml", "events": 11, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge fingerprint and field-combination code plus recorded merge provenance are relevant to this mixed target. They do not prove exact historical execution or justify recipe equivalence; maintain each source contributor separately. |
| writer-1 | src/culturemech/merge/fingerprint.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge fingerprint and field-combination code plus recorded merge provenance are relevant to this mixed target. They do not prove exact historical execution or justify recipe equivalence; maintain each source contributor separately. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge fingerprint and field-combination code plus recorded merge provenance are relevant to this mixed target. They do not prove exact historical execution or justify recipe equivalence; maintain each source contributor separately. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge fingerprint and field-combination code plus recorded merge provenance are relevant to this mixed target. They do not prove exact historical execution or justify recipe equivalence; maintain each source contributor separately. |
| writer-4 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge fingerprint and field-combination code plus recorded merge provenance are relevant to this mixed target. They do not prove exact historical execution or justify recipe equivalence; maintain each source contributor separately. |
| mediadiveJ993api-attempt | https://mediadive.dsmz.de/rest/medium/J993; Preserved exact public retrieval result | context_only | The current optional J993 MediaDive API and its preserved retry returned503. Exact JCM993 and TOGO source content are available, so current recipe differences can be assessed without historical byte-equivalence claims. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current optional J993 MediaDive API and its preserved retry returned503. Exact JCM993 and TOGO source content are available, so current recipe differences can be assessed without historical byte-equivalence claims.
- No final measured volume, unqualified percentage basis, gas pressure, incubation temperature or species growth is inferred. Current J1076 API values are explicitly provider-normalized and do not establish historical chronology.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T194605Z-culturemech-007563-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobic_alkaline_ye_medium (CultureMech:007563)'
started_at: '2026-10-21T19:39:57Z'
finished_at: '2026-10-21T19:46:05Z'
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
summary: 'The generated record combines two distinct JCM formulations: JCM993 identity
  and supplement doses with JCM1076 salt and water amounts. Both maintained contributors
  remain identifiable. Liquid units, resazurin scale, source-stage preparation and
  the scoped trace stock also require curation.'
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
  - path: data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
    sha256: 20cff8b332f4526c7b9a07645112345a1e5a4d7236567e76f90f09bb9a071c38
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    sha256: d89bacd332c1f11200e53cf7b125553599b1b5b90d1c076fba890f382ffb172d
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    sha256: 61b72e39e60ca8f44e869309dd78d47a3277760d3bf16ffaaaac30da77fab6b0
    role: context
  - path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
    sha256: f32daa7eba476ec34c9b41bc8d76fa3c8ad4daa46c48beaf9cf1e98ae2ab761b
    role: context
  - path: data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml
    sha256: 71842b041a0726cd1ebe7dd973c979ee357e5af67874fd2200edcba45820aac0
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
  selection: Task review 355; batch 036 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-five task batches
    contain 350 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 353 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007563
targets:
- target_id: CultureMech:007563
  path: data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  label: anaerobic_alkaline_ye_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch036/355/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch036/355/strict.tsv"
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007563
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
  - CultureMech:007563
- check_id: mediadiveJ993api-source-access
  name: 'Exact source content access: mediadiveJ993api'
  required: false
  status: unavailable
  summary: The current optional J993 MediaDive API and its preserved retry returned503.
    Exact JCM993 and TOGO source content are available, so current recipe differences
    can be assessed without historical byte-equivalence claims.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - mediadiveJ993api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:02.298860Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch036/355/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:04.370647Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch036/355/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:06.096952Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:07.730450Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:46:04Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml:1:id:
    CultureMech:007563

    ./data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml:1:id: CultureMech:007563

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/source-preflight-bound/355/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:46:04Z'
  support: supports
  summary: 35 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: fb60ca86bf00f644496023042c40c460296b83ece5b95f737fcaeddf6d124527
- evidence_id: jcm993
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993
  locator: Complete exact primary formulation and preparation
  accessed_at: '2026-10-21T19:22:06.289432Z'
  support: supports
  summary: The source is a distinct recipe and must retain its own quantities and
    conditions.
  quote: 'NaCl 2.0 g NH 4 Cl 1.0 g KH 2 PO 4 0.1 g K 2 HPO 4 0.1 g KCl 0.1 g MgCl
    2 ·6H 2 O 0.1 g Tris base 3.0 g Na 2 S 2 O 3 ·5H 2 O 3.0 g Trace element solution
    (see Medium No. 439 ) 1.0 ml Resazurin 1.0 mg Distilled water 900.0 ml Mix components
    thoroughly, adjust pH to 9.0 with NaOH and  autoclave under a N 2 atmosphere.  After
    cooling, replace the gas phase with a N 2 -CO 2 (4:1, v/v) gas mixture.  Add the
    following solutions from sterile anaerobic stocks (autoclaved and stored under
    a N 2 atmosphere): 10% (w/v) Yeast extract solution 20.0 ml 8% NaHCO 3 solution
    30.0 ml 5% Na 2 S·9H 2 O solution 8.0 ml'
  snapshot_sha256: 54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a
- evidence_id: jcm1076
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076
  locator: Complete exact primary formulation and preparation
  accessed_at: '2026-10-21T13:13:22.044257Z'
  support: supports
  summary: The source is a distinct recipe and must retain its own quantities and
    conditions.
  quote: 'NaCl 20.0 g NH 4 Cl 1.0 g KH 2 PO 4 0.1 g K 2 HPO 4 0.1 g KCl 0.1 g MgCl
    2 ·6H 2 O 0.1 g Tris base 3.0 g Na 2 S 2 O 3 ·5H 2 O 3.0 g Trace element solution
    (see Medium No. 439 ) 1.0 ml Resazurin 1.0 mg Distilled water 950.0 ml Mix components
    thoroughly, adjust pH to 9.0 with NaOH and  autoclave under a N 2 atmosphere.  After
    cooling, replace the gas phase with a N 2 -CO 2 (4:1, v/v) gas mixture.  Add the
    following solutions from sterile anaerobic stocks (autoclaved and stored under
    a N 2 atmosphere): 10% (w/v) Yeast extract solution 10.0 ml 0.5 M Maltose solution
    20.0 ml 8% Na 2 CO 3 solution 20.0 ml 5% Na 2 S·9H 2 O solution 6.0 ml Check final
    pH be around 8.2.'
  snapshot_sha256: cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2
- evidence_id: trace
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439
  locator: Trace element solution subsection only
  accessed_at: '2026-10-21T13:13:22.895121Z'
  support: supports
  summary: Only this stock transfers; parent basal medium, gas handling, pH, dose
    timing and other stocks are excluded.
  quote: 'Trace element solution: HCl (25%) 12.5 ml FeSO 4 ·7H 2 O 2.1 g H 3 BO 3
    30.0 mg MnCl 2 ·4H 2 O 100.0 mg CoCl 2 ·6H 2 O 190.0 mg NiCl 2 ·6H 2 O 24.0 mg
    CuCl 2 ·2H 2 O 2.0 mg ZnSO 4 ·7H 2 O 144.0 mg Na 2 MoO 4 ·2H 2 O 36.0 mg Distilled
    water 987.0 ml'
  snapshot_sha256: 2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda
- evidence_id: togoM1047original
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047
  locator: $.meta and complete components/comments
  accessed_at: '2026-10-21T19:22:04.018923Z'
  support: supports
  summary: Exact TOGO-to-JCM accession correspondence; these are separate recipes.
  quote: '"original_media_id": "JCM_M993"'
  snapshot_sha256: ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af
- evidence_id: togoM1145original
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145
  locator: $.meta and complete components/comments
  accessed_at: '2026-10-21T19:22:04.019056Z'
  support: supports
  summary: Exact TOGO-to-JCM accession correspondence; these are separate recipes.
  quote: '"original_media_id": "JCM_M1076"'
  snapshot_sha256: 5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f
- evidence_id: md1076
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1076
  locator: $.medium and solutions[*] complete composition/steps
  accessed_at: '2026-10-21T13:13:18.386812Z'
  support: supports
  summary: Provider declares main1007 ml and trace1000 ml; normalized g_l values are
    distinct from original batch amounts. No measured-volume or historical-revision
    equivalence inferred.
  quote: "{\n    \"status\": 200,\n    \"count\": 1,\n    \"data\": {\n        \"\
    medium\": {\n            \"id\": \"J1076\",\n            \"name\": \"ALKALIPHILUS\
    \ LACT MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\"\
    : 8.2,\n            \"max_pH\": 8.2,\n            \"source\": \"JCM\",\n     \
    \       \"link\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\n\
    \        },\n        \"solutions\": [\n            {\n                \"id\":\
    \ 5141,\n                \"name\": \"Main sol. J1076\",\n                \"volume\"\
    : 1007,\n                \"recipe\": [\n                    {\n              \
    \          \"recipe_order\": 1,\n                        \"compound\": \"NaCl\"\
    ,\n                        \"compound_id\": 43,\n                        \"amount\"\
    : 20,\n                        \"unit\": \"g\",\n                        \"g_l\"\
    : 19.861,\n                        \"mmol_l\": 339.852,\n                    \
    \    \"optional\": 0\n                    },\n                    {\n        \
    \                \"recipe_order\": 2,\n                        \"compound\": \"\
    NH4Cl\",\n                        \"compound_id\": 42,\n                     \
    \   \"amount\": 1,\n                        \"unit\": \"g\",\n               \
    \         \"g_l\": 0.993049,\n                        \"mmol_l\": 18.5651,\n \
    \                       \"optional\": 0\n                    },\n            \
    \        {\n                        \"recipe_order\": 3,\n                   \
    \     \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n\
    \                        \"amount\": 0.1,\n                        \"unit\": \"\
    g\",\n                        \"g_l\": 0.0993049,\n                        \"\
    mmol_l\": 0.729721,\n                        \"optional\": 0\n               \
    \     },\n                    {\n                        \"recipe_order\": 4,\n\
    \                        \"compound\": \"K2HPO4\",\n                        \"\
    compound_id\": 10,\n                        \"amount\": 0.1,\n               \
    \         \"unit\": \"g\",\n                        \"g_l\": 0.0993049,\n    \
    \                    \"mmol_l\": 0.570141,\n                        \"optional\"\
    : 0\n                    },\n                    {\n                        \"\
    recipe_order\": 5,\n                        \"compound\": \"KCl\",\n         \
    \               \"compound_id\": 61,\n                        \"amount\": 0.1,\n\
    \                        \"unit\": \"g\",\n                        \"g_l\": 0.0993049,\n\
    \                        \"mmol_l\": 1.33206,\n                        \"optional\"\
    : 0\n                    },\n                    {\n                        \"\
    recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n\
    \                        \"compound_id\": 79,\n                        \"amount\"\
    : 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\"\
    : 0.0993049,\n                        \"mmol_l\": 0.488457,\n                \
    \        \"optional\": 0\n                    },\n                    {\n    \
    \                    \"recipe_order\": 7,\n                        \"compound\"\
    : \"Tris base\",\n                        \"compound_id\": 1698,\n           \
    \             \"amount\": 3,\n                        \"unit\": \"g\",\n     \
    \                   \"g_l\": 2.97915,\n                        \"mmol_l\": 24.5926,\n\
    \                        \"optional\": 0\n                    },\n           \
    \         {\n                        \"recipe_order\": 8,\n                  \
    \      \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\"\
    : 65,\n                        \"amount\": 3,\n                        \"unit\"\
    : \"g\",\n                        \"g_l\": 2.97915,\n                        \"\
    mmol_l\": 12.0037,\n                        \"optional\": 0\n                \
    \    },\n                    {\n                        \"recipe_order\": 9,\n\
    \                        \"solution\": \"Trace element solution\",\n         \
    \               \"solution_id\": 4186,\n                        \"amount\": 1,\n\
    \                        \"unit\": \"ml\",\n                        \"optional\"\
    : 0\n                    },\n                    {\n                        \"\
    recipe_order\": 10,\n                        \"compound\": \"Resazurin\",\n  \
    \                      \"compound_id\": 25,\n                        \"amount\"\
    : 1,\n                        \"unit\": \"mg\",\n                        \"g_l\"\
    : 0.000993049,\n                        \"mmol_l\": 0.00433286,\n            \
    \            \"optional\": 0\n                    },\n                    {\n\
    \                        \"recipe_order\": 11,\n                        \"compound\"\
    : \"Distilled water\",\n                        \"compound_id\": 4,\n        \
    \                \"amount\": 950,\n                        \"unit\": \"ml\",\n\
    \                        \"optional\": 0\n                    },\n           \
    \         {\n                        \"recipe_order\": 12,\n                 \
    \       \"compound\": \"Yeast extract\",\n                        \"compound_id\"\
    : 16,\n                        \"attribute\": \"w/v, 10%\",\n                \
    \        \"amount\": 10,\n                        \"unit\": \"ml\",\n        \
    \                \"optional\": 0\n                    },\n                   \
    \ {\n                        \"recipe_order\": 13,\n                        \"\
    compound\": \"Maltose\",\n                        \"compound_id\": 171,\n    \
    \                    \"attribute\": \"0.5 M\",\n                        \"amount\"\
    : 20,\n                        \"unit\": \"ml\",\n                        \"optional\"\
    : 0\n                    },\n                    {\n                        \"\
    recipe_order\": 14,\n                        \"compound\": \"Na2CO3\",\n     \
    \                   \"compound_id\": 32,\n                        \"attribute\"\
    : \"8%\",\n                        \"amount\": 20,\n                        \"\
    unit\": \"ml\",\n                        \"optional\": 0\n                   \
    \ },\n                    {\n                        \"recipe_order\": 15,\n \
    \                       \"compound\": \"Na2S x 9 H2O\",\n                    \
    \    \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n  \
    \                      \"amount\": 6,\n                        \"unit\": \"ml\"\
    ,\n                        \"optional\": 0\n                    }\n          \
    \      ],\n                \"steps\": [\n                    {\n             \
    \           \"recipe_order\": 12,\n                        \"step\": \"Mix components\
    \ thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere.\
    \ After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add\
    \ the following solutions from sterile anaerobic stocks (autoclaved and stored\
    \ under a N2 atmosphere): \"\n                    },\n                    {\n\
    \                        \"step\": \"Check final pH be around 8.2.\"\n       \
    \             }\n                ],\n                \"equipment\": {\n      \
    \              \"353\": \"Autoclave\",\n                    \"1898\": \"Anaerobic\
    \ workbench\"\n                }\n            },\n            {\n            \
    \    \"id\": 4186,\n                \"name\": \"Trace element solution\",\n  \
    \              \"volume\": 1000,\n                \"recipe\": [\n            \
    \        {\n                        \"recipe_order\": 1,\n                   \
    \     \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n \
    \                       \"attribute\": \"25%\",\n                        \"amount\"\
    : 12.5,\n                        \"unit\": \"ml\",\n                        \"\
    optional\": 0\n                    },\n                    {\n               \
    \         \"recipe_order\": 2,\n                        \"compound\": \"FeSO4\
    \ x 7 H2O\",\n                        \"compound_id\": 12,\n                 \
    \       \"amount\": 2.1,\n                        \"unit\": \"g\",\n         \
    \               \"g_l\": 2.1,\n                        \"mmol_l\": 7.55355,\n\
    \                        \"optional\": 0\n                    },\n           \
    \         {\n                        \"recipe_order\": 3,\n                  \
    \      \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n\
    \                        \"amount\": 30,\n                        \"unit\": \"\
    mg\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\"\
    : 0.485123,\n                        \"optional\": 0\n                    },\n\
    \                    {\n                        \"recipe_order\": 4,\n       \
    \                 \"compound\": \"MnCl2 x 4 H2O\",\n                        \"\
    compound_id\": 36,\n                        \"amount\": 100,\n               \
    \         \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n         \
    \               \"optional\": 0\n                    },\n                    {\n\
    \                        \"recipe_order\": 5,\n                        \"compound\"\
    : \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n         \
    \               \"amount\": 190,\n                        \"unit\": \"mg\",\n\
    \                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n\
    \                        \"optional\": 0\n                    },\n           \
    \         {\n                        \"recipe_order\": 6,\n                  \
    \      \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\"\
    : 40,\n                        \"amount\": 24,\n                        \"unit\"\
    : \"mg\",\n                        \"g_l\": 0.024,\n                        \"\
    mmol_l\": 0.185187,\n                        \"optional\": 0\n               \
    \     },\n                    {\n                        \"recipe_order\": 7,\n\
    \                        \"compound\": \"CuCl2 x 2 H2O\",\n                  \
    \      \"compound_id\": 39,\n                        \"amount\": 2,\n        \
    \                \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n\
    \                        \"mmol_l\": 0.0117314,\n                        \"optional\"\
    : 0\n                    },\n                    {\n                        \"\
    recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n\
    \                        \"compound_id\": 35,\n                        \"amount\"\
    : 144,\n                        \"unit\": \"mg\",\n                        \"\
    g_l\": 0.144,\n                        \"mmol_l\": 0.500763,\n               \
    \         \"optional\": 0\n                    },\n                    {\n   \
    \                     \"recipe_order\": 9,\n                        \"compound\"\
    : \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n        \
    \                \"amount\": 36,\n                        \"unit\": \"mg\",\n\
    \                        \"g_l\": 0.036,\n                        \"mmol_l\":\
    \ 0.148791,\n                        \"optional\": 0\n                    },\n\
    \                    {\n                        \"recipe_order\": 10,\n      \
    \                  \"compound\": \"Distilled water\",\n                      \
    \  \"compound_id\": 4,\n                        \"amount\": 987,\n           \
    \             \"unit\": \"ml\",\n                        \"optional\": 0\n   \
    \                 }\n                ]\n            }\n        ]\n    }\n}"
  snapshot_sha256: 53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/355/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 622c029e8a51ba8a5a89c1477a235282ff8fee55fd10194e0b2fa9731379efcc
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
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
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
- evidence_id: chebi9754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:13.713319Z'
  support: supports
  summary: CHEBI:9754 resolves to tris. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T19:46:04Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145":
    [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145",
    "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754": [{"label":
    "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term":
    "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: scoped-grounding
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/355/grounding-inventory.json
  locator: Every asserted target/owner and transferred-stock primary/secondary slot
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: All exact labels resolved. Source form correspondence remains separate.
  snapshot_sha256: 0151625dd277c9c737f76d1d768e10b7af7e17fe39d7888150552f4b18afd4e8
- evidence_id: chebi35696-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact formula/structure
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: The asserted term is anhydrous dichloride, whereas the transferred stock
    source names a hexahydrate.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact formula/structure
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: The asserted term is anhydrous dichloride, whereas the transferred stock
    source names a hexahydrate.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml;
    data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml", "events":
    11, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml",
    "events": 11, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Current merge fingerprint and field-combination code plus recorded merge
    provenance are relevant to this mixed target. They do not prove exact historical
    execution or justify recipe equivalence; maintain each source contributor separately.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/fingerprint.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Current merge fingerprint and field-combination code plus recorded merge
    provenance are relevant to this mixed target. They do not prove exact historical
    execution or justify recipe equivalence; maintain each source contributor separately.
  snapshot_sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Current merge fingerprint and field-combination code plus recorded merge
    provenance are relevant to this mixed target. They do not prove exact historical
    execution or justify recipe equivalence; maintain each source contributor separately.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Current merge fingerprint and field-combination code plus recorded merge
    provenance are relevant to this mixed target. They do not prove exact historical
    execution or justify recipe equivalence; maintain each source contributor separately.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-4
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:46:04Z'
  support: context_only
  summary: Current merge fingerprint and field-combination code plus recorded merge
    provenance are relevant to this mixed target. They do not prove exact historical
    execution or justify recipe equivalence; maintain each source contributor separately.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: mediadiveJ993api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J993
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:22:02.342926Z'
  support: context_only
  summary: The current optional J993 MediaDive API and its preserved retry returned503.
    Exact JCM993 and TOGO source content are available, so current recipe differences
    can be assessed without historical byte-equivalence claims.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 77 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"Distilled\
    \ water\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"950\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 10; Distilled\
    \ water / 900.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\n      }\n\
    \    ],\n    \"interpretation\": \"Preserve the exact source batch amount and\
    \ unit, with no inferred measured final volume. Water is ml and resazurin is mg.\
    \ The target salt/water values follow JCM1076 despite its JCM993 identity; matching\
    \ numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"ingredient\": \"NaCl\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 0; NaCl / 2.0\
    \ / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaCl          \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 2,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"ingredient\": \"KH2PO4\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 2; KH 2 PO 4\
    \ / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"NH4Cl\",\n  \
    \  \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 1; NH 4 Cl /\
    \ 1.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl\
    \                                                </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q5\",\n    \"ingredient\": \"K2HPO4\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 3; K 2 HPO 4\
    \ / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q6\",\n    \"ingredient\": \"Resazurin\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 9; Resazurin\
    \ / 1.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Resazurin\
    \                                               </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q7\",\n    \"ingredient\": \"MgCl2・6H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 5; MgCl 2 ·6H\
    \ 2 O / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"ingredient\": \"KCl\",\n    \"\
    decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 4; KCl / 0.1\
    \ / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KCl           \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"ingredient\": \"Tris base\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 6; Tris base\
    \ / 3.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Tris base\
    \                                               </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tris base\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"ingredient\": \"Na2S2O3・5H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal batch\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal batch; raw HTML row 7; Na 2 S 2\
    \ O 3 ·5H 2 O / 3.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub>&#183;5H<sub>2</sub>O              \
    \            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S2O3・5H2O\\\",\\n          \\\"volume\\\":\
    \ 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"ingredient\": \"Trace stock\
    \ receiving dose\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 basal\
    \ trace addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 basal trace dose; raw HTML row 8; Trace\
    \ element solution (see Medium No. 439 ) / 1.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Trace element solution (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=439\\\
    \">439</a>)           </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M439])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 1 ml of the named\
    \ JCM439 stock; the existing G_PER_L unit is wrong. Preserve trace composition\
    \ at stock scope.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"ingredient\"\
    : \"8% NaHCO3 solution\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993\
    \ post-cooling stock dose\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"solutions[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"claim_present\"\
    : true\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 post-cooling stock dose; raw HTML row\
    \ 12; 8% NaHCO 3 solution / 30.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> 8% NaHCO<sub>3</sub> solution                                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"8% NaHCO3 solution\\\",\\n          \\\"volume\\\
    \": 30,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 8,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml dose,\
    \ distinct from the other contributor. Missing target branch constituents require\
    \ resolving the merged identity; do not add mutually different recipes together.\
    \ Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\": \"q13\"\
    ,\n    \"ingredient\": \"8% NaHCO3 solution strength\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"JCM993 stock preparation\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 post-cooling stock dose; raw HTML row\
    \ 12; 8% NaHCO 3 solution / 30.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> 8% NaHCO<sub>3</sub> solution                                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"8% NaHCO3 solution\\\",\\n          \\\"volume\\\
    \": 30,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 8,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Keep stock strength separate from its receiving\
    \ dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and\
    \ sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q14\",\n    \"ingredient\": \"10% (w/v) Yeast extract\
    \ solution\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 post-cooling\
    \ stock dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 post-cooling stock dose; raw HTML row\
    \ 11; 10% (w/v) Yeast extract solution / 20.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 10% (w/v) Yeast extract solution                      </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Yeast extract solution\\\",\\n     \
    \     \\\"volume\\\": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n      \
    \  \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml\
    \ dose, distinct from the other contributor. Missing target branch constituents\
    \ require resolving the merged identity; do not add mutually different recipes\
    \ together. Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"ingredient\": \"10% (w/v) Yeast extract solution strength\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"JCM993 stock preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 post-cooling stock dose; raw HTML row\
    \ 11; 10% (w/v) Yeast extract solution / 20.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 10% (w/v) Yeast extract solution                      </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    \n      },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Yeast extract solution\\\",\\n     \
    \     \\\"volume\\\": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n      \
    \  \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep stock strength separate from\
    \ its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate\
    \ and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q16\",\n    \"ingredient\": \"5% Na2S・9H2O solution\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 post-cooling stock\
    \ dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 post-cooling stock dose; raw HTML row\
    \ 13; 5% Na 2 S·9H 2 O solution / 8.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution      \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\",\n\
    \        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 8,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml\
    \ dose, distinct from the other contributor. Missing target branch constituents\
    \ require resolving the merged identity; do not add mutually different recipes\
    \ together. Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"ingredient\": \"5% Na2S・9H2O solution strength\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"JCM993 stock preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 post-cooling stock dose; raw HTML row\
    \ 13; 5% Na 2 S·9H 2 O solution / 8.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution      \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM1047original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1047\",\n\
    \        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 8,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"ba56877950f094d18d253d683beafcf55c0cb73cf0ee4a01d5a1f3ad52bae0af\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep stock strength separate from\
    \ its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate\
    \ and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q18\",\n    \"ingredient\": \"NaOH quantity and concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"stage\": \"JCM993 initial pH adjustment\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 initial pH adjustment; NaOH quantity and\
    \ concentration\",\n        \"exact_source_quote\": \"adjust pH to 9.0 with NaOH\"\
    ,\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE preserves the unquantified\
    \ dose; stock concentration is also unspecified. Add source evidence without an\
    \ invented amount.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"ingredient\"\
    : \"Initial pH\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM993 before\
    \ autoclaving\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm993\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 before autoclaving; Initial pH\",\n  \
    \      \"exact_source_quote\": \"adjust pH to 9.0 with NaOH\",\n        \"snapshot_sha256\"\
    : \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\",\n    \
    \    \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"This is an initial adjustment, not\
    \ the measured final pH. For JCM1076 retain the separate final target around8.2.\"\
    \n  },\n  {\n    \"decision_id\": \"q20\",\n    \"ingredient\": \"CO2 post-cooling\
    \ gas ratio\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM993 after\
    \ cooling\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 after cooling; CO2 post-cooling gas ratio\"\
    ,\n        \"exact_source_quote\": \"replace the gas phase with a N 2 -CO 2 (4:1,\
    \ v/v) gas mixture.\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the explicit4:1 v/v mixture\
    \ at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer\
    \ pressure or whole-medium gas dose.\"\n  },\n  {\n    \"decision_id\": \"q21\"\
    ,\n    \"ingredient\": \"N2 post-cooling gas ratio\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"JCM993 after cooling\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 after cooling; N2 post-cooling gas ratio\"\
    ,\n        \"exact_source_quote\": \"replace the gas phase with a N 2 -CO 2 (4:1,\
    \ v/v) gas mixture.\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the explicit4:1 v/v mixture\
    \ at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer\
    \ pressure or whole-medium gas dose.\"\n  },\n  {\n    \"decision_id\": \"q22\"\
    ,\n    \"ingredient\": \"Initial and stock-storage N2 fraction\",\n    \"decision\"\
    : \"not_quantified\",\n    \"stage\": \"JCM993 sterilization and sterile-stock\
    \ storage\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 sterilization and sterile-stock storage;\
    \ Initial and stock-storage N2 fraction\",\n        \"exact_source_quote\": \"\
    autoclave under a N 2 atmosphere.\",\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"N2 is named without a percentage.\
    \ This differs from the explicitly proportioned post-cooling gas replacement.\"\
    \n  },\n  {\n    \"decision_id\": \"q23\",\n    \"ingredient\": \"Source default\
    \ autoclave cycle\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM993 stated\
    \ default\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 stated default; Source default autoclave\
    \ cycle\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\",\n        \"\
    parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"Record121 C for15 min only for the\
    \ exact source autoclaved stages; pressure and stock storage duration are unspecified.\"\
    \n  },\n  {\n    \"decision_id\": \"q24\",\n    \"ingredient\": \"Stock handling\
    \ and order\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM993 after cooling\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 after cooling; Stock handling and order\"\
    ,\n        \"exact_source_quote\": \"Add the following solutions from sterile\
    \ anaerobic stocks (autoclaved and stored under a N 2 atmosphere):\",\n      \
    \  \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the source-specific supplementation\
    \ after gas replacement and the distinct stock preparation/storage scope.\"\n\
    \  },\n  {\n    \"decision_id\": \"q25\",\n    \"ingredient\": \"Final measured\
    \ medium volume\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"JCM993\
    \ complete receiving batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm993\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 complete receiving batch; Final measured\
    \ medium volume\",\n        \"exact_source_quote\": \"Distilled water 900.0 ml\"\
    ,\n        \"snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"Source water and liquid additions\
    \ are explicit; a measured final volume or make-up instruction is not. Do not\
    \ normalize batch grams silently or add entire stock preparation volumes.\"\n\
    \  },\n  {\n    \"decision_id\": \"q26\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"950\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"950\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 10; Distilled\
    \ water / 950.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;950.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 950,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Preserve the exact source batch amount and\
    \ unit, with no inferred measured final volume. Water is ml and resazurin is mg.\
    \ The target salt/water values follow JCM1076 despite its JCM993 identity; matching\
    \ numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\n  },\n\
    \  {\n    \"decision_id\": \"q27\",\n    \"ingredient\": \"NaCl\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 0; NaCl / 20.0\
    \ / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaCl          \
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 20,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q28\",\n    \"ingredient\": \"KH2PO4\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 2; KH 2 PO\
    \ 4 / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q29\",\n    \"ingredient\": \"NH4Cl\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 1; NH 4 Cl\
    \ / 1.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl\
    \                                                </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q30\",\n    \"ingredient\": \"K2HPO4\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 3; K 2 HPO\
    \ 4 / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q31\",\n    \"ingredient\": \"Resazurin\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 9; Resazurin\
    \ / 1.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Resazurin\
    \                                               </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q32\",\n    \"ingredient\": \"MgCl2・6H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 5; MgCl 2 ·6H\
    \ 2 O / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q33\",\n    \"ingredient\": \"KCl\",\n   \
    \ \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 4; KCl / 0.1\
    \ / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KCl           \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q34\",\n    \"ingredient\": \"Tris base\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 6; Tris base\
    \ / 3.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Tris base\
    \                                               </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tris base\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q35\",\n    \"ingredient\": \"Na2S2O3・5H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 basal batch\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal batch; raw HTML row 7; Na 2 S 2\
    \ O 3 ·5H 2 O / 3.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub>&#183;5H<sub>2</sub>O              \
    \            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S2O3・5H2O\\\",\\n          \\\"volume\\\":\
    \ 3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact source batch amount\
    \ and unit, with no inferred measured final volume. Water is ml and resazurin\
    \ is mg. The target salt/water values follow JCM1076 despite its JCM993 identity;\
    \ matching numbers elsewhere do not authenticate G_PER_L or merge equivalence.\"\
    \n  },\n  {\n    \"decision_id\": \"q36\",\n    \"ingredient\": \"Trace stock\
    \ receiving dose\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076\
    \ basal trace addition\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"solutions[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 basal trace dose; raw HTML row 8; Trace\
    \ element solution (see Medium No. 439 ) / 1.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Trace element solution (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=439\\\
    \">439</a>)           </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M439])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 1 ml of the named\
    \ JCM439 stock; the existing G_PER_L unit is wrong. Preserve trace composition\
    \ at stock scope.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"ingredient\"\
    : \"8% Na2CO3 solution\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076\
    \ post-cooling stock dose\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": [\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M439])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M439\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"8% NaHCO3 solution\"\
    ,\n            \"composition\": [],\n            \"concentration\": {\n      \
    \        \"value\": \"30\",\n              \"unit\": \"G_PER_L\"\n           \
    \ },\n            \"notes\": \"Role: Buffer; Properties: Defined component, Inorganic\
    \ compound, Solution\",\n            \"name\": \"Unknown solution\"\n        \
    \  },\n          {\n            \"preferred_term\": \"10% (w/v) Yeast extract\
    \ solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Nutrient source; Properties: Undefined\
    \ component\",\n            \"name\": \"Unknown solution\"\n          },\n   \
    \       {\n            \"preferred_term\": \"5% Na2S・9H2O solution\",\n      \
    \      \"composition\": [],\n            \"concentration\": {\n              \"\
    value\": \"8\",\n              \"unit\": \"G_PER_L\"\n            },\n       \
    \     \"notes\": \"Role: Reducing agent; Properties: Defined component, Inorganic\
    \ compound, Solution\",\n            \"name\": \"Unknown solution\"\n        \
    \  }\n        ],\n        \"claim_present\": false\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 13; 8% Na 2 CO 3 solution / 20.0 / ml\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> 8% Na<sub>2</sub>CO<sub>3</sub> solution                  \
    \            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"8% Na2CO3 solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 8,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml dose,\
    \ distinct from the other contributor. Missing target branch constituents require\
    \ resolving the merged identity; do not add mutually different recipes together.\
    \ Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\": \"q38\"\
    ,\n    \"ingredient\": \"8% Na2CO3 solution strength\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"JCM1076 stock preparation\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Trace element solution (see Medium [M439])\"\
    ,\n            \"composition\": [],\n            \"notes\": \"Cross-reference\
    \ to Medium M439\",\n            \"concentration\": {\n              \"value\"\
    : \"1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    name\": \"Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"8% NaHCO3 solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"30\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Buffer; Properties: Defined component,\
    \ Inorganic compound, Solution\",\n            \"name\": \"Unknown solution\"\n\
    \          },\n          {\n            \"preferred_term\": \"10% (w/v) Yeast\
    \ extract solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Nutrient source; Properties: Undefined\
    \ component\",\n            \"name\": \"Unknown solution\"\n          },\n   \
    \       {\n            \"preferred_term\": \"5% Na2S・9H2O solution\",\n      \
    \      \"composition\": [],\n            \"concentration\": {\n              \"\
    value\": \"8\",\n              \"unit\": \"G_PER_L\"\n            },\n       \
    \     \"notes\": \"Role: Reducing agent; Properties: Defined component, Inorganic\
    \ compound, Solution\",\n            \"name\": \"Unknown solution\"\n        \
    \  }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 13; 8% Na 2 CO 3 solution / 20.0 / ml\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> 8% Na<sub>2</sub>CO<sub>3</sub> solution                  \
    \            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"8% Na2CO3 solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 8,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Keep stock strength separate from its receiving\
    \ dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and\
    \ sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q39\",\n    \"ingredient\": \"10% (w/v) Yeast extract\
    \ solution\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 post-cooling\
    \ stock dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 11; 10% (w/v) Yeast extract solution / 10.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 10% (w/v) Yeast extract solution                      </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Yeast extract solution\\\",\\n     \
    \     \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n      \
    \  \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml\
    \ dose, distinct from the other contributor. Missing target branch constituents\
    \ require resolving the merged identity; do not add mutually different recipes\
    \ together. Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\"\
    : \"q40\",\n    \"ingredient\": \"10% (w/v) Yeast extract solution strength\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"JCM1076 stock preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 11; 10% (w/v) Yeast extract solution / 10.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 10% (w/v) Yeast extract solution                      </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Yeast extract solution\\\",\\n     \
    \     \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n      \
    \  \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep stock strength separate from\
    \ its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate\
    \ and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q41\",\n    \"ingredient\": \"5% Na2S・9H2O solution\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 post-cooling stock\
    \ dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 14; 5% Na 2 S·9H 2 O solution / 6.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution      \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 6,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml\
    \ dose, distinct from the other contributor. Missing target branch constituents\
    \ require resolving the merged identity; do not add mutually different recipes\
    \ together. Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\"\
    : \"q42\",\n    \"ingredient\": \"5% Na2S・9H2O solution strength\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"JCM1076 stock preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 14; 5% Na 2 S·9H 2 O solution / 6.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution      \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 6,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep stock strength separate from\
    \ its receiving dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate\
    \ and sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q43\",\n    \"ingredient\": \"0.5 M Maltose solution\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 post-cooling stock\
    \ dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Trace element solution (see Medium [M439])\"\
    ,\n            \"composition\": [],\n            \"notes\": \"Cross-reference\
    \ to Medium M439\",\n            \"concentration\": {\n              \"value\"\
    : \"1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    name\": \"Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"8% NaHCO3 solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"30\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Buffer; Properties: Defined component,\
    \ Inorganic compound, Solution\",\n            \"name\": \"Unknown solution\"\n\
    \          },\n          {\n            \"preferred_term\": \"10% (w/v) Yeast\
    \ extract solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Nutrient source; Properties: Undefined\
    \ component\",\n            \"name\": \"Unknown solution\"\n          },\n   \
    \       {\n            \"preferred_term\": \"5% Na2S・9H2O solution\",\n      \
    \      \"composition\": [],\n            \"concentration\": {\n              \"\
    value\": \"8\",\n              \"unit\": \"G_PER_L\"\n            },\n       \
    \     \"notes\": \"Role: Reducing agent; Properties: Defined component, Inorganic\
    \ compound, Solution\",\n            \"name\": \"Unknown solution\"\n        \
    \  }\n        ],\n        \"claim_present\": false\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"claim_present\": true\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 12; 0.5 M Maltose solution / 20.0 / ml\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> 0.5 M Maltose solution                           </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"0.5 M Maltose solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 0.5,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Preserve this source-specific ml dose,\
    \ distinct from the other contributor. Missing target branch constituents require\
    \ resolving the merged identity; do not add mutually different recipes together.\
    \ Existing G_PER_L doses are wrong.\"\n  },\n  {\n    \"decision_id\": \"q44\"\
    ,\n    \"ingredient\": \"0.5 M Maltose solution strength\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"JCM1076 stock preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Trace element solution (see Medium [M439])\"\
    ,\n            \"composition\": [],\n            \"notes\": \"Cross-reference\
    \ to Medium M439\",\n            \"concentration\": {\n              \"value\"\
    : \"1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    name\": \"Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"8% NaHCO3 solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"30\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Buffer; Properties: Defined component,\
    \ Inorganic compound, Solution\",\n            \"name\": \"Unknown solution\"\n\
    \          },\n          {\n            \"preferred_term\": \"10% (w/v) Yeast\
    \ extract solution\",\n            \"composition\": [],\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \"Role: Nutrient source; Properties: Undefined\
    \ component\",\n            \"name\": \"Unknown solution\"\n          },\n   \
    \       {\n            \"preferred_term\": \"5% Na2S・9H2O solution\",\n      \
    \      \"composition\": [],\n            \"concentration\": {\n              \"\
    value\": \"8\",\n              \"unit\": \"G_PER_L\"\n            },\n       \
    \     \"notes\": \"Role: Reducing agent; Properties: Defined component, Inorganic\
    \ compound, Solution\",\n            \"name\": \"Unknown solution\"\n        \
    \  }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 post-cooling stock dose; raw HTML row\
    \ 12; 0.5 M Maltose solution / 20.0 / ml\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> 0.5 M Maltose solution                           </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    \n      },\n      {\n        \"source_key\": \"togoM1145original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1145\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"0.5 M Maltose solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 0.5,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"5eba2f706bdf8c6d9e8e3c2f62ffb9a30d739294019004098c93e117bd43af9f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Keep stock strength separate from its receiving\
    \ dose. Yeast extract explicitly specifies 10% w/v; carbonate/bicarbonate and\
    \ sulfide percentages have unspecified basis. JCM1076 maltose explicitly specifies\
    \ 0.5 M. No mass conversion or final-medium concentration is invented.\"\n  },\n\
    \  {\n    \"decision_id\": \"q45\",\n    \"ingredient\": \"NaOH quantity and concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"stage\": \"JCM1076 initial pH\
    \ adjustment\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 initial pH adjustment; NaOH quantity\
    \ and concentration\",\n        \"exact_source_quote\": \"adjust pH to 9.0 with\
    \ NaOH\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE preserves the unquantified\
    \ dose; stock concentration is also unspecified. Add source evidence without an\
    \ invented amount.\"\n  },\n  {\n    \"decision_id\": \"q46\",\n    \"ingredient\"\
    : \"Initial pH\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM1076 before\
    \ autoclaving\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 before autoclaving; Initial pH\",\n \
    \       \"exact_source_quote\": \"adjust pH to 9.0 with NaOH\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"This is an initial adjustment, not\
    \ the measured final pH. For JCM1076 retain the separate final target around8.2.\"\
    \n  },\n  {\n    \"decision_id\": \"q47\",\n    \"ingredient\": \"CO2 post-cooling\
    \ gas ratio\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1076 after\
    \ cooling\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 after cooling; CO2 post-cooling gas ratio\"\
    ,\n        \"exact_source_quote\": \"replace the gas phase with a N 2 -CO 2 (4:1,\
    \ v/v) gas mixture.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the explicit4:1 v/v mixture\
    \ at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer\
    \ pressure or whole-medium gas dose.\"\n  },\n  {\n    \"decision_id\": \"q48\"\
    ,\n    \"ingredient\": \"N2 post-cooling gas ratio\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"JCM1076 after cooling\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 after cooling; N2 post-cooling gas ratio\"\
    ,\n        \"exact_source_quote\": \"replace the gas phase with a N 2 -CO 2 (4:1,\
    \ v/v) gas mixture.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the explicit4:1 v/v mixture\
    \ at this stage while keeping the earlier N2 atmosphere unquantified. Do not infer\
    \ pressure or whole-medium gas dose.\"\n  },\n  {\n    \"decision_id\": \"q49\"\
    ,\n    \"ingredient\": \"Initial and stock-storage N2 fraction\",\n    \"decision\"\
    : \"not_quantified\",\n    \"stage\": \"JCM1076 sterilization and sterile-stock\
    \ storage\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 sterilization and sterile-stock storage;\
    \ Initial and stock-storage N2 fraction\",\n        \"exact_source_quote\": \"\
    autoclave under a N 2 atmosphere.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"N2 is named without a percentage.\
    \ This differs from the explicitly proportioned post-cooling gas replacement.\"\
    \n  },\n  {\n    \"decision_id\": \"q50\",\n    \"ingredient\": \"Source default\
    \ autoclave cycle\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM1076 stated\
    \ default\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 stated default; Source default autoclave\
    \ cycle\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n        \"\
    parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"Record121 C for15 min only for the\
    \ exact source autoclaved stages; pressure and stock storage duration are unspecified.\"\
    \n  },\n  {\n    \"decision_id\": \"q51\",\n    \"ingredient\": \"Stock handling\
    \ and order\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM1076 after cooling\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 after cooling; Stock handling and order\"\
    ,\n        \"exact_source_quote\": \"Add the following solutions from sterile\
    \ anaerobic stocks (autoclaved and stored under a N 2 atmosphere):\",\n      \
    \  \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the source-specific supplementation\
    \ after gas replacement and the distinct stock preparation/storage scope.\"\n\
    \  },\n  {\n    \"decision_id\": \"q52\",\n    \"ingredient\": \"Final measured\
    \ medium volume\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"JCM1076\
    \ complete receiving batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 complete receiving batch; Final measured\
    \ medium volume\",\n        \"exact_source_quote\": \"Distilled water 950.0 ml\"\
    ,\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"Source water and liquid additions\
    \ are explicit; a measured final volume or make-up instruction is not. Do not\
    \ normalize batch grams silently or add entire stock preparation volumes.\"\n\
    \  },\n  {\n    \"decision_id\": \"q53\",\n    \"ingredient\": \"JCM1076 final\
    \ target pH\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM1076 after its\
    \ specific supplementation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 after its specific supplementation; JCM1076\
    \ final target pH\",\n        \"exact_source_quote\": \"Check final pH be around\
    \ 8.2.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"interpretation\": \"This final target belongs only to\
    \ JCM1076. JCM993 does not state a final pH; no transfer between recipes.\"\n\
    \  },\n  {\n    \"decision_id\": \"q54\",\n    \"ingredient\": \"JCM993 final\
    \ pH\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"JCM993 after\
    \ supplementation\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\",\n    \
    \    \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm993\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993\"\
    ,\n        \"source_locator\": \"JCM993 after supplementation; JCM993 final pH\"\
    ,\n        \"exact_source_quote\": \"adjust pH to 9.0 with NaOH\",\n        \"\
    snapshot_sha256\": \"54cfed37ba22b0c7997ce9009d6b3ff27a85cbf97153f6e3fd78b8f8e698412a\"\
    ,\n        \"parsed_text_sha256\": \"4f437c5f6813f2c5bf436fb1d20b264b6a7d741de230c4d98fe0cb1f93dac39d\"\
    \n      }\n    ],\n    \"interpretation\": \"Only the pre-autoclave adjustment\
    \ is given; do not convert it into a final measured value or import JCM1076 final\
    \ pH.\"\n  },\n  {\n    \"decision_id\": \"q55\",\n    \"ingredient\": \"HCl (25%)\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Receiving trace composition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 18; HCl\
    \ (25%) / 12.5 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> HCl\
    \ (25%)                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;12.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%)\\\",\\n          \\\"volume\\\": 12.5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\n  \
    \        \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"ingredient\":\
    \ \"HCl (25%)\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 18; HCl\
    \ (25%) / 12.5 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> HCl\
    \ (25%)                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;12.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%)\\\",\\n          \\\"volume\\\": 12.5,\\\
    n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\n  \
    \        \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q57\",\n    \"ingredient\": \"Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 27; Distilled\
    \ water / 987.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;987.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q58\",\n    \"ingredient\":\
    \ \"Distilled water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing\
    \ M439 trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"988.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 27; Distilled\
    \ water / 987.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;987.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 987,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"interpretation\": \"The local parent flattens stock batch mass/liquid\
    \ into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml.\
    \ Its water also combines separate parent stages. Preserve the exact source basis,\
    \ not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\": \"\
    q59\",\n    \"ingredient\": \"Na2MoO4・2H2O\",\n    \"decision\": \"add\",\n  \
    \  \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 26; Na\
    \ 2 MoO 4 ·2H 2 O / 36.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                         \
    \   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q60\",\n    \"ingredient\":\
    \ \"Na2MoO4・2H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing\
    \ M439 trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 26; Na\
    \ 2 MoO 4 ·2H 2 O / 36.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                         \
    \   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\n      }\n\
    \    ],\n    \"interpretation\": \"The local parent flattens stock batch mass/liquid\
    \ into G_PER_L; seven salts are printed in mg, iron in grams, acid/water in ml.\
    \ Its water also combines separate parent stages. Preserve the exact source basis,\
    \ not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\": \"\
    q61\",\n    \"ingredient\": \"H3BO3\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Receiving trace composition\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n \
    \       \"field_path\": \"solutions[0].composition\",\n        \"stored\": []\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 20; H 3\
    \ BO 3 / 30.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 30,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q62\",\n    \"ingredient\":\
    \ \"H3BO3\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 20; H 3\
    \ BO 3 / 30.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 30,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q63\",\n    \"ingredient\": \"FeSO4・7H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 19; FeSO\
    \ 4 ·7H 2 O / 2.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 2.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q64\",\n    \"ingredient\":\
    \ \"FeSO4・7H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 19; FeSO\
    \ 4 ·7H 2 O / 2.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 2.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q65\",\n    \"ingredient\": \"MnCl2・4H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 21; MnCl\
    \ 2 ·4H 2 O / 100.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q66\",\n    \"ingredient\":\
    \ \"MnCl2・4H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 21; MnCl\
    \ 2 ·4H 2 O / 100.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q67\",\n    \"ingredient\": \"CoCl2・6H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 22; CoCl\
    \ 2 ·6H 2 O / 190.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q68\",\n    \"ingredient\":\
    \ \"CoCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 22; CoCl\
    \ 2 ·6H 2 O / 190.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q69\",\n    \"ingredient\": \"NiCl2・6H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 23; NiCl\
    \ 2 ·6H 2 O / 24.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q70\",\n    \"ingredient\":\
    \ \"NiCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 23; NiCl\
    \ 2 ·6H 2 O / 24.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q71\",\n    \"ingredient\": \"ZnSO4・7H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 25; ZnSO\
    \ 4 ·7H 2 O / 144.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                                </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;144.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 144,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q72\",\n    \"ingredient\":\
    \ \"ZnSO4・7H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"144\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 25; ZnSO\
    \ 4 ·7H 2 O / 144.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                                </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;144.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 144,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q73\",\n    \"ingredient\": \"CuCl2・2H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace composition\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 24; CuCl\
    \ 2 ·2H 2 O / 2.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent only the named JCM439 trace-stock\
    \ constituent and batch amount; no parent basal medium or other referenced stock\
    \ transfers.\"\n  },\n  {\n    \"decision_id\": \"q74\",\n    \"ingredient\":\
    \ \"CuCl2・2H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Existing M439\
    \ trace constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; raw HTML row 24; CuCl\
    \ 2 ·2H 2 O / 2.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    \n      },\n      {\n        \"source_key\": \"togoM439original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c\"\
    \n      }\n    ],\n    \"interpretation\": \"The local parent flattens stock batch\
    \ mass/liquid into G_PER_L; seven salts are printed in mg, iron in grams, acid/water\
    \ in ml. Its water also combines separate parent stages. Preserve the exact source\
    \ basis, not an assumed one-liter concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q75\",\n    \"ingredient\": \"Trace acid strength\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"JCM439 trace stock only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; Trace acid strength\"\
    ,\n        \"exact_source_quote\": \"HCl (25%) 12.5 ml\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain25% and12.5 ml separately;\
    \ source percentage basis and density are unqualified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q76\",\n    \"ingredient\": \"Trace final measured volume\",\n    \"decision\"\
    : \"not_quantified\",\n    \"stage\": \"JCM439 trace stock only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 trace stock only; Trace final measured\
    \ volume\",\n        \"exact_source_quote\": \"Distilled water 987.0 ml\",\n \
    \       \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      }\n    ],\n    \"interpretation\": \"Listed water987 ml plus acid12.5\
    \ ml totals999.5 ml, not a measured final volume. The API separately declares1000\
    \ ml; retain this provider normalization without rewriting the primary.\"\n  },\n\
    \  {\n    \"decision_id\": \"q77\",\n    \"ingredient\": \"Provider-declared normalization\
    \ volumes\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"J1076 main\
    \ and trace API normalizations\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadiveJ1076api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1007\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1000\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"interpretation\": \"The provider explicitly declares\
    \ these denominators. They are not independent experimental measurements or an\
    \ instruction to modify primary batch amounts. Trace input liquids total999.5\
    \ ml; main liquids total1007 ml.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '13 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 13/13
    primary and 9/13 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi26710
  - chebi31206
  - chebi32145
  - chebi32150
  - chebi32588
  - chebi63036
  - chebi86345
  - chebi8806
  - chebi9754
  details: 'Instance coverage on a 0–100 percent scale, denominator 13: primary 100.00%;
    secondary 69.23%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Distinct contributor recipes incorrectly merged
  outcome: concern
  summary: 'JCM993/M1047 and JCM1076/M1145 are both exact contributors, not interchangeable
    synonyms: NaCl2 versus20 g, water900 versus950 ml, bicarbonate versus carbonate,
    different yeast/sulfide doses and maltose only in JCM1076. The target combines
    JCM1076 basal values with JCM993 identity/supplements. The specialized namesake
    is excluded by stable ID and import provenance.'
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm993
  - jcm1076
  - togoM1047original
  - togoM1145original
- assessment_id: stocks
  area: representation
  topic: Named stock scope and API normalization
  outcome: concern
  summary: Only JCM439 trace stock transfers, not its parent basal medium, pH7, vessel
    example, vitamins, lactate or receiving doses. Empty trace stubs and incorrect
    volume units lose that distinction. Provider normalization volumes remain separate
    from primary amounts.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - trace
  - md1076
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Main and transferred chemical forms
  outcome: concern
  summary: Main hydrate terms and generic resazurin match the source specificity;
    no unsupported resazurin salt claim is introduced. Transferred M439 cobalt and
    nickel hexahydrates are grounded to anhydrous CHEBI35696 and34887. Other parent
    groundings are excluded.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - jcm993
  - jcm1076
  - trace
  - scoped-grounding
  - chebi35696-form
  - chebi34887-form
- assessment_id: preparation
  area: completeness
  topic: Preparation, pH stages and gas ratios
  outcome: concern
  summary: All three layers omit initial pH9, exact default autoclave cycle, post-cooling4:1
    v/v N2/CO2 and stock handling. JCM1076 final pH around8.2 belongs only to that
    contributor.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - jcm993
  - jcm1076
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Mixture classification and growth claims
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID fit the yeast-containing sources. Names and
    generic microbial-cultivation applications do not establish strain growth, taxonomy
    or interchangeability.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - jcm993
  - jcm1076
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 35 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: ownership
  area: ownership
  topic: Two maintained contributors and regeneration
  outcome: concern
  summary: The complete merge event and merged_from resolve two exact maintained inputs
    with distinct formulations. The generated identity must be resolved without overwriting
    either source recipe or adopting the excluded namesake.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - writer-1
  - writer-3
- assessment_id: evidence
  area: evidence
  topic: Source support and attachment
  outcome: concern
  summary: Current primary/TOGO evidence is available, but target and both owners
    lack attached amount/preparation evidence. A current source match does not prove
    historical byte equivalence.
  target_ids:
  - CultureMech:007563
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - jcm993
  - jcm1076
  - trace
findings:
- finding_id: f1
  issue_key: culturemech.007563.distinct-recipes-merged
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Two distinct recipes form a mixed generated identity
  description: Target JCM993 identity/supplementation carries JCM1076 water and salt
    values; its synonym field implies equivalence unsupported by the exact recipes.
  target_ids:
  - CultureMech:007563
  field_paths:
  - media_term
  - synonyms
  - ingredients
  - solutions
  - merged_from
  evidence_ids:
  - jcm993
  - jcm1076
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  issue_key: culturemech.007563.units-and-stage-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid units and resazurin scale are wrong
  description: All local volume doses are G_PER_L, resazurin1 mg is stored1 G_PER_L,
    and batch amounts and trace stock fields lack source-stage basis.
  target_ids:
  - CultureMech:007563
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - quantity-inventory
  - jcm993
  - jcm1076
  - trace
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  issue_key: culturemech.007563.preparation-ph-gas
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Distinct preparation and gas stages are missing
  description: Initial pH9, source default121 C/15 min, post-cooling4:1 v/v gas and
    JCM1076-only final pH8.2 are absent.
  target_ids:
  - CultureMech:007563
  field_paths:
  - preparation_steps
  - ph_value
  - sterilization
  - ingredients[11]
  - ingredients[12]
  evidence_ids:
  - jcm993
  - jcm1076
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  issue_key: culturemech.007563.trace-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Transferred trace hydrates use anhydrous identities
  description: The M439 cobalt and nickel source names are hexahydrates, while the
    stored primary terms35696 and34887 are anhydrous.
  target_ids:
  - CultureMech:007563
  field_paths:
  - solutions[0].composition
  evidence_ids:
  - trace
  - scoped-grounding
  - chebi35696-form
  - chebi34887-form
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  issue_key: culturemech.007563.claim-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Claims lack attached source evidence
  description: Accessions and merge histories do not attach exact amounts, stages
    or preparation support.
  target_ids:
  - CultureMech:007563
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  description: Resolve the merge boundary and retain separate source recipes/variants
    with exact ownership; then regenerate after source-specific comparisons.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007563
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  description: Correct units and exact batch/stock basis within each separate owner;
    retain strengths and doses without invented final concentrations.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007563
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  description: Add exact source-scoped handling and gas proportions, preserving unknown
    pressure, NaOH dose and JCM993 final pH.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007563
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  description: Independently resolve hydrate identities before copying parent grounding
    into receiving trace stocks; preserve source mass amounts.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007563
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
  description: Attach narrow literal snippets and exact source locators/hash/times
    after curation; retain append-only history and distinct contributor sources.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007563
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1145_Alkaliphilus_Lact_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml
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
- The current optional J993 MediaDive API and its preserved retry returned503. Exact
  JCM993 and TOGO source content are available, so current recipe differences can
  be assessed without historical byte-equivalence claims.
- No final measured volume, unqualified percentage basis, gas pressure, incubation
  temperature or species growth is inferred. Current J1076 API values are explicitly
  provider-normalized and do not establish historical chronology.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-036
- generated-medium
```
