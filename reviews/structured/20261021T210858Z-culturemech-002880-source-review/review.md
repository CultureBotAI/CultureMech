# Source and formulation review: bacillus_filiformis_medium (CultureMech:002880)

- Review: 20261021T210858Z-culturemech-002880-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:59:32Z
- Finished UTC: 2026-10-21T21:08:58Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact JCM 531 separates a main batch from two 1 mL metal-stock additions. Both local layers flatten the manganese and iron stock preparations into the medium and normalize main masses with an unsupported final-volume denominator. Magnesium sulfate monohydrate is assigned an anhydrous structure; the source preparation and approximate pH are partly retained without evidence.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 375; batch 038 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-seven task batches contain 370 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 373 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002880 | data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml | generated | bacillus_filiformis_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002880 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002880 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch038/375/strict.tsv |
| validate-terms | passed | True | CultureMech:002880 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002880 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002880 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ531_network_retry | unavailable | False | CultureMech:002880 | The preserved current MediaDive J531 request returned HTTP 503. The exact JCM primary is available and supports the complete current formulation assessment; historical API raw bytes remain unrecovered and no byte-equivalence claim is made. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002880.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002880.

18 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Yeast extract",
    "stage": "JCM 531 main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "9.98004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "9.98004",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "g",
      "basis": "Printed main recipe with 1 L water and two distinct 1 mL stock doses; measured final volume unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 0; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Preserve the printed mass and preparation stage. The present G_PER_L value is numerically consistent with division by 1.002 L, but adding listed liquid inputs does not establish measured final volume or authenticate that normalization."
  },
  {
    "decision_id": "q2",
    "name": "Sodium citrate",
    "stage": "JCM 531 main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2.99401",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2.99401",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "basis": "Printed main recipe with 1 L water and two distinct 1 mL stock doses; measured final volume unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 1; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium citrate                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Preserve the printed mass and preparation stage. The present G_PER_L value is numerically consistent with division by 1.002 L, but adding listed liquid inputs does not establish measured final volume or authenticate that normalization."
  },
  {
    "decision_id": "q3",
    "name": "KCl",
    "stage": "JCM 531 main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.99601",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.99601",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 2,
      "source_unit": "g",
      "basis": "Printed main recipe with 1 L water and two distinct 1 mL stock doses; measured final volume unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 2; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Preserve the printed mass and preparation stage. The present G_PER_L value is numerically consistent with division by 1.002 L, but adding listed liquid inputs does not establish measured final volume or authenticate that normalization."
  },
  {
    "decision_id": "q4",
    "name": "MgSO4 x H2O",
    "stage": "JCM 531 main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.998004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.998004",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 1,
      "source_unit": "g",
      "basis": "Printed main recipe with 1 L water and two distinct 1 mL stock doses; measured final volume unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 3; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Preserve the printed mass and preparation stage. The present G_PER_L value is numerically consistent with division by 1.002 L, but adding listed liquid inputs does not establish measured final volume or authenticate that normalization."
  },
  {
    "decision_id": "q5",
    "name": "Na2CO3",
    "stage": "JCM 531 main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.99401",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.99401",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "basis": "Printed main recipe with 1 L water and two distinct 1 mL stock doses; measured final volume unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 4; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Preserve the printed mass and preparation stage. The present G_PER_L value is numerically consistent with division by 1.002 L, but adding listed liquid inputs does not establish measured final volume or authenticate that normalization."
  },
  {
    "decision_id": "q6",
    "name": "NaCl",
    "stage": "JCM 531 main batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "99.8004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "99.8004",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 100,
      "source_unit": "g",
      "basis": "Printed main recipe with 1 L water and two distinct 1 mL stock doses; measured final volume unspecified"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 5; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Preserve the printed mass and preparation stage. The present G_PER_L value is numerically consistent with division by 1.002 L, but adding listed liquid inputs does not establish measured final volume or authenticate that normalization."
  },
  {
    "decision_id": "q7",
    "name": "MnCl2 x 4 H2O",
    "stage": "MnCl2 stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 0.36,
      "source_unit": "g",
      "stock_water_input_L": 1,
      "receiving_dose_ml": 1,
      "scope": "MnCl2 stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 9; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.36&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "The local numeral belongs to the named stock preparation, not to the main-medium concentration. Preserve the hydrate, stock water input and receiving dose; do not infer measured stock or medium final volume."
  },
  {
    "decision_id": "q8",
    "name": "FeSO4 x H2O",
    "stage": "FeSO4 stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 50,
      "source_unit": "g",
      "stock_water_input_L": 1,
      "receiving_dose_ml": 1,
      "scope": "FeSO4 stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 11; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;50.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "The local numeral belongs to the named stock preparation, not to the main-medium concentration. Preserve the hydrate, stock water input and receiving dose; do not infer measured stock or medium final volume."
  },
  {
    "decision_id": "q9",
    "name": "Main water",
    "stage": "Main batch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 1,
      "source_unit": "L",
      "scope": "Main batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 8; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "This solvent input is missing in both layers. Keep all three water entries separate: the entire stock preparations are not added to the main batch."
  },
  {
    "decision_id": "q10",
    "name": "Manganese stock water",
    "stage": "MnCl2 stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 1,
      "source_unit": "L",
      "scope": "MnCl2 stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 10; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "This solvent input is missing in both layers. Keep all three water entries separate: the entire stock preparations are not added to the main batch."
  },
  {
    "decision_id": "q11",
    "name": "Iron stock water",
    "stage": "FeSO4 stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 1,
      "source_unit": "L",
      "scope": "FeSO4 stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 12; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "This solvent input is missing in both layers. Keep all three water entries separate: the entire stock preparations are not added to the main batch."
  },
  {
    "decision_id": "q12",
    "name": "Manganese stock dose",
    "stage": "Main receiving recipe",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 1,
      "source_unit": "ml",
      "basis": "Exact main JCM 531 recipe"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 6; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt; solution (see below)                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Represent the exact named stock addition independently of its preparation concentration. No final-medium concentration is inferred from the 1 mL dose alone."
  },
  {
    "decision_id": "q13",
    "name": "Iron stock dose",
    "stage": "Main receiving recipe",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 1,
      "source_unit": "ml",
      "basis": "Exact main JCM 531 recipe"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 7; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt; solution (see below)                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "Represent the exact named stock addition independently of its preparation concentration. No final-medium concentration is inferred from the 1 mL dose alone."
  },
  {
    "decision_id": "q14",
    "name": "Approximate final pH",
    "stage": "Complete medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 9.0
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 9.0
      }
    ],
    "desired": {
      "value": 9,
      "qualifier": "about"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Terminal procedure",
        "exact_source_quote": "Check final pH to be about 9.0.",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62",
        "parsed_text_sha256": "8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa"
      }
    ],
    "interpretation": "The numerical pH agrees with the primary, and existing preparation prose retains the approximation. Attach evidence rather than asserting exact titration or changing the number."
  },
  {
    "decision_id": "q15",
    "name": "Existing preparation pH and separate autoclaving",
    "stage": "Complete medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
      }
    ],
    "desired": {
      "pH": 9,
      "qualifier": "about",
      "procedure": "Separately autoclave Na2CO3 and NaCl"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Terminal procedure",
        "exact_source_quote": "Separately autoclave Na 2 CO 3 and NaCl. Check final pH to be about 9.0.",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62",
        "parsed_text_sha256": "8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa"
      }
    ],
    "interpretation": "Both layers already contain this instruction. Preserve it and add direct evidence; do not report preparation as entirely absent."
  },
  {
    "decision_id": "q16",
    "name": "Collection default autoclave temperature",
    "stage": "Sterilization under displayed JCM default",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
        }
      }
    ],
    "desired": {
      "value": 121,
      "source_unit": "°C",
      "scope": "Displayed collection default, subject to medium-specific separate autoclaving"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Displayed collection default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62",
        "parsed_text_sha256": "8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa"
      }
    ],
    "interpretation": "This numerical default appears on the exact JCM 531 page but is not recorded locally. Retain its conditional scope and the separate carbonate/NaCl instruction."
  },
  {
    "decision_id": "q17",
    "name": "Collection default autoclave duration",
    "stage": "Sterilization under displayed JCM default",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
        }
      }
    ],
    "desired": {
      "value": 15,
      "source_unit": "min",
      "scope": "Displayed collection default, subject to medium-specific separate autoclaving"
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Displayed collection default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62",
        "parsed_text_sha256": "8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa"
      }
    ],
    "interpretation": "This numerical default appears on the exact JCM 531 page but is not recorded locally. Retain its conditional scope and the separate carbonate/NaCl instruction."
  },
  {
    "decision_id": "q18",
    "name": "Unquantified final volumes, titration and growth conditions",
    "stage": "Main and stock preparations",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0."
          }
        ]
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      }
    ],
    "desired": {
      "measured_final_medium_volume": null,
      "measured_final_stock_volumes": null,
      "titrant_identity_strength_or_dose": null,
      "incubation_temperature": null,
      "incubation_time": null
    },
    "source_snippets": [
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Terminal procedure",
        "exact_source_quote": "Check final pH to be about 9.0.",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62",
        "parsed_text_sha256": "8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa"
      },
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 8; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      },
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 10; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      },
      {
        "source_key": "jcm531_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531",
        "source_locator": "Exact JCM 531 raw HTML table row 12; source stage identified by enclosing table heading",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62"
      }
    ],
    "interpretation": "The source lists water inputs and approximate final pH but no measured final volumes or fixed titrant recipe. Autoclave temperature is not growth temperature. Neither the medium name nor generic application establishes a specific strain-growth claim."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:002880.

