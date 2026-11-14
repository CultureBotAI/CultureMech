# Source and formulation review: anaerobic_alkaline_glucose_medium (CultureMech:007857)

- Review: 20261021T194412Z-culturemech-007857-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:39:56Z
- Finished UTC: 2026-10-21T19:44:12Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM1228 recipe is available, but the target and owner flatten separate A/B preparations, store liquid additions as mass concentrations, link unrelated stocks, and generalize a JCM32929-only supplement branch. Named trace and vitamin stocks require separate source and chemical-form accounting.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 354; batch 036 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-five task batches contain 350 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 353 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007857 | data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml | generated | anaerobic_alkaline_glucose_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007857 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007857 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch036/354/strict.tsv |
| validate-terms | passed | True | CultureMech:007857 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007857 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007857 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ1228api | unavailable | False | CultureMech:007857 | The current optional MediaDive J1228 API and preserved retry returned503. Exact JCM1228 and original TOGO content are available; historical byte equivalence is not inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007857.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007857.

72 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "JCM1228 Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution A preparation; raw HTML row 3; Distilled water / 900.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;900.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q2",
    "ingredient": "NaCl",
    "decision": "correct",
    "stage": "JCM1228 Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution A preparation; raw HTML row 0; NaCl / 20.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q3",
    "ingredient": "NaHCO3",
    "decision": "correct",
    "stage": "JCM1228 Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "60",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "60",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution A preparation; raw HTML row 2; NaHCO 3 / 60.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaHCO&lt;sub&gt;3&lt;/sub&gt;                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;60.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 60,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q4",
    "ingredient": "Na2CO3",
    "decision": "correct",
    "stage": "JCM1228 Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution A preparation; raw HTML row 1; Na 2 CO 3 / 50.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;50.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 50,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q5",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "JCM1228 Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution B preparation; raw HTML row 10; Distilled water / 100.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q6",
    "ingredient": "Yeast extract",
    "decision": "correct",
    "stage": "JCM1228 Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution B preparation; raw HTML row 7; Yeast extract / 0.05 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.05&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 0.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q7",
    "ingredient": "KH2PO4",
    "decision": "correct",
    "stage": "JCM1228 Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution B preparation; raw HTML row 6; KH 2 PO 4 / 0.2 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q8",
    "ingredient": "NH4Cl",
    "decision": "correct",
    "stage": "JCM1228 Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution B preparation; raw HTML row 5; NH 4 Cl / 0.5 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q9",
    "ingredient": "MgCl2・6H2O",
    "decision": "correct",
    "stage": "JCM1228 Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution B preparation; raw HTML row 4; MgCl 2 ·6H 2 O / 0.1 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q10",
    "ingredient": "Glucose",
    "decision": "correct",
    "stage": "JCM1228 Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 Solution B preparation; raw HTML row 8; Glucose / 3.0 / g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Glucose                                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"Glucose\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "Preserve the printed batch mass or water volume in this preparation. Both layers collapse the source stages into final-medium G_PER_L; neither stock preparation volume nor summed water establishes a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q11",
    "ingredient": "Solution A receiving addition",
    "decision": "correct",
    "stage": "TOGO assembly layer",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      },
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 A/B combination sentence",
        "exact_source_quote": "Aseptically and anaerobically combine Solutions A and B.",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "TOGO explicitly lists 900 ml and 100 ml assembly additions; JCM defines A/B then instructs combination. Preserve that provenance difference and correct G_PER_L to volume; do not add these doses again as extra stock water."
  },
  {
    "decision_id": "q12",
    "ingredient": "Solution B receiving addition",
    "decision": "correct",
    "stage": "TOGO assembly layer",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      },
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM1228 A/B combination sentence",
        "exact_source_quote": "Aseptically and anaerobically combine Solutions A and B.",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "TOGO explicitly lists 900 ml and 100 ml assembly additions; JCM defines A/B then instructs combination. Preserve that provenance difference and correct G_PER_L to volume; do not add these doses again as extra stock water."
  },
  {
    "decision_id": "q13",
    "ingredient": "Trace element solution (see Medium [M940])",
    "decision": "correct",
    "stage": "Solution B trace dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "Solution B trace dose; raw HTML row 9; Trace element solution (see Medium No. 899 ) / 1.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=899\"&gt;899&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M940])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "The source amount is ml, not G_PER_L. Retain the named stock and stage; the JCM32929 supplements are conditional per-liter additions and must not become universal basal ingredients."
  },
  {
    "decision_id": "q14",
    "ingredient": "Trace vitamins (see Medium [M190])",
    "decision": "correct",
    "stage": "Post-combination vitamin dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "Post-combination vitamin dose; raw HTML row 11; Trace vitamins (see Medium No. 197 ) / 10.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "The source amount is ml, not G_PER_L. Retain the named stock and stage; the JCM32929 supplements are conditional per-liter additions and must not become universal basal ingredients."
  },
  {
    "decision_id": "q15",
    "ingredient": "5% Na2S・9H2O solution",
    "decision": "correct",
    "stage": "JCM32929-only sulfide addition per liter",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM32929-only sulfide addition per liter; raw HTML row 13; 5% Na 2 S·9H 2 O solution / 6.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 6,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "The source amount is ml, not G_PER_L. Retain the named stock and stage; the JCM32929 supplements are conditional per-liter additions and must not become universal basal ingredients."
  },
  {
    "decision_id": "q16",
    "ingredient": "10% Peptone solution",
    "decision": "correct",
    "stage": "JCM32929-only peptone addition per liter",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM32929-only peptone addition per liter; raw HTML row 12; 10% Peptone solution / 10.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 10% Peptone solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      },
      {
        "source_key": "togoM1320original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"10% Peptone solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38"
      }
    ],
    "interpretation": "The source amount is ml, not G_PER_L. Retain the named stock and stage; the JCM32929 supplements are conditional per-liter additions and must not become universal basal ingredients."
  },
  {
    "decision_id": "q17",
    "ingredient": "Nitrogen atmosphere",
    "decision": "not_quantified",
    "stage": "Separate A/B sterilization and stock storage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "Separate A/B sterilization and stock storage; Nitrogen atmosphere",
        "exact_source_quote": "Mix components thoroughly and autoclave under a N 2 gas atmosphere.",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "VARIABLE correctly avoids an invented gas fraction; source N2 identity and separate handling need evidence. No 100% or pressure is supplied."
  },
  {
    "decision_id": "q18",
    "ingredient": "sulfide stock strength",
    "decision": "add",
    "stage": "JCM32929-only stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM32929-only stock strength; raw HTML row 13; 5% Na 2 S·9H 2 O solution / 6.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      }
    ],
    "interpretation": "Retain literal 5% stock strength with unspecified percentage basis, distinct from receiving dose. Do not convert to g/L, infer density or treat the supplement as universal."
  },
  {
    "decision_id": "q19",
    "ingredient": "peptone stock strength",
    "decision": "add",
    "stage": "JCM32929-only stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM32929-only stock strength; raw HTML row 12; 10% Peptone solution / 10.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 10% Peptone solution &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847"
      }
    ],
    "interpretation": "Retain literal 10% stock strength with unspecified percentage basis, distinct from receiving dose. Do not convert to g/L, infer density or treat the supplement as universal."
  },
  {
    "decision_id": "q20",
    "ingredient": "Conditional branch denominator and accession",
    "decision": "correct",
    "stage": "JCM32929 supplementation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Solution A",
            "term": {
              "id": "mediadive.solution:5342",
              "label": "Solution A"
            },
            "concentration": {
              "value": "900",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_5342_Solution_A.yaml for composition",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Solution B",
            "term": {
              "id": "mediadive.solution:5343",
              "label": "Solution B"
            },
            "concentration": {
              "value": "100",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_5343_Solution_B.yaml for composition",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M940])",
            "composition": [],
            "notes": "Cross-reference to Medium M940",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "5% Na2S・9H2O solution",
            "composition": [],
            "concentration": {
              "value": "6",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "10% Peptone solution",
            "composition": [],
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Undefined component",
            "name": "Unknown solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Solution A",
            "term": {
              "id": "mediadive.solution:5342",
              "label": "Solution A"
            },
            "concentration": {
              "value": "900",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_5342_Solution_A.yaml for composition",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Solution B",
            "term": {
              "id": "mediadive.solution:5343",
              "label": "Solution B"
            },
            "concentration": {
              "value": "100",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_5343_Solution_B.yaml for composition",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M940])",
            "composition": [],
            "notes": "Cross-reference to Medium M940",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "5% Na2S・9H2O solution",
            "composition": [],
            "concentration": {
              "value": "6",
              "unit": "G_PER_L"
            },
            "notes": "Role: Reducing agent; Properties: Defined component, Inorganic compound, Solution",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "10% Peptone solution",
            "composition": [],
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "notes": "Properties: Undefined component",
            "name": "Unknown solution"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "JCM32929 supplementation; Conditional branch denominator and accession",
        "exact_source_quote": "For JCM 32929, aseptically and anaerobically add per liter the following solutions",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "The per-liter basis and accession restriction are explicit and absent from the local solution claims; no independent strain growth observation is inferred."
  },
  {
    "decision_id": "q21",
    "ingredient": "Final target pH",
    "decision": "add",
    "stage": "After A/B combination, before listed vitamin addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "After A/B combination, before listed vitamin addition; Final target pH",
        "exact_source_quote": "Check final pH of the medium to be around 9.2.",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "Record approximate target pH 9.2 at this source stage, not measured pH."
  },
  {
    "decision_id": "q22",
    "ingredient": "Default sterilization temperature and duration",
    "decision": "add",
    "stage": "A/B and conditional autoclaved stocks unless exception",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "A/B and conditional autoclaved stocks unless exception; Default sterilization temperature and duration",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "The exact source page supplies 121 C for 15 min. The filter-sterilized vitamin addition is an explicit exception; no extra pressure is supplied."
  },
  {
    "decision_id": "q23",
    "ingredient": "A/B combination and vitamin handling",
    "decision": "add",
    "stage": "Aseptic anaerobic assembly and stock storage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "Aseptic anaerobic assembly and stock storage; A/B combination and vitamin handling",
        "exact_source_quote": "Aseptically and anaerobically combine Solutions A and B.  Check final pH of the medium to be around 9.2.  Add the following solution into the medium (filter-sterilized and stored under a N 2 atmosphere):",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "Add the exact order, filtering and N2 storage. Do not import JCM197 parent basal gases or pH."
  },
  {
    "decision_id": "q24",
    "ingredient": "Final measured volume",
    "decision": "not_quantified",
    "stage": "Complete receiving batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1228",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228",
        "source_locator": "Complete receiving batch; Final measured volume",
        "exact_source_quote": "Trace vitamins (see Medium No. 197 ) 10.0 ml",
        "snapshot_sha256": "299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847",
        "parsed_text_sha256": "1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b"
      }
    ],
    "interpretation": "Basal water inputs total 1000 ml and later additions are listed; no measured final-volume or make-up instruction is supplied. Do not flatten stocks or assume final concentrations."
  },
  {
    "decision_id": "q25",
    "ingredient": "Distilled water",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 34; Distilled water / 995.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;995.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 995,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q26",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "997.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 34; Distilled water / 995.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;995.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 995,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q27",
    "ingredient": "Na2MoO4·2H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 27; Na 2 MoO 4 ·2H 2 O / 36.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4·2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q28",
    "ingredient": "Na2MoO4·2H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 27; Na 2 MoO 4 ·2H 2 O / 36.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4·2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q29",
    "ingredient": "H3BO3",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 32; H 3 BO 3 / 6.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0   &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q30",
    "ingredient": "H3BO3",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 32; H 3 BO 3 / 6.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0   &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q31",
    "ingredient": "MnCl2·4H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 33; MnCl 2 ·4H 2 O / 99.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;99.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2·4H2O\",\n          \"volume\": 99,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q32",
    "ingredient": "MnCl2·4H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "99",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 33; MnCl 2 ·4H 2 O / 99.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;99.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2·4H2O\",\n          \"volume\": 99,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q33",
    "ingredient": "CoCl2·6H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 25; CoCl 2 ·6H 2 O / 238.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;238.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 238,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q34",
    "ingredient": "CoCl2·6H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "238",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 25; CoCl 2 ·6H 2 O / 238.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;238.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 238,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q35",
    "ingredient": "ZnSO4·7H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 29; ZnSO 4 ·7H 2 O / 144.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;144.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"ZnSO4·7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q36",
    "ingredient": "ZnSO4·7H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "144",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 29; ZnSO 4 ·7H 2 O / 144.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;144.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"ZnSO4·7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q37",
    "ingredient": "CuCl2·2H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 30; CuCl 2 ·2H 2 O / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0   &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2·2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q38",
    "ingredient": "CuCl2·2H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 30; CuCl 2 ·2H 2 O / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0   &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2·2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q39",
    "ingredient": "Na2WO4·2H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 28; Na 2 WO 4 ·2H 2 O / 33.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;33.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"Na2WO4·2H2O\",\n          \"volume\": 33,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q40",
    "ingredient": "Na2WO4·2H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "33",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 28; Na 2 WO 4 ·2H 2 O / 33.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;33.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"Na2WO4·2H2O\",\n          \"volume\": 33,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q41",
    "ingredient": "(NH4)2Fe(SO4)2·6H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 23; (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O / 784.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; (NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;Fe(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;784.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"(NH4)2Fe(SO4)2·6H2O\",\n          \"volume\": 784,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q42",
    "ingredient": "(NH4)2Fe(SO4)2·6H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "784",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 23; (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O / 784.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; (NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;Fe(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;784.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"(NH4)2Fe(SO4)2·6H2O\",\n          \"volume\": 784,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q43",
    "ingredient": "(NH4)2Ni(SO4)2•6H2O",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 26; (NH 4 ) 2 Ni(SO 4 ) 2 •6H 2 O / 395.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; (NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;Ni(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;•6H&lt;sub&gt;2&lt;/sub&gt;O         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;395.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"(NH4)2Ni(SO4)2•6H2O\",\n          \"volume\": 395,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q44",
    "ingredient": "(NH4)2Ni(SO4)2•6H2O",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "395",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 26; (NH 4 ) 2 Ni(SO 4 ) 2 •6H 2 O / 395.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; (NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;Ni(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;•6H&lt;sub&gt;2&lt;/sub&gt;O         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;395.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"(NH4)2Ni(SO4)2•6H2O\",\n          \"volume\": 395,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q45",
    "ingredient": "25% HCl",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 24; 25% HCl / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0   &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[10]",
        "exact_source_quote": "\"component_name\": \"25% HCl\",\n          \"volume\": 5,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q46",
    "ingredient": "25% HCl",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 24; 25% HCl / 5.0 / ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0   &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[10]",
        "exact_source_quote": "\"component_name\": \"25% HCl\",\n          \"volume\": 5,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q47",
    "ingredient": "Na2SeO4",
    "decision": "add",
    "stage": "Receiving trace-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 31; Na 2 SeO 4 / 94.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;4&lt;/sub&gt;                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;94.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[11]",
        "exact_source_quote": "\"component_name\": \"Na2SeO4\",\n          \"volume\": 94,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "Represent the exact named trace-stock batch amount in the receiving recipe. Missing nested composition is separate from the parent quantity problem; no whole-parent formulation transfer."
  },
  {
    "decision_id": "q48",
    "ingredient": "Na2SeO4",
    "decision": "correct",
    "stage": "Existing scoped M940 trace constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "94",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace preparation only; raw HTML row 31; Na 2 SeO 4 / 94.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;4&lt;/sub&gt;                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;94.0  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638"
      },
      {
        "source_key": "togoM940original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940",
        "source_locator": "$.components[3].items[11]",
        "exact_source_quote": "\"component_name\": \"Na2SeO4\",\n          \"volume\": 94,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8"
      }
    ],
    "interpretation": "The parent flattens batch quantities into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock membership. Its water field also combines unrelated parent waters. No final stock volume is independently established."
  },
  {
    "decision_id": "q49",
    "ingredient": "Trace acid strength",
    "decision": "add",
    "stage": "JCM899 trace-stock acid",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace-stock acid; Trace acid strength",
        "exact_source_quote": "25% HCl 5.0 ml",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638",
        "parsed_text_sha256": "1d083a65546e065a4cf390cd836d1aa0de38be6a32596205efc79dc1add7ec7c"
      }
    ],
    "interpretation": "Keep 25% strength and 5 ml dose distinct. Percentage basis and density are not stated; no molarity or mass conversion."
  },
  {
    "decision_id": "q50",
    "ingredient": "Trace preparation order",
    "decision": "add",
    "stage": "JCM899 trace stock only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm899",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899",
        "source_locator": "JCM899 trace stock only; Trace preparation order",
        "exact_source_quote": "Dissolve (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O in 25% HCl first, then dilute in distilled water.  Add the remaining salts in the sequence indicated",
        "snapshot_sha256": "2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638",
        "parsed_text_sha256": "1d083a65546e065a4cf390cd836d1aa0de38be6a32596205efc79dc1add7ec7c"
      }
    ],
    "interpretation": "Preserve the exact iron-first acid sequence; parent main pH, gas and vitamin formulation are outside transfer."
  },
  {
    "decision_id": "q51",
    "ingredient": "Distilled water",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 25; Distilled water / 1.0 / L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q52",
    "ingredient": "Distilled water",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
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
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 25; Distilled water / 1.0 / L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in concentration with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q53",
    "ingredient": "Biotin",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 15; Biotin / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q54",
    "ingredient": "Biotin",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 15; Biotin / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q55",
    "ingredient": "p--Aminobenzoic acid",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 23; p -Aminobenzoic acid / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q56",
    "ingredient": "p--Aminobenzoic acid",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 23; p -Aminobenzoic acid / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q57",
    "ingredient": "Thiamine・HCl",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 18; Thiamine·HCl / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q58",
    "ingredient": "Thiamine・HCl",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 18; Thiamine·HCl / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q59",
    "ingredient": "Calcium pantothenate",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 21; Calcium pantothenate / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q60",
    "ingredient": "Calcium pantothenate",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 21; Calcium pantothenate / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q61",
    "ingredient": "Pyridoxine・HCl",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 17; Pyridoxine·HCl / 10.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q62",
    "ingredient": "Pyridoxine・HCl",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 17; Pyridoxine·HCl / 10.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q63",
    "ingredient": "Folic acid",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 16; Folic acid / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q64",
    "ingredient": "Folic acid",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 16; Folic acid / 2.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q65",
    "ingredient": "Vitamin B12",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 22; Vitamin B 1 2 / 0.1 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q66",
    "ingredient": "Vitamin B12",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 22; Vitamin B 1 2 / 0.1 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q67",
    "ingredient": "Riboflavin",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 19; Riboflavin / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q68",
    "ingredient": "Riboflavin",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[8].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 19; Riboflavin / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q69",
    "ingredient": "Nicotinic acid",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 20; Nicotinic acid / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q70",
    "ingredient": "Nicotinic acid",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[9].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 20; Nicotinic acid / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  },
  {
    "decision_id": "q71",
    "ingredient": "Lipoic acid",
    "decision": "add",
    "stage": "Receiving vitamin-stock representation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 24; Lipoic acid / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Add the named source-stock batch amount without importing parent basal medium or its final-volume assumptions."
  },
  {
    "decision_id": "q72",
    "ingredient": "Lipoic acid",
    "decision": "verified",
    "stage": "Existing M190 vitamin stock only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[10].notes",
        "stored": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins only; raw HTML row 24; Lipoic acid / 5.0 / mg",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "interpretation": "Existing scoped parent value, unit and batch basis are retained in notes with matching attached source snippet and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target evidence or chemical-form certification is inherited."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:007857.

9 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 9/10 primary and 7/10 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 10: primary 90.00%; secondary 70.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact source and excluded namesake

identity: supported. Targets: CultureMech:007857.

JCM1228 and TOGO M1320 resolve the sole maintained bacterial contributor. The specialized namesake has a different stable ID and is excluded. Its legacy000198 does not constrain this review; accession-conditioned JCM32929 is retained without a new growth assertion.

### Stock identity and stage membership

identity: concern. Targets: CultureMech:007857.

5342/5343 resolve but are wrong formulations for the A/B recipes. Their API volume and g_l fields are null and preparations say 500 ml. M940 transfers only trace elements; M190 transfers only vitamins.

### Scoped source chemical specificity

grounding: concern. Targets: CultureMech:007857.

Main magnesium hexahydrate and other represented main chemical forms are consistent with the primary. Scoped M940 cobalt hexahydrate is linked to anhydrous CHEBI35696; M190 generic calcium pantothenate does not establish the D-specific structure of CHEBI31345. Other unrelated parent groundings are excluded. No replacement identifier is guessed.

### A/B handling and conditional formulation

completeness: concern. Targets: CultureMech:007857.

Both layers lack separate A/B preparations, explicit source default cycle, final target pH and filter-sterile vitamin handling. The two JCM32929 supplements are flattened into universal solution entries.

### Mixture and organism scope

scope: supported. Targets: CultureMech:007857.

COMPLEX/SEMI_DEFINED and LIQUID are compatible with the source mixture and yeast extract. No source-supported organism growth or target incubation temperature is inferred from the title or accession note.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007857.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained fixes and regeneration boundary

ownership: concern. Targets: CultureMech:007857.

The maintained owner has the same scientific claims as the target and lacks the generated merge event. Correct owner scope and evidence first; do not edit the generated target or the unrelated stock records to force identity.

### Claim-level support and historical scope

evidence: concern. Targets: CultureMech:007857.

Target and maintained owner have no attached quantity/preparation evidence. Eleven M190 stock amounts are locally evidenced and hash-authenticated; that evidence does not attach to target claims or prove chemical specificity. The parent-only sulfide metadata override does not alter vitamin transfer.

## Findings

### f1: Solution A/B links identify unrelated stocks

blocker / open / confirmed; issue key: culturemech.007857.wrong-stock-identities.

Both layers link to solutions 5342/5343 despite incompatible source formulations.

### f2: Batch and stock quantities are flattened into mass concentrations

major / open / confirmed; issue key: culturemech.007857.stage-units-and-stock-expansion.

Main water and all receiving liquid doses use G_PER_L; A/B batch masses lack their source-stage basis. Trace parent mg values are also flattened as grams per liter, while target stocks are empty.

### f3: Conditional supplements and preparation are incomplete

major / open / confirmed; issue key: culturemech.007857.conditional-preparation.

JCM32929-only peptone and sulfide are represented universally; separate autoclaving, final target pH and vitamin handling are missing.

### f4: Transferred stock forms need source-specific grounding

major / open / confirmed; issue key: culturemech.007857.transferred-form-specificity.

M940 cobalt hexahydrate uses anhydrous CHEBI35696; generic M190 calcium pantothenate does not establish D-specific grounding.

### f5: Source links do not provide claim-level evidence

minor / open / confirmed; issue key: culturemech.007857.attached-evidence.

Both receiving layers lack attached amount and preparation evidence; parent stock evidence must retain its exact layer.

## Recommended Actions And Acceptance Checks

### a1

Resolve source-defined A/B identities and represent exact compositions before any replacement link or regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore stage-specific batch amounts, volume units, named stock composition and claim-level evidence; preserve existing authenticated vitamin batch notes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the accession-conditioned variant and exact per-liter dose, percentage ambiguity and preparation order; add only supported pH and source default cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Verify the exact supplied forms and qualify unresolved stereochemistry before linking or copying parent groundings; do not invent replacement IDs.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach exact source snippets, locators, original access times and hashes to each curated receiving claim and preserve existing history.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch036/354/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch036/354/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml:1:id: CultureMech:007857<br>./data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml:1:id: CultureMech:007857<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch036/source-preflight-bound/354/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 57 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| scope-addenda | /private/tmp/culturemech-review-work-batch036/source-preflight-bound/354/source-context-addenda.json; Exact bound interpretation addendum and its parent-only scope | context_only | The recovered JCM197 raw hash and nonliteral compact sulfide snippet are distinguished. That sulfide claim is excluded from vitamin transfer. Legacy000198 belongs only to the excluded specialized namesake; actual M940 sodium selenate uses CHEBI:77775 in both slots. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228; JCM1228 complete A/B recipe, handling and conditional JCM32929 branch | supports | Exact source stages and amounts; other parent-medium sections do not transfer. |
| trace-source | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899; JCM899 Trace element solution subsection only | supports | Exact source stages and amounts; other parent-medium sections do not transfer. |
| vitamin-source | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; JCM197 Trace vitamins subsection only | supports | Exact source stages and amounts; other parent-medium sections do not transfer. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320; $.meta and components[0..4], all comments | supports | TOGO identifies JCM1228 and preserves A/B, post-mix vitamin and conditional supplement stages. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch036/354/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| scoped-grounding | /private/tmp/culturemech-review-work-batch036/354/grounding-inventory.json; Every primary and current CHEBI secondary slot in target, owner and transferred constituents | context_only | Exact OLS label/obsolete checks and scoped source-form comparisons. No legacy000198 occurs in actual target, owner or transferred M940 record. |
| chebi35696-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS structure, formula and stereochemistry | supports | CHEBI35696 is anhydrous cobalt dichloride; CHEBI31345 specifies calcium pantothenate stereochemistry beyond generic source wording. |
| chebi31345-form | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS structure, formula and stereochemistry | supports | CHEBI35696 is anhydrous cobalt dichloride; CHEBI31345 specifies calcium pantothenate stereochemistry beyond generic source wording. |
| solution5342 | https://mediadive.dsmz.de/rest/solution/5342; Complete exact referenced solution API | refutes | The resolved high-salt stock is compositionally unrelated to JCM1228 A/B; comparison only, no ingredient transfer. |
| solution5343 | https://mediadive.dsmz.de/rest/solution/5343; Complete exact referenced solution API | refutes | The resolved high-salt stock is compositionally unrelated to JCM1228 A/B; comparison only, no ingredient transfer. |
| history-metadata | data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml; data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml", "events": 12, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, generic stock-name resolver and numerical cleanup are relevant mechanisms; they are not proof of historical execution or source-specific stock equivalence. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, generic stock-name resolver and numerical cleanup are relevant mechanisms; they are not proof of historical execution or source-specific stock equivalence. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, generic stock-name resolver and numerical cleanup are relevant mechanisms; they are not proof of historical execution or source-specific stock equivalence. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, generic stock-name resolver and numerical cleanup are relevant mechanisms; they are not proof of historical execution or source-specific stock equivalence. |
| mediadiveJ1228api-attempt | https://mediadive.dsmz.de/rest/medium/J1228; Preserved exact public retrieval result | context_only | The current optional MediaDive J1228 API and preserved retry returned503. Exact JCM1228 and original TOGO content are available; historical byte equivalence is not inferred. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The current optional MediaDive J1228 API and preserved retry returned503. Exact JCM1228 and original TOGO content are available; historical byte equivalence is not inferred.
- No measured final-volume, unspecified percent basis, gas fraction or pressure is invented. Parent JCM899 basal/vitamin and JCM197 basal/mineral/reducing claims are excluded.
- Legacy000198 is an excluded-name comparison only. Its bounded current absence and unresolved historical correspondence do not make this actual target review partial.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T194412Z-culturemech-007857-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobic_alkaline_glucose_medium (CultureMech:007857)'
started_at: '2026-10-21T19:39:56Z'
finished_at: '2026-10-21T19:44:12Z'
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
summary: The exact JCM1228 recipe is available, but the target and owner flatten separate
  A/B preparations, store liquid additions as mass concentrations, link unrelated
  stocks, and generalize a JCM32929-only supplement branch. Named trace and vitamin
  stocks require separate source and chemical-form accounting.
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
  - path: data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
    sha256: ca75517cccb368eb6ac098751cb45242fad1d4ed39b212b7df519cf654dcd312
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml
    sha256: c1ceeaa10137bc48e7cc7ee584f964ba6f38189c776b21f4db2fda3f8a3a393a
    role: context
  - path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
    sha256: 1115025f1299031e86853d5a89c5eb3a52e65a598ef8efda49e2d015582fffd5
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
    role: context
  - path: data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml
    sha256: 9f2b703f1065a3f2fa8e9b23bad3a68126006e2c3e5af82ff2ef0581cec7c63c
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
  selection: Task review 354; batch 036 item 4 of 10, selected in Python lexicographic
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
  - CultureMech:007857
targets:
- target_id: CultureMech:007857
  path: data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  label: anaerobic_alkaline_glucose_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch036/354/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch036/354/strict.tsv"
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007857
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
  - CultureMech:007857
- check_id: mediadiveJ1228api-source-access
  name: 'Exact source content access: mediadiveJ1228api'
  required: false
  status: unavailable
  summary: The current optional MediaDive J1228 API and preserved retry returned503.
    Exact JCM1228 and original TOGO content are available; historical byte equivalence
    is not inferred.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - mediadiveJ1228api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:40:57.542778Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch036/354/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:40:58.877133Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-036/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch036/354/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:00.189589Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:41:01.118832Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:44:10Z'
  support: supports
  summary: './data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml:1:id:
    CultureMech:007857

    ./data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml:1:id:
    CultureMech:007857

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/source-preflight-bound/354/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:44:10Z'
  support: supports
  summary: 57 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 8aa45e7ded3ec0e78290997879b2695e5fe2b03bcc4bacdfd17bb6f02afa2165
- evidence_id: scope-addenda
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/source-preflight-bound/354/source-context-addenda.json
  locator: Exact bound interpretation addendum and its parent-only scope
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: The recovered JCM197 raw hash and nonliteral compact sulfide snippet are
    distinguished. That sulfide claim is excluded from vitamin transfer. Legacy000198
    belongs only to the excluded specialized namesake; actual M940 sodium selenate
    uses CHEBI:77775 in both slots.
  snapshot_sha256: 0a1137876da0f99419a9b58731cd5654db2e390a27038ff692718419c38d2fcb
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228
  locator: JCM1228 complete A/B recipe, handling and conditional JCM32929 branch
  accessed_at: '2026-10-21T19:22:06.186618Z'
  support: supports
  summary: Exact source stages and amounts; other parent-medium sections do not transfer.
  quote: 'Solution A: NaCl 20.0 g Na 2 CO 3 50.0 g NaHCO 3 60.0 g Distilled water
    900.0 ml Mix components thoroughly and autoclave under a N 2 gas atmosphere. Solution
    B: MgCl 2 ·6H 2 O 0.1 g NH 4 Cl 0.5 g KH 2 PO 4 0.2 g Yeast extract 0.05 g Glucose
    3.0 g Trace element solution (see Medium No. 899 ) 1.0 ml Distilled water 100.0
    ml Mix components thoroughly and autoclave under a N 2 gas atmosphere. Aseptically
    and anaerobically combine Solutions A and B.  Check final pH of the medium to
    be around 9.2.  Add the following solution into the medium (filter-sterilized
    and stored under a N 2 atmosphere): Trace vitamins (see Medium No. 197 ) 10.0
    ml Comment: For JCM 32929, aseptically and anaerobically add per liter the following
    solutions (autoclaved and stored under a N 2 atmosphere): 10% Peptone solution
    10.0 ml 5% Na 2 S·9H 2 O solution 6.0 ml'
  snapshot_sha256: 299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847
- evidence_id: trace-source
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899
  locator: JCM899 Trace element solution subsection only
  accessed_at: '2026-10-21T19:22:06.277896Z'
  support: supports
  summary: Exact source stages and amounts; other parent-medium sections do not transfer.
  quote: 'Trace element solution: (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O 784.0 mg 25% HCl 5.0
    ml CoCl 2 ·6H 2 O 238.0 mg (NH 4 ) 2 Ni(SO 4 ) 2 •6H 2 O 395.0 mg Na 2 MoO 4 ·2H
    2 O 36.0 mg Na 2 WO 4 ·2H 2 O 33.0 mg ZnSO 4 ·7H 2 O 144.0 mg CuCl 2 ·2H 2 O 2.0
    mg Na 2 SeO 4 94.0 mg H 3 BO 3 6.0 mg MnCl 2 ·4H 2 O 99.0 mg Distilled water 995.0
    ml Dissolve (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O in 25% HCl first, then dilute in distilled
    water.  Add the remaining salts in the sequence indicated'
  snapshot_sha256: 2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638
- evidence_id: vitamin-source
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: JCM197 Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Exact source stages and amounts; other parent-medium sections do not transfer.
  quote: 'Trace vitamins: Biotin 2.0 mg Folic acid 2.0 mg Pyridoxine·HCl 10.0 mg Thiamine·HCl
    5.0 mg Riboflavin 5.0 mg Nicotinic acid 5.0 mg Calcium pantothenate 5.0 mg Vitamin
    B 1 2 0.1 mg p -Aminobenzoic acid 5.0 mg Lipoic acid 5.0 mg Distilled water 1.0
    L'
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320
  locator: $.meta and components[0..4], all comments
  accessed_at: '2026-10-21T19:22:04.022285Z'
  support: supports
  summary: TOGO identifies JCM1228 and preserves A/B, post-mix vitamin and conditional
    supplement stages.
  quote: '"original_media_id": "JCM_M1228"'
  snapshot_sha256: bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/354/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7286db1e4340d26af8c8aa826d87a58e14979de3811c340031fd53ddfc1f3d44
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T19:44:10Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id":
    "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: scoped-grounding
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch036/354/grounding-inventory.json
  locator: Every primary and current CHEBI secondary slot in target, owner and transferred
    constituents
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Exact OLS label/obsolete checks and scoped source-form comparisons. No
    legacy000198 occurs in actual target, owner or transferred M940 record.
  snapshot_sha256: 87d746df74de35c669e54a2dac2df60f34ff2e4a78e1973f11a90b0711846a19
- evidence_id: chebi35696-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS structure, formula and stereochemistry
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI35696 is anhydrous cobalt dichloride; CHEBI31345 specifies calcium
    pantothenate stereochemistry beyond generic source wording.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi31345-form
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS structure, formula and stereochemistry
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI35696 is anhydrous cobalt dichloride; CHEBI31345 specifies calcium
    pantothenate stereochemistry beyond generic source wording.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: solution5342
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: Complete exact referenced solution API
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: refutes
  summary: The resolved high-salt stock is compositionally unrelated to JCM1228 A/B;
    comparison only, no ingredient transfer.
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
- evidence_id: solution5343
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: Complete exact referenced solution API
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: refutes
  summary: The resolved high-salt stock is compositionally unrelated to JCM1228 A/B;
    comparison only, no ingredient transfer.
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
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml; data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml", "events":
    12, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Current importer, generic stock-name resolver and numerical cleanup are
    relevant mechanisms; they are not proof of historical execution or source-specific
    stock equivalence.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Current importer, generic stock-name resolver and numerical cleanup are
    relevant mechanisms; they are not proof of historical execution or source-specific
    stock equivalence.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Current importer, generic stock-name resolver and numerical cleanup are
    relevant mechanisms; they are not proof of historical execution or source-specific
    stock equivalence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:44:10Z'
  support: context_only
  summary: Current importer, generic stock-name resolver and numerical cleanup are
    relevant mechanisms; they are not proof of historical execution or source-specific
    stock equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: mediadiveJ1228api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1228
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:22:02.343070Z'
  support: context_only
  summary: The current optional MediaDive J1228 API and preserved retry returned503.
    Exact JCM1228 and original TOGO content are available; historical byte equivalence
    is not inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 72 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"Distilled\
    \ water\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM1228 Solution\
    \ A preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution A preparation; raw HTML row\
    \ 3; Distilled water / 900.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Distilled water                                       </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;900.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\n      }\n\
    \    ],\n    \"interpretation\": \"Preserve the printed batch mass or water volume\
    \ in this preparation. Both layers collapse the source stages into final-medium\
    \ G_PER_L; neither stock preparation volume nor summed water establishes a measured\
    \ final volume. No attached amount evidence is present.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"ingredient\": \"NaCl\",\n    \"decision\": \"correct\",\n   \
    \ \"stage\": \"JCM1228 Solution A preparation\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution A preparation; raw HTML row\
    \ 0; NaCl / 20.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ NaCl                                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 20,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q3\",\n    \"ingredient\": \"NaHCO3\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"JCM1228 Solution A preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"60\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"60\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution A preparation; raw HTML row\
    \ 2; NaHCO 3 / 60.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ NaHCO<sub>3</sub>                                              </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;60.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 60,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"Na2CO3\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"JCM1228 Solution A preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution A preparation; raw HTML row\
    \ 1; Na 2 CO 3 / 50.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>CO<sub>3</sub>                                           </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;50.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 50,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q5\",\n    \"ingredient\": \"Distilled water\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM1228 Solution B preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution B preparation; raw HTML row\
    \ 10; Distilled water / 100.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Distilled water                                       </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\n      }\n\
    \    ],\n    \"interpretation\": \"Preserve the printed batch mass or water volume\
    \ in this preparation. Both layers collapse the source stages into final-medium\
    \ G_PER_L; neither stock preparation volume nor summed water establishes a measured\
    \ final volume. No attached amount evidence is present.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"ingredient\": \"Yeast extract\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"JCM1228 Solution B preparation\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution B preparation; raw HTML row\
    \ 7; Yeast extract / 0.05 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Yeast extract                                           </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.05&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 0.05,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\n      }\n\
    \    ],\n    \"interpretation\": \"Preserve the printed batch mass or water volume\
    \ in this preparation. Both layers collapse the source stages into final-medium\
    \ G_PER_L; neither stock preparation volume nor summed water establishes a measured\
    \ final volume. No attached amount evidence is present.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"ingredient\": \"KH2PO4\",\n    \"decision\": \"correct\",\n \
    \   \"stage\": \"JCM1228 Solution B preparation\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution B preparation; raw HTML row\
    \ 6; KH 2 PO 4 / 0.2 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q8\",\n    \"ingredient\": \"NH4Cl\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"JCM1228 Solution B preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution B preparation; raw HTML row\
    \ 5; NH 4 Cl / 0.5 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ NH<sub>4</sub>Cl                                                </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q9\",\n    \"ingredient\": \"MgCl2・6H2O\",\n    \"\
    decision\": \"correct\",\n    \"stage\": \"JCM1228 Solution B preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution B preparation; raw HTML row\
    \ 4; MgCl 2 ·6H 2 O / 0.1 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q10\",\n    \"ingredient\": \"Glucose\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"JCM1228 Solution B preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM1228 Solution B preparation; raw HTML row\
    \ 8; Glucose / 3.0 / g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Glucose                                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Glucose\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed batch mass or\
    \ water volume in this preparation. Both layers collapse the source stages into\
    \ final-medium G_PER_L; neither stock preparation volume nor summed water establishes\
    \ a measured final volume. No attached amount evidence is present.\"\n  },\n \
    \ {\n    \"decision_id\": \"q11\",\n    \"ingredient\": \"Solution A receiving\
    \ addition\",\n    \"decision\": \"correct\",\n    \"stage\": \"TOGO assembly\
    \ layer\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1320original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 900,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      },\n      {\n        \"source_key\": \"jcm1228\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\",\n        \"source_locator\"\
    : \"JCM1228 A/B combination sentence\",\n        \"exact_source_quote\": \"Aseptically\
    \ and anaerobically combine Solutions A and B.\",\n        \"snapshot_sha256\"\
    : \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\",\n    \
    \    \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"TOGO explicitly lists 900 ml and\
    \ 100 ml assembly additions; JCM defines A/B then instructs combination. Preserve\
    \ that provenance difference and correct G_PER_L to volume; do not add these doses\
    \ again as extra stock water.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n  \
    \  \"ingredient\": \"Solution B receiving addition\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"TOGO assembly layer\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1320original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      },\n      {\n        \"source_key\": \"jcm1228\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\",\n        \"source_locator\"\
    : \"JCM1228 A/B combination sentence\",\n        \"exact_source_quote\": \"Aseptically\
    \ and anaerobically combine Solutions A and B.\",\n        \"snapshot_sha256\"\
    : \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\",\n    \
    \    \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"TOGO explicitly lists 900 ml and\
    \ 100 ml assembly additions; JCM defines A/B then instructs combination. Preserve\
    \ that provenance difference and correct G_PER_L to volume; do not add these doses\
    \ again as extra stock water.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n  \
    \  \"ingredient\": \"Trace element solution (see Medium [M940])\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Solution B trace dose\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"Solution B trace dose; raw HTML row 9; Trace\
    \ element solution (see Medium No. 899 ) / 1.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Trace element solution (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=899\\\
    \">899</a>)           </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M940])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"The source amount is ml, not G_PER_L.\
    \ Retain the named stock and stage; the JCM32929 supplements are conditional per-liter\
    \ additions and must not become universal basal ingredients.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q14\",\n    \"ingredient\": \"Trace vitamins (see Medium\
    \ [M190])\",\n    \"decision\": \"correct\",\n    \"stage\": \"Post-combination\
    \ vitamin dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"Post-combination vitamin dose; raw HTML row 11;\
    \ Trace vitamins (see Medium No. 197 ) / 10.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Trace vitamins (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=197\\\
    \">197</a>)                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"The source amount is ml, not G_PER_L.\
    \ Retain the named stock and stage; the JCM32929 supplements are conditional per-liter\
    \ additions and must not become universal basal ingredients.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q15\",\n    \"ingredient\": \"5% Na2S・9H2O solution\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM32929-only sulfide addition\
    \ per liter\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM32929-only sulfide addition per liter; raw\
    \ HTML row 13; 5% Na 2 S·9H 2 O solution / 6.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\",\n\
    \        \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 6,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\
    \n      }\n    ],\n    \"interpretation\": \"The source amount is ml, not G_PER_L.\
    \ Retain the named stock and stage; the JCM32929 supplements are conditional per-liter\
    \ additions and must not become universal basal ingredients.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q16\",\n    \"ingredient\": \"10% Peptone solution\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"JCM32929-only peptone addition\
    \ per liter\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM32929-only peptone addition per liter; raw\
    \ HTML row 12; 10% Peptone solution / 10.0 / ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 10% Peptone solution </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      },\n      {\n        \"source_key\": \"togoM1320original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1320\"\
    ,\n        \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% Peptone solution\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"bb7850ed4f3d0dde5feb32c90e5255932cfc9fcd64526d3a3935c74eaabb1f38\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The source amount is ml, not G_PER_L. Retain\
    \ the named stock and stage; the JCM32929 supplements are conditional per-liter\
    \ additions and must not become universal basal ingredients.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q17\",\n    \"ingredient\": \"Nitrogen atmosphere\",\n \
    \   \"decision\": \"not_quantified\",\n    \"stage\": \"Separate A/B sterilization\
    \ and stock storage\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"Separate A/B sterilization and stock storage;\
    \ Nitrogen atmosphere\",\n        \"exact_source_quote\": \"Mix components thoroughly\
    \ and autoclave under a N 2 gas atmosphere.\",\n        \"snapshot_sha256\": \"\
    299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\",\n        \"\
    parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE correctly avoids an invented\
    \ gas fraction; source N2 identity and separate handling need evidence. No 100%\
    \ or pressure is supplied.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"\
    ingredient\": \"sulfide stock strength\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"JCM32929-only stock preparation\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM32929-only stock strength; raw HTML row 13;\
    \ 5% Na 2 S·9H 2 O solution / 6.0 / ml\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Retain literal 5% stock strength with unspecified\
    \ percentage basis, distinct from receiving dose. Do not convert to g/L, infer\
    \ density or treat the supplement as universal.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"ingredient\": \"peptone stock strength\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"JCM32929-only stock preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM32929-only stock strength; raw HTML row 12;\
    \ 10% Peptone solution / 10.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> 10% Peptone solution </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain literal 10% stock strength\
    \ with unspecified percentage basis, distinct from receiving dose. Do not convert\
    \ to g/L, infer density or treat the supplement as universal.\"\n  },\n  {\n \
    \   \"decision_id\": \"q20\",\n    \"ingredient\": \"Conditional branch denominator\
    \ and accession\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM32929\
    \ supplementation\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": [\n          {\n            \"preferred_term\"\
    : \"Solution A\",\n            \"term\": {\n              \"id\": \"mediadive.solution:5342\"\
    ,\n              \"label\": \"Solution A\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"900\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"notes\": \"See mediadive_5342_Solution_A.yaml for\
    \ composition\",\n            \"name\": \"Unknown solution\"\n          },\n \
    \         {\n            \"preferred_term\": \"Solution B\",\n            \"term\"\
    : {\n              \"id\": \"mediadive.solution:5343\",\n              \"label\"\
    : \"Solution B\"\n            },\n            \"concentration\": {\n         \
    \     \"value\": \"100\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"notes\": \"See mediadive_5343_Solution_B.yaml for composition\"\
    ,\n            \"name\": \"Unknown solution\"\n          },\n          {\n   \
    \         \"preferred_term\": \"Trace element solution (see Medium [M940])\",\n\
    \            \"composition\": [],\n            \"notes\": \"Cross-reference to\
    \ Medium M940\",\n            \"concentration\": {\n              \"value\": \"\
    1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"name\"\
    : \"Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace vitamins (see Medium [M190])\",\n            \"composition\": [],\n\
    \            \"notes\": \"Cross-reference to Medium M190\",\n            \"concentration\"\
    : {\n              \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"name\": \"Unknown solution\"\n          },\n   \
    \       {\n            \"preferred_term\": \"5% Na2S・9H2O solution\",\n      \
    \      \"composition\": [],\n            \"concentration\": {\n              \"\
    value\": \"6\",\n              \"unit\": \"G_PER_L\"\n            },\n       \
    \     \"notes\": \"Role: Reducing agent; Properties: Defined component, Inorganic\
    \ compound, Solution\",\n            \"name\": \"Unknown solution\"\n        \
    \  },\n          {\n            \"preferred_term\": \"10% Peptone solution\",\n\
    \            \"composition\": [],\n            \"concentration\": {\n        \
    \      \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"notes\": \"Properties: Undefined component\",\n            \"name\"\
    : \"Unknown solution\"\n          }\n        ]\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Solution A\",\n            \"term\": {\n  \
    \            \"id\": \"mediadive.solution:5342\",\n              \"label\": \"\
    Solution A\"\n            },\n            \"concentration\": {\n             \
    \ \"value\": \"900\",\n              \"unit\": \"G_PER_L\"\n            },\n \
    \           \"notes\": \"See mediadive_5342_Solution_A.yaml for composition\"\
    ,\n            \"name\": \"Unknown solution\"\n          },\n          {\n   \
    \         \"preferred_term\": \"Solution B\",\n            \"term\": {\n     \
    \         \"id\": \"mediadive.solution:5343\",\n              \"label\": \"Solution\
    \ B\"\n            },\n            \"concentration\": {\n              \"value\"\
    : \"100\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    notes\": \"See mediadive_5343_Solution_B.yaml for composition\",\n           \
    \ \"name\": \"Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M940])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M940\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          },\n          {\n\
    \            \"preferred_term\": \"5% Na2S・9H2O solution\",\n            \"composition\"\
    : [],\n            \"concentration\": {\n              \"value\": \"6\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"notes\": \"Role:\
    \ Reducing agent; Properties: Defined component, Inorganic compound, Solution\"\
    ,\n            \"name\": \"Unknown solution\"\n          },\n          {\n   \
    \         \"preferred_term\": \"10% Peptone solution\",\n            \"composition\"\
    : [],\n            \"concentration\": {\n              \"value\": \"10\",\n  \
    \            \"unit\": \"G_PER_L\"\n            },\n            \"notes\": \"\
    Properties: Undefined component\",\n            \"name\": \"Unknown solution\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"JCM32929 supplementation; Conditional branch\
    \ denominator and accession\",\n        \"exact_source_quote\": \"For JCM 32929,\
    \ aseptically and anaerobically add per liter the following solutions\",\n   \
    \     \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    ,\n        \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"The per-liter basis and accession\
    \ restriction are explicit and absent from the local solution claims; no independent\
    \ strain growth observation is inferred.\"\n  },\n  {\n    \"decision_id\": \"\
    q21\",\n    \"ingredient\": \"Final target pH\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"After A/B combination, before listed vitamin addition\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1228\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"After A/B combination, before listed vitamin\
    \ addition; Final target pH\",\n        \"exact_source_quote\": \"Check final\
    \ pH of the medium to be around 9.2.\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    ,\n        \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"Record approximate target pH 9.2\
    \ at this source stage, not measured pH.\"\n  },\n  {\n    \"decision_id\": \"\
    q22\",\n    \"ingredient\": \"Default sterilization temperature and duration\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"A/B and conditional autoclaved\
    \ stocks unless exception\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\",\n       \
    \ \"field_path\": \"sterilization\",\n        \"stored\": null\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"A/B and conditional autoclaved stocks unless\
    \ exception; Default sterilization temperature and duration\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    ,\n        \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"The exact source page supplies 121\
    \ C for 15 min. The filter-sterilized vitamin addition is an explicit exception;\
    \ no extra pressure is supplied.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n\
    \    \"ingredient\": \"A/B combination and vitamin handling\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"Aseptic anaerobic assembly and stock storage\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"Aseptic anaerobic assembly and stock storage;\
    \ A/B combination and vitamin handling\",\n        \"exact_source_quote\": \"\
    Aseptically and anaerobically combine Solutions A and B.  Check final pH of the\
    \ medium to be around 9.2.  Add the following solution into the medium (filter-sterilized\
    \ and stored under a N 2 atmosphere):\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    ,\n        \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the exact order, filtering and\
    \ N2 storage. Do not import JCM197 parent basal gases or pH.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q24\",\n    \"ingredient\": \"Final measured volume\",\n\
    \    \"decision\": \"not_quantified\",\n    \"stage\": \"Complete receiving batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1228\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1228\"\
    ,\n        \"source_locator\": \"Complete receiving batch; Final measured volume\"\
    ,\n        \"exact_source_quote\": \"Trace vitamins (see Medium No. 197 ) 10.0\
    \ ml\",\n        \"snapshot_sha256\": \"299de672d2a4da461c14feff084b0aa798d6eac36c8ac9518a47119fff4b6847\"\
    ,\n        \"parsed_text_sha256\": \"1d2b5829cae4177b1418b45d6343712d850037e02baccfcee394f2e1cc5ced1b\"\
    \n      }\n    ],\n    \"interpretation\": \"Basal water inputs total 1000 ml\
    \ and later additions are listed; no measured final-volume or make-up instruction\
    \ is supplied. Do not flatten stocks or assume final concentrations.\"\n  },\n\
    \  {\n    \"decision_id\": \"q25\",\n    \"ingredient\": \"Distilled water\",\n\
    \    \"decision\": \"add\",\n    \"stage\": \"Receiving trace-stock representation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 34;\
    \ Distilled water / 995.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;995.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 995,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n      }\n\
    \    ],\n    \"interpretation\": \"Represent the exact named trace-stock batch\
    \ amount in the receiving recipe. Missing nested composition is separate from\
    \ the parent quantity problem; no whole-parent formulation transfer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q26\",\n    \"ingredient\": \"Distilled water\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace constituent\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"997.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 34;\
    \ Distilled water / 995.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;995.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 995,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n      }\n\
    \    ],\n    \"interpretation\": \"The parent flattens batch quantities into G_PER_L,\
    \ including mg-scale salts and liquid inputs; preserve mg or ml and stock membership.\
    \ Its water field also combines unrelated parent waters. No final stock volume\
    \ is independently established.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n\
    \    \"ingredient\": \"Na2MoO4·2H2O\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Receiving trace-stock representation\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 27;\
    \ Na 2 MoO 4 ·2H 2 O / 36.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O              \
    \   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4·2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n      }\n\
    \    ],\n    \"interpretation\": \"Represent the exact named trace-stock batch\
    \ amount in the receiving recipe. Missing nested composition is separate from\
    \ the parent quantity problem; no whole-parent formulation transfer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q28\",\n    \"ingredient\": \"Na2MoO4·2H2O\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace constituent\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 27;\
    \ Na 2 MoO 4 ·2H 2 O / 36.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O              \
    \   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4·2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n      }\n\
    \    ],\n    \"interpretation\": \"The parent flattens batch quantities into G_PER_L,\
    \ including mg-scale salts and liquid inputs; preserve mg or ml and stock membership.\
    \ Its water field also combines unrelated parent waters. No final stock volume\
    \ is independently established.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n\
    \    \"ingredient\": \"H3BO3\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Receiving trace-stock representation\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 32;\
    \ H 3 BO 3 / 6.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ H<sub>3</sub>BO<sub>3</sub>                                            </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0   &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q30\",\n    \"ingredient\": \"H3BO3\",\n  \
    \  \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace constituent\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 32;\
    \ H 3 BO 3 / 6.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ H<sub>3</sub>BO<sub>3</sub>                                            </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0   &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q31\",\n    \"ingredient\": \"MnCl2·4H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 33;\
    \ MnCl 2 ·4H 2 O / 99.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                              </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;99.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2·4H2O\\\",\\n          \\\"volume\\\": 99,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q32\",\n    \"ingredient\": \"MnCl2·4H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"99\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 33;\
    \ MnCl 2 ·4H 2 O / 99.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                              </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;99.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2·4H2O\\\",\\n          \\\"volume\\\": 99,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q33\",\n    \"ingredient\": \"CoCl2·6H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 25;\
    \ CoCl 2 ·6H 2 O / 238.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                             </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;238.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2·6H2O\\\",\\n          \\\"volume\\\": 238,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q34\",\n    \"ingredient\": \"CoCl2·6H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"238\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 25;\
    \ CoCl 2 ·6H 2 O / 238.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                             </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;238.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2·6H2O\\\",\\n          \\\"volume\\\": 238,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q35\",\n    \"ingredient\": \"ZnSO4·7H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 29;\
    \ ZnSO 4 ·7H 2 O / 144.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                             </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;144.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4·7H2O\\\",\\n          \\\"volume\\\": 144,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q36\",\n    \"ingredient\": \"ZnSO4·7H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"144\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 29;\
    \ ZnSO 4 ·7H 2 O / 144.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                             </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;144.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4·7H2O\\\",\\n          \\\"volume\\\": 144,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q37\",\n    \"ingredient\": \"CuCl2·2H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 30;\
    \ CuCl 2 ·2H 2 O / 2.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0   &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2·2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q38\",\n    \"ingredient\": \"CuCl2·2H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 30;\
    \ CuCl 2 ·2H 2 O / 2.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0   &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2·2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q39\",\n    \"ingredient\": \"Na2WO4·2H2O\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 28;\
    \ Na 2 WO 4 ·2H 2 O / 33.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Na<sub>2</sub>WO<sub>4</sub>&#183;2H<sub>2</sub>O               \
    \             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;33.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4·2H2O\\\",\\n          \\\"volume\\\": 33,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q40\",\n    \"ingredient\": \"Na2WO4·2H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"33\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 28;\
    \ Na 2 WO 4 ·2H 2 O / 33.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Na<sub>2</sub>WO<sub>4</sub>&#183;2H<sub>2</sub>O               \
    \             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;33.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4·2H2O\\\",\\n          \\\"volume\\\": 33,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q41\",\n    \"ingredient\": \"(NH4)2Fe(SO4)2·6H2O\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 23;\
    \ (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O / 784.0 / mg\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> (NH<sub>4</sub>)<sub>2</sub>Fe(SO<sub>4</sub>)<sub>2</sub>&#183;6H<sub>2</sub>O    \
    \      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;784.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2Fe(SO4)2·6H2O\\\",\\n          \\\"volume\\\
    \": 784,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\"\
    : \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock batch\
    \ amount in the receiving recipe. Missing nested composition is separate from\
    \ the parent quantity problem; no whole-parent formulation transfer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q42\",\n    \"ingredient\": \"(NH4)2Fe(SO4)2·6H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"784\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 23;\
    \ (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O / 784.0 / mg\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> (NH<sub>4</sub>)<sub>2</sub>Fe(SO<sub>4</sub>)<sub>2</sub>&#183;6H<sub>2</sub>O    \
    \      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;784.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2Fe(SO4)2·6H2O\\\",\\n          \\\"volume\\\
    \": 784,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\"\
    : \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities into\
    \ G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock\
    \ membership. Its water field also combines unrelated parent waters. No final\
    \ stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q43\",\n    \"ingredient\": \"(NH4)2Ni(SO4)2•6H2O\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 26;\
    \ (NH 4 ) 2 Ni(SO 4 ) 2 •6H 2 O / 395.0 / mg\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> (NH<sub>4</sub>)<sub>2</sub>Ni(SO<sub>4</sub>)<sub>2</sub>•6H<sub>2</sub>O     \
    \    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;395.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2Ni(SO4)2•6H2O\\\",\\n          \\\"volume\\\
    \": 395,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\"\
    : \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock batch\
    \ amount in the receiving recipe. Missing nested composition is separate from\
    \ the parent quantity problem; no whole-parent formulation transfer.\"\n  },\n\
    \  {\n    \"decision_id\": \"q44\",\n    \"ingredient\": \"(NH4)2Ni(SO4)2•6H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace\
    \ constituent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"395\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 26;\
    \ (NH 4 ) 2 Ni(SO 4 ) 2 •6H 2 O / 395.0 / mg\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> (NH<sub>4</sub>)<sub>2</sub>Ni(SO<sub>4</sub>)<sub>2</sub>•6H<sub>2</sub>O     \
    \    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;395.0 &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2Ni(SO4)2•6H2O\\\",\\n          \\\"volume\\\
    \": 395,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\"\
    : \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities into\
    \ G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml and stock\
    \ membership. Its water field also combines unrelated parent waters. No final\
    \ stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q45\",\n    \"ingredient\": \"25% HCl\",\n    \"decision\": \"add\",\n   \
    \ \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 24;\
    \ 25% HCl / 5.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ 25% HCl                                        </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0   &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q46\",\n    \"ingredient\": \"25% HCl\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace constituent\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 24;\
    \ 25% HCl / 5.0 / ml\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ 25% HCl                                        </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0   &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q47\",\n    \"ingredient\": \"Na2SeO4\",\n    \"decision\": \"add\",\n   \
    \ \"stage\": \"Receiving trace-stock representation\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 31;\
    \ Na 2 SeO 4 / 94.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>SeO<sub>4</sub>                                 </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;94.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO4\\\",\\n          \\\"volume\\\": 94,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named trace-stock\
    \ batch amount in the receiving recipe. Missing nested composition is separate\
    \ from the parent quantity problem; no whole-parent formulation transfer.\"\n\
    \  },\n  {\n    \"decision_id\": \"q48\",\n    \"ingredient\": \"Na2SeO4\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Existing scoped M940 trace constituent\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M940_Thermobacter_Roseum_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"94\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace preparation only; raw HTML row 31;\
    \ Na 2 SeO 4 / 94.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Na<sub>2</sub>SeO<sub>4</sub>                                 </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;94.0  &nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    \n      },\n      {\n        \"source_key\": \"togoM940original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M940\"\
    ,\n        \"source_locator\": \"$.components[3].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO4\\\",\\n          \\\"volume\\\": 94,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"9ebf700a211ec2dc7bd441c0c67cfff9d561e259e9771485963160e4d89acec8\"\
    \n      }\n    ],\n    \"interpretation\": \"The parent flattens batch quantities\
    \ into G_PER_L, including mg-scale salts and liquid inputs; preserve mg or ml\
    \ and stock membership. Its water field also combines unrelated parent waters.\
    \ No final stock volume is independently established.\"\n  },\n  {\n    \"decision_id\"\
    : \"q49\",\n    \"ingredient\": \"Trace acid strength\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"JCM899 trace-stock acid\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace-stock acid; Trace acid strength\"\
    ,\n        \"exact_source_quote\": \"25% HCl 5.0 ml\",\n        \"snapshot_sha256\"\
    : \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\",\n    \
    \    \"parsed_text_sha256\": \"1d083a65546e065a4cf390cd836d1aa0de38be6a32596205efc79dc1add7ec7c\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep 25% strength and 5 ml dose distinct.\
    \ Percentage basis and density are not stated; no molarity or mass conversion.\"\
    \n  },\n  {\n    \"decision_id\": \"q50\",\n    \"ingredient\": \"Trace preparation\
    \ order\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM899 trace stock only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm899\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=899\"\
    ,\n        \"source_locator\": \"JCM899 trace stock only; Trace preparation order\"\
    ,\n        \"exact_source_quote\": \"Dissolve (NH 4 ) 2 Fe(SO 4 ) 2 ·6H 2 O in\
    \ 25% HCl first, then dilute in distilled water.  Add the remaining salts in the\
    \ sequence indicated\",\n        \"snapshot_sha256\": \"2c585e16c7ae77a0e3254221bf86749e42b6c974198fa0bf913a06a21b1f0638\"\
    ,\n        \"parsed_text_sha256\": \"1d083a65546e065a4cf390cd836d1aa0de38be6a32596205efc79dc1add7ec7c\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the exact iron-first acid\
    \ sequence; parent main pH, gas and vitamin formulation are outside transfer.\"\
    \n  },\n  {\n    \"decision_id\": \"q51\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Receiving vitamin-stock representation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 25;\
    \ Distilled water / 1.0 / L\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the named source-stock batch\
    \ amount without importing parent basal medium or its final-volume assumptions.\"\
    \n  },\n  {\n    \"decision_id\": \"q52\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 25;\
    \ Distilled water / 1.0 / L\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Distilled water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing scoped parent value, unit\
    \ and batch basis are retained in concentration with matching attached source\
    \ snippet and cited raw hash. Verification is limited to this stock-layer amount;\
    \ no receiving-target evidence or chemical-form certification is inherited.\"\n\
    \  },\n  {\n    \"decision_id\": \"q53\",\n    \"ingredient\": \"Biotin\",\n \
    \   \"decision\": \"add\",\n    \"stage\": \"Receiving vitamin-stock representation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 15;\
    \ Biotin / 2.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Biotin\
    \                                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the named source-stock batch\
    \ amount without importing parent basal medium or its final-volume assumptions.\"\
    \n  },\n  {\n    \"decision_id\": \"q54\",\n    \"ingredient\": \"Biotin\",\n\
    \    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 2 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 15; Biotin / 2.0 / mg\",\n      \
    \  \"exact_source_quote\": \"<TR><TD WIDTH=75%> Biotin                       \
    \                           </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing scoped parent value, unit\
    \ and batch basis are retained in notes with matching attached source snippet\
    \ and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q55\",\n    \"ingredient\": \"p--Aminobenzoic acid\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 23;\
    \ p -Aminobenzoic acid / 5.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Add the named source-stock batch amount without\
    \ importing parent basal medium or its final-volume assumptions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q56\",\n    \"ingredient\": \"p--Aminobenzoic acid\",\n\
    \    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 23; p -Aminobenzoic acid / 5.0 /\
    \ mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic\
    \ acid                             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Existing scoped parent value, unit and batch\
    \ basis are retained in notes with matching attached source snippet and cited\
    \ raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q57\",\n    \"ingredient\": \"Thiamine・HCl\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 18;\
    \ Thiamine·HCl / 5.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Thiamine&#183;HCl                                      </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Add the named source-stock batch amount without\
    \ importing parent basal medium or its final-volume assumptions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q58\",\n    \"ingredient\": \"Thiamine・HCl\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 18; Thiamine·HCl / 5.0 / mg\",\n\
    \        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Thiamine&#183;HCl      \
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Existing scoped parent value, unit and batch\
    \ basis are retained in notes with matching attached source snippet and cited\
    \ raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q59\",\n    \"ingredient\": \"Calcium pantothenate\",\n    \"decision\": \"\
    add\",\n    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 21;\
    \ Calcium pantothenate / 5.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> Calcium pantothenate                                    </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Add the named source-stock batch amount without\
    \ importing parent basal medium or its final-volume assumptions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q60\",\n    \"ingredient\": \"Calcium pantothenate\",\n\
    \    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 21; Calcium pantothenate / 5.0 /\
    \ mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Calcium pantothenate\
    \                                    </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Existing scoped parent value, unit and batch\
    \ basis are retained in notes with matching attached source snippet and cited\
    \ raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q61\",\n    \"ingredient\": \"Pyridoxine・HCl\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 17;\
    \ Pyridoxine·HCl / 10.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Pyridoxine&#183;HCl                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Add the named source-stock batch amount without\
    \ importing parent basal medium or its final-volume assumptions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q62\",\n    \"ingredient\": \"Pyridoxine・HCl\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 10 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 17; Pyridoxine·HCl / 10.0 / mg\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl  \
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Existing scoped parent value, unit and batch\
    \ basis are retained in notes with matching attached source snippet and cited\
    \ raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q63\",\n    \"ingredient\": \"Folic acid\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 16;\
    \ Folic acid / 2.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Folic acid                                              </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the named source-stock batch\
    \ amount without importing parent basal medium or its final-volume assumptions.\"\
    \n  },\n  {\n    \"decision_id\": \"q64\",\n    \"ingredient\": \"Folic acid\"\
    ,\n    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 2 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 16; Folic acid / 2.0 / mg\",\n  \
    \      \"exact_source_quote\": \"<TR><TD WIDTH=75%> Folic acid               \
    \                               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing scoped parent value, unit\
    \ and batch basis are retained in notes with matching attached source snippet\
    \ and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q65\",\n    \"ingredient\": \"Vitamin B12\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 22;\
    \ Vitamin B 1 2 / 0.1 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the named source-stock batch\
    \ amount without importing parent basal medium or its final-volume assumptions.\"\
    \n  },\n  {\n    \"decision_id\": \"q66\",\n    \"ingredient\": \"Vitamin B12\"\
    ,\n    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 22; Vitamin B 1 2 / 0.1 / mg\",\n\
    \        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>\
    \                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing scoped parent value, unit\
    \ and batch basis are retained in notes with matching attached source snippet\
    \ and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q67\",\n    \"ingredient\": \"Riboflavin\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 19;\
    \ Riboflavin / 5.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Riboflavin                                              </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the named source-stock batch\
    \ amount without importing parent basal medium or its final-volume assumptions.\"\
    \n  },\n  {\n    \"decision_id\": \"q68\",\n    \"ingredient\": \"Riboflavin\"\
    ,\n    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[8].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 19; Riboflavin / 5.0 / mg\",\n  \
    \      \"exact_source_quote\": \"<TR><TD WIDTH=75%> Riboflavin               \
    \                               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing scoped parent value, unit\
    \ and batch basis are retained in notes with matching attached source snippet\
    \ and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q69\",\n    \"ingredient\": \"Nicotinic acid\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 20;\
    \ Nicotinic acid / 5.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Nicotinic acid                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Add the named source-stock batch amount without\
    \ importing parent basal medium or its final-volume assumptions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q70\",\n    \"ingredient\": \"Nicotinic acid\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[9].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 20; Nicotinic acid / 5.0 / mg\",\n\
    \        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Nicotinic acid         \
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"interpretation\": \"Existing scoped parent value, unit and batch\
    \ basis are retained in notes with matching attached source snippet and cited\
    \ raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  },\n  {\n    \"decision_id\"\
    : \"q71\",\n    \"ingredient\": \"Lipoic acid\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Receiving vitamin-stock representation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins only; raw HTML row 24;\
    \ Lipoic acid / 5.0 / mg\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%>\
    \ Lipoic acid                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Add the named source-stock batch\
    \ amount without importing parent basal medium or its final-volume assumptions.\"\
    \n  },\n  {\n    \"decision_id\": \"q72\",\n    \"ingredient\": \"Lipoic acid\"\
    ,\n    \"decision\": \"verified\",\n    \"stage\": \"Existing M190 vitamin stock\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].notes\",\n        \"\
    stored\": \"Role: Growth factor; Properties: Organic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 5 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins only; raw HTML row 24; Lipoic acid / 5.0 / mg\",\n \
    \       \"exact_source_quote\": \"<TR><TD WIDTH=75%> Lipoic acid             \
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing scoped parent value, unit\
    \ and batch basis are retained in notes with matching attached source snippet\
    \ and cited raw hash. Verification is limited to this stock-layer amount; no receiving-target\
    \ evidence or chemical-form certification is inherited.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '9 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 9/10 primary
    and 7/10 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi17234
  - chebi17997
  - chebi26710
  - chebi29377
  - chebi31206
  - chebi32139
  - chebi63036
  - chebi86345
  details: 'Instance coverage on a 0–100 percent scale, denominator 10: primary 90.00%;
    secondary 70.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact source and excluded namesake
  outcome: supported
  summary: JCM1228 and TOGO M1320 resolve the sole maintained bacterial contributor.
    The specialized namesake has a different stable ID and is excluded. Its legacy000198
    does not constrain this review; accession-conditioned JCM32929 is retained without
    a new growth assertion.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - scope-addenda
- assessment_id: stocks
  area: identity
  topic: Stock identity and stage membership
  outcome: concern
  summary: 5342/5343 resolve but are wrong formulations for the A/B recipes. Their
    API volume and g_l fields are null and preparations say 500 ml. M940 transfers
    only trace elements; M190 transfers only vitamins.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - primary
  - trace-source
  - vitamin-source
  - solution5342
  - solution5343
- assessment_id: source-forms
  area: grounding
  topic: Scoped source chemical specificity
  outcome: concern
  summary: Main magnesium hexahydrate and other represented main chemical forms are
    consistent with the primary. Scoped M940 cobalt hexahydrate is linked to anhydrous
    CHEBI35696; M190 generic calcium pantothenate does not establish the D-specific
    structure of CHEBI31345. Other unrelated parent groundings are excluded. No replacement
    identifier is guessed.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - primary
  - trace-source
  - vitamin-source
  - scoped-grounding
  - chebi35696-form
  - chebi31345-form
- assessment_id: preparation
  area: completeness
  topic: A/B handling and conditional formulation
  outcome: concern
  summary: Both layers lack separate A/B preparations, explicit source default cycle,
    final target pH and filter-sterile vitamin handling. The two JCM32929 supplements
    are flattened into universal solution entries.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Mixture and organism scope
  outcome: supported
  summary: COMPLEX/SEMI_DEFINED and LIQUID are compatible with the source mixture
    and yeast extract. No source-supported organism growth or target incubation temperature
    is inferred from the title or accession note.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - primary
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: ownership
  area: ownership
  topic: Maintained fixes and regeneration boundary
  outcome: concern
  summary: The maintained owner has the same scientific claims as the target and lacks
    the generated merge event. Correct owner scope and evidence first; do not edit
    the generated target or the unrelated stock records to force identity.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
- assessment_id: evidence
  area: evidence
  topic: Claim-level support and historical scope
  outcome: concern
  summary: Target and maintained owner have no attached quantity/preparation evidence.
    Eleven M190 stock amounts are locally evidenced and hash-authenticated; that evidence
    does not attach to target claims or prove chemical specificity. The parent-only
    sulfide metadata override does not alter vitamin transfer.
  target_ids:
  - CultureMech:007857
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
  - scope-addenda
findings:
- finding_id: f1
  issue_key: culturemech.007857.wrong-stock-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Solution A/B links identify unrelated stocks
  description: Both layers link to solutions 5342/5343 despite incompatible source
    formulations.
  target_ids:
  - CultureMech:007857
  field_paths:
  - solutions[0].term
  - solutions[1].term
  evidence_ids:
  - primary
  - solution5342
  - solution5343
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  issue_key: culturemech.007857.stage-units-and-stock-expansion
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Batch and stock quantities are flattened into mass concentrations
  description: Main water and all receiving liquid doses use G_PER_L; A/B batch masses
    lack their source-stage basis. Trace parent mg values are also flattened as grams
    per liter, while target stocks are empty.
  target_ids:
  - CultureMech:007857
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - trace-source
  - vitamin-source
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  issue_key: culturemech.007857.conditional-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Conditional supplements and preparation are incomplete
  description: JCM32929-only peptone and sulfide are represented universally; separate
    autoclaving, final target pH and vitamin handling are missing.
  target_ids:
  - CultureMech:007857
  field_paths:
  - solutions[4]
  - solutions[5]
  - preparation_steps
  - ph_value
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  issue_key: culturemech.007857.transferred-form-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Transferred stock forms need source-specific grounding
  description: M940 cobalt hexahydrate uses anhydrous CHEBI35696; generic M190 calcium
    pantothenate does not establish D-specific grounding.
  target_ids:
  - CultureMech:007857
  field_paths:
  - solutions[2].composition
  - solutions[3].composition
  evidence_ids:
  - trace-source
  - vitamin-source
  - scoped-grounding
  - chebi35696-form
  - chebi31345-form
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  issue_key: culturemech.007857.attached-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source links do not provide claim-level evidence
  description: Both receiving layers lack attached amount and preparation evidence;
    parent stock evidence must retain its exact layer.
  target_ids:
  - CultureMech:007857
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  description: Resolve source-defined A/B identities and represent exact compositions
    before any replacement link or regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007857
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  description: Restore stage-specific batch amounts, volume units, named stock composition
    and claim-level evidence; preserve existing authenticated vitamin batch notes.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007857
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  description: Retain the accession-conditioned variant and exact per-liter dose,
    percentage ambiguity and preparation order; add only supported pH and source default
    cycle.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007857
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  description: Verify the exact supplied forms and qualify unresolved stereochemistry
    before linking or copying parent groundings; do not invent replacement IDs.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007857
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
  description: Attach exact source snippets, locators, original access times and hashes
    to each curated receiving claim and preserve existing history.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007857
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml
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
- The current optional MediaDive J1228 API and preserved retry returned503. Exact
  JCM1228 and original TOGO content are available; historical byte equivalence is
  not inferred.
- No measured final-volume, unspecified percent basis, gas fraction or pressure is
  invented. Parent JCM899 basal/vitamin and JCM197 basal/mineral/reducing claims are
  excluded.
- Legacy000198 is an excluded-name comparison only. Its bounded current absence and
  unresolved historical correspondence do not make this actual target review partial.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-036
- generated-medium
```
