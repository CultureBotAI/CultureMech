# Source and formulation review: bacillus_aa_medium (CultureMech:009980)

- Review: 20261021T210353Z-culturemech-009980-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:59:30Z
- Finished UTC: 2026-10-21T21:03:53Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 579 specifies a separate Solution A, a 10 mL Solution B stock and completion doses per 10 mL A. Both local layers flatten those stages, store liquid doses as mass concentrations, and link A/B to unrelated high-salt stocks. The named JCM 151 trace recipe is independently available; thirteen existing M142 trace claims authenticate that stock layer only.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 372; batch 038 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-seven task batches contain 370 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 373 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009980 | data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml | generated | bacillus_aa_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009980 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009980 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch038/372/strict.tsv |
| validate-terms | passed | True | CultureMech:009980 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009980 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009980 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009980.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009980.

55 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Yeast extract",
    "stage": "Solution A batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "Yeast extract",
        "1.0",
        "g"
      ],
      "basis": "A batch with 1 L water and 10 mL trace stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 5: Yeast extract &#124; 1.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Retain the printed batch mass and its A-stage membership. The current flat G_PER_L field does not encode the staged recipe or establish a measured final-medium denominator."
  },
  {
    "decision_id": "q2",
    "name": "NaCl",
    "stage": "Solution A batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "NaCl",
        "1.0",
        "g"
      ],
      "basis": "A batch with 1 L water and 10 mL trace stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 3: NaCl &#124; 1.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Retain the printed batch mass and its A-stage membership. The current flat G_PER_L field does not encode the staged recipe or establish a measured final-medium denominator."
  },
  {
    "decision_id": "q3",
    "name": "KH2PO4",
    "stage": "Solution A batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "KH 2 PO 4",
        "0.3",
        "g"
      ],
      "basis": "A batch with 1 L water and 10 mL trace stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 0: KH 2 PO 4 &#124; 0.3 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Retain the printed batch mass and its A-stage membership. The current flat G_PER_L field does not encode the staged recipe or establish a measured final-medium denominator."
  },
  {
    "decision_id": "q4",
    "name": "NH4Cl",
    "stage": "Solution A batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "NH 4 Cl",
        "1.0",
        "g"
      ],
      "basis": "A batch with 1 L water and 10 mL trace stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 2: NH 4 Cl &#124; 1.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Retain the printed batch mass and its A-stage membership. The current flat G_PER_L field does not encode the staged recipe or establish a measured final-medium denominator."
  },
  {
    "decision_id": "q5",
    "name": "K2HPO4",
    "stage": "Solution A batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "K 2 HPO 4",
        "0.3",
        "g"
      ],
      "basis": "A batch with 1 L water and 10 mL trace stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 1: K 2 HPO 4 &#124; 0.3 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Retain the printed batch mass and its A-stage membership. The current flat G_PER_L field does not encode the staged recipe or establish a measured final-medium denominator."
  },
  {
    "decision_id": "q6",
    "name": "KCl",
    "stage": "Solution A batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "KCl",
        "0.1",
        "g"
      ],
      "basis": "A batch with 1 L water and 10 mL trace stock"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 4: KCl &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Retain the printed batch mass and its A-stage membership. The current flat G_PER_L field does not encode the staged recipe or establish a measured final-medium denominator."
  },
  {
    "decision_id": "q7",
    "name": "Distilled water",
    "stage": "Solution A water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "L",
      "scope": "Solution A water"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 7: Distilled water &#124; 1.0 &#124; L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Split the single merged 11 G_PER_L field into the two exact water inputs. The numerals 1 L and 10 mL must not be summed without units or treated as a final-medium mass."
  },
  {
    "decision_id": "q8",
    "name": "Distilled water",
    "stage": "Solution B water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "ML",
      "scope": "Solution B water"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 13: Distilled water &#124; 10.0 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "Split the single merged 11 G_PER_L field into the two exact water inputs. The numerals 1 L and 10 mL must not be summed without units or treated as a final-medium mass."
  },
  {
    "decision_id": "q9",
    "name": "MgCl2・6H2O",
    "stage": "Solution B stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "MgCl 2 ·6H 2 O",
        "0.5",
        "g"
      ],
      "basis": "B stock prepared with 10 mL water"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 12: MgCl 2 ·6H 2 O &#124; 0.5 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "These are gram quantities for the B stock, not final-medium concentrations. Keep the receiving 0.1 mL B dose separate."
  },
  {
    "decision_id": "q10",
    "name": "CaCl2",
    "stage": "Solution B stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "CaCl 2",
        "0.1",
        "g"
      ],
      "basis": "B stock prepared with 10 mL water"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 11: CaCl 2 &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "These are gram quantities for the B stock, not final-medium concentrations. Keep the receiving 0.1 mL B dose separate."
  },
  {
    "decision_id": "q11",
    "name": "Sodium acetate dose",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.2,
      "unit": "ML",
      "basis": "Per 10 mL A"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 9: 1.0 M Sodium acetate (filter-sterilized) &#124; 0.2 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1.0 M Sodium acetate (filter-sterilized)               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"1.0 M Sodium acetate (filter--sterilized)\",\n          \"volume\": 0.2,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "The stored G_PER_L value misrepresents a liquid dose. Preserve the explicit receiving stage and do not use the volume of an entire stock preparation as a medium addition."
  },
  {
    "decision_id": "q12",
    "name": "Bicarbonate dose",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.4,
      "unit": "ML",
      "basis": "Per 10 mL A"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 10: 5% NaHCO 3 solution (filter-sterilized) &#124; 0.4 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution (filter-sterilized)             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"5% NaHCO3 solution (filter--sterilized)\",\n          \"volume\": 0.4,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "The stored G_PER_L value misrepresents a liquid dose. Preserve the explicit receiving stage and do not use the volume of an entire stock preparation as a medium addition."
  },
  {
    "decision_id": "q13",
    "name": "Solution B dose",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.1,
      "unit": "ML",
      "basis": "Per 10 mL A"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 8: Solution B (see below) &#124; 0.1 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Solution B (see below)                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 0.1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "The stored G_PER_L value misrepresents a liquid dose. Preserve the explicit receiving stage and do not use the volume of an entire stock preparation as a medium addition."
  },
  {
    "decision_id": "q14",
    "name": "Trace-mineral dose",
    "stage": "Receiving stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "ML",
      "basis": "Per A batch with 1 L water"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 6: Trace minerals (see Medium No. 151 ) &#124; 10.0 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace minerals (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=151\"&gt;151&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      },
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "The stored G_PER_L value misrepresents a liquid dose. Preserve the explicit receiving stage and do not use the volume of an entire stock preparation as a medium addition."
  },
  {
    "decision_id": "q15",
    "name": "Solution A receiving aliquot",
    "stage": "Completion basis",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "ML",
      "basis": "A aliquot before the three completion doses"
    },
    "source_snippets": [
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      },
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Completion paragraph",
        "exact_source_quote": "To complete medium, aseptically add the following solutions to the medium (per 10 ml):",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "The main A entry is a 10 mL aliquot, not 10 g/L or the full A preparation."
  },
  {
    "decision_id": "q16",
    "name": "Sodium acetate strength",
    "stage": "Filtered completion stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[0]",
        "stored": {
          "preferred_term": "1.0 M Sodium acetate (filter--sterilized)",
          "concentration": {
            "value": "0.2",
            "unit": "G_PER_L"
          },
          "notes": "Role: Buffer; Properties: Defined component, Solution, Organic compound"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[0]",
        "stored": {
          "preferred_term": "1.0 M Sodium acetate (filter--sterilized)",
          "concentration": {
            "value": "0.2",
            "unit": "G_PER_L"
          },
          "notes": "Role: Buffer; Properties: Defined component, Solution, Organic compound"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "MOLAR"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 9: 1.0 M Sodium acetate (filter-sterilized) &#124; 0.2 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1.0 M Sodium acetate (filter-sterilized)               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      }
    ],
    "interpretation": "Represent stock strength separately from its milliliter dose. The bicarbonate source does not state w/v, w/w or v/v; the acetate source explicitly states 1.0 M."
  },
  {
    "decision_id": "q17",
    "name": "Bicarbonate strength",
    "stage": "Filtered completion stock",
    "decision": "schema_gap",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[0]",
        "stored": {
          "preferred_term": "5% NaHCO3 solution (filter--sterilized)",
          "composition": [],
          "concentration": {
            "value": "0.4",
            "unit": "G_PER_L"
          },
          "notes": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[0]",
        "stored": {
          "preferred_term": "5% NaHCO3 solution (filter--sterilized)",
          "composition": [],
          "concentration": {
            "value": "0.4",
            "unit": "G_PER_L"
          },
          "notes": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution",
          "name": "Unknown solution"
        }
      }
    ],
    "desired": {
      "source_value": 5,
      "source_literal_unit": "%",
      "percentage_basis": null,
      "structured_concentration_unit": null
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Exact HTML table row 10: 5% NaHCO 3 solution (filter-sterilized) &#124; 0.4 &#124; ml",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution (filter-sterilized)             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae"
      }
    ],
    "interpretation": "Represent stock strength separately from its milliliter dose. The bicarbonate source does not state w/v, w/w or v/v; the acetate source explicitly states 1.0 M."
  },
  {
    "decision_id": "q18",
    "name": "Carbon dioxide gas",
    "stage": "A gas phase",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dissolved_mass_concentration": null,
      "scope": "A atmosphere"
    },
    "source_snippets": [
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "VARIABLE does not quantify dissolved gas. Preserve the separate stage; the explicit A mixture ratio is recorded independently and must not be transferred to B."
  },
  {
    "decision_id": "q19",
    "name": "Nitrogen gas",
    "stage": "A gas phase",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dissolved_mass_concentration": null,
      "scope": "A atmosphere"
    },
    "source_snippets": [
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nitrogen gas\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "VARIABLE does not quantify dissolved gas. Preserve the separate stage; the explicit A mixture ratio is recorded independently and must not be transferred to B."
  },
  {
    "decision_id": "q20",
    "name": "N2",
    "stage": "B stock gas phase",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dissolved_mass_concentration": null,
      "scope": "B atmosphere"
    },
    "source_snippets": [
      {
        "source_key": "togoM584original_network_retry",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"N2\"",
        "snapshot_sha256": "6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b"
      }
    ],
    "interpretation": "VARIABLE does not quantify dissolved gas. Preserve the separate stage; the explicit A mixture ratio is recorded independently and must not be transferred to B."
  },
  {
    "decision_id": "q21",
    "name": "Distilled water",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "desired": {
      "source_row": [
        "Distilled water",
        "1.0",
        "L"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 32: Distilled water &#124; 1.0 &#124; L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q22",
    "name": "Distilled water",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "Distilled water",
        "1.0",
        "L"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 32: Distilled water &#124; 1.0 &#124; L",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q23",
    "name": "MgSO4・7H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 3.5, 3.0]\n\nSource batch input: 3 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "MgSO 4 ·7H 2 O",
        "3.0",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 21: MgSO 4 ·7H 2 O &#124; 3.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q24",
    "name": "MgSO4・7H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "MgSO 4 ·7H 2 O",
        "3.0",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 21: MgSO 4 ·7H 2 O &#124; 3.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q25",
    "name": "NaCl",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 13.85, 1.0]\n\nSource batch input: 1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "NaCl",
        "1.0",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 23: NaCl &#124; 1.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q26",
    "name": "NaCl",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "NaCl",
        "1.0",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 23: NaCl &#124; 1.0 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q27",
    "name": "CaCl2・2H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "CaCl 2 ·2H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 26: CaCl 2 ·2H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q28",
    "name": "CaCl2・2H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "CaCl 2 ·2H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 26: CaCl 2 ·2H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q29",
    "name": "Na2MoO4・2H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "Na 2 MoO 4 ·2H 2 O",
        "0.01",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 31: Na 2 MoO 4 ·2H 2 O &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q30",
    "name": "Na2MoO4・2H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "Na 2 MoO 4 ·2H 2 O",
        "0.01",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 31: Na 2 MoO 4 ·2H 2 O &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q31",
    "name": "H3BO3",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "H 3 BO 3",
        "0.01",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 30: H 3 BO 3 &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q32",
    "name": "H3BO3",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "H 3 BO 3",
        "0.01",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 30: H 3 BO 3 &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q33",
    "name": "FeSO4・7H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "FeSO 4 ·7H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 24: FeSO 4 ·7H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q34",
    "name": "FeSO4・7H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "FeSO 4 ·7H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 24: FeSO 4 ·7H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q35",
    "name": "ZnSO4・7H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "ZnSO 4 ·7H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 27: ZnSO 4 ·7H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q36",
    "name": "ZnSO4・7H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "ZnSO 4 ·7H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 27: ZnSO 4 ·7H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q37",
    "name": "CuSO4・5H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[8].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "CuSO 4 ·5H 2 O",
        "0.01",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 28: CuSO 4 ·5H 2 O &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q38",
    "name": "CuSO4・5H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "CuSO 4 ·5H 2 O",
        "0.01",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 28: CuSO 4 ·5H 2 O &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q39",
    "name": "CoSO4・7H2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[9].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "CoSO 4 ·7H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 25: CoSO 4 ·7H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[9]",
        "exact_source_quote": "\"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q40",
    "name": "CoSO4・7H2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "CoSO 4 ·7H 2 O",
        "0.1",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 25: CoSO 4 ·7H 2 O &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[9]",
        "exact_source_quote": "\"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q41",
    "name": "Nitrilotriacetic acid",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[10].notes",
        "stored": "Role: Mineral source; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "Nitrilotriacetic acid",
        "1.5",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 20: Nitrilotriacetic acid &#124; 1.5 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nitrilotriacetic acid                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[10]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q42",
    "name": "Nitrilotriacetic acid",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "Nitrilotriacetic acid",
        "1.5",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 20: Nitrilotriacetic acid &#124; 1.5 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nitrilotriacetic acid                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[10]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q43",
    "name": "MnSO4・xH2O",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[11].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "MnSO 4 · x H 2 O",
        "0.5",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 22: MnSO 4 · x H 2 O &#124; 0.5 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[11]",
        "exact_source_quote": "\"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q44",
    "name": "MnSO4・xH2O",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "MnSO 4 · x H 2 O",
        "0.5",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 22: MnSO 4 · x H 2 O &#124; 0.5 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[11]",
        "exact_source_quote": "\"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q45",
    "name": "AlK(SO4)2",
    "stage": "Existing M142 trace-stock entry",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].composition[12].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "desired": {
      "source_row": [
        "AlK(SO 4 ) 2",
        "0.01",
        "g"
      ],
      "scope": "Stock batch, not receiving medium"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 29: AlK(SO 4 ) 2 &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; AlK(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[12]",
        "exact_source_quote": "\"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The existing stock water volume or batch-mass note has attached exact raw/hash evidence. This verifies that amount representation only, not the child amount, stock dose, chemical form or final-medium concentration."
  },
  {
    "decision_id": "q46",
    "name": "AlK(SO4)2",
    "stage": "JCM 579 resolved trace stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "desired": {
      "source_row": [
        "AlK(SO 4 ) 2",
        "0.01",
        "g"
      ],
      "scope": "Named trace recipe; receiving dose 10 mL per A batch"
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact HTML table row 29: AlK(SO 4 ) 2 &#124; 0.01 &#124; g",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; AlK(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[12]",
        "exact_source_quote": "\"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "Retain a verified scoped stock reference or composition. Do not flatten this trace recipe into the A ingredients or transfer unrelated M142 content."
  },
  {
    "decision_id": "q47",
    "name": "A pH",
    "stage": "JCM 579 preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 7.2
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "A pH exact text",
        "exact_source_quote": "Mix ingredients and adjust pH to 7.2.",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "Preserve the A-stage pH and atmosphere, example status of the tube fill, and the displayed collection default for autoclaved A/B. The acetate and bicarbonate stocks are filtered."
  },
  {
    "decision_id": "q48",
    "name": "A gas ratio",
    "stage": "JCM 579 preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "species": [
        "N2",
        "CO2"
      ],
      "ratio": "4:1",
      "basis": "v/v"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "A gas ratio exact text",
        "exact_source_quote": "under a N 2 -CO 2 gas mixture (4:1, v/v)",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "Preserve the A-stage pH and atmosphere, example status of the tube fill, and the displayed collection default for autoclaved A/B. The acetate and bicarbonate stocks are filtered."
  },
  {
    "decision_id": "q49",
    "name": "Tube fill example",
    "stage": "JCM 579 preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 10,
      "unit": "ML",
      "conditional": "example"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Tube fill example exact text",
        "exact_source_quote": "e.g., 10 ml in the Hungate tubes",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "Preserve the A-stage pH and atmosphere, example status of the tube fill, and the displayed collection default for autoclaved A/B. The acetate and bicarbonate stocks are filtered."
  },
  {
    "decision_id": "q50",
    "name": "Autoclave temperature",
    "stage": "JCM 579 preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 121,
      "unit": "DEG_C"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Autoclave temperature exact text",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "Preserve the A-stage pH and atmosphere, example status of the tube fill, and the displayed collection default for autoclaved A/B. The acetate and bicarbonate stocks are filtered."
  },
  {
    "decision_id": "q51",
    "name": "Autoclave duration",
    "stage": "JCM 579 preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 15,
      "unit": "MIN"
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Autoclave duration exact text",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "Preserve the A-stage pH and atmosphere, example status of the tube fill, and the displayed collection default for autoclaved A/B. The acetate and bicarbonate stocks are filtered."
  },
  {
    "decision_id": "q52",
    "name": "Trace initial pH",
    "stage": "Transferred trace-stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      }
    ],
    "desired": {
      "value": 6.5
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Trace-minerals preparation",
        "exact_source_quote": "adjust pH to 6.5 with KOH solution.",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
        "parsed_text_sha256": "e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9"
      }
    ],
    "interpretation": "Preserve the named stock pH stages separately from A pH 7.2 and any final-medium pH."
  },
  {
    "decision_id": "q53",
    "name": "Trace final pH",
    "stage": "Transferred trace-stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      }
    ],
    "desired": {
      "value": 7
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Trace-minerals preparation",
        "exact_source_quote": "Adjust final pH to 7.0.",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
        "parsed_text_sha256": "e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9"
      }
    ],
    "interpretation": "Preserve the named stock pH stages separately from A pH 7.2 and any final-medium pH."
  },
  {
    "decision_id": "q54",
    "name": "KOH strength and dose",
    "stage": "Trace-stock titration",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
        "field_path": "solutions[1].solutions[0]",
        "stored": {
          "preferred_term": "KOH solution",
          "composition": [],
          "notes": "Role: Mineral source; Properties: Defined component, Solution\n\npH-adjustment reagent; no fixed dose is specified. Normality is not converted to molarity.",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      }
    ],
    "desired": {
      "strength": null,
      "dose": null
    },
    "source_snippets": [
      {
        "source_key": "jcm151",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Trace stock pH adjustment",
        "exact_source_quote": "adjust pH to 6.5 with KOH solution.",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
        "parsed_text_sha256": "e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9"
      },
      {
        "source_key": "togoM142original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[13]",
        "exact_source_quote": "\"component_name\": \"KOH solution\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ],
    "interpretation": "The source names KOH solution without a strength or fixed dose. Existing absence of a numerical concentration is retained; no conventional solution is invented."
  },
  {
    "decision_id": "q55",
    "name": "B nitrogen purity and measured final volume",
    "stage": "B handling and completed medium",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "B_gas": "N2",
      "B_purity_percent": null,
      "measured_final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "B preparation",
        "exact_source_quote": "Autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      },
      {
        "source_key": "jcm579_network_retry",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579",
        "source_locator": "Completion basis",
        "exact_source_quote": "To complete medium, aseptically add the following solutions to the medium (per 10 ml):",
        "snapshot_sha256": "9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae",
        "parsed_text_sha256": "f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6"
      }
    ],
    "interpretation": "Do not infer 100% nitrogen, a measured final volume, or a final pH from a stock aliquot and additive volume arithmetic."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009980.

10 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 11/13 primary and 7/13 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 13: primary 84.62%; secondary 53.85%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009980.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Receiving recipe and exact stock boundaries

identity: concern. Targets: CultureMech:009980.

TOGO M584 resolves to JCM 579. Its A/B references are internal recipe stages; local links 5342/5343 resolve to incompatible high-salt recipes. The trace dependency transfers only JCM 151 trace minerals.

### Receiving and transferred supplied forms

grounding: concern. Targets: CultureMech:009980.

Receiving B explicitly uses unhydrated CaCl2 and MgCl2 hexahydrate; the distinct trace stock uses calcium chloride dihydrate. Those distinctions are supported. The transferred MnSO4·xH2O leaves hydration unspecified while its maintained ID encodes anhydrous MnSO4; preserve the source qualification without inventing x. Other in-scope supplied forms and labels were checked.

### Separate preparation, gas and pH stages

completeness: concern. Targets: CultureMech:009980.

A pH 7.2, A nitrogen/carbon dioxide 4:1 v/v, filtered completion stocks, B nitrogen handling and the collection sterilization default are missing. Trace pH 6.5 then 7 belongs only to that stock.

### Classification and growth evidence

scope: supported. Targets: CultureMech:009980.

Yeast extract supports an undefined complex formulation. The medium name and bacterial provenance do not establish strain growth, temperature or incubation duration; no such assertion is added.

## Findings

### f1: A and B point to unrelated high-salt stocks

blocker / open / confirmed; issue key: culturemech.009980.wrong-stock-identities.

Both local layers link A and B to 5342/5343 despite incompatible source formulations. Exact identity resolution does not establish recipe equivalence.

### f2: Liquid doses, water and stock masses lose their stages

major / open / confirmed; issue key: culturemech.009980.collapsed-preparation-quantities.

Both layers store the completion liquid doses and A aliquot as G_PER_L, merge 1 L A water with 10 mL B water as 11 G_PER_L, and flatten B salts and A masses. The receiving basis is explicitly per 10 mL A.

### f3: Named trace recipe and handling remain unresolved in the receiving record

major / open / confirmed; issue key: culturemech.009980.unrepresented-trace-stock.

The receiving trace entry has empty composition and no exact maintained stock reference. Its thirteen available historical amount claims belong to the M142 trace stock only. Parent basal, sulfur and variant material must remain excluded.

### f4: Transferred manganese sulfate hydration is not represented

major / open / confirmed; issue key: culturemech.009980.trace-hydration-scope.

JCM 151 and TOGO M142 print MnSO4·xH2O while the transferred maintained term has an anhydrous MnSO4 structure. The exact hydration number is unresolved; no replacement hydrate is inferred.

### f5: Source pH, atmosphere and sterilization stages are absent

major / open / confirmed; issue key: culturemech.009980.missing-preparation.

Both receiving layers lack the explicit A pH, A gas ratio, separately autoclaved B and filtered completion-stock procedure. An unqualified B nitrogen atmosphere does not supply a numerical purity.

## Recommended Actions And Acceptance Checks

### a1

Resolve the specific JCM 579 A/B stages in maintained inputs and remove incompatible references; do not modify the unrelated stock records to fit this medium.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore original units and separate A, B and completion stock scopes without assuming a measured final volume or bicarbonate percentage basis.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent the named trace recipe through a verified scoped reference or composition; retain its own quantities, pH steps and evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the unspecified hydrate qualification in the maintained stock and resolve its chemical correspondence independently of the amount evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Add the exact scoped procedure and collection default with evidence, preserving example tube fill and unresolved percent/final-volume quantities.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch038/372/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch038/372/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml:1:id: CultureMech:009980<br>./data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml:1:id: CultureMech:009980<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch038/source-preflight-bound/372/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 50 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| main | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579; Completion paragraph | supports | Exact JCM 579 defines the receiving basis independently of stock preparation quantities. |
| trace | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Trace minerals subsection only | supports | Only the named trace stock transfers; basal medium, sulfur, reducers and parent variants are excluded. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584; $.meta | supports | Exact TOGO M584 points to JCM 579 and preserves separate A/B component sections. |
| wrong-a | https://mediadive.dsmz.de/rest/solution/5342; $.data.recipe and $.data.steps | supports | Asserted solution 5342 is a distinct high-salt A recipe made up to 500 mL; it is not JCM 579 A. |
| wrong-b | https://mediadive.dsmz.de/rest/solution/5343; $.data.recipe and $.data.steps | supports | Asserted solution 5343 is a carbonate/high-salt B recipe made up to 500 mL; it is not JCM 579 B. |
| trace-owner | data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml; solutions[1], its 13 composition entries, preparation and attached evidence | context_only | Read the exact transferred stock and source history. Parent receiving dose and unrelated basal, sulfur and variant content are excluded. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch038/372/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3312 resolves to calcium dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| trace-grounding | /private/tmp/culturemech-review-work-batch038/372/grounding-inventory.json; All asserted transferred trace IDs and current secondary rows checked; manganese hydration remains source-unspecified xH2O, unlike the anhydrous structure. | context_only | All asserted transferred trace IDs and current secondary rows checked; manganese hydration remains source-unspecified xH2O, unlike the anhydrous structure. |
| trace-history | /private/tmp/culturemech-review-work-batch038/372/history-inventory.json; Thirteen transferred stock claims match exact raw bytes and recorded source hashes; their original access metadata is retained. | context_only | Thirteen transferred stock claims match exact raw bytes and recorded source hashes; their original access metadata is retained. |
| history-metadata | data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import, generic-name resolution and duplicate handling are mechanisms only; their historical execution is not inferred from current fields. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import, generic-name resolution and duplicate handling are mechanisms only; their historical execution is not inferred from current fields. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import, generic-name resolution and duplicate handling are mechanisms only; their historical execution is not inferred from current fields. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import, generic-name resolution and duplicate handling are mechanisms only; their historical execution is not inferred from current fields. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No target or maintained receiving amount is verified by attached evidence. The thirteen verified decisions refer exclusively to existing M142 trace-stock notes or water volume.
- Parent sulfur legacy MediaIngredientMech:001072 and all unrelated parent formulations/variants are outside this review transfer; they are not a required missing correspondence for JCM 579.
- Current exact primaries resolve the scientific recipe; unavailable redundant APIs are not treated as evidence of recipe absence or historical byte equivalence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T210353Z-culturemech-009980-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_aa_medium (CultureMech:009980)'
started_at: '2026-10-21T20:59:30Z'
finished_at: '2026-10-21T21:03:53Z'
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
summary: JCM 579 specifies a separate Solution A, a 10 mL Solution B stock and completion
  doses per 10 mL A. Both local layers flatten those stages, store liquid doses as
  mass concentrations, and link A/B to unrelated high-salt stocks. The named JCM 151
  trace recipe is independently available; thirteen existing M142 trace claims authenticate
  that stock layer only.
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
  - path: data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
    sha256: 4bd982be14d3b22375990e0ef49226b9f25f03b5fa558139dfd854036ab777de
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
    sha256: e4d99cb535887ebc7962871c18fb0c44c39cd004e189ae753a5c85fc0bf81187
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
  selection: Task review 372; batch 038 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:009980
targets:
- target_id: CultureMech:009980
  path: data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  label: bacillus_aa_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch038/372/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch038/372/strict.tsv"
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009980
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
  - CultureMech:009980
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:59:58.982845Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch038/372/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:00.142517Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-038/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch038/372/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:01.639294Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:00:02.621518Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T21:03:52Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml:1:id:
    CultureMech:009980

    ./data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml:1:id: CultureMech:009980

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/source-preflight-bound/372/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T21:03:52Z'
  support: supports
  summary: 50 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: aadfa8418bd19f8da9914e6545574482be3af892a249d5a6ab4122fec4033519
- evidence_id: main
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579
  locator: Completion paragraph
  accessed_at: '2026-10-21T20:20:20.593622Z'
  support: supports
  summary: Exact JCM 579 defines the receiving basis independently of stock preparation
    quantities.
  quote: 'To complete medium, aseptically add the following solutions to the medium
    (per 10 ml):'
  snapshot_sha256: 9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae
- evidence_id: trace
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  locator: Trace minerals subsection only
  accessed_at: '2026-10-21T09:01:28.851101Z'
  support: supports
  summary: Only the named trace stock transfers; basal medium, sulfur, reducers and
    parent variants are excluded.
  quote: 'Trace minerals:'
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584
  locator: $.meta
  accessed_at: '2026-10-21T20:20:19.870808Z'
  support: supports
  summary: Exact TOGO M584 points to JCM 579 and preserves separate A/B component
    sections.
  quote: '"original_media_id": "JCM_M579"'
  snapshot_sha256: 6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b
- evidence_id: wrong-a
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: $.data.recipe and $.data.steps
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: supports
  summary: Asserted solution 5342 is a distinct high-salt A recipe made up to 500
    mL; it is not JCM 579 A.
  quote: '"amount": 100'
  snapshot_sha256: 4bf262e02d0a83f9d1a24a52d2a14383aa8c6f27384e446d7da6274a05319240
- evidence_id: wrong-b
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: $.data.recipe and $.data.steps
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: supports
  summary: Asserted solution 5343 is a carbonate/high-salt B recipe made up to 500
    mL; it is not JCM 579 B.
  quote: '"amount": 80'
  snapshot_sha256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- evidence_id: trace-owner
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
  locator: solutions[1], its 13 composition entries, preparation and attached evidence
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Read the exact transferred stock and source history. Parent receiving dose
    and unrelated basal, sulfur and variant content are excluded.
  snapshot_sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/372/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 956bf1fe7c3423a95e9bbdb02ca7d7aee4113f7dcb233d1d8b08ee0691075875
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
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: CHEBI:3312 resolves to calcium dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
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
  accessed_at: '2026-10-21T21:03:52Z'
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
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: trace-grounding
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/372/grounding-inventory.json
  locator: All asserted transferred trace IDs and current secondary rows checked;
    manganese hydration remains source-unspecified xH2O, unlike the anhydrous structure.
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: All asserted transferred trace IDs and current secondary rows checked;
    manganese hydration remains source-unspecified xH2O, unlike the anhydrous structure.
  snapshot_sha256: e96a93576fa8cbff4ed9eeb1c4ff6e87adcccb4bfbab68b199bebd904c1fb29b
- evidence_id: trace-history
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch038/372/history-inventory.json
  locator: Thirteen transferred stock claims match exact raw bytes and recorded source
    hashes; their original access metadata is retained.
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Thirteen transferred stock claims match exact raw bytes and recorded source
    hashes; their original access metadata is retained.
  snapshot_sha256: 047bfe7cc71943617ce4e04297c87a4faff1e5dab703a9ff2d3c8bd456082d06
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml", "events":
    12, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Current import, generic-name resolution and duplicate handling are mechanisms
    only; their historical execution is not inferred from current fields.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Current import, generic-name resolution and duplicate handling are mechanisms
    only; their historical execution is not inferred from current fields.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Current import, generic-name resolution and duplicate handling are mechanisms
    only; their historical execution is not inferred from current fields.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:03:52Z'
  support: context_only
  summary: Current import, generic-name resolution and duplicate handling are mechanisms
    only; their historical execution is not inferred from current fields.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009980
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
  - CultureMech:009980
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Yeast extract\"\
    ,\n    \"stage\": \"Solution A batch\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"Yeast\
    \ extract\",\n        \"1.0\",\n        \"g\"\n      ],\n      \"basis\": \"A\
    \ batch with 1 L water and 10 mL trace stock\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 5: Yeast extract | 1.0 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Yeast extract                                         \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch mass and\
    \ its A-stage membership. The current flat G_PER_L field does not encode the staged\
    \ recipe or establish a measured final-medium denominator.\"\n  },\n  {\n    \"\
    decision_id\": \"q2\",\n    \"name\": \"NaCl\",\n    \"stage\": \"Solution A batch\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"NaCl\"\
    ,\n        \"1.0\",\n        \"g\"\n      ],\n      \"basis\": \"A batch with\
    \ 1 L water and 10 mL trace stock\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 3: NaCl | 1.0 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> NaCl                                                  \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch mass and\
    \ its A-stage membership. The current flat G_PER_L field does not encode the staged\
    \ recipe or establish a measured final-medium denominator.\"\n  },\n  {\n    \"\
    decision_id\": \"q3\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"Solution A\
    \ batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"KH 2\
    \ PO 4\",\n        \"0.3\",\n        \"g\"\n      ],\n      \"basis\": \"A batch\
    \ with 1 L water and 10 mL trace stock\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 0: KH 2 PO 4 | 0.3 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                          \
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch mass and\
    \ its A-stage membership. The current flat G_PER_L field does not encode the staged\
    \ recipe or establish a measured final-medium denominator.\"\n  },\n  {\n    \"\
    decision_id\": \"q4\",\n    \"name\": \"NH4Cl\",\n    \"stage\": \"Solution A\
    \ batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"NH 4\
    \ Cl\",\n        \"1.0\",\n        \"g\"\n      ],\n      \"basis\": \"A batch\
    \ with 1 L water and 10 mL trace stock\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 2: NH 4 Cl | 1.0 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                      \
    \          </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch mass and\
    \ its A-stage membership. The current flat G_PER_L field does not encode the staged\
    \ recipe or establish a measured final-medium denominator.\"\n  },\n  {\n    \"\
    decision_id\": \"q5\",\n    \"name\": \"K2HPO4\",\n    \"stage\": \"Solution A\
    \ batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"K 2 HPO\
    \ 4\",\n        \"0.3\",\n        \"g\"\n      ],\n      \"basis\": \"A batch\
    \ with 1 L water and 10 mL trace stock\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 1: K 2 HPO 4 | 0.3 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>                          \
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch mass and\
    \ its A-stage membership. The current flat G_PER_L field does not encode the staged\
    \ recipe or establish a measured final-medium denominator.\"\n  },\n  {\n    \"\
    decision_id\": \"q6\",\n    \"name\": \"KCl\",\n    \"stage\": \"Solution A batch\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"KCl\"\
    ,\n        \"0.1\",\n        \"g\"\n      ],\n      \"basis\": \"A batch with\
    \ 1 L water and 10 mL trace stock\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 4: KCl | 0.1 | g\",\n        \"exact_source_quote\":\
    \ \"<TR><TD WIDTH=75%> KCl                                                   \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch mass and\
    \ its A-stage membership. The current flat G_PER_L field does not encode the staged\
    \ recipe or establish a measured final-medium denominator.\"\n  },\n  {\n    \"\
    decision_id\": \"q7\",\n    \"name\": \"Distilled water\",\n    \"stage\": \"\
    Solution A water\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\",\n      \"scope\": \"Solution A water\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 7: Distilled water | 1.0 | L\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"Split the single merged 11 G_PER_L\
    \ field into the two exact water inputs. The numerals 1 L and 10 mL must not be\
    \ summed without units or treated as a final-medium mass.\"\n  },\n  {\n    \"\
    decision_id\": \"q8\",\n    \"name\": \"Distilled water\",\n    \"stage\": \"\
    Solution B water\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\"\
    : \"ML\",\n      \"scope\": \"Solution B water\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 13: Distilled water | 10.0 | ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \ </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\n      }\n\
    \    ],\n    \"interpretation\": \"Split the single merged 11 G_PER_L field into\
    \ the two exact water inputs. The numerals 1 L and 10 mL must not be summed without\
    \ units or treated as a final-medium mass.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q9\",\n    \"name\": \"MgCl2・6H2O\",\n    \"stage\": \"Solution B stock batch\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"MgCl\
    \ 2 ·6H 2 O\",\n        \"0.5\",\n        \"g\"\n      ],\n      \"basis\": \"\
    B stock prepared with 10 mL water\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 12: MgCl 2 ·6H 2 O | 0.5 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"These are gram quantities for the\
    \ B stock, not final-medium concentrations. Keep the receiving 0.1 mL B dose separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"name\": \"CaCl2\",\n    \"stage\"\
    : \"Solution B stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"CaCl\
    \ 2\",\n        \"0.1\",\n        \"g\"\n      ],\n      \"basis\": \"B stock\
    \ prepared with 10 mL water\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm579_network_retry\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 11: CaCl 2 | 0.1 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> CaCl<sub>2</sub>                                      \
    \          </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"These are gram quantities for the\
    \ B stock, not final-medium concentrations. Keep the receiving 0.1 mL B dose separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q11\",\n    \"name\": \"Sodium acetate dose\"\
    ,\n    \"stage\": \"Receiving stock addition\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.2,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"Per 10 mL A\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 9: 1.0 M Sodium acetate (filter-sterilized) | 0.2 | ml\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 1.0 M Sodium acetate (filter-sterilized)\
    \               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1.0 M Sodium acetate (filter--sterilized)\\\"\
    ,\\n          \\\"volume\\\": 0.2,\\n          \\\"unit\\\": \\\"ml\\\",\\n  \
    \        \\\"conc_value\\\": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n\
    \        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored G_PER_L value misrepresents\
    \ a liquid dose. Preserve the explicit receiving stage and do not use the volume\
    \ of an entire stock preparation as a medium addition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"Bicarbonate dose\",\n    \"stage\": \"Receiving stock\
    \ addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.4,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"Per 10 mL A\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 10: 5% NaHCO 3 solution (filter-sterilized) | 0.4 | ml\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% NaHCO<sub>3</sub> solution\
    \ (filter-sterilized)             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% NaHCO3 solution (filter--sterilized)\\\",\\\
    n          \\\"volume\\\": 0.4,\\n          \\\"unit\\\": \\\"ml\\\",\\n     \
    \     \\\"conc_value\\\": 5,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n   \
    \     \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored G_PER_L value misrepresents\
    \ a liquid dose. Preserve the explicit receiving stage and do not use the volume\
    \ of an entire stock preparation as a medium addition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"name\": \"Solution B dose\",\n    \"stage\": \"Receiving stock\
    \ addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.1,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"Per 10 mL A\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 8: Solution B (see below) | 0.1 | ml\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Solution B (see below)                                \
    \   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored G_PER_L value misrepresents\
    \ a liquid dose. Preserve the explicit receiving stage and do not use the volume\
    \ of an entire stock preparation as a medium addition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"name\": \"Trace-mineral dose\",\n    \"stage\": \"Receiving\
    \ stock addition\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"Per A batch with 1 L water\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Exact HTML table row 6: Trace minerals (see Medium No. 151 ) | 10.0 | ml\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Trace minerals (see Medium\
    \ No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=151\\\">151</a>)                \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      },\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace minerals (see Medium [M142])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored G_PER_L value misrepresents\
    \ a liquid dose. Preserve the explicit receiving stage and do not use the volume\
    \ of an entire stock preparation as a medium addition.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"name\": \"Solution A receiving aliquot\",\n    \"stage\": \"\
    Completion basis\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\": \"\
    ML\",\n      \"basis\": \"A aliquot before the three completion doses\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM584original_network_retry\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      },\n      {\n        \"source_key\": \"jcm579_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"Completion paragraph\",\n        \"exact_source_quote\"\
    : \"To complete medium, aseptically add the following solutions to the medium\
    \ (per 10 ml):\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"The main A entry is a 10 mL aliquot,\
    \ not 10 g/L or the full A preparation.\"\n  },\n  {\n    \"decision_id\": \"\
    q16\",\n    \"name\": \"Sodium acetate strength\",\n    \"stage\": \"Filtered\
    \ completion stock\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0]\",\n        \"stored\": {\n      \
    \    \"preferred_term\": \"1.0 M Sodium acetate (filter--sterilized)\",\n    \
    \      \"concentration\": {\n            \"value\": \"0.2\",\n            \"unit\"\
    : \"G_PER_L\"\n          },\n          \"notes\": \"Role: Buffer; Properties:\
    \ Defined component, Solution, Organic compound\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0]\",\n        \"stored\": {\n      \
    \    \"preferred_term\": \"1.0 M Sodium acetate (filter--sterilized)\",\n    \
    \      \"concentration\": {\n            \"value\": \"0.2\",\n            \"unit\"\
    : \"G_PER_L\"\n          },\n          \"notes\": \"Role: Buffer; Properties:\
    \ Defined component, Solution, Organic compound\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"value\": 1,\n      \"unit\": \"MOLAR\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm579_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"Exact HTML table row 9: 1.0 M Sodium acetate\
    \ (filter-sterilized) | 0.2 | ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> 1.0 M Sodium acetate (filter-sterilized)               </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent stock strength separately\
    \ from its milliliter dose. The bicarbonate source does not state w/v, w/w or\
    \ v/v; the acetate source explicitly states 1.0 M.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"name\": \"Bicarbonate strength\",\n    \"stage\": \"Filtered\
    \ completion stock\",\n    \"decision\": \"schema_gap\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"5% NaHCO3 solution (filter--sterilized)\",\n        \
    \  \"composition\": [],\n          \"concentration\": {\n            \"value\"\
    : \"0.4\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"Role: Buffer; Properties: Defined component, Inorganic compound, Solution\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"5% NaHCO3 solution (filter--sterilized)\",\n        \
    \  \"composition\": [],\n          \"concentration\": {\n            \"value\"\
    : \"0.4\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"Role: Buffer; Properties: Defined component, Inorganic compound, Solution\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"source_value\": 5,\n      \"source_literal_unit\": \"%\"\
    ,\n      \"percentage_basis\": null,\n      \"structured_concentration_unit\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm579_network_retry\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"Exact HTML table row 10: 5% NaHCO 3 solution\
    \ (filter-sterilized) | 0.4 | ml\",\n        \"exact_source_quote\": \"<TR><TD\
    \ WIDTH=75%> 5% NaHCO<sub>3</sub> solution (filter-sterilized)             </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    \n      }\n    ],\n    \"interpretation\": \"Represent stock strength separately\
    \ from its milliliter dose. The bicarbonate source does not state w/v, w/w or\
    \ v/v; the acetate source explicitly states 1.0 M.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"name\": \"Carbon dioxide gas\",\n    \"stage\": \"A gas phase\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dissolved_mass_concentration\"\
    : null,\n      \"scope\": \"A atmosphere\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM584original_network_retry\",\n      \
    \  \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\n     \
    \ }\n    ],\n    \"interpretation\": \"VARIABLE does not quantify dissolved gas.\
    \ Preserve the separate stage; the explicit A mixture ratio is recorded independently\
    \ and must not be transferred to B.\"\n  },\n  {\n    \"decision_id\": \"q19\"\
    ,\n    \"name\": \"Nitrogen gas\",\n    \"stage\": \"A gas phase\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\": \"\
    ingredients[9].concentration\",\n        \"stored\": {\n          \"value\": \"\
    variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dissolved_mass_concentration\"\
    : null,\n      \"scope\": \"A atmosphere\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM584original_network_retry\",\n      \
    \  \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\n     \
    \ }\n    ],\n    \"interpretation\": \"VARIABLE does not quantify dissolved gas.\
    \ Preserve the separate stage; the explicit A mixture ratio is recorded independently\
    \ and must not be transferred to B.\"\n  },\n  {\n    \"decision_id\": \"q20\"\
    ,\n    \"name\": \"N2\",\n    \"stage\": \"B stock gas phase\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\": \"\
    ingredients[12].concentration\",\n        \"stored\": {\n          \"value\":\
    \ \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dissolved_mass_concentration\"\
    : null,\n      \"scope\": \"B atmosphere\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM584original_network_retry\",\n      \
    \  \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M584\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"N2\\\"\",\n        \"snapshot_sha256\": \"6bc815263d2d689089c1d5fd054996550d8733d603ff1b3de4b697ac43a9247b\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE does not quantify dissolved\
    \ gas. Preserve the separate stage; the explicit A mixture ratio is recorded independently\
    \ and must not be transferred to B.\"\n  },\n  {\n    \"decision_id\": \"q21\"\
    ,\n    \"name\": \"Distilled water\",\n    \"stage\": \"Existing M142 trace-stock\
    \ entry\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        }\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n   \
    \     \"Distilled water\",\n        \"1.0\",\n        \"L\"\n      ],\n      \"\
    scope\": \"Stock batch, not receiving medium\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 32: Distilled water | 1.0 | L\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    Distilled water\",\n        \"1.0\",\n        \"L\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 32: Distilled water | 1.0 | L\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"\
    name\": \"MgSO4・7H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[1].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component [Merged 2 duplicates: 3.5, 3.0]\\n\\nSource batch input: 3 g. Final\
    \ preparation volume is not independently established; the unsupported g/L assertion\
    \ is withdrawn, not replaced by an assumed one-liter concentration.\"\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_row\": [\n        \"MgSO 4 ·7H 2 O\"\
    ,\n        \"3.0\",\n        \"g\"\n      ],\n      \"scope\": \"Stock batch,\
    \ not receiving medium\"\n    },\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"jcm151\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 21: MgSO 4 ·7H 2 O | 3.0\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"name\": \"\
    MgSO4・7H2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    MgSO 4 ·7H 2 O\",\n        \"3.0\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 21: MgSO 4 ·7H 2 O | 3.0 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"\
    name\": \"NaCl\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n       \
    \ \"field_path\": \"solutions[1].composition[2].notes\",\n        \"stored\":\
    \ \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component [Merged 2 duplicates: 13.85, 1.0]\\n\\nSource batch input: 1 g. Final\
    \ preparation volume is not independently established; the unsupported g/L assertion\
    \ is withdrawn, not replaced by an assumed one-liter concentration.\"\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_row\": [\n        \"NaCl\",\n    \
    \    \"1.0\",\n        \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving\
    \ medium\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 23: NaCl | 1.0 | g\",\n\
    \        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaCl                   \
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"name\": \"\
    NaCl\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    NaCl\",\n        \"1.0\",\n        \"g\"\n      ],\n      \"scope\": \"Named trace\
    \ recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 23: NaCl | 1.0 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> NaCl                                                  \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"\
    name\": \"CaCl2・2H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[3].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"CaCl 2 ·2H 2 O\",\n        \"0.1\",\n      \
    \  \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 26: CaCl 2 ·2H 2 O | 0.1\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"name\": \"\
    CaCl2・2H2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    CaCl 2 ·2H 2 O\",\n        \"0.1\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 26: CaCl 2 ·2H 2 O | 0.1 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"\
    name\": \"Na2MoO4・2H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 0.01 g. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\"\
    : {\n      \"source_row\": [\n        \"Na 2 MoO 4 ·2H 2 O\",\n        \"0.01\"\
    ,\n        \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 31: Na 2 MoO 4 ·2H 2 O |\
    \ 0.01 | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O\
    \                             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n      }\n\
    \    ],\n    \"interpretation\": \"The existing stock water volume or batch-mass\
    \ note has attached exact raw/hash evidence. This verifies that amount representation\
    \ only, not the child amount, stock dose, chemical form or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q30\",\n    \"name\": \"Na2MoO4・2H2O\",\n\
    \    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    Na 2 MoO 4 ·2H 2 O\",\n        \"0.01\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 31: Na 2 MoO 4 ·2H 2 O | 0.01 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O    \
    \                         </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n      }\n\
    \    ],\n    \"interpretation\": \"Retain a verified scoped stock reference or\
    \ composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"\
    name\": \"H3BO3\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n       \
    \ \"field_path\": \"solutions[1].composition[5].notes\",\n        \"stored\":\
    \ \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component [Merged 2 duplicates: 15.0, 0.01]\\n\\nSource batch input: 0.01 g.\
    \ Final preparation volume is not independently established; the unsupported g/L\
    \ assertion is withdrawn, not replaced by an assumed one-liter concentration.\"\
    \n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"H 3\
    \ BO 3\",\n        \"0.01\",\n        \"g\"\n      ],\n      \"scope\": \"Stock\
    \ batch, not receiving medium\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm151\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 30: H 3 BO 3 | 0.01 | g\"\
    ,\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>\
    \                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"name\": \"\
    H3BO3\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\":\
    \ \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    H 3 BO 3\",\n        \"0.01\",\n        \"g\"\n      ],\n      \"scope\": \"Named\
    \ trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 30: H 3 BO 3 | 0.01 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                           \
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"\
    name\": \"FeSO4・7H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[6].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"FeSO 4 ·7H 2 O\",\n        \"0.1\",\n      \
    \  \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 24: FeSO 4 ·7H 2 O | 0.1\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q34\",\n    \"name\": \"\
    FeSO4・7H2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    FeSO 4 ·7H 2 O\",\n        \"0.1\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 24: FeSO 4 ·7H 2 O | 0.1 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"\
    name\": \"ZnSO4・7H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[7].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"ZnSO 4 ·7H 2 O\",\n        \"0.1\",\n      \
    \  \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 27: ZnSO 4 ·7H 2 O | 0.1\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"name\": \"\
    ZnSO4・7H2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    ZnSO 4 ·7H 2 O\",\n        \"0.1\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 27: ZnSO 4 ·7H 2 O | 0.1 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"\
    name\": \"CuSO4・5H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[8].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.01 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"CuSO 4 ·5H 2 O\",\n        \"0.01\",\n     \
    \   \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 28: CuSO 4 ·5H 2 O | 0.01\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"name\": \"\
    CuSO4・5H2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    CuSO 4 ·5H 2 O\",\n        \"0.01\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 28: CuSO 4 ·5H 2 O | 0.01 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"\
    name\": \"CoSO4・7H2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[9].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"CoSO 4 ·7H 2 O\",\n        \"0.1\",\n      \
    \  \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 25: CoSO 4 ·7H 2 O | 0.1\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CoSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n    \"name\": \"\
    CoSO4・7H2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    CoSO 4 ·7H 2 O\",\n        \"0.1\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 25: CoSO 4 ·7H 2 O | 0.1 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> CoSO<sub>4</sub>&#183;7H<sub>2</sub>O                 \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"\
    name\": \"Nitrilotriacetic acid\",\n    \"stage\": \"Existing M142 trace-stock\
    \ entry\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Organic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 1.5 g. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\"\
    : {\n      \"source_row\": [\n        \"Nitrilotriacetic acid\",\n        \"1.5\"\
    ,\n        \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 20: Nitrilotriacetic acid\
    \ | 1.5 | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Nitrilotriacetic\
    \ acid                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid\\\",\\n          \\\"volume\\\
    \": 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The existing stock water volume or batch-mass\
    \ note has attached exact raw/hash evidence. This verifies that amount representation\
    \ only, not the child amount, stock dose, chemical form or final-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q42\",\n    \"name\": \"Nitrilotriacetic acid\"\
    ,\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    Nitrilotriacetic acid\",\n        \"1.5\",\n        \"g\"\n      ],\n      \"\
    scope\": \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 20: Nitrilotriacetic acid\
    \ | 1.5 | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Nitrilotriacetic\
    \ acid                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid\\\",\\n          \\\"volume\\\
    \": 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q43\",\n    \"\
    name\": \"MnSO4・xH2O\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[11].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.5 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"MnSO 4 · x H 2 O\",\n        \"0.5\",\n    \
    \    \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 22: MnSO 4 · x H 2 O | 0.5\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MnSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O\
    \                           </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4・xH2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q44\",\n    \"name\": \"\
    MnSO4・xH2O\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    MnSO 4 · x H 2 O\",\n        \"0.5\",\n        \"g\"\n      ],\n      \"scope\"\
    : \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 22: MnSO 4 · x H 2 O | 0.5 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> MnSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O          \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4・xH2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q45\",\n    \"\
    name\": \"AlK(SO4)2\",\n    \"stage\": \"Existing M142 trace-stock entry\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\",\n\
    \        \"field_path\": \"solutions[1].composition[12].notes\",\n        \"stored\"\
    : \"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.01 g. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"desired\": {\n  \
    \    \"source_row\": [\n        \"AlK(SO 4 ) 2\",\n        \"0.01\",\n       \
    \ \"g\"\n      ],\n      \"scope\": \"Stock batch, not receiving medium\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact HTML table row 29: AlK(SO 4 ) 2 | 0.01\
    \ | g\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> AlK(SO<sub>4</sub>)<sub>2</sub>\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"AlK(SO4)2\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing stock water volume or\
    \ batch-mass note has attached exact raw/hash evidence. This verifies that amount\
    \ representation only, not the child amount, stock dose, chemical form or final-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q46\",\n    \"name\": \"\
    AlK(SO4)2\",\n    \"stage\": \"JCM 579 resolved trace stock\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"desired\": {\n      \"source_row\": [\n        \"\
    AlK(SO 4 ) 2\",\n        \"0.01\",\n        \"g\"\n      ],\n      \"scope\":\
    \ \"Named trace recipe; receiving dose 10 mL per A batch\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm151\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact HTML table row 29: AlK(SO 4 ) 2 | 0.01 | g\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> AlK(SO<sub>4</sub>)<sub>2</sub>                       \
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"AlK(SO4)2\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain a verified scoped stock reference\
    \ or composition. Do not flatten this trace recipe into the A ingredients or transfer\
    \ unrelated M142 content.\"\n  },\n  {\n    \"decision_id\": \"q47\",\n    \"\
    name\": \"A pH\",\n    \"stage\": \"JCM 579 preparation\",\n    \"decision\":\
    \ \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 7.2\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"A pH exact text\",\n        \"exact_source_quote\": \"Mix ingredients and\
    \ adjust pH to 7.2.\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the A-stage pH and atmosphere,\
    \ example status of the tube fill, and the displayed collection default for autoclaved\
    \ A/B. The acetate and bicarbonate stocks are filtered.\"\n  },\n  {\n    \"decision_id\"\
    : \"q48\",\n    \"name\": \"A gas ratio\",\n    \"stage\": \"JCM 579 preparation\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"species\": [\n        \"N2\",\n\
    \        \"CO2\"\n      ],\n      \"ratio\": \"4:1\",\n      \"basis\": \"v/v\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm579_network_retry\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"A gas ratio exact text\",\n        \"exact_source_quote\"\
    : \"under a N 2 -CO 2 gas mixture (4:1, v/v)\",\n        \"snapshot_sha256\":\
    \ \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\",\n    \
    \    \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the A-stage pH and atmosphere,\
    \ example status of the tube fill, and the displayed collection default for autoclaved\
    \ A/B. The acetate and bicarbonate stocks are filtered.\"\n  },\n  {\n    \"decision_id\"\
    : \"q49\",\n    \"name\": \"Tube fill example\",\n    \"stage\": \"JCM 579 preparation\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\": \"\
    ML\",\n      \"conditional\": \"example\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"Tube fill example exact text\",\n        \"exact_source_quote\": \"e.g., 10\
    \ ml in the Hungate tubes\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the A-stage pH and atmosphere,\
    \ example status of the tube fill, and the displayed collection default for autoclaved\
    \ A/B. The acetate and bicarbonate stocks are filtered.\"\n  },\n  {\n    \"decision_id\"\
    : \"q50\",\n    \"name\": \"Autoclave temperature\",\n    \"stage\": \"JCM 579\
    \ preparation\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"preparation_steps\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 121,\n      \"unit\": \"\
    DEG_C\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"jcm579_network_retry\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"Autoclave temperature exact text\",\n       \
    \ \"exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the A-stage pH and atmosphere,\
    \ example status of the tube fill, and the displayed collection default for autoclaved\
    \ A/B. The acetate and bicarbonate stocks are filtered.\"\n  },\n  {\n    \"decision_id\"\
    : \"q51\",\n    \"name\": \"Autoclave duration\",\n    \"stage\": \"JCM 579 preparation\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 15,\n      \"unit\": \"\
    MIN\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm579_network_retry\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"Autoclave duration exact text\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the A-stage pH and atmosphere,\
    \ example status of the tube fill, and the displayed collection default for autoclaved\
    \ A/B. The acetate and bicarbonate stocks are filtered.\"\n  },\n  {\n    \"decision_id\"\
    : \"q52\",\n    \"name\": \"Trace initial pH\",\n    \"stage\": \"Transferred\
    \ trace-stock preparation\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"desired\": {\n      \"value\": 6.5\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Trace-minerals preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 6.5 with KOH solution.\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    ,\n        \"parsed_text_sha256\": \"e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the named stock pH stages\
    \ separately from A pH 7.2 and any final-medium pH.\"\n  },\n  {\n    \"decision_id\"\
    : \"q53\",\n    \"name\": \"Trace final pH\",\n    \"stage\": \"Transferred trace-stock\
    \ preparation\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\":\
    \ null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"desired\": {\n      \"value\": 7\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm151\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n  \
    \      \"source_locator\": \"Trace-minerals preparation\",\n        \"exact_source_quote\"\
    : \"Adjust final pH to 7.0.\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    ,\n        \"parsed_text_sha256\": \"e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the named stock pH stages\
    \ separately from A pH 7.2 and any final-medium pH.\"\n  },\n  {\n    \"decision_id\"\
    : \"q54\",\n    \"name\": \"KOH strength and dose\",\n    \"stage\": \"Trace-stock\
    \ titration\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].solutions[0]\",\n        \"stored\"\
    : {\n          \"preferred_term\": \"KOH solution\",\n          \"composition\"\
    : [],\n          \"notes\": \"Role: Mineral source; Properties: Defined component,\
    \ Solution\\n\\npH-adjustment reagent; no fixed dose is specified. Normality is\
    \ not converted to molarity.\",\n          \"name\": \"Unknown solution\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"desired\": {\n      \"strength\": null,\n     \
    \ \"dose\": null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Trace stock pH adjustment\",\n        \"exact_source_quote\"\
    : \"adjust pH to 6.5 with KOH solution.\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    ,\n        \"parsed_text_sha256\": \"e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9\"\
    \n      },\n      {\n        \"source_key\": \"togoM142original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KOH solution\\\"\",\n        \"snapshot_sha256\"\
    : \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The source names KOH solution without a\
    \ strength or fixed dose. Existing absence of a numerical concentration is retained;\
    \ no conventional solution is invented.\"\n  },\n  {\n    \"decision_id\": \"\
    q55\",\n    \"name\": \"B nitrogen purity and measured final volume\",\n    \"\
    stage\": \"B handling and completed medium\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_AA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"B_gas\": \"N2\",\n      \"B_purity_percent\"\
    : null,\n      \"measured_final_volume\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm579_network_retry\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\",\n        \"source_locator\"\
    : \"B preparation\",\n        \"exact_source_quote\": \"Autoclave under a N 2\
    \ atmosphere.\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      },\n      {\n        \"source_key\": \"jcm579_network_retry\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=579\"\
    ,\n        \"source_locator\": \"Completion basis\",\n        \"exact_source_quote\"\
    : \"To complete medium, aseptically add the following solutions to the medium\
    \ (per 10 ml):\",\n        \"snapshot_sha256\": \"9a2bbe546766415ee310bbafc19f0300d7daa611997e9f57d0c3d68ed3ee69ae\"\
    ,\n        \"parsed_text_sha256\": \"f0b5943566490d8f735149540bcaeb3c1e7be7a6d722aa0eb316de2cf88124e6\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not infer 100% nitrogen, a measured\
    \ final volume, or a final pH from a stock aliquot and additive volume arithmetic.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '10 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 11/13
    primary and 7/13 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi26710
  - chebi31206
  - chebi32588
  - chebi3312
  - chebi63036
  - chebi86345
  details: 'Instance coverage on a 0–100 percent scale, denominator 13: primary 84.62%;
    secondary 53.85%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Receiving recipe and exact stock boundaries
  outcome: concern
  summary: TOGO M584 resolves to JCM 579. Its A/B references are internal recipe stages;
    local links 5342/5343 resolve to incompatible high-salt recipes. The trace dependency
    transfers only JCM 151 trace minerals.
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - main
  - provider
  - wrong-a
  - wrong-b
  - trace
  - trace-owner
- assessment_id: forms
  area: grounding
  topic: Receiving and transferred supplied forms
  outcome: concern
  summary: Receiving B explicitly uses unhydrated CaCl2 and MgCl2 hexahydrate; the
    distinct trace stock uses calcium chloride dihydrate. Those distinctions are supported.
    The transferred MnSO4·xH2O leaves hydration unspecified while its maintained ID
    encodes anhydrous MnSO4; preserve the source qualification without inventing x.
    Other in-scope supplied forms and labels were checked.
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - main
  - trace
  - trace-grounding
- assessment_id: preparation
  area: completeness
  topic: Separate preparation, gas and pH stages
  outcome: concern
  summary: A pH 7.2, A nitrogen/carbon dioxide 4:1 v/v, filtered completion stocks,
    B nitrogen handling and the collection sterilization default are missing. Trace
    pH 6.5 then 7 belongs only to that stock.
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - main
  - trace
  - quantity-inventory
- assessment_id: growth
  area: scope
  topic: Classification and growth evidence
  outcome: supported
  summary: Yeast extract supports an undefined complex formulation. The medium name
    and bacterial provenance do not establish strain growth, temperature or incubation
    duration; no such assertion is added.
  target_ids:
  - CultureMech:009980
  evidence_ids:
  - record
  - owner-0
  - main
findings:
- finding_id: f1
  issue_key: culturemech.009980.wrong-stock-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: A and B point to unrelated high-salt stocks
  description: Both local layers link A and B to 5342/5343 despite incompatible source
    formulations. Exact identity resolution does not establish recipe equivalence.
  target_ids:
  - CultureMech:009980
  field_paths:
  - solutions[1].term
  - solutions[2].term
  evidence_ids:
  - main
  - wrong-a
  - wrong-b
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  issue_key: culturemech.009980.collapsed-preparation-quantities
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid doses, water and stock masses lose their stages
  description: Both layers store the completion liquid doses and A aliquot as G_PER_L,
    merge 1 L A water with 10 mL B water as 11 G_PER_L, and flatten B salts and A
    masses. The receiving basis is explicitly per 10 mL A.
  target_ids:
  - CultureMech:009980
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - main
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  issue_key: culturemech.009980.unrepresented-trace-stock
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Named trace recipe and handling remain unresolved in the receiving record
  description: The receiving trace entry has empty composition and no exact maintained
    stock reference. Its thirteen available historical amount claims belong to the
    M142 trace stock only. Parent basal, sulfur and variant material must remain excluded.
  target_ids:
  - CultureMech:009980
  field_paths:
  - solutions[3]
  evidence_ids:
  - trace
  - trace-owner
  - trace-history
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  issue_key: culturemech.009980.trace-hydration-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Transferred manganese sulfate hydration is not represented
  description: JCM 151 and TOGO M142 print MnSO4·xH2O while the transferred maintained
    term has an anhydrous MnSO4 structure. The exact hydration number is unresolved;
    no replacement hydrate is inferred.
  target_ids:
  - CultureMech:009980
  field_paths:
  - solutions[3]
  evidence_ids:
  - trace
  - trace-grounding
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  issue_key: culturemech.009980.missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH, atmosphere and sterilization stages are absent
  description: Both receiving layers lack the explicit A pH, A gas ratio, separately
    autoclaved B and filtered completion-stock procedure. An unqualified B nitrogen
    atmosphere does not supply a numerical purity.
  target_ids:
  - CultureMech:009980
  field_paths:
  - preparation_steps
  - ph_value
  - solutions
  evidence_ids:
  - main
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  description: Resolve the specific JCM 579 A/B stages in maintained inputs and remove
    incompatible references; do not modify the unrelated stock records to fit this
    medium.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009980
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  description: Restore original units and separate A, B and completion stock scopes
    without assuming a measured final volume or bicarbonate percentage basis.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009980
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  description: Represent the named trace recipe through a verified scoped reference
    or composition; retain its own quantities, pH steps and evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009980
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  description: Preserve the unspecified hydrate qualification in the maintained stock
    and resolve its chemical correspondence independently of the amount evidence.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009980
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
  description: Add the exact scoped procedure and collection default with evidence,
    preserving example tube fill and unresolved percent/final-volume quantities.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009980
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M584_Bacillus_AA_Medium.yaml
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
- No target or maintained receiving amount is verified by attached evidence. The thirteen
  verified decisions refer exclusively to existing M142 trace-stock notes or water
  volume.
- Parent sulfur legacy MediaIngredientMech:001072 and all unrelated parent formulations/variants
  are outside this review transfer; they are not a required missing correspondence
  for JCM 579.
- Current exact primaries resolve the scientific recipe; unavailable redundant APIs
  are not treated as evidence of recipe absence or historical byte equivalence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-038
- generated-medium
```