7 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 7/8 primary and 7/8 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 8: primary 87.50%; secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002880.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact JCM 531 and maintained owner

identity: supported. Targets: CultureMech:002880.

The complete generated target and single exact maintained contributor share CultureMech:002880 and the JCM J531 accession. The linked JCM 531 primary title and full recipe resolve. The unavailable API does not make the available current primary unusable, and historical formula equivalence is not asserted.

### Explicit magnesium hydrate and other supplied forms

grounding: concern. Targets: CultureMech:002880.

JCM explicitly supplies MgSO4·H2O, while both asserted slots use CHEBI:32599 with formula Mg.O4S and an anhydrous synonym. This is a confirmed missing-water structural distinction. In contrast, manganese tetrahydrate and iron sulfate monohydrate agree with CHEBI:86368 and CHEBI:75834. KCl, Na2CO3 and NaCl match their source names without unsupported form substitutions. Source sodium citrate is not qualified for hydration or sodium stoichiometry; CHEBI:53258 is trisodium citrate, so that extra specificity remains unconfirmed rather than a proven different compound. Yeast extract is a complex BD-Difco ingredient, not an asserted single chemical.

### Retained preparation versus missing stocks, solvent and cycle

completeness: concern. Targets: CultureMech:002880.

Both layers retain separate autoclaving of carbonate/NaCl and final pH about 9, but lack source evidence, explicit stock boundaries and solvent inputs, and the displayed 121°C/15 min default. No final-volume make-up or titrant dose is supplied by the exact primary.

### Composition and biological claims

scope: supported. Targets: CultureMech:002880.

The substantial yeast extract supports the complex/undefined classification; the primary supplies a liquid formulation without agar. Bacterial categorization and the generic cultivation application are compatible with the medium identity, but the name alone does not establish a particular strain, growth temperature or growth outcome. Sterilization conditions must not become incubation conditions.

## Findings

### f1: Two metal stocks are flattened into main-medium concentrations

blocker / open / confirmed; issue key: culturemech.002880.metal-stock-flattening.

Both layers store manganese tetrahydrate 0.36 G_PER_L and iron sulfate monohydrate 50 G_PER_L as direct ingredients. The exact primary instead prepares each with 1 L water and adds only 1 mL of each stock to the main recipe.

### f2: Main masses use an unsupported final-volume denominator

major / open / confirmed; issue key: culturemech.002880.unproved-final-volume-normalization.

The first six values numerically resemble division of printed batch masses by 1.002 L. The primary lists 1 L water plus two 1 mL stock additions without specifying measured final volume. The record does not retain that original basis or direct evidence.

### f3: Magnesium monohydrate is grounded to an anhydrous structure

major / open / confirmed; issue key: culturemech.002880.magnesium-hydrate-and-citrate-specificity.

The supplied and stored magnesium name explicitly contains one water, but both ontology slots point to MgSO4 without water. Separately, generic source sodium citrate does not establish the more specific trisodium/hydration state represented by its identifier. The manganese and iron hydrate structures are supported.

### f4: Retained preparation lacks direct evidence and numerical cycle

minor / open / confirmed; issue key: culturemech.002880.preparation-evidence-and-default.

Both layers already preserve separate autoclaving and approximate pH 9, but do not attach source evidence or record the displayed 121°C/15 min collection default.

## Recommended Actions And Acceptance Checks

### a1

Restore the two named stock preparations and 1 mL receiving doses in the maintained owner, preserving solvent and hydrate scope before regenerating the target.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve exact original gram amounts, water input and stock additions. Establish a justified normalization basis before expressing final concentrations; do not infer historical causation from the numerical pattern.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve magnesium monohydrate with exact form evidence and qualify citrate specificity without guessing a replacement ID or altering supported manganese/iron hydrates.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact primary evidence to existing prose and pH, adding the conditional cycle while retaining source-unquantified titration and final volumes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch038/375/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch038/375/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml:1:id: CultureMech:002880<br>./data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml:1:id: CultureMech:002880<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch038/source-preflight-bound/375/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 12 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| main | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531; Exact JCM medium 531 main table | supports | Exact accession and title support the main formulation; its gram amounts and 1 L water input are distinct from the two receiving stock doses. |
| manganese-stock | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531; Named MnCl2 stock table, raw row 9 | supports | Manganese chloride tetrahydrate belongs to its own stock preparation with 1 L water; main receiving dose is 1 mL. |
| iron-stock | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531; Named FeSO4 stock table, raw row 11 | supports | Iron sulfate monohydrate belongs to its own stock preparation with 1 L water; main receiving dose is 1 mL. |
| preparation | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531; Collection default and terminal medium-specific procedure | supports | The collection default is 121°C for 15 min. The medium-specific text separately autoclaves carbonate and NaCl and asks for final pH about 9.0. |
| final-ph | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531; Terminal medium-specific procedure | supports | Approximate final pH and separate autoclaving are retained in both local preparation descriptions. |
| mediadiveJ531_network_retry-attempt | https://mediadive.dsmz.de/rest/medium/J531; Preserved exact public retrieval result | context_only | The preserved current MediaDive J531 request returned HTTP 503. The exact JCM primary is available and supports the complete current formulation assessment; historical API raw bytes remain unrecovered and no byte-equivalence claim is made. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch038/375/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53258 resolves to sodium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75834 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75834; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75834 resolves to iron(2+) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:75834": [{"label": "FeSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:75834", "preferred_term": "FeSO4 x H2O", "ontology_id": "CHEBI:75834", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml", "events": 6, "timestamp_issues": []}] |
| ontology-retry-provenance | /private/tmp/culturemech-review-work-batch038/source-preflight-bound/375/source-catalog.json; chebi75834 initial failed capture and chebi75834_network_retry successful response | context_only | The record-local chemical lookup uses the separately preserved successful CHEBI:75834 response, retaining its actual URL, hash and time. The original failed response and shared helper/catalog bytes remain unchanged. |
| historical-report | /private/tmp/culturemech-review-work-batch038/375/history-inventory.json; Complete exact local report, header and source-row context | context_only | The earlier report records normalized provider values and named stocks but left this record unchanged. Its decoded quotations are derivative historical context, not recovered original response bytes. Primary JCM evidence independently supports this review. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current flattening, concentration, stock migration and merge mechanisms are contextual. Present code and numerical resemblance do not prove the historical execution responsible for these stored values. |
| writer-1 | src/culturemech/convert/mediadive_raw_yaml.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current flattening, concentration, stock migration and merge mechanisms are contextual. Present code and numerical resemblance do not prove the historical execution responsible for these stored values. |
| writer-2 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current flattening, concentration, stock migration and merge mechanisms are contextual. Present code and numerical resemblance do not prove the historical execution responsible for these stored values. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current flattening, concentration, stock migration and merge mechanisms are contextual. Present code and numerical resemblance do not prove the historical execution responsible for these stored values. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved current MediaDive J531 request returned HTTP 503. The exact JCM primary is available and supports the complete current formulation assessment; historical API raw bytes remain unrecovered and no byte-equivalence claim is made.
- No target or owner concentration has attached matching evidence; no quantity is marked verified. The complete historical report remains derivative-only.
- Current primary JCM formulation is fully available despite the optional API failure. No historical raw equivalence or reconstructed provider response is asserted.
- The main and two stock water entries are inputs, not independently measured final volumes. No stock volume sum or growth condition is silently inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T210858Z-culturemech-002880-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_filiformis_medium (CultureMech:002880)'
started_at: '2026-10-21T20:59:32Z'
finished_at: '2026-10-21T21:08:58Z'
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
summary: Exact JCM 531 separates a main batch from two 1 mL metal-stock additions.
  Both local layers flatten the manganese and iron stock preparations into the medium
  and normalize main masses with an unsupported final-volume denominator. Magnesium
  sulfate monohydrate is assigned an anhydrous structure; the source preparation and
  approximate pH are partly retained without evidence.
source:
  git_revision: 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
    sha256: b0a5dbd85ccec126939cff45bdb568e53685a1bd869a9f3e84ab48244df90d78
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
    sha256: 7549a928fa0fc8238dd05ec614971d0b7a61fc8ab17ca1cd1078f8019ceffe9a
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml.md
    sha256: e2535e71fcfe59d1c440cbc21b991772d1ea3cab2e6540204c047526f297bbaa
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
  selection: Task review 375; batch 038 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-seven task batches
    contain 370 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 373 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002880
targets:
- target_id: CultureMech:002880
  path: data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  label: bacillus_filiformis_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch038/375/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch038/375/strict.tsv"
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002880
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
  - CultureMech:002880
- check_id: mediadiveJ531_network_retry-source-access
  name: 'Exact source content access: mediadiveJ531_network_retry'
  required: false
  status: unavailable
  summary: The preserved current MediaDive J531 request returned HTTP 503. The exact
    JCM primary is available and supports the complete current formulation assessment;
    historical API raw bytes remain unrecovered and no byte-equivalence claim is made.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - mediadiveJ531_network_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:16.926592Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch038/375/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:18.862985Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch038/375/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:21.546976Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:23.124385Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T21:08:57Z'
  support: supports
  summary: './data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml:1:id: CultureMech:002880

    ./data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml:1:id:
    CultureMech:002880

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/source-preflight-bound/375/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T21:08:57Z'
  support: supports
  summary: 12 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 0f8966ca1a345293d4ceb42b47b1f10b6ae062aa55422fa8b6fca8845ebc3502
- evidence_id: main
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531
  locator: Exact JCM medium 531 main table
  accessed_at: '2026-10-21T20:20:23.213072Z'
  support: supports
  summary: Exact accession and title support the main formulation; its gram amounts
    and 1 L water input are distinct from the two receiving stock doses.
  quote: BACILLUS FILIFORMIS MEDIUM
  snapshot_sha256: 8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62
- evidence_id: manganese-stock
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531
  locator: Named MnCl2 stock table, raw row 9
  accessed_at: '2026-10-21T20:20:23.213072Z'
  support: supports
  summary: Manganese chloride tetrahydrate belongs to its own stock preparation with
    1 L water; main receiving dose is 1 mL.
  quote: <TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.36&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>
  snapshot_sha256: 8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62
- evidence_id: iron-stock
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531
  locator: Named FeSO4 stock table, raw row 11
  accessed_at: '2026-10-21T20:20:23.213072Z'
  support: supports
  summary: Iron sulfate monohydrate belongs to its own stock preparation with 1 L
    water; main receiving dose is 1 mL.
  quote: <TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;50.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>
  snapshot_sha256: 8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62
- evidence_id: preparation
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531
  locator: Collection default and terminal medium-specific procedure
  accessed_at: '2026-10-21T20:20:23.213072Z'
  support: supports
  summary: The collection default is 121°C for 15 min. The medium-specific text separately
    autoclaves carbonate and NaCl and asks for final pH about 9.0.
  quote: Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.
  snapshot_sha256: 8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62
- evidence_id: final-ph
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531
  locator: Terminal medium-specific procedure
  accessed_at: '2026-10-21T20:20:23.213072Z'
  support: supports
  summary: Approximate final pH and separate autoclaving are retained in both local
    preparation descriptions.
  quote: Separately autoclave Na 2 CO 3 and NaCl. Check final pH to be about 9.0.
  snapshot_sha256: 8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62
- evidence_id: mediadiveJ531_network_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J531
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:20:23.538243Z'
  support: context_only
  summary: The preserved current MediaDive J531 request returned HTTP 503. The exact
    JCM primary is available and supports the complete current formulation assessment;
    historical API raw bytes remain unrecovered and no byte-equivalence claim is made.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/375/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a33dfa10809565691999508f4510bcbe5b4439c4ef8a25e2c6931e37e00e7498
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
- evidence_id: chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.640268Z'
  support: supports
  summary: CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: CHEBI:53258 resolves to sodium citrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
- evidence_id: chebi75834
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75834
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T20:20:23.692493Z'
  support: supports
  summary: CHEBI:75834 resolves to iron(2+) sulfate monohydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 62b4a4aa2ddad989a3dc12e1c926b509fa63d10bcf136bee321155d186978f1e
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T21:08:57Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label":
    "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599",
    "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate",
    "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term":
    "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED",
    "ambiguity": "resolved:owned"}], "CHEBI:75834": [{"label": "FeSO4 x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75834", "preferred_term": "FeSO4 x H2O",
    "ontology_id": "CHEBI:75834", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: ontology-retry-provenance
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/source-preflight-bound/375/source-catalog.json
  locator: chebi75834 initial failed capture and chebi75834_network_retry successful
    response
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: The record-local chemical lookup uses the separately preserved successful
    CHEBI:75834 response, retaining its actual URL, hash and time. The original failed
    response and shared helper/catalog bytes remain unchanged.
  snapshot_sha256: 0f8966ca1a345293d4ceb42b47b1f10b6ae062aa55422fa8b6fca8845ebc3502
- evidence_id: historical-report
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/375/history-inventory.json
  locator: Complete exact local report, header and source-row context
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: The earlier report records normalized provider values and named stocks
    but left this record unchanged. Its decoded quotations are derivative historical
    context, not recovered original response bytes. Primary JCM evidence independently
    supports this review.
  snapshot_sha256: 2b0968dce5bcd8cf8d3612e81cbc2c8641c09a2b7c7613b63f28b74335d39b6c
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Current flattening, concentration, stock migration and merge mechanisms
    are contextual. Present code and numerical resemblance do not prove the historical
    execution responsible for these stored values.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/convert/mediadive_raw_yaml.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Current flattening, concentration, stock migration and merge mechanisms
    are contextual. Present code and numerical resemblance do not prove the historical
    execution responsible for these stored values.
  snapshot_sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
- evidence_id: writer-2
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Current flattening, concentration, stock migration and merge mechanisms
    are contextual. Present code and numerical resemblance do not prove the historical
    execution responsible for these stored values.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:08:57Z'
  support: context_only
  summary: Current flattening, concentration, stock migration and merge mechanisms
    are contextual. Present code and numerical resemblance do not prove the historical
    execution responsible for these stored values.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 18 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Yeast extract\"\
    ,\n    \"stage\": \"JCM 531 main batch\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.98004\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.98004\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 10,\n  \
    \    \"source_unit\": \"g\",\n      \"basis\": \"Printed main recipe with 1 L\
    \ water and two distinct 1 mL stock doses; measured final volume unspecified\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 0; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed mass and preparation\
    \ stage. The present G_PER_L value is numerically consistent with division by\
    \ 1.002 L, but adding listed liquid inputs does not establish measured final volume\
    \ or authenticate that normalization.\"\n  },\n  {\n    \"decision_id\": \"q2\"\
    ,\n    \"name\": \"Sodium citrate\",\n    \"stage\": \"JCM 531 main batch\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n       \
    \ \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.99401\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.99401\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n   \
    \   \"source_unit\": \"g\",\n      \"basis\": \"Printed main recipe with 1 L water\
    \ and two distinct 1 mL stock doses; measured final volume unspecified\"\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 1; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> Sodium citrate                                          </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed mass and preparation\
    \ stage. The present G_PER_L value is numerically consistent with division by\
    \ 1.002 L, but adding listed liquid inputs does not establish measured final volume\
    \ or authenticate that normalization.\"\n  },\n  {\n    \"decision_id\": \"q3\"\
    ,\n    \"name\": \"KCl\",\n    \"stage\": \"JCM 531 main batch\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.99601\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.99601\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 2,\n   \
    \   \"source_unit\": \"g\",\n      \"basis\": \"Printed main recipe with 1 L water\
    \ and two distinct 1 mL stock doses; measured final volume unspecified\"\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 2; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> KCl                                                     </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed mass and preparation\
    \ stage. The present G_PER_L value is numerically consistent with division by\
    \ 1.002 L, but adding listed liquid inputs does not establish measured final volume\
    \ or authenticate that normalization.\"\n  },\n  {\n    \"decision_id\": \"q4\"\
    ,\n    \"name\": \"MgSO4 x H2O\",\n    \"stage\": \"JCM 531 main batch\",\n  \
    \  \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.998004\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.998004\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 1,\n  \
    \    \"source_unit\": \"g\",\n      \"basis\": \"Printed main recipe with 1 L\
    \ water and two distinct 1 mL stock doses; measured final volume unspecified\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 3; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;H<sub>2</sub>O                      \
    \             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed mass and preparation\
    \ stage. The present G_PER_L value is numerically consistent with division by\
    \ 1.002 L, but adding listed liquid inputs does not establish measured final volume\
    \ or authenticate that normalization.\"\n  },\n  {\n    \"decision_id\": \"q5\"\
    ,\n    \"name\": \"Na2CO3\",\n    \"stage\": \"JCM 531 main batch\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.99401\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.99401\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n   \
    \   \"source_unit\": \"g\",\n      \"basis\": \"Printed main recipe with 1 L water\
    \ and two distinct 1 mL stock doses; measured final volume unspecified\"\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 4; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> Na<sub>2</sub>CO<sub>3</sub>                              \
    \              </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed mass and preparation\
    \ stage. The present G_PER_L value is numerically consistent with division by\
    \ 1.002 L, but adding listed liquid inputs does not establish measured final volume\
    \ or authenticate that normalization.\"\n  },\n  {\n    \"decision_id\": \"q6\"\
    ,\n    \"name\": \"NaCl\",\n    \"stage\": \"JCM 531 main batch\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"99.8004\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"99.8004\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 100,\n \
    \     \"source_unit\": \"g\",\n      \"basis\": \"Printed main recipe with 1 L\
    \ water and two distinct 1 mL stock doses; measured final volume unspecified\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 5; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> NaCl                                                  </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed mass and preparation\
    \ stage. The present G_PER_L value is numerically consistent with division by\
    \ 1.002 L, but adding listed liquid inputs does not establish measured final volume\
    \ or authenticate that normalization.\"\n  },\n  {\n    \"decision_id\": \"q7\"\
    ,\n    \"name\": \"MnCl2 x 4 H2O\",\n    \"stage\": \"MnCl2 stock\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"source_amount\": 0.36,\n   \
    \   \"source_unit\": \"g\",\n      \"stock_water_input_L\": 1,\n      \"receiving_dose_ml\"\
    : 1,\n      \"scope\": \"MnCl2 stock\"\n    },\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 9; source stage identified by enclosing table\
    \ heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.36&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"The local numeral belongs to the\
    \ named stock preparation, not to the main-medium concentration. Preserve the\
    \ hydrate, stock water input and receiving dose; do not infer measured stock or\
    \ medium final volume.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\"\
    : \"FeSO4 x H2O\",\n    \"stage\": \"FeSO4 stock\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 50,\n      \"source_unit\"\
    : \"g\",\n      \"stock_water_input_L\": 1,\n      \"receiving_dose_ml\": 1,\n\
    \      \"scope\": \"FeSO4 stock\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 11; source stage identified by enclosing\
    \ table heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;50.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"The local numeral belongs to the\
    \ named stock preparation, not to the main-medium concentration. Preserve the\
    \ hydrate, stock water input and receiving dose; do not infer measured stock or\
    \ medium final volume.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"name\"\
    : \"Main water\",\n    \"stage\": \"Main batch\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_amount\": 1,\n      \"source_unit\"\
    : \"L\",\n      \"scope\": \"Main batch\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 8; source stage identified by enclosing table\
    \ heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"This solvent input is missing in\
    \ both layers. Keep all three water entries separate: the entire stock preparations\
    \ are not added to the main batch.\"\n  },\n  {\n    \"decision_id\": \"q10\"\
    ,\n    \"name\": \"Manganese stock water\",\n    \"stage\": \"MnCl2 stock\",\n\
    \    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_amount\": 1,\n      \"source_unit\"\
    : \"L\",\n      \"scope\": \"MnCl2 stock\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 10; source stage identified by enclosing\
    \ table heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled\
    \ water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"This solvent input is missing in\
    \ both layers. Keep all three water entries separate: the entire stock preparations\
    \ are not added to the main batch.\"\n  },\n  {\n    \"decision_id\": \"q11\"\
    ,\n    \"name\": \"Iron stock water\",\n    \"stage\": \"FeSO4 stock\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_amount\": 1,\n      \"source_unit\"\
    : \"L\",\n      \"scope\": \"FeSO4 stock\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 12; source stage identified by enclosing\
    \ table heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled\
    \ water                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"This solvent input is missing in\
    \ both layers. Keep all three water entries separate: the entire stock preparations\
    \ are not added to the main batch.\"\n  },\n  {\n    \"decision_id\": \"q12\"\
    ,\n    \"name\": \"Manganese stock dose\",\n    \"stage\": \"Main receiving recipe\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_amount\": 1,\n      \"source_unit\"\
    : \"ml\",\n      \"basis\": \"Exact main JCM 531 recipe\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 6; source stage identified by enclosing table\
    \ heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MnCl<sub>2</sub>\
    \ solution (see below)                           </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named stock addition\
    \ independently of its preparation concentration. No final-medium concentration\
    \ is inferred from the 1 mL dose alone.\"\n  },\n  {\n    \"decision_id\": \"\
    q13\",\n    \"name\": \"Iron stock dose\",\n    \"stage\": \"Main receiving recipe\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_amount\": 1,\n      \"source_unit\"\
    : \"ml\",\n      \"basis\": \"Exact main JCM 531 recipe\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Exact JCM 531 raw HTML table row 7; source stage identified by enclosing table\
    \ heading\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> FeSO<sub>4</sub>\
    \ solution (see below)                           </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent the exact named stock addition\
    \ independently of its preparation concentration. No final-medium concentration\
    \ is inferred from the 1 mL dose alone.\"\n  },\n  {\n    \"decision_id\": \"\
    q14\",\n    \"name\": \"Approximate final pH\",\n    \"stage\": \"Complete medium\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": 9.0\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0\n      }\n \
    \   ],\n    \"desired\": {\n      \"value\": 9,\n      \"qualifier\": \"about\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Terminal procedure\",\n        \"exact_source_quote\"\
    : \"Check final pH to be about 9.0.\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    ,\n        \"parsed_text_sha256\": \"8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa\"\
    \n      }\n    ],\n    \"interpretation\": \"The numerical pH agrees with the\
    \ primary, and existing preparation prose retains the approximation. Attach evidence\
    \ rather than asserting exact titration or changing the number.\"\n  },\n  {\n\
    \    \"decision_id\": \"q15\",\n    \"name\": \"Existing preparation pH and separate\
    \ autoclaving\",\n    \"stage\": \"Complete medium\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Separately autoclave Na2CO3 and NaCl. Check final pH to be about 9.0.\"\n\
    \      }\n    ],\n    \"desired\": {\n      \"pH\": 9,\n      \"qualifier\": \"\
    about\",\n      \"procedure\": \"Separately autoclave Na2CO3 and NaCl\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Terminal procedure\",\n        \"exact_source_quote\"\
    : \"Separately autoclave Na 2 CO 3 and NaCl. Check final pH to be about 9.0.\"\
    ,\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    ,\n        \"parsed_text_sha256\": \"8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already contain this\
    \ instruction. Preserve it and add direct evidence; do not report preparation\
    \ as entirely absent.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"name\"\
    : \"Collection default autoclave temperature\",\n    \"stage\": \"Sterilization\
    \ under displayed JCM default\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Separately autoclave Na2CO3 and NaCl. Check final pH to\
    \ be about 9.0.\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Separately autoclave Na2CO3 and NaCl. Check final pH to\
    \ be about 9.0.\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\"\
    : 121,\n      \"source_unit\": \"°C\",\n      \"scope\": \"Displayed collection\
    \ default, subject to medium-specific separate autoclaving\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Displayed collection default\",\n        \"exact_source_quote\": \"Unless\
    \ otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\",\n \
    \       \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    ,\n        \"parsed_text_sha256\": \"8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa\"\
    \n      }\n    ],\n    \"interpretation\": \"This numerical default appears on\
    \ the exact JCM 531 page but is not recorded locally. Retain its conditional scope\
    \ and the separate carbonate/NaCl instruction.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"name\": \"Collection default autoclave duration\",\n    \"stage\"\
    : \"Sterilization under displayed JCM default\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Separately autoclave Na2CO3 and NaCl. Check final pH to\
    \ be about 9.0.\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Separately autoclave Na2CO3 and NaCl. Check final pH to\
    \ be about 9.0.\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\"\
    : 15,\n      \"source_unit\": \"min\",\n      \"scope\": \"Displayed collection\
    \ default, subject to medium-specific separate autoclaving\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm531_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\",\n        \"source_locator\"\
    : \"Displayed collection default\",\n        \"exact_source_quote\": \"Unless\
    \ otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\",\n \
    \       \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    ,\n        \"parsed_text_sha256\": \"8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa\"\
    \n      }\n    ],\n    \"interpretation\": \"This numerical default appears on\
    \ the exact JCM 531 page but is not recorded locally. Retain its conditional scope\
    \ and the separate carbonate/NaCl instruction.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"name\": \"Unquantified final volumes, titration and growth conditions\"\
    ,\n    \"stage\": \"Main and stock preparations\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Separately autoclave Na2CO3 and NaCl. Check\
    \ final pH to be about 9.0.\"\n          }\n        ]\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Separately autoclave Na2CO3 and NaCl. Check\
    \ final pH to be about 9.0.\"\n          }\n        ]\n      },\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"temperature_value\",\n        \"stored\": null\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"measured_final_medium_volume\":\
    \ null,\n      \"measured_final_stock_volumes\": null,\n      \"titrant_identity_strength_or_dose\"\
    : null,\n      \"incubation_temperature\": null,\n      \"incubation_time\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm531_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Terminal procedure\",\n        \"exact_source_quote\"\
    : \"Check final pH to be about 9.0.\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    ,\n        \"parsed_text_sha256\": \"8a862637f614eea27e608e9d26d58da62277d8793a9c6531c84e46cdcb342daa\"\
    \n      },\n      {\n        \"source_key\": \"jcm531_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 8; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> Distilled water                                         </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      },\n      {\n        \"source_key\": \"jcm531_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 10; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> Distilled water                                         </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      },\n      {\n        \"source_key\": \"jcm531_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=531\"\
    ,\n        \"source_locator\": \"Exact JCM 531 raw HTML table row 12; source stage\
    \ identified by enclosing table heading\",\n        \"exact_source_quote\": \"\
    <TR><TD WIDTH=75%> Distilled water                                         </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"8c975097eba5369e4d0f4dfeaddf7f2fba2429ffef53fa7e47d2b79273d0df62\"\
    \n      }\n    ],\n    \"interpretation\": \"The source lists water inputs and\
    \ approximate final pH but no measured final volumes or fixed titrant recipe.\
    \ Autoclave temperature is not growth temperature. Neither the medium name nor\
    \ generic application establishes a specific strain-growth claim.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '7 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 7/8 primary
    and 7/8 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi26710
  - chebi29377
  - chebi32588
  - chebi32599
  - chebi53258
  - chebi75834
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 87.50%;
    secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact JCM 531 and maintained owner
  outcome: supported
  summary: The complete generated target and single exact maintained contributor share
    CultureMech:002880 and the JCM J531 accession. The linked JCM 531 primary title
    and full recipe resolve. The unavailable API does not make the available current
    primary unusable, and historical formula equivalence is not asserted.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - record
  - owner-0
  - main
  - historical-report
- assessment_id: source-forms
  area: grounding
  topic: Explicit magnesium hydrate and other supplied forms
  outcome: concern
  summary: JCM explicitly supplies MgSO4·H2O, while both asserted slots use CHEBI:32599
    with formula Mg.O4S and an anhydrous synonym. This is a confirmed missing-water
    structural distinction. In contrast, manganese tetrahydrate and iron sulfate monohydrate
    agree with CHEBI:86368 and CHEBI:75834. KCl, Na2CO3 and NaCl match their source
    names without unsupported form substitutions. Source sodium citrate is not qualified
    for hydration or sodium stoichiometry; CHEBI:53258 is trisodium citrate, so that
    extra specificity remains unconfirmed rather than a proven different compound.
    Yeast extract is a complex BD-Difco ingredient, not an asserted single chemical.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - main
  - manganese-stock
  - iron-stock
  - chebi32599
  - chebi86368
  - chebi75834
  - chebi53258
  - chebi32588
  - chebi29377
  - chebi26710
- assessment_id: preparation
  area: completeness
  topic: Retained preparation versus missing stocks, solvent and cycle
  outcome: concern
  summary: Both layers retain separate autoclaving of carbonate/NaCl and final pH
    about 9, but lack source evidence, explicit stock boundaries and solvent inputs,
    and the displayed 121°C/15 min default. No final-volume make-up or titrant dose
    is supplied by the exact primary.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - preparation
  - final-ph
  - quantity-inventory
- assessment_id: growth
  area: scope
  topic: Composition and biological claims
  outcome: supported
  summary: The substantial yeast extract supports the complex/undefined classification;
    the primary supplies a liquid formulation without agar. Bacterial categorization
    and the generic cultivation application are compatible with the medium identity,
    but the name alone does not establish a particular strain, growth temperature
    or growth outcome. Sterilization conditions must not become incubation conditions.
  target_ids:
  - CultureMech:002880
  evidence_ids:
  - main
  - record
  - owner-0
  - preparation
findings:
- finding_id: f1
  issue_key: culturemech.002880.metal-stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Two metal stocks are flattened into main-medium concentrations
  description: Both layers store manganese tetrahydrate 0.36 G_PER_L and iron sulfate
    monohydrate 50 G_PER_L as direct ingredients. The exact primary instead prepares
    each with 1 L water and adds only 1 mL of each stock to the main recipe.
  target_ids:
  - CultureMech:002880
  field_paths:
  - ingredients[6].concentration
  - ingredients[7].concentration
  - solutions
  evidence_ids:
  - manganese-stock
  - iron-stock
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  issue_key: culturemech.002880.unproved-final-volume-normalization
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main masses use an unsupported final-volume denominator
  description: The first six values numerically resemble division of printed batch
    masses by 1.002 L. The primary lists 1 L water plus two 1 mL stock additions without
    specifying measured final volume. The record does not retain that original basis
    or direct evidence.
  target_ids:
  - CultureMech:002880
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  evidence_ids:
  - main
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  issue_key: culturemech.002880.magnesium-hydrate-and-citrate-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Magnesium monohydrate is grounded to an anhydrous structure
  description: The supplied and stored magnesium name explicitly contains one water,
    but both ontology slots point to MgSO4 without water. Separately, generic source
    sodium citrate does not establish the more specific trisodium/hydration state
    represented by its identifier. The manganese and iron hydrate structures are supported.
  target_ids:
  - CultureMech:002880
  field_paths:
  - ingredients[3].term
  - ingredients[3].mediaingredientmech_chebi_term
  - ingredients[1].term
  - ingredients[1].mediaingredientmech_chebi_term
  evidence_ids:
  - main
  - chebi32599
  - chebi53258
  - chebi86368
  - chebi75834
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  issue_key: culturemech.002880.preparation-evidence-and-default
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Retained preparation lacks direct evidence and numerical cycle
  description: Both layers already preserve separate autoclaving and approximate pH
    9, but do not attach source evidence or record the displayed 121°C/15 min collection
    default.
  target_ids:
  - CultureMech:002880
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - preparation
  - final-ph
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  description: Restore the two named stock preparations and 1 mL receiving doses in
    the maintained owner, preserving solvent and hydrate scope before regenerating
    the target.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002880
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  description: Preserve exact original gram amounts, water input and stock additions.
    Establish a justified normalization basis before expressing final concentrations;
    do not infer historical causation from the numerical pattern.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002880
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  description: Resolve magnesium monohydrate with exact form evidence and qualify
    citrate specificity without guessing a replacement ID or altering supported manganese/iron
    hydrates.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002880
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
  description: Attach exact primary evidence to existing prose and pH, adding the
    conditional cycle while retaining source-unquantified titration and final volumes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002880
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J531_BACILLUS_FILIFORMIS_MEDIUM.yaml
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
- The preserved current MediaDive J531 request returned HTTP 503. The exact JCM primary
  is available and supports the complete current formulation assessment; historical
  API raw bytes remain unrecovered and no byte-equivalence claim is made.
- No target or owner concentration has attached matching evidence; no quantity is
  marked verified. The complete historical report remains derivative-only.
- Current primary JCM formulation is fully available despite the optional API failure.
  No historical raw equivalence or reconstructed provider response is asserted.
- The main and two stock water entries are inputs, not independently measured final
  volumes. No stock volume sum or growth condition is silently inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-038
- generated-medium
```
