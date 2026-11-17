# Source and formulation review: artificial_seawater_medium_for_strain_js_srb250lac (CultureMech:008354)

- Review: 20261021T202425Z-culturemech-008354-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:11:19Z
- Finished UTC: 2026-10-21T20:24:25Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC 1005 and exact TOGO M1787 agree on a staged basal medium plus four separate stocks. Both local layers flatten stock recipes and misstate water, milligram amounts and liquid doses. The linked SL-10 has 70 mg zinc rather than the source 7 mg, and the linked vitamin stock has three species rather than ten. Existing external-stock evidence is valid only within those stock records. Hydrate and calcium-pantothenate grounding errors and a completed current MIM lookup gap are separate findings.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 365; batch 037 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-six task batches contain 360 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 363 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008354 | data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml | generated | artificial_seawater_medium_for_strain_js_srb250lac |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008354 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008354 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/365/strict.tsv |
| validate-terms | passed | True | CultureMech:008354 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008354 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008354 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008354.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008354.

86 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Distilled water",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "L",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 18:  &#124; Distilled water &#124; 1 &#124; L",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q2",
    "name": "NaCl",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "26",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "26",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 26,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 5:  &#124; NaCl &#124; 26 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;NaCl&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;26&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;NaCl&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;26&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 26,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q3",
    "name": "CaCl2·2H2O",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1.4,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 8:  &#124; CaCl 2 ·2H 2 O &#124; 1.4 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1.4&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1.4&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 1.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q4",
    "name": "KH2PO4",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.2,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 3: KH 2 PO 4 0.2 g &#124;  &#124; KH 2 PO 4 &#124; 0.2 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n                            &lt;td colspan=\"2\" id=\"medium-comp\"&gt;&lt;table border=\"0\" width=\"600\"&gt;\n&lt;tbody&gt;\n&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.2&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\n                            &lt;td colspan=\"2\" id=\"medium-comp\"&gt;&lt;table border=\"0\" width=\"600\"&gt;\r\n&lt;tbody&gt;\r\n&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.2&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q5",
    "name": "NH4Cl",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.25,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 4:  &#124; NH 4 Cl &#124; 0.25 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;NH&lt;sub&gt;4&lt;/sub&gt;Cl&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.25&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;NH&lt;sub&gt;4&lt;/sub&gt;Cl&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.25&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q6",
    "name": "Resazurin",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.5,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 13:  &#124; Resazurin &#124; 0.5 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Resazurin&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Resazurin&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator. The source explicitly prints 0.5 g resazurin; no familiar milligram amount is substituted."
  },
  {
    "decision_id": "q7",
    "name": "MgCl2·6H2O",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "11.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "11.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 11.2,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 6:  &#124; MgCl 2 ·6H 2 O &#124; 11.2 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;11.2&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;11.2&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"MgCl2·6H2O\",\n          \"volume\": 11.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q8",
    "name": "KCl",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.7",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.7",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.7,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 7:  &#124; KCl &#124; 0.7 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;KCl&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.7&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;KCl&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.7&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.7,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q9",
    "name": "NaHCO3",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 2.5,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 11:  &#124; NaHCO 3 &#124; 2.5 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;NaHCO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;2.5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;NaHCO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;2.5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 2.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q10",
    "name": "Na2SO4",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 4,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 9:  &#124; Na 2 SO 4 &#124; 4 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;4&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;4&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2SO4\",\n          \"volume\": 4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q11",
    "name": "Sodium lactate",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 2.3,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 12:  &#124; Sodium lactate &#124; 2.3 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Sodium lactate&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;2.3&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Sodium lactate&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;2.3&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Sodium lactate\",\n          \"volume\": 2.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q12",
    "name": "KBr",
    "stage": "NBRC main batch before selective post-cooling additions",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.1,
      "unit": "g",
      "basis": "Source-listed main batch; 1 L water plus stock doses, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 10:  &#124; KBr &#124; 0.1 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;KBr&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;KBr&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"KBr\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve the printed amount and stage. Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams do not by themselves establish a final-medium g/L denominator."
  },
  {
    "decision_id": "q13",
    "name": "Carbon dioxide gas",
    "stage": "Main gas ingredient entry",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dissolved_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[16]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Variable gas entries supply no dissolved concentration. The main atmosphere ratio is an independent preparation decision."
  },
  {
    "decision_id": "q14",
    "name": "Nitrogen gas",
    "stage": "Main gas ingredient entry",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dissolved_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[17]",
        "exact_source_quote": "\"component_name\": \"Nitrogen gas\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Variable gas entries supply no dissolved concentration. The main atmosphere ratio is an independent preparation decision."
  },
  {
    "decision_id": "q15",
    "name": "Trace element solution SL-10*",
    "stage": "Main receiving stock dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "ml",
      "basis": "Dose into the listed main preparation"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 14:  &#124; Trace element solution SL-10* &#124; 1 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Trace element solution SL-10*&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Trace element solution SL-10*&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Trace element solution SL-10*\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "The receiving dose is liquid milliliters, not G_PER_L. Keep the exact stock identity and batch recipe distinct from this dose."
  },
  {
    "decision_id": "q16",
    "name": "Selenite-tungstate solution**",
    "stage": "Main receiving stock dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "ml",
      "basis": "Dose into the listed main preparation"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 15:  &#124; Selenite-tungstate solution** &#124; 1 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Selenite-tungstate solution**&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Selenite-tungstate solution**&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"Selenite-tungstate solution**\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "The receiving dose is liquid milliliters, not G_PER_L. Keep the exact stock identity and batch recipe distinct from this dose."
  },
  {
    "decision_id": "q17",
    "name": "Vitamin solution***",
    "stage": "Main receiving stock dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "ml",
      "basis": "Dose into the listed main preparation"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 16:  &#124; Vitamin solution*** &#124; 1 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Vitamin solution***&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Vitamin solution***&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"Vitamin solution***\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "The receiving dose is liquid milliliters, not G_PER_L. Keep the exact stock identity and batch recipe distinct from this dose."
  },
  {
    "decision_id": "q18",
    "name": "Sulfide solution****",
    "stage": "Main receiving stock dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "ml",
      "basis": "Dose into the listed main preparation"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 17:  &#124; Sulfide solution**** &#124; 10 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Sulfide solution****&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Sulfide solution****&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[0].items[15]",
        "exact_source_quote": "\"component_name\": \"Sulfide solution****\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "The receiving dose is liquid milliliters, not G_PER_L. Keep the exact stock identity and batch recipe distinct from this dose."
  },
  {
    "decision_id": "q19",
    "name": "Distilled water",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 990,
      "unit": "ml",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 32:  &#124;  &#124;  &#124; Distilled water &#124; 990 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;990&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;990&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q20",
    "name": "Na2MoO4·2H2O",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 36,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 31:  &#124;  &#124;  &#124; Na 2 MoO 4 ·2H 2 O &#124; 36 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;36&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;36&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4·2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q21",
    "name": "H3BO3",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 6,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 27:  &#124;  &#124;  &#124; H 3 BO 3 &#124; 6 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;6&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;6&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q22",
    "name": "MnCl2·4H2O",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 100,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 26:  &#124;  &#124;  &#124; MnCl 2 ·4H 2 O &#124; 100 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;4H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;100&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;4H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;100&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2·4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q23",
    "name": "CoCl2·6H2O",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 190,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 28:  &#124;  &#124;  &#124; CoCl 2 ·6H 2 O &#124; 190 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;190&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;190&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q24",
    "name": "NiCl2·6H2O",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 24,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 30:  &#124;  &#124;  &#124; NiCl 2 ·6H 2 O &#124; 24 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;24&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;24&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2·6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q25",
    "name": "CuCl2·2H2O",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 2,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 29:  &#124;  &#124;  &#124; CuCl 2 ·2H 2 O &#124; 2 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2·2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q26",
    "name": "ZnCl2",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 7,
      "unit": "mg",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 25:  &#124;  &#124;  &#124; ZnCl 2 &#124; 7 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;ZnCl&lt;sub&gt;2&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;7&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;ZnCl&lt;sub&gt;2&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;7&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 7,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q27",
    "name": "HCl (25%; 7.7 M)",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "ml",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 23:  &#124;  &#124;  &#124; HCl (25%; 7.7 M) &#124; 10 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;HCl (25%; 7.7 M)&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;HCl (25%; 7.7 M)&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q28",
    "name": "FeCl2·4H2O",
    "stage": "SL-10 stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1.5,
      "unit": "g",
      "proposed_scope": "solutions[0].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 24:  &#124;  &#124;  &#124; FeCl 2 ·4H 2 O &#124; 1.5 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;4H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1.5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;4H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1.5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"FeCl2·4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q29",
    "name": "distilled water",
    "stage": "Selenite-tungstate stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "L",
      "proposed_scope": "solutions[1].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 38:  &#124;  &#124;  &#124; distilled water &#124; 1 &#124; L",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q30",
    "name": "Na2SeO3·5H2O",
    "stage": "Selenite-tungstate stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 3,
      "unit": "mg",
      "proposed_scope": "solutions[1].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 36:  &#124;  &#124;  &#124; Na 2 SeO 3 ·5H 2 O &#124; 3 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;3&lt;/sub&gt;&amp;middot;5H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;3&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;3&lt;/sub&gt;&amp;middot;5H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;3&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2SeO3·5H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q31",
    "name": "Na2WO4·2H2O",
    "stage": "Selenite-tungstate stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 4,
      "unit": "mg",
      "proposed_scope": "solutions[1].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 37:  &#124;  &#124;  &#124; Na 2 WO 4 ·2H 2 O &#124; 4 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;4&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;4&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2WO4·2H2O\",\n          \"volume\": 4,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q32",
    "name": "NaOH",
    "stage": "Selenite-tungstate stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.5,
      "unit": "g",
      "proposed_scope": "solutions[1].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 35:  &#124;  &#124;  &#124; NaOH &#124; 0.5 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;NaOH&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;NaOH&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q33",
    "name": "Distilled water",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1,
      "unit": "L",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 53:  &#124;  &#124;  &#124; Distilled water &#124; 1 &#124; L",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q34",
    "name": "Biotin",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 2,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 43:  &#124;  &#124;  &#124; Biotin &#124; 2 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Biotin&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Biotin&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q35",
    "name": "p-Aminobenzoic acid",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 5,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 51:  &#124;  &#124;  &#124; p -Aminobenzoic acid &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;&lt;em&gt;p&lt;/em&gt;-Aminobenzoic acid&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;&lt;em&gt;p&lt;/em&gt;-Aminobenzoic acid&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q36",
    "name": "Thiamine-HCl",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 5,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 46:  &#124;  &#124;  &#124; Thiamine-HCl &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Thiamine-HCl&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Thiamine-HCl&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q37",
    "name": "Ca-pantothenate",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 5,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 49:  &#124;  &#124;  &#124; Ca-pantothenate &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Ca-pantothenate&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Ca-pantothenate&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q38",
    "name": "Pyridoxine-HCl",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 10,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 45:  &#124;  &#124;  &#124; Pyridoxine-HCl &#124; 10 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Pyridoxine-HCl&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Pyridoxine-HCl&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q39",
    "name": "Folic acid",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 2,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 44:  &#124;  &#124;  &#124; Folic acid &#124; 2 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Folic acid&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Folic acid&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q40",
    "name": "Vitamin B12",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 0.1,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 50:  &#124;  &#124;  &#124; Vitamin B 12 &#124; 0.1 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Vitamin B&lt;sub&gt;12&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;0.1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Vitamin B&lt;sub&gt;12&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;0.1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q41",
    "name": "Riboflavin",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 5,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 47:  &#124;  &#124;  &#124; Riboflavin &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Riboflavin&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Riboflavin&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q42",
    "name": "Nicotinic acid",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[34].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[34].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 5,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 48:  &#124;  &#124;  &#124; Nicotinic acid &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Nicotinic acid&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Nicotinic acid&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q43",
    "name": "Lipoic acid",
    "stage": "Ten-vitamin stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[35].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[35].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 5,
      "unit": "mg",
      "proposed_scope": "solutions[2].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 52:  &#124;  &#124;  &#124; Lipoic acid &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Lipoic acid&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Lipoic acid&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[3].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q44",
    "name": "Distilled water",
    "stage": "Neutralized sulfide stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1093.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 100,
      "unit": "ml",
      "proposed_scope": "solutions[3].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 57:  &#124;  &#124;  &#124; Distilled water &#124; 100 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;100&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;100&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q45",
    "name": "Na2S·9H2O",
    "stage": "Neutralized sulfide stock batch",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[36].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[36].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 1.5,
      "unit": "g",
      "proposed_scope": "solutions[3].composition",
      "basis": "Separate stock input"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 56:  &#124;  &#124;  &#124; Na 2 S·9H 2 O &#124; 1.5 &#124; g",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1.5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1.5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;g&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2S·9H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Move this amount into its exact named stock recipe. Milligrams are not grams per liter of the receiving medium. Five separate water entries were combined in the local field; neither their mixed-unit numeric sum nor full stock batches belong in main-medium water."
  },
  {
    "decision_id": "q46",
    "name": "Sulfuric acid dose",
    "stage": "Neutralized sulfide stock titration",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[37].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[37].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "dose": null,
      "endpoint": "about pH 7.3"
    },
    "source_snippets": [
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[4].items[2]",
        "exact_source_quote": "\"component_name\": \"H2SO4\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "The source gives dropwise titration and acid strength, not a fixed acid dose. Preserve the variable-dose status within the sulfide stock rather than the main recipe."
  },
  {
    "decision_id": "q47",
    "name": "Nitrogen gas",
    "stage": "Neutralized sulfide stock atmosphere",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[38].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[38].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "gas": "N2",
      "purity_percent": null
    },
    "source_snippets": [
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[4].items[3]",
        "exact_source_quote": "\"component_name\": \"N2\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "The stock specifies N2 without purity or dissolved concentration. It is distinct from the main N2/CO2 mixture."
  },
  {
    "decision_id": "q48",
    "name": "HCl strength",
    "stage": "SL-10 acid component",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[21].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[21].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      }
    ],
    "desired": {
      "value": 25,
      "unit": "PERCENT",
      "basis": "not specified"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 23:  &#124;  &#124;  &#124; HCl (25%; 7.7 M) &#124; 10 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;HCl (25%; 7.7 M)&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;HCl (25%; 7.7 M)&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "The printed percentage has no w/v, v/v or w/w qualifier. Do not infer density from the adjacent molarity."
  },
  {
    "decision_id": "q49",
    "name": "HCl molarity",
    "stage": "SL-10 acid component",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ingredients[21].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ingredients[21].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      }
    ],
    "desired": {
      "value": 7.7,
      "unit": "MOLAR"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 23:  &#124;  &#124;  &#124; HCl (25%; 7.7 M) &#124; 10 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;HCl (25%; 7.7 M)&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;HCl (25%; 7.7 M)&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      }
    ],
    "interpretation": "Preserve source-stated molarity separately from the 10 mL dose and 25% label."
  },
  {
    "decision_id": "q50",
    "name": "Final main pH",
    "stage": "Main preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "ph_range",
        "stored": null
      }
    ],
    "desired": {
      "minimum": 7.2,
      "maximum": 7.4
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 20:  &#124;  &#124; Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20) gas mixture in culture vessels.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "This is explicitly the final main-medium pH, not a stock pH."
  },
  {
    "decision_id": "q51",
    "name": "N2/CO2 mixture",
    "stage": "Main dispensing",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "ratio": "80/20",
      "species": [
        "N2",
        "CO2"
      ],
      "basis": "not printed"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 20:  &#124;  &#124; Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20) gas mixture in culture vessels.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "The source prints 80/20 without v/v. No ratio is transferred to separately prepared sulfide stock."
  },
  {
    "decision_id": "q52",
    "name": "Autoclave temperature",
    "stage": "Neutralized sulfide stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 121,
      "unit": "DEG_C",
      "scope": "Sulfide stock only; not a default for the main medium or Se/W stock."
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Sulfide stock only; not a default for the main medium or Se/W stock."
  },
  {
    "decision_id": "q53",
    "name": "Autoclave duration",
    "stage": "Neutralized sulfide stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 15,
      "unit": "MIN",
      "scope": "Sulfide stock only; no main-medium cycle is specified."
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Sulfide stock only; no main-medium cycle is specified."
  },
  {
    "decision_id": "q54",
    "name": "Sulfide pH endpoint",
    "stage": "Neutralized sulfide stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 7.3,
      "unit": "PH",
      "scope": "Approximate endpoint; not identical to the separately described yellow-color pH."
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Approximate endpoint; not identical to the separately described yellow-color pH."
  },
  {
    "decision_id": "q55",
    "name": "Acid titrant strength",
    "stage": "Neutralized sulfide stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 2,
      "unit": "NORMAL",
      "scope": "Strength only; dropwise dose is unquantified."
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Strength only; dropwise dose is unquantified."
  },
  {
    "decision_id": "q56",
    "name": "Yellow-color observation pH",
    "stage": "Neutralized sulfide stock preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "value": 8,
      "unit": "PH",
      "scope": "Approximate color observation; preserve the source’s separate pH 7.3 and transparent-yellow wording."
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Approximate color observation; preserve the source’s separate pH 7.3 and transparent-yellow wording."
  },
  {
    "decision_id": "q57",
    "name": "Main and Se/W autoclave cycles",
    "stage": "Separate sterilization stages",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "main_temperature": null,
      "main_duration": null,
      "SeW_temperature": null,
      "SeW_duration": null
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 20:  &#124;  &#124; Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20) gas mixture in culture vessels.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 40:  &#124;  &#124; Sterilized by autoclaving.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;Sterilized by autoclaving.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;Sterilized by autoclaving.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "The main and Se/W instructions name autoclaving without numerical cycles. The sulfide-specific 121°C/15 min must not be silently inherited."
  },
  {
    "decision_id": "q58",
    "name": "Sterile stock strengths for delayed basal additions",
    "stage": "After cooling under nitrogen",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "phosphate_stock_strength": null,
      "ammonium_stock_strength": null,
      "bicarbonate_stock_strength": null,
      "lactate_stock_strength": null
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 20:  &#124;  &#124; Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20) gas mixture in culture vessels.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;Dissolve ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust the final pH of the medium to 7.2-7.4. Dispense the medium under N&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) gas mixture in culture vessels.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "The primary instructs sterile stocks for phosphate, ammonium, bicarbonate and lactate but gives no concentrations or solvent doses for those additional stocks."
  },
  {
    "decision_id": "q59",
    "name": "Room-temperature cooling",
    "stage": "Sulfide neutralization",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "temperature": null
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 59:  &#124;  &#124; The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"5\" width=\"90%\"&gt;The sulfide solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. After cooling to room temperature, the pH is adjusted to about 7.3 by adding of sterile 2 N H&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt; drop-wise with a syringe without opening the bottle. Appearance of yellow colour indicates the pH is about 8. The vessel should be shaken continuously to avoid precipitation of elemental sulfur. The final solution should be transparent yellow.&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Room temperature is not converted to an invented numerical temperature."
  },
  {
    "decision_id": "q60",
    "name": "Independent final volume",
    "stage": "Main and stock assembly",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "measured_final_medium_volume": null
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 18:  &#124; Distilled water &#124; 1 &#124; L",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 14:  &#124; Trace element solution SL-10* &#124; 1 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Trace element solution SL-10*&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Trace element solution SL-10*&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 15:  &#124; Selenite-tungstate solution** &#124; 1 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Selenite-tungstate solution**&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Selenite-tungstate solution**&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 16:  &#124; Vitamin solution*** &#124; 1 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Vitamin solution***&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Vitamin solution***&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 17:  &#124; Sulfide solution**** &#124; 10 &#124; ml",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Sulfide solution****&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"4\" align=\"left\" width=\"60%\"&gt;Sulfide solution****&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;10&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;ml&lt;/td&gt;\r\n&lt;/tr&gt;"
      }
    ],
    "interpretation": "Main 1 L water and 1/1/1/10 mL doses do not state an independently measured final volume; whole-stock preparation waters are not receiving-medium additions."
  },
  {
    "decision_id": "q61",
    "name": "HCl",
    "stage": "External MediaDive 4178 stock only",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_dose": 10,
      "dose_unit": "ml",
      "attribute": "25%, 7.7 M",
      "provider_g_l": 2.5
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "The API supplies both a 10 mL stock-acid dose and g_l=2.5. Preserve the conflicting concentration interpretation without deriving mass from an unqualified percentage or treating g_l as the literal dose."
  },
  {
    "decision_id": "q62",
    "name": "FeCl2 x 4 H2O",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q63",
    "name": "ZnCl2",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q64",
    "name": "MnCl2 x 4 H2O",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q65",
    "name": "H3BO3",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q66",
    "name": "CoCl2 x 6 H2O",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.19",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q67",
    "name": "CuCl2 x 2 H2O",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q68",
    "name": "NiCl2 x 6 H2O",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.024",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q69",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "External MediaDive 4178 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[8].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.036",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q70",
    "name": "Distilled water",
    "stage": "External MediaDive 4178 stock only",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[9].concentration",
        "stored": {
          "value": "990",
          "unit": "PERCENT_V_V"
        }
      }
    ],
    "desired": {
      "value": 990,
      "unit": "ML"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[9]",
        "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "Provider water is a 990 mL batch input, not 990% v/v. Its 1000 mL declared solution volume is separate."
  },
  {
    "decision_id": "q71",
    "name": "Provider-declared stock volume",
    "stage": "External MediaDive 4178 metadata",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "preparation_notes",
        "stored": "Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."
      }
    ],
    "desired": {
      "value": 1000,
      "unit": "ML",
      "basis": "Provider declaration"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "This declaration belongs to the external stock and must not be treated as a measured receiving-medium volume or automatic proof of NBRC stock equivalence."
  },
  {
    "decision_id": "q72",
    "name": "Placeholder ingredient",
    "stage": "External MediaDive 4178 generated placeholder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "interpretation": "Not an additional reagent; use the actual composition array"
    },
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "The placeholder See source for composition is provenance/structure debt, not a quantified ingredient to transfer into the medium."
  },
  {
    "decision_id": "q73",
    "name": "NaOH",
    "stage": "External MediaDive 5543 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q74",
    "name": "Na2SeO3 x 5 H2O",
    "stage": "External MediaDive 5543 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.003",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q75",
    "name": "Na2WO4 x 2 H2O",
    "stage": "External MediaDive 5543 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.004",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q76",
    "name": "Distilled water",
    "stage": "External MediaDive 5543 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "L"
    },
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q77",
    "name": "Provider-declared stock volume",
    "stage": "External MediaDive 5543 metadata",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "preparation_notes",
        "stored": null
      }
    ],
    "desired": {
      "value": 1000,
      "unit": "ML",
      "basis": "Provider declaration"
    },
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "interpretation": "This declaration belongs to the external stock and must not be treated as a measured receiving-medium volume or automatic proof of NBRC stock equivalence."
  },
  {
    "decision_id": "q78",
    "name": "Placeholder ingredient",
    "stage": "External MediaDive 5543 generated placeholder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "interpretation": "Not an additional reagent; use the actual composition array"
    },
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "interpretation": "The placeholder See source for composition is provenance/structure debt, not a quantified ingredient to transfer into the medium."
  },
  {
    "decision_id": "q79",
    "name": "Cyanocobalamine",
    "stage": "External MediaDive 6241 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q80",
    "name": "Thiamine HCl",
    "stage": "External MediaDive 6241 stock only",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "Attached exact source-hash evidence decodes to the same provider recipe object. Verification covers the current external stock amount/basis only; source correspondence to NBRC 1005 is separate."
  },
  {
    "decision_id": "q81",
    "name": "Biotin",
    "stage": "External MediaDive 6241 stock only",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "2000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": 200,
      "unit": "MICROGRAM",
      "basis": "External 100 mL stock"
    },
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The exact external stock prints 200 micrograms, not 2000 G_PER_L. This external three-vitamin stock still is not the NBRC ten-vitamin mixture."
  },
  {
    "decision_id": "q82",
    "name": "Distilled water",
    "stage": "External MediaDive 6241 stock only",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "PERCENT_V_V"
        }
      }
    ],
    "desired": {
      "make_up_to": 100,
      "unit": "ML"
    },
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      },
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.steps[0].step",
        "exact_source_quote": "Make up to 100 ml with distilled water.",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The provider explicitly says make up to 100 mL. Its water field and 100 mL declared volume do not support 1000% v/v."
  },
  {
    "decision_id": "q83",
    "name": "Provider-declared stock volume",
    "stage": "External MediaDive 6241 metadata",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "preparation_notes",
        "stored": "Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"
      }
    ],
    "desired": {
      "value": 100,
      "unit": "ML",
      "basis": "Provider declaration"
    },
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.volume",
        "exact_source_quote": "\"volume\": 100",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "This declaration belongs to the external stock and must not be treated as a measured receiving-medium volume or automatic proof of NBRC stock equivalence."
  },
  {
    "decision_id": "q84",
    "name": "Placeholder ingredient",
    "stage": "External MediaDive 6241 generated placeholder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "desired": {
      "interpretation": "Not an additional reagent; use the actual composition array"
    },
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The placeholder See source for composition is provenance/structure debt, not a quantified ingredient to transfer into the medium."
  },
  {
    "decision_id": "q85",
    "name": "SL-10 zinc identity comparison",
    "stage": "NBRC stock versus linked 4178",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "solutions[0].term",
        "stored": {
          "id": "mediadive.solution:4178",
          "label": "Trace element solution SL-10"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "solutions[0].term",
        "stored": {
          "id": "mediadive.solution:4178",
          "label": "Trace element solution SL-10"
        }
      }
    ],
    "desired": {
      "NBRC_ZnCl2": {
        "value": 7,
        "unit": "MG"
      },
      "linked_4178_ZnCl2": {
        "value": 70,
        "unit": "MG"
      }
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 25:  &#124;  &#124;  &#124; ZnCl 2 &#124; 7 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;ZnCl&lt;sub&gt;2&lt;/sub&gt;&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;7&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;ZnCl&lt;sub&gt;2&lt;/sub&gt;&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;7&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "togoM1787original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 7,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f"
      },
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "interpretation": "The tenfold zinc difference is explicit. Similar names and matching other rows do not authenticate this linkage."
  },
  {
    "decision_id": "q86",
    "name": "Vitamin mixture identity comparison",
    "stage": "NBRC stock versus linked 6241",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml",
        "field_path": "solutions[2].term",
        "stored": {
          "id": "mediadive.solution:6241",
          "label": "Vitamin solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
        "field_path": "solutions[2].term",
        "stored": {
          "id": "mediadive.solution:6241",
          "label": "Vitamin solution"
        }
      }
    ],
    "desired": {
      "NBRC": "Ten vitamin species in 1 L stock water",
      "linked_6241": "Three vitamin species, make up to 100 mL"
    },
    "source_snippets": [
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 43:  &#124;  &#124;  &#124; Biotin &#124; 2 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Biotin&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Biotin&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;2&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 49:  &#124;  &#124;  &#124; Ca-pantothenate &#124; 5 &#124; mg",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Ca-pantothenate&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Ca-pantothenate&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;5&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;mg&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "nbrc1005",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005",
        "source_locator": "NBRC 1005 HTML row 53:  &#124;  &#124;  &#124; Distilled water &#124; 1 &#124; L",
        "exact_source_quote": "&lt;tr&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\n&lt;/tr&gt;",
        "snapshot_sha256": "fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4",
        "quotation_normalization": "Raw HTML CRLF line breaks normalized to LF; original byte-literal row separately preserved.",
        "raw_bytes_quote": "&lt;tr&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td width=\"5%\"&gt;&amp;nbsp;&lt;/td&gt;\r\n&lt;td colspan=\"2\" align=\"left\" width=\"50%\"&gt;Distilled water&lt;/td&gt;\r\n&lt;td align=\"right\" width=\"20%\"&gt;1&lt;/td&gt;\r\n&lt;td align=\"left\" width=\"15%\"&gt;L&lt;/td&gt;\r\n&lt;/tr&gt;"
      },
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      },
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      },
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The source does not support replacing its ten-vitamin mixture with this three-vitamin formulation; do not transfer external stock evidence to the medium."
  }
]

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008354.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact medium and stock correspondence

identity: concern. Targets: CultureMech:008354.

The medium is exactly NBRC 1005/TOGO M1787 with one maintained owner. Solutions 4178 and 6241 resolve as records but their formulas differ from the named source stocks. Solution 5543 agrees with the four Se/W rows; that correspondence does not repair dose units or attach evidence to the medium.

### Chemical structures versus labels and current secondary keys

grounding: concern. Targets: CultureMech:008354.

160 asserted CHEBI slots were inspected across medium and stock layers. Canonical labels agree with nonobsolete OLS records. Cobalt/nickel hydrate and calcium-pantothenate counterion/stereo problems remain; CHEBI29032 has no current MIM index row. The negative lookup is complete, so it does not itself make this review partial.

### Selective sterilization and stock procedures

completeness: concern. Targets: CultureMech:008354.

Main preparation, delayed sterile additions, main pH 7.2–7.4 and dispensing gas ratio are absent. The sulfide stock alone specifies 121°C/15 min, approximate pH 7.3, 2 N sulfuric acid and the distinct yellow-color pH 8 observation. Preserve unknown gas/percent bases, doses and other sterilization cycles.

### High-metal, complexity and growth scope

scope: concern. Targets: CultureMech:008354.

The source names the medium for JS_SRB250Lac but supplies no taxonomic accession or independent growth result to add. COMPLEX/UNDEFINED and high_metal are local classifications, not primary claims. Current metal code aggregates flat ingredient values and uses a corpus percentile; the mis-scoped and misunit quantities prevent accepting the flag as a scientifically verified concentration classification. No population threshold was recomputed.

### Historical external claims and current writer boundaries

provenance: supported. Targets: CultureMech:008354.

The fourteen attached amount claims authenticate only their exact external stocks. Current source bytes match the cited hashes, and decoded recipe snippets match despite indentation normalization. Medium history records prior processing but does not prove current scientific correctness or a particular historical matching mechanism.

## Findings

### f1: Two resolved stock links select different formulations

blocker / open / confirmed; issue key: culturemech.008354.wrong-stock-correspondence.

Both layers link their NBRC SL-10 to solution 4178 despite 7 versus 70 mg zinc, and their ten-vitamin stock to three-vitamin solution 6241. These are observed formula mismatches, not assertions about the historical matching algorithm. Existing external evidence cannot validate the links.

### f2: Main and stock quantities lose units and stage boundaries

major / open / confirmed; issue key: culturemech.008354.flattened-stock-quantities.

Five distinct water inputs are collapsed to 1093 G_PER_L; stock milligrams and liquid milliliter doses are stored as G_PER_L alongside basal ingredients. Source resazurin 0.5 g is literal and is not an identified thousandfold error. The complete per-stage inventory supplies exact values without assuming measured final volume.

### f3: Supplied hydrates and calcium pantothenate are misgrounded

major / open / confirmed; issue key: culturemech.008354.hydrate-pantothenate-forms.

CoCl2·6H2O and NiCl2·6H2O are represented by anhydrous structures. Calcium pantothenate is assigned an R-pantothenate anion that omits calcium and asserts stereochemistry absent from the source. These form problems are separate from the current MIM lookup gap.

### f4: Asserted pantothenate secondary key is absent from the current index

major / open / confirmed; issue key: culturemech.008354.current-secondary-gap.

Exact inspection of the pinned complete MIM index found no CHEBI29032 rows. Its primary OLS term exists; that does not establish asserted secondary membership. No unavailable check or historical correspondence is inferred from this completed negative lookup.

### f5: Required anaerobic and stock preparation is absent

major / open / confirmed; issue key: culturemech.008354.missing-preparation.

The records lack the main selective-sterilization sequence and the distinct neutralized-sulfide procedure. Main pH, gas handling and stock-specific cycle/acid conditions must retain their separate scopes and literal ambiguities.

### f6: High-metal classification depends on unreconciled quantities

minor / open / confirmed; issue key: culturemech.008354.unverified-classification.

Both records assert high_metal despite flattened stock quantities and unit errors. The current writer is a corpus-relative numerical classifier, not source evidence; its existence does not prove historical execution or justify a true/false replacement without a corrected analysis.

## Recommended Actions And Acceptance Checks

### a1

Replace or qualify the incompatible links using exact NBRC stock identities; preserve 5543 correspondence separately and retain external stock evidence only in its original layer.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore the basal recipe, four stock recipes and receiving doses with source units/bases, retain the literal resazurin amount and attach exact per-layer evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Correct confirmed hydrate/counterion mismatches with verified source-specific identifiers; preserve unresolved pantothenate stereochemistry without inventing a racemate or replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve or remove the unsupported current secondary assertion through the maintained mapping workflow; do not create a guessed historical MIM identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Add exact source-scoped preparation and evidence; retain unknown cycles, percentage bases, titration doses and the separate pH/color statements.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Reassess classification after quantity and stock corrections, preserving the method and comparison population; keep strain naming separate from demonstrated growth.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch037/365/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/365/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml:1:id: CultureMech:008354<br>./data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml:1:id: CultureMech:008354<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch037/source-preflight-bound/365/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 47 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005; Exact Medium No.1005, full main table and four named stock sections | supports | Primary source identifies this medium and supplies amounts, stages and preparation. Resazurin is explicitly 0.5 g; no presumed mg correction is made. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787; $.meta; five components and scoped comments | supports | Exact provider corroborates primary quantities and stages; its text does not turn stock amounts into final concentrations. |
| procedure | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005; Main preparation paragraph and neutralized sulfide instructions | supports | Basal sterilization excludes six named additions; final main pH is 7.2–7.4, separate from sulfide-stock pH. |
| stock-4178 | data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml; Complete local stock composition, preparation, evidence, history and placeholder fields | context_only | Asserted stock identity was checked against its exact public endpoint; no evidence or amount is inherited by the medium merely through a link. |
| api-4178 | https://mediadive.dsmz.de/rest/solution/4178; $.data.id/name/volume/recipe/steps | supports | Exact external stock formula and declared denominator; receiving-medium identity is assessed separately. |
| stock-5543 | data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml; Complete local stock composition, preparation, evidence, history and placeholder fields | context_only | Asserted stock identity was checked against its exact public endpoint; no evidence or amount is inherited by the medium merely through a link. |
| api-5543 | https://mediadive.dsmz.de/rest/solution/5543; $.data.id/name/volume/recipe/steps | supports | Exact external stock formula and declared denominator; receiving-medium identity is assessed separately. |
| stock-6241 | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Complete local stock composition, preparation, evidence, history and placeholder fields | context_only | Asserted stock identity was checked against its exact public endpoint; no evidence or amount is inherited by the medium merely through a link. |
| api-6241 | https://mediadive.dsmz.de/rest/solution/6241; $.data.id/name/volume/recipe/steps | supports | Exact external stock formula and declared denominator; receiving-medium identity is assessed separately. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch037/365/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch037/365/grounding-inventory.json; Every asserted ingredient/stock CHEBI slot and exact current MIM identifier lookup | context_only | Canonical labels resolve, but supplied forms are a separate question. CHEBI29032 has zero current MIM rows; other asserted current CHEBI secondary keys have mapped preferred rows. No historical mapping is fabricated. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi29032 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29032; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi32030 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32030; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi75228 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75228; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS ID, label, nonobsolete status and scientific form | supports | Live ontology metadata was compared with supplied-form scope; existence alone does not establish the source correspondence. |
| history-metadata | data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml; data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml", "events": 13, "timestamp_issues": []}] |
| stock-history | /private/tmp/culturemech-review-work-batch037/365/history-inventory.json; Eight 4178, four 5543 and two 6241 amount claims, including exact decoded-object and hash comparison | supports | Authenticated stock-only quantities are not evidence of the medium’s stock links, receiving doses, final concentrations or chemical grounding. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import/stock resolution/merge and metal-label mechanisms were read only. Current mechanisms do not prove historical execution or justify the stored high_metal flag from mis-scoped quantities. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import/stock resolution/merge and metal-label mechanisms were read only. Current mechanisms do not prove historical execution or justify the stored high_metal flag from mis-scoped quantities. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import/stock resolution/merge and metal-label mechanisms were read only. Current mechanisms do not prove historical execution or justify the stored high_metal flag from mis-scoped quantities. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import/stock resolution/merge and metal-label mechanisms were read only. Current mechanisms do not prove historical execution or justify the stored high_metal flag from mis-scoped quantities. |
| writer-4 | scripts/analyze_metal_concentrations.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import/stock resolution/merge and metal-label mechanisms were read only. Current mechanisms do not prove historical execution or justify the stored high_metal flag from mis-scoped quantities. |
| writer-5 | scripts/add_metal_ree_labels.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current import/stock resolution/merge and metal-label mechanisms were read only. Current mechanisms do not prove historical execution or justify the stored high_metal flag from mis-scoped quantities. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- All substantive medium and stock source identities are available. Failed optional alternate-provider retrievals remain in the bound catalog and are not treated as missing primary evidence.
- No current negative lookup establishes historical MIM validity or invalidity. No legacy identifier is asserted in the inspected medium or stock layers.
- Source resazurin is 0.5 g. Main and stock water amounts, percentage/molarity labels, sulfide pH/color observations and undefined final volume are preserved without typical-recipe substitutions.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202425Z-culturemech-008354-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: artificial_seawater_medium_for_strain_js_srb250lac
  (CultureMech:008354)'
started_at: '2026-10-21T20:11:19Z'
finished_at: '2026-10-21T20:24:25Z'
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
summary: NBRC 1005 and exact TOGO M1787 agree on a staged basal medium plus four separate
  stocks. Both local layers flatten stock recipes and misstate water, milligram amounts
  and liquid doses. The linked SL-10 has 70 mg zinc rather than the source 7 mg, and
  the linked vitamin stock has three species rather than ten. Existing external-stock
  evidence is valid only within those stock records. Hydrate and calcium-pantothenate
  grounding errors and a completed current MIM lookup gap are separate findings.
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
  - path: data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
    sha256: fa9673659e9c3120839492747cac61832ec1f7611ab5db782f81739024cd1499
    role: target
  - path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
    sha256: 8fc4704838b57bf3f27e12494ea11c09c5e5985f119d6a50d50bc5d92a193e23
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
    sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
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
  - path: scripts/add_metal_ree_labels.py
    sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
    role: context
  - path: scripts/analyze_metal_concentrations.py
    sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
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
  selection: Task review 365; batch 037 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-six task batches
    contain 360 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 363 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008354
targets:
- target_id: CultureMech:008354
  path: data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  label: artificial_seawater_medium_for_strain_js_srb250lac
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/365/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/365/strict.tsv"
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008354
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
  - CultureMech:008354
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:03.650422Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/365/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:04.845291Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/365/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:06.352433Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:07.297378Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T20:24:24Z'
  support: supports
  summary: './data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml:1:id:
    CultureMech:008354

    ./data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml:1:id:
    CultureMech:008354

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/source-preflight-bound/365/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T20:24:24Z'
  support: supports
  summary: 47 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e6d092a302e5f265b5125ed44bb5f6fff1c75af2f4f4c51e21c769a6ac7923bd
- evidence_id: primary
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005
  locator: Exact Medium No.1005, full main table and four named stock sections
  accessed_at: '2026-10-21T19:52:57.597210Z'
  support: supports
  summary: Primary source identifies this medium and supplies amounts, stages and
    preparation. Resazurin is explicitly 0.5 g; no presumed mg correction is made.
  quote: Resazurin 0.5 g
  snapshot_sha256: fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787
  locator: $.meta; five components and scoped comments
  accessed_at: '2026-10-21T19:52:53.725315Z'
  support: supports
  summary: Exact provider corroborates primary quantities and stages; its text does
    not turn stock amounts into final concentrations.
  quote: NBRC_M1005
  snapshot_sha256: b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f
- evidence_id: procedure
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005
  locator: Main preparation paragraph and neutralized sulfide instructions
  accessed_at: '2026-10-21T19:52:57.597210Z'
  support: supports
  summary: Basal sterilization excludes six named additions; final main pH is 7.2–7.4,
    separate from sulfide-stock pH.
  quote: Adjust the final pH of the medium to 7.2-7.4.
  snapshot_sha256: fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4
- evidence_id: stock-4178
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
  locator: Complete local stock composition, preparation, evidence, history and placeholder
    fields
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Asserted stock identity was checked against its exact public endpoint;
    no evidence or amount is inherited by the medium merely through a link.
  snapshot_sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
- evidence_id: api-4178
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4178
  locator: $.data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T14:02:49.091885Z'
  support: supports
  summary: Exact external stock formula and declared denominator; receiving-medium
    identity is assessed separately.
  snapshot_sha256: 7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da
- evidence_id: stock-5543
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
  locator: Complete local stock composition, preparation, evidence, history and placeholder
    fields
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Asserted stock identity was checked against its exact public endpoint;
    no evidence or amount is inherited by the medium merely through a link.
  snapshot_sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
- evidence_id: api-5543
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5543
  locator: $.data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T14:01:44.555275Z'
  support: supports
  summary: Exact external stock formula and declared denominator; receiving-medium
    identity is assessed separately.
  snapshot_sha256: 7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882
- evidence_id: stock-6241
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Complete local stock composition, preparation, evidence, history and placeholder
    fields
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Asserted stock identity was checked against its exact public endpoint;
    no evidence or amount is inherited by the medium merely through a link.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: api-6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  locator: $.data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T09:46:49.463537Z'
  support: supports
  summary: Exact external stock formula and declared denominator; receiving-medium
    identity is assessed separately.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/365/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 60d2fa1bd4b6a5fa62dfc91be53e0499a81a6697aa098deab02c16061815aea4
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/365/grounding-inventory.json
  locator: Every asserted ingredient/stock CHEBI slot and exact current MIM identifier
    lookup
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Canonical labels resolve, but supplied forms are a separate question. CHEBI29032
    has zero current MIM rows; other asserted current CHEBI secondary keys have mapped
    preferred rows. No historical mapping is fabricated.
  snapshot_sha256: c42d57020d35ba63b39ecae0d5b364127ae29453cfc340890d96b7c8fb1efcb9
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi17439
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T07:16:23.574834Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi29032
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29032
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T16:01:40.896676Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 09b8e88386839f2c0111bf74dfd64335371f99f9e069def6ef7e28d88d0e0d48
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32030
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32030
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T07:18:36.747994Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 2dfff20bf274927ceb7d33e95e02fb24aca53828fc68b5fa5b21db63bdb318e6
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75228
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75228
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T14:35:48.010081Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 725fbc04444c481cec25519a6f632470427a7020613af93e84e05b5f23d66ccf
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS ID, label, nonobsolete status and scientific form
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: Live ontology metadata was compared with supplied-form scope; existence
    alone does not establish the source correspondence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml;
    data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml",
    "events": 13, "timestamp_issues": []}]'
- evidence_id: stock-history
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/365/history-inventory.json
  locator: Eight 4178, four 5543 and two 6241 amount claims, including exact decoded-object
    and hash comparison
  accessed_at: '2026-10-21T20:24:24Z'
  support: supports
  summary: Authenticated stock-only quantities are not evidence of the medium’s stock
    links, receiving doses, final concentrations or chemical grounding.
  snapshot_sha256: 6b01513e652c8c1465e9ba2f3d4f026c4f591402e6c474e985de4143a9279b50
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Current import/stock resolution/merge and metal-label mechanisms were read
    only. Current mechanisms do not prove historical execution or justify the stored
    high_metal flag from mis-scoped quantities.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Current import/stock resolution/merge and metal-label mechanisms were read
    only. Current mechanisms do not prove historical execution or justify the stored
    high_metal flag from mis-scoped quantities.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Current import/stock resolution/merge and metal-label mechanisms were read
    only. Current mechanisms do not prove historical execution or justify the stored
    high_metal flag from mis-scoped quantities.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Current import/stock resolution/merge and metal-label mechanisms were read
    only. Current mechanisms do not prove historical execution or justify the stored
    high_metal flag from mis-scoped quantities.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-4
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Current import/stock resolution/merge and metal-label mechanisms were read
    only. Current mechanisms do not prove historical execution or justify the stored
    high_metal flag from mis-scoped quantities.
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: writer-5
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:24:24Z'
  support: context_only
  summary: Current import/stock resolution/merge and metal-label mechanisms were read
    only. Current mechanisms do not prove historical execution or justify the stored
    high_metal flag from mis-scoped quantities.
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 86 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Distilled water\"\
    ,\n    \"stage\": \"NBRC main batch before selective post-cooling additions\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 18:  | Distilled water | 1\
    \ | L\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Distilled water</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">L</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Distilled water</td>\\r\\n<td align=\\\"right\\\"\
    \ width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">L</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"name\": \"NaCl\",\n    \"stage\": \"\
    NBRC main batch before selective post-cooling additions\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"26\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"26\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 26,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 5:  | NaCl | 26 | g\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">NaCl</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">26</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">NaCl</td>\\r\\n<td align=\\\"right\\\" width=\\\"\
    20%\\\">26</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 26,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q3\",\n    \"name\": \"CaCl2·2H2O\",\n    \"stage\"\
    : \"NBRC main batch before selective post-cooling additions\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1.4,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 8:  | CaCl 2 ·2H 2 O | 1.4\
    \ | g\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">CaCl<sub>2</sub>&middot;2H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1.4</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">CaCl<sub>2</sub>&middot;2H<sub>2</sub>O</td>\\r\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1.4</td>\\r\\n<td align=\\\"left\\\"\
    \ width=\\\"15%\\\">g</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\"\
    : \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2·2H2O\\\",\\n          \\\"volume\\\": 1.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q4\",\n    \"name\": \"KH2PO4\",\n    \"stage\":\
    \ \"NBRC main batch before selective post-cooling additions\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.2,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 3: KH 2 PO 4 0.2 g |  | KH\
    \ 2 PO 4 | 0.2 | g\",\n        \"exact_source_quote\": \"<tr>\\n             \
    \               <td colspan=\\\"2\\\" id=\\\"medium-comp\\\"><table border=\\\"\
    0\\\" width=\\\"600\\\">\\n<tbody>\\n<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">KH<sub>2</sub>PO<sub>4</sub></td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">0.2</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\n                            <td colspan=\\\"2\\\" id=\\\"medium-comp\\\
    \"><table border=\\\"0\\\" width=\\\"600\\\">\\r\\n<tbody>\\r\\n<tr>\\r\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\
    \"60%\\\">KH<sub>2</sub>PO<sub>4</sub></td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">0.2</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q5\",\n    \"name\": \"NH4Cl\",\n    \"stage\": \"\
    NBRC main batch before selective post-cooling additions\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": 0.25,\n      \"unit\"\
    : \"g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 4:  | NH 4 Cl | 0.25 | g\"\
    ,\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">NH<sub>4</sub>Cl</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">0.25</td>\\n<td align=\\\"left\\\"\
    \ width=\\\"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">NH<sub>4</sub>Cl</td>\\r\\n<td align=\\\"right\\\"\
    \ width=\\\"20%\\\">0.25</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q6\",\n    \"name\": \"Resazurin\",\n    \"stage\"\
    : \"NBRC main batch before selective post-cooling additions\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.5,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 13:  | Resazurin | 0.5 | g\"\
    ,\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Resazurin</td>\\n<td\
    \ align=\\\"right\\\" width=\\\"20%\\\">0.5</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Resazurin</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">0.5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator. The source\
    \ explicitly prints 0.5 g resazurin; no familiar milligram amount is substituted.\"\
    \n  },\n  {\n    \"decision_id\": \"q7\",\n    \"name\": \"MgCl2·6H2O\",\n   \
    \ \"stage\": \"NBRC main batch before selective post-cooling additions\",\n  \
    \  \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.2\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.2\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": 11.2,\n      \"unit\"\
    : \"g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 6:  | MgCl 2 ·6H 2 O | 11.2\
    \ | g\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">MgCl<sub>2</sub>&middot;6H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">11.2</td>\\n<td align=\\\"left\\\"\
    \ width=\\\"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">MgCl<sub>2</sub>&middot;6H<sub>2</sub>O</td>\\r\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">11.2</td>\\r\\n<td align=\\\"left\\\
    \" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\"\
    : \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2·6H2O\\\",\\n          \\\"volume\\\": 11.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q8\",\n    \"name\": \"KCl\",\n    \"stage\": \"\
    NBRC main batch before selective post-cooling additions\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.7,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 7:  | KCl | 0.7 | g\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">KCl</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">0.7</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">KCl</td>\\r\\n<td align=\\\"right\\\" width=\\\"\
    20%\\\">0.7</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.7,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q9\",\n    \"name\": \"NaHCO3\",\n    \"stage\":\
    \ \"NBRC main batch before selective post-cooling additions\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2.5,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 11:  | NaHCO 3 | 2.5 | g\"\
    ,\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">NaHCO<sub>3</sub></td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">2.5</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">NaHCO<sub>3</sub></td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">2.5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 2.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q10\",\n    \"name\": \"Na2SO4\",\n    \"stage\"\
    : \"NBRC main batch before selective post-cooling additions\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 4,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 9:  | Na 2 SO 4 | 4 | g\"\
    ,\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Na<sub>2</sub>SO<sub>4</sub></td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">4</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Na<sub>2</sub>SO<sub>4</sub></td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">4</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">g</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SO4\\\",\\n          \\\"volume\\\": 4,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q11\",\n    \"name\": \"Sodium lactate\",\n    \"\
    stage\": \"NBRC main batch before selective post-cooling additions\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2.3,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 12:  | Sodium lactate | 2.3\
    \ | g\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Sodium lactate</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">2.3</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Sodium lactate</td>\\r\\n<td align=\\\"right\\\"\
    \ width=\\\"20%\\\">2.3</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sodium lactate\\\",\\n          \\\"volume\\\"\
    : 2.3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Preserve the printed amount and stage. Main\
    \ water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main grams\
    \ do not by themselves establish a final-medium g/L denominator.\"\n  },\n  {\n\
    \    \"decision_id\": \"q12\",\n    \"name\": \"KBr\",\n    \"stage\": \"NBRC\
    \ main batch before selective post-cooling additions\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.1,\n      \"unit\": \"\
    g\",\n      \"basis\": \"Source-listed main batch; 1 L water plus stock doses,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 10:  | KBr | 0.1 | g\",\n\
    \        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">KBr</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">0.1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">KBr</td>\\r\\n<td align=\\\"right\\\" width=\\\"\
    20%\\\">0.1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KBr\\\",\\n          \\\"volume\\\": 0.1,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the printed amount and stage.\
    \ Main water is 1 L, not the mixed-unit duplicate total 1093 G_PER_L. Other main\
    \ grams do not by themselves establish a final-medium g/L denominator.\"\n  },\n\
    \  {\n    \"decision_id\": \"q13\",\n    \"name\": \"Carbon dioxide gas\",\n \
    \   \"stage\": \"Main gas ingredient entry\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dissolved_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[16]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Variable gas entries supply no dissolved\
    \ concentration. The main atmosphere ratio is an independent preparation decision.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"name\": \"Nitrogen gas\",\n\
    \    \"stage\": \"Main gas ingredient entry\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dissolved_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[17]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Variable gas entries supply no dissolved\
    \ concentration. The main atmosphere ratio is an independent preparation decision.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"name\": \"Trace element solution\
    \ SL-10*\",\n    \"stage\": \"Main receiving stock dose\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\": \"\
    ml\",\n      \"basis\": \"Dose into the listed main preparation\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n  \
    \      \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 14:  | Trace element solution\
    \ SL-10* | 1 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"\
    5%\\\">&nbsp;</td>\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\"\
    >Trace element solution SL-10*</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\"\
    >1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\n</tr>\",\n      \
    \  \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Trace element solution SL-10*</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">ml</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution SL-10*\\\",\\n        \
    \  \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The receiving dose is liquid milliliters,\
    \ not G_PER_L. Keep the exact stock identity and batch recipe distinct from this\
    \ dose.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"name\": \"Selenite-tungstate\
    \ solution**\",\n    \"stage\": \"Main receiving stock dose\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\": \"\
    ml\",\n      \"basis\": \"Dose into the listed main preparation\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n  \
    \      \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 15:  | Selenite-tungstate\
    \ solution** | 1 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\
    \"5%\\\">&nbsp;</td>\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\
    \">Selenite-tungstate solution**</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\
    \">1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\n</tr>\",\n    \
    \    \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Selenite-tungstate solution**</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">ml</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Selenite-tungstate solution**\\\",\\n        \
    \  \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The receiving dose is liquid milliliters,\
    \ not G_PER_L. Keep the exact stock identity and batch recipe distinct from this\
    \ dose.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"name\": \"Vitamin solution***\"\
    ,\n    \"stage\": \"Main receiving stock dose\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\": \"\
    ml\",\n      \"basis\": \"Dose into the listed main preparation\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n  \
    \      \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 16:  | Vitamin solution***\
    \ | 1 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Vitamin solution***</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Vitamin solution***</td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin solution***\\\",\\n          \\\"volume\\\
    \": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"The receiving dose is liquid milliliters, not\
    \ G_PER_L. Keep the exact stock identity and batch recipe distinct from this dose.\"\
    \n  },\n  {\n    \"decision_id\": \"q18\",\n    \"name\": \"Sulfide solution****\"\
    ,\n    \"stage\": \"Main receiving stock dose\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\": \"\
    ml\",\n      \"basis\": \"Dose into the listed main preparation\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n  \
    \      \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 17:  | Sulfide solution****\
    \ | 10 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Sulfide\
    \ solution****</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\">10</td>\\n<td\
    \ align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\"\
    : \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n    \
    \    \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF;\
    \ original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Sulfide solution****</td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">10</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[0].items[15]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sulfide solution****\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The receiving dose is liquid milliliters,\
    \ not G_PER_L. Keep the exact stock identity and batch recipe distinct from this\
    \ dose.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"Distilled\
    \ water\",\n    \"stage\": \"SL-10 stock batch\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": 990,\n      \"unit\"\
    : \"ml\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 32:  |  |  | Distilled water\
    \ | 990 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Distilled water</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">990</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Distilled water</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">990</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\r\\\
    n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 990,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q20\",\n    \"name\": \"Na2MoO4·2H2O\",\n    \"stage\": \"SL-10\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 36,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 31:  |  |  | Na 2 MoO 4 ·2H\
    \ 2 O | 36 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Na<sub>2</sub>MoO<sub>4</sub>&middot;2H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">36</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Na<sub>2</sub>MoO<sub>4</sub>&middot;2H<sub>2</sub>O</td>\\\
    r\\n<td align=\\\"right\\\" width=\\\"20%\\\">36</td>\\r\\n<td align=\\\"left\\\
    \" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\"\
    : \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4·2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q21\",\n    \"name\": \"H3BO3\",\n    \"stage\": \"SL-10 stock\
    \ batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 6,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 27:  |  |  | H 3 BO 3 | 6\
    \ | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">H<sub>3</sub>BO<sub>3</sub></td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">6</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">H<sub>3</sub>BO<sub>3</sub></td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">6</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q22\",\n    \"name\": \"MnCl2·4H2O\",\n    \"stage\":\
    \ \"SL-10 stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 100,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 26:  |  |  | MnCl 2 ·4H 2\
    \ O | 100 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">MnCl<sub>2</sub>&middot;4H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">100</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">MnCl<sub>2</sub>&middot;4H<sub>2</sub>O</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">100</td>\\r\\n<td align=\\\"left\\\" width=\\\"\
    15%\\\">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2·4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q23\",\n    \"name\": \"CoCl2·6H2O\",\n    \"stage\":\
    \ \"SL-10 stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 190,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 28:  |  |  | CoCl 2 ·6H 2\
    \ O | 190 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">CoCl<sub>2</sub>&middot;6H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">190</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">CoCl<sub>2</sub>&middot;6H<sub>2</sub>O</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">190</td>\\r\\n<td align=\\\"left\\\" width=\\\"\
    15%\\\">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2·6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q24\",\n    \"name\": \"NiCl2·6H2O\",\n    \"stage\":\
    \ \"SL-10 stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 24,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 30:  |  |  | NiCl 2 ·6H 2\
    \ O | 24 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">NiCl<sub>2</sub>&middot;6H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">24</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">NiCl<sub>2</sub>&middot;6H<sub>2</sub>O</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">24</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2·6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q25\",\n    \"name\": \"CuCl2·2H2O\",\n    \"stage\":\
    \ \"SL-10 stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 29:  |  |  | CuCl 2 ·2H 2\
    \ O | 2 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">CuCl<sub>2</sub>&middot;2H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">2</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">CuCl<sub>2</sub>&middot;2H<sub>2</sub>O</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">2</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2·2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q26\",\n    \"name\": \"ZnCl2\",\n    \"stage\": \"SL-10\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 7,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 25:  |  |  | ZnCl 2 | 7 |\
    \ mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">ZnCl<sub>2</sub></td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">7</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">ZnCl<sub>2</sub></td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">7</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 7,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q27\",\n    \"name\": \"HCl (25%; 7.7 M)\",\n    \"stage\"\
    : \"SL-10 stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\": \"\
    ml\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 23:  |  |  | HCl (25%; 7.7\
    \ M) | 10 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">HCl (25%; 7.7 M)</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">10</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">HCl (25%; 7.7 M)</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">10</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%; 7.7 M)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q28\",\n    \"name\": \"FeCl2·4H2O\",\n    \"stage\": \"SL-10\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1.5,\n      \"unit\": \"\
    g\",\n      \"proposed_scope\": \"solutions[0].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 24:  |  |  | FeCl 2 ·4H 2\
    \ O | 1.5 | g\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">FeCl<sub>2</sub>&middot;4H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1.5</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">FeCl<sub>2</sub>&middot;4H<sub>2</sub>O</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1.5</td>\\r\\n<td align=\\\"left\\\" width=\\\"\
    15%\\\">g</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2·4H2O\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q29\",\n    \"name\": \"distilled water\",\n    \"stage\"\
    : \"Selenite-tungstate stock batch\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\",\n      \"proposed_scope\": \"solutions[1].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 38:  |  |  | distilled water\
    \ | 1 | L\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">distilled water</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >L</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">distilled water</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">L</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q30\",\n    \"name\": \"Na2SeO3·5H2O\",\n    \"stage\"\
    : \"Selenite-tungstate stock batch\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 3,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[1].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 36:  |  |  | Na 2 SeO 3 ·5H\
    \ 2 O | 3 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Na<sub>2</sub>SeO<sub>3</sub>&middot;5H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">3</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Na<sub>2</sub>SeO<sub>3</sub>&middot;5H<sub>2</sub>O</td>\\\
    r\\n<td align=\\\"right\\\" width=\\\"20%\\\">3</td>\\r\\n<td align=\\\"left\\\
    \" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\"\
    : \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO3·5H2O\\\",\\n          \\\"volume\\\":\
    \ 3,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q31\",\n    \"name\": \"Na2WO4·2H2O\",\n    \"stage\": \"Selenite-tungstate\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 4,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[1].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 37:  |  |  | Na 2 WO 4 ·2H\
    \ 2 O | 4 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Na<sub>2</sub>WO<sub>4</sub>&middot;2H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">4</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Na<sub>2</sub>WO<sub>4</sub>&middot;2H<sub>2</sub>O</td>\\\
    r\\n<td align=\\\"right\\\" width=\\\"20%\\\">4</td>\\r\\n<td align=\\\"left\\\
    \" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\"\
    : \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4·2H2O\\\",\\n          \\\"volume\\\": 4,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q32\",\n    \"name\": \"NaOH\",\n    \"stage\": \"Selenite-tungstate\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.5,\n      \"unit\": \"\
    g\",\n      \"proposed_scope\": \"solutions[1].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 35:  |  |  | NaOH | 0.5 |\
    \ g\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">NaOH</td>\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">0.5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\\
    n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">NaOH</td>\\r\\n<td align=\\\"right\\\" width=\\\"20%\\\"\
    >0.5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">g</td>\\r\\n</tr>\"\n\
    \      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"volume\\\": 0.5,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q33\",\n    \"name\": \"Distilled water\",\n    \"stage\"\
    : \"Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": 1,\n      \"unit\"\
    : \"L\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 53:  |  |  | Distilled water\
    \ | 1 | L\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Distilled water</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >L</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Distilled water</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">L</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q34\",\n    \"name\": \"Biotin\",\n    \"stage\": \"Ten-vitamin\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 43:  |  |  | Biotin | 2 |\
    \ mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Biotin</td>\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">2</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\\
    n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Biotin</td>\\r\\n<td align=\\\"right\\\" width=\\\"20%\\\"\
    >2</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n \
    \     },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q35\",\n    \"name\": \"p-Aminobenzoic acid\",\n    \"\
    stage\": \"Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 5,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 51:  |  |  | p -Aminobenzoic\
    \ acid | 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\"><em>p</em>-Aminobenzoic\
    \ acid</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"\
    left\\\" width=\\\"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"\
    fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n        \"\
    quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF; original\
    \ byte-literal row separately preserved.\",\n        \"raw_bytes_quote\": \"<tr>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\"\
    \ width=\\\"50%\\\"><em>p</em>-Aminobenzoic acid</td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p-Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q36\",\n    \"name\": \"Thiamine-HCl\",\n    \"stage\": \"Ten-vitamin\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 5,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 46:  |  |  | Thiamine-HCl\
    \ | 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Thiamine-HCl</td>\\n<td align=\\\"\
    right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Thiamine-HCl</td>\\r\\n<td align=\\\"right\\\" width=\\\"\
    20%\\\">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine-HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q37\",\n    \"name\": \"Ca-pantothenate\",\n    \"stage\": \"\
    Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 5,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 49:  |  |  | Ca-pantothenate\
    \ | 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Ca-pantothenate</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Ca-pantothenate</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Ca-pantothenate\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q38\",\n    \"name\": \"Pyridoxine-HCl\",\n    \"stage\": \"\
    Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 10,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 45:  |  |  | Pyridoxine-HCl\
    \ | 10 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Pyridoxine-HCl</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">10</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Pyridoxine-HCl</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">10</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine-HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q39\",\n    \"name\": \"Folic acid\",\n    \"stage\": \"Ten-vitamin\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 44:  |  |  | Folic acid |\
    \ 2 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Folic acid</td>\\n<td align=\\\"\
    right\\\" width=\\\"20%\\\">2</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Folic acid</td>\\r\\n<td align=\\\"right\\\" width=\\\"20%\\\
    \">2</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n\
    \      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q40\",\n    \"name\": \"Vitamin B12\",\n    \"stage\"\
    : \"Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 0.1,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 50:  |  |  | Vitamin B 12\
    \ | 0.1 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Vitamin B<sub>12</sub></td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">0.1</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Vitamin B<sub>12</sub></td>\\r\\n<td align=\\\"right\\\"\
    \ width=\\\"20%\\\">0.1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q41\",\n    \"name\": \"Riboflavin\",\n    \"stage\":\
    \ \"Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 5,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 47:  |  |  | Riboflavin |\
    \ 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Riboflavin</td>\\n<td align=\\\"\
    right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Riboflavin</td>\\r\\n<td align=\\\"right\\\" width=\\\"20%\\\
    \">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n\
    \      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q42\",\n    \"name\": \"Nicotinic acid\",\n    \"stage\"\
    : \"Ten-vitamin stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[34].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[34].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 5,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 48:  |  |  | Nicotinic acid\
    \ | 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Nicotinic acid</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Nicotinic acid</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q43\",\n    \"name\": \"Lipoic acid\",\n    \"stage\": \"Ten-vitamin\
    \ stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[35].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[35].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 5,\n      \"unit\": \"\
    mg\",\n      \"proposed_scope\": \"solutions[2].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 52:  |  |  | Lipoic acid |\
    \ 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Lipoic acid</td>\\n<td align=\\\"\
    right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Lipoic acid</td>\\r\\n<td align=\\\"right\\\" width=\\\"\
    20%\\\">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[3].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q44\",\n    \"name\": \"Distilled water\",\n    \"stage\"\
    : \"Neutralized sulfide stock batch\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1093.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": 100,\n      \"unit\"\
    : \"ml\",\n      \"proposed_scope\": \"solutions[3].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 57:  |  |  | Distilled water\
    \ | 100 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Distilled water</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">100</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Distilled water</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">100</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\r\\\
    n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n      }\n\
    \    ],\n    \"interpretation\": \"Move this amount into its exact named stock\
    \ recipe. Milligrams are not grams per liter of the receiving medium. Five separate\
    \ water entries were combined in the local field; neither their mixed-unit numeric\
    \ sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n    \"\
    decision_id\": \"q45\",\n    \"name\": \"Na2S·9H2O\",\n    \"stage\": \"Neutralized\
    \ sulfide stock batch\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[36].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[36].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1.5,\n      \"unit\": \"\
    g\",\n      \"proposed_scope\": \"solutions[3].composition\",\n      \"basis\"\
    : \"Separate stock input\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 56:  |  |  | Na 2 S·9H 2 O\
    \ | 1.5 | g\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Na<sub>2</sub>S&middot;9H<sub>2</sub>O</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1.5</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">g</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Na<sub>2</sub>S&middot;9H<sub>2</sub>O</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1.5</td>\\r\\n<td align=\\\"left\\\" width=\\\"\
    15%\\\">g</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"togoM1787original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S·9H2O\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      }\n    ],\n    \"interpretation\": \"Move this amount into its exact named\
    \ stock recipe. Milligrams are not grams per liter of the receiving medium. Five\
    \ separate water entries were combined in the local field; neither their mixed-unit\
    \ numeric sum nor full stock batches belong in main-medium water.\"\n  },\n  {\n\
    \    \"decision_id\": \"q46\",\n    \"name\": \"Sulfuric acid dose\",\n    \"\
    stage\": \"Neutralized sulfide stock titration\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[37].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[37].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"dose\": null,\n      \"\
    endpoint\": \"about pH 7.3\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[4].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H2SO4\\\",\\n          \\\"conc_value\\\": 2,\\\
    n          \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1005\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\",\n\
    \        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"The source gives dropwise\
    \ titration and acid strength, not a fixed acid dose. Preserve the variable-dose\
    \ status within the sulfide stock rather than the main recipe.\"\n  },\n  {\n\
    \    \"decision_id\": \"q47\",\n    \"name\": \"Nitrogen gas\",\n    \"stage\"\
    : \"Neutralized sulfide stock atmosphere\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[38].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[38].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"gas\": \"N2\",\n      \"\
    purity_percent\": null\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"togoM1787original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[4].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"N2\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1005\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\",\n\
    \        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"The stock specifies N2\
    \ without purity or dissolved concentration. It is distinct from the main N2/CO2\
    \ mixture.\"\n  },\n  {\n    \"decision_id\": \"q48\",\n    \"name\": \"HCl strength\"\
    ,\n    \"stage\": \"SL-10 acid component\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].preferred_term\",\n        \"stored\"\
    : \"HCl (25%; 7.7 M)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].preferred_term\",\n        \"stored\"\
    : \"HCl (25%; 7.7 M)\"\n      }\n    ],\n    \"desired\": {\n      \"value\":\
    \ 25,\n      \"unit\": \"PERCENT\",\n      \"basis\": \"not specified\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n\
    \        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 23:  |  |  | HCl (25%; 7.7\
    \ M) | 10 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">HCl (25%; 7.7 M)</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">10</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">HCl (25%; 7.7 M)</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">10</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%; 7.7 M)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The printed percentage has no w/v, v/v\
    \ or w/w qualifier. Do not infer density from the adjacent molarity.\"\n  },\n\
    \  {\n    \"decision_id\": \"q49\",\n    \"name\": \"HCl molarity\",\n    \"stage\"\
    : \"SL-10 acid component\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].preferred_term\",\n        \"stored\"\
    : \"HCl (25%; 7.7 M)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].preferred_term\",\n        \"stored\"\
    : \"HCl (25%; 7.7 M)\"\n      }\n    ],\n    \"desired\": {\n      \"value\":\
    \ 7.7,\n      \"unit\": \"MOLAR\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 23:  |  |  | HCl (25%; 7.7\
    \ M) | 10 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\
    \">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"2\\\" align=\\\"left\\\" width=\\\"50%\\\">HCl (25%; 7.7 M)</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">10</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">HCl (25%; 7.7 M)</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">10</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%; 7.7 M)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Preserve source-stated molarity separately\
    \ from the 10 mL dose and 25% label.\"\n  },\n  {\n    \"decision_id\": \"q50\"\
    ,\n    \"name\": \"Final main pH\",\n    \"stage\": \"Main preparation\",\n  \
    \  \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"minimum\": 7.2,\n      \"maximum\": 7.4\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 20:  |  | Dissolve ingredients\
    \ except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins\
    \ and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization\
    \ and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride,\
    \ bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust\
    \ the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20)\
    \ gas mixture in culture vessels.\",\n        \"exact_source_quote\": \"<tr>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate, ammonium\
    \ chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a\
    \ cultivation device for anaerobes. After sterilization and cooling under a nitrogen\
    \ atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate,\
    \ vitamins and sulfide from sterile stock solutions. Adjust the final pH of the\
    \ medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub> (80/20)\
    \ gas mixture in culture vessels.</td>\\n</tr>\",\n        \"snapshot_sha256\"\
    : \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n    \
    \    \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF;\
    \ original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate,\
    \ ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave\
    \ it in a cultivation device for anaerobes. After sterilization and cooling under\
    \ a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate,\
    \ lactate, vitamins and sulfide from sterile stock solutions. Adjust the final\
    \ pH of the medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub>\
    \ (80/20) gas mixture in culture vessels.</td>\\r\\n</tr>\"\n      }\n    ],\n\
    \    \"interpretation\": \"This is explicitly the final main-medium pH, not a\
    \ stock pH.\"\n  },\n  {\n    \"decision_id\": \"q51\",\n    \"name\": \"N2/CO2\
    \ mixture\",\n    \"stage\": \"Main dispensing\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"ratio\": \"80/20\",\n      \"species\"\
    : [\n        \"N2\",\n        \"CO2\"\n      ],\n      \"basis\": \"not printed\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 20:  |  | Dissolve ingredients\
    \ except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins\
    \ and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization\
    \ and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride,\
    \ bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust\
    \ the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20)\
    \ gas mixture in culture vessels.\",\n        \"exact_source_quote\": \"<tr>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate, ammonium\
    \ chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a\
    \ cultivation device for anaerobes. After sterilization and cooling under a nitrogen\
    \ atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate,\
    \ vitamins and sulfide from sterile stock solutions. Adjust the final pH of the\
    \ medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub> (80/20)\
    \ gas mixture in culture vessels.</td>\\n</tr>\",\n        \"snapshot_sha256\"\
    : \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n    \
    \    \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF;\
    \ original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate,\
    \ ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave\
    \ it in a cultivation device for anaerobes. After sterilization and cooling under\
    \ a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate,\
    \ lactate, vitamins and sulfide from sterile stock solutions. Adjust the final\
    \ pH of the medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub>\
    \ (80/20) gas mixture in culture vessels.</td>\\r\\n</tr>\"\n      }\n    ],\n\
    \    \"interpretation\": \"The source prints 80/20 without v/v. No ratio is transferred\
    \ to separately prepared sulfide stock.\"\n  },\n  {\n    \"decision_id\": \"\
    q52\",\n    \"name\": \"Autoclave temperature\",\n    \"stage\": \"Neutralized\
    \ sulfide stock preparation\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 121,\n      \"unit\": \"\
    DEG_C\",\n      \"scope\": \"Sulfide stock only; not a default for the main medium\
    \ or Se/W stock.\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Sulfide stock only; not\
    \ a default for the main medium or Se/W stock.\"\n  },\n  {\n    \"decision_id\"\
    : \"q53\",\n    \"name\": \"Autoclave duration\",\n    \"stage\": \"Neutralized\
    \ sulfide stock preparation\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 15,\n      \"unit\": \"\
    MIN\",\n      \"scope\": \"Sulfide stock only; no main-medium cycle is specified.\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Sulfide stock only; no\
    \ main-medium cycle is specified.\"\n  },\n  {\n    \"decision_id\": \"q54\",\n\
    \    \"name\": \"Sulfide pH endpoint\",\n    \"stage\": \"Neutralized sulfide\
    \ stock preparation\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 7.3,\n      \"unit\": \"\
    PH\",\n      \"scope\": \"Approximate endpoint; not identical to the separately\
    \ described yellow-color pH.\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Approximate endpoint;\
    \ not identical to the separately described yellow-color pH.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q55\",\n    \"name\": \"Acid titrant strength\",\n    \"\
    stage\": \"Neutralized sulfide stock preparation\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 2,\n      \"unit\": \"\
    NORMAL\",\n      \"scope\": \"Strength only; dropwise dose is unquantified.\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Strength only; dropwise\
    \ dose is unquantified.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"name\"\
    : \"Yellow-color observation pH\",\n    \"stage\": \"Neutralized sulfide stock\
    \ preparation\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 8,\n      \"unit\": \"\
    PH\",\n      \"scope\": \"Approximate color observation; preserve the source’s\
    \ separate pH 7.3 and transparent-yellow wording.\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"nbrc1005\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\",\n   \
    \     \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Approximate color observation;\
    \ preserve the source’s separate pH 7.3 and transparent-yellow wording.\"\n  },\n\
    \  {\n    \"decision_id\": \"q57\",\n    \"name\": \"Main and Se/W autoclave cycles\"\
    ,\n    \"stage\": \"Separate sterilization stages\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"main_temperature\": null,\n    \
    \  \"main_duration\": null,\n      \"SeW_temperature\": null,\n      \"SeW_duration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 20:  |  | Dissolve ingredients\
    \ except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins\
    \ and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization\
    \ and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride,\
    \ bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust\
    \ the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20)\
    \ gas mixture in culture vessels.\",\n        \"exact_source_quote\": \"<tr>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate, ammonium\
    \ chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a\
    \ cultivation device for anaerobes. After sterilization and cooling under a nitrogen\
    \ atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate,\
    \ vitamins and sulfide from sterile stock solutions. Adjust the final pH of the\
    \ medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub> (80/20)\
    \ gas mixture in culture vessels.</td>\\n</tr>\",\n        \"snapshot_sha256\"\
    : \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n    \
    \    \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF;\
    \ original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate,\
    \ ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave\
    \ it in a cultivation device for anaerobes. After sterilization and cooling under\
    \ a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate,\
    \ lactate, vitamins and sulfide from sterile stock solutions. Adjust the final\
    \ pH of the medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub>\
    \ (80/20) gas mixture in culture vessels.</td>\\r\\n</tr>\"\n      },\n      {\n\
    \        \"source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 40:  |  | Sterilized by autoclaving.\"\
    ,\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">Sterilized\
    \ by autoclaving.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">Sterilized by autoclaving.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"The main and Se/W instructions\
    \ name autoclaving without numerical cycles. The sulfide-specific 121°C/15 min\
    \ must not be silently inherited.\"\n  },\n  {\n    \"decision_id\": \"q58\",\n\
    \    \"name\": \"Sterile stock strengths for delayed basal additions\",\n    \"\
    stage\": \"After cooling under nitrogen\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"phosphate_stock_strength\": null,\n\
    \      \"ammonium_stock_strength\": null,\n      \"bicarbonate_stock_strength\"\
    : null,\n      \"lactate_stock_strength\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"nbrc1005\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\",\n   \
    \     \"source_locator\": \"NBRC 1005 HTML row 20:  |  | Dissolve ingredients\
    \ except dihydrogenphosphate, ammonium chloride, bicarbonate, lactate, vitamins\
    \ and sulfide, and autoclave it in a cultivation device for anaerobes. After sterilization\
    \ and cooling under a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride,\
    \ bicarbonate, lactate, vitamins and sulfide from sterile stock solutions. Adjust\
    \ the final pH of the medium to 7.2-7.4. Dispense the medium under N 2 /CO 2 (80/20)\
    \ gas mixture in culture vessels.\",\n        \"exact_source_quote\": \"<tr>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate, ammonium\
    \ chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave it in a\
    \ cultivation device for anaerobes. After sterilization and cooling under a nitrogen\
    \ atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate, lactate,\
    \ vitamins and sulfide from sterile stock solutions. Adjust the final pH of the\
    \ medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub> (80/20)\
    \ gas mixture in culture vessels.</td>\\n</tr>\",\n        \"snapshot_sha256\"\
    : \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n    \
    \    \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF;\
    \ original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">Dissolve ingredients except dihydrogenphosphate,\
    \ ammonium chloride, bicarbonate, lactate, vitamins and sulfide, and autoclave\
    \ it in a cultivation device for anaerobes. After sterilization and cooling under\
    \ a nitrogen atmosphere, add dihydrogenphosphate, ammonium chloride, bicarbonate,\
    \ lactate, vitamins and sulfide from sterile stock solutions. Adjust the final\
    \ pH of the medium to 7.2-7.4. Dispense the medium under N<sub>2</sub>/CO<sub>2</sub>\
    \ (80/20) gas mixture in culture vessels.</td>\\r\\n</tr>\"\n      }\n    ],\n\
    \    \"interpretation\": \"The primary instructs sterile stocks for phosphate,\
    \ ammonium, bicarbonate and lactate but gives no concentrations or solvent doses\
    \ for those additional stocks.\"\n  },\n  {\n    \"decision_id\": \"q59\",\n \
    \   \"name\": \"Room-temperature cooling\",\n    \"stage\": \"Sulfide neutralization\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"temperature\": null\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n  \
    \      \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 59:  |  | The sulfide solution\
    \ is prepared in a vessel sealed with a butyl rubber stopper. Autoclave at 121℃\
    \ for 15 min under a N 2 atmosphere. After cooling to room temperature, the pH\
    \ is adjusted to about 7.3 by adding of sterile 2 N H 2 SO 4 drop-wise with a\
    \ syringe without opening the bottle. Appearance of yellow colour indicates the\
    \ pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.\",\n \
    \       \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td\
    \ width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide\
    \ solution is prepared in a vessel sealed with a butyl rubber stopper. Autoclave\
    \ at 121℃ for 15 min under a N<sub>2</sub> atmosphere. After cooling to room temperature,\
    \ the pH is adjusted to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub>\
    \ drop-wise with a syringe without opening the bottle. Appearance of yellow colour\
    \ indicates the pH is about 8. The vessel should be shaken continuously to avoid\
    \ precipitation of elemental sulfur. The final solution should be transparent\
    \ yellow.</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td colspan=\\\"5\\\" width=\\\"90%\\\">The sulfide solution is prepared in\
    \ a vessel sealed with a butyl rubber stopper. Autoclave at 121℃ for 15 min under\
    \ a N<sub>2</sub> atmosphere. After cooling to room temperature, the pH is adjusted\
    \ to about 7.3 by adding of sterile 2 N H<sub>2</sub>SO<sub>4</sub> drop-wise\
    \ with a syringe without opening the bottle. Appearance of yellow colour indicates\
    \ the pH is about 8. The vessel should be shaken continuously to avoid precipitation\
    \ of elemental sulfur. The final solution should be transparent yellow.</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Room temperature is not\
    \ converted to an invented numerical temperature.\"\n  },\n  {\n    \"decision_id\"\
    : \"q60\",\n    \"name\": \"Independent final volume\",\n    \"stage\": \"Main\
    \ and stock assembly\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"measured_final_medium_volume\":\
    \ null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 18:  | Distilled water | 1\
    \ | L\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Distilled water</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">L</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Distilled water</td>\\r\\n<td align=\\\"right\\\"\
    \ width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">L</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"nbrc1005\",\n      \
    \  \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 14:  | Trace element solution\
    \ SL-10* | 1 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"\
    5%\\\">&nbsp;</td>\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\"\
    >Trace element solution SL-10*</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\"\
    >1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\n</tr>\",\n      \
    \  \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Trace element solution SL-10*</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">ml</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"nbrc1005\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 15:  | Selenite-tungstate\
    \ solution** | 1 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\
    \"5%\\\">&nbsp;</td>\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\
    \">Selenite-tungstate solution**</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\
    \">1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\n</tr>\",\n    \
    \    \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Selenite-tungstate solution**</td>\\r\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\
    \">ml</td>\\r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"nbrc1005\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 16:  | Vitamin solution***\
    \ | 1 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Vitamin solution***</td>\\\
    n<td align=\\\"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\
    \"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Vitamin solution***</td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\\
    r\\n</tr>\"\n      },\n      {\n        \"source_key\": \"nbrc1005\",\n      \
    \  \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 17:  | Sulfide solution****\
    \ | 10 | ml\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\"\
    >&nbsp;</td>\\n<td colspan=\\\"4\\\" align=\\\"left\\\" width=\\\"60%\\\">Sulfide\
    \ solution****</td>\\n<td align=\\\"right\\\" width=\\\"20%\\\">10</td>\\n<td\
    \ align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\n</tr>\",\n        \"snapshot_sha256\"\
    : \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\",\n    \
    \    \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized to LF;\
    \ original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"4\\\" align=\\\
    \"left\\\" width=\\\"60%\\\">Sulfide solution****</td>\\r\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">10</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">ml</td>\\\
    r\\n</tr>\"\n      }\n    ],\n    \"interpretation\": \"Main 1 L water and 1/1/1/10\
    \ mL doses do not state an independently measured final volume; whole-stock preparation\
    \ waters are not receiving-medium additions.\"\n  },\n  {\n    \"decision_id\"\
    : \"q61\",\n    \"name\": \"HCl\",\n    \"stage\": \"External MediaDive 4178 stock\
    \ only\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_dose\": 10,\n      \"dose_unit\"\
    : \"ml\",\n      \"attribute\": \"25%, 7.7 M\",\n      \"provider_g_l\": 2.5\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution4178\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\",\n\
    \        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"HCl\\\",\\n                \\\"compound_id\\\": 68,\\n               \
    \ \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n    \
    \            \\\"condition\\\": null,\\n                \\\"attribute\\\": \\\"\
    25%, 7.7 M\\\",\\n                \\\"amount\\\": 10,\\n                \\\"unit\\\
    \": \\\"ml\\\",\\n                \\\"g_l\\\": 2.5,\\n                \\\"mmol_l\\\
    \": 68.5683,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"The API supplies both a 10 mL stock-acid\
    \ dose and g_l=2.5. Preserve the conflicting concentration interpretation without\
    \ deriving mass from an unqualified percentage or treating g_l as the literal\
    \ dose.\"\n  },\n  {\n    \"decision_id\": \"q62\",\n    \"name\": \"FeCl2 x 4\
    \ H2O\",\n    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"1.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"FeCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 260,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1.5,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 1.5,\\n                \\\"mmol_l\\\
    \": 7.54482,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q63\",\n    \"name\": \"ZnCl2\",\n    \"stage\"\
    : \"External MediaDive 4178 stock only\",\n    \"decision\": \"verified\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.07\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"ZnCl2\\\",\\n                \\\"compound_id\\\": 64,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 70,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.07,\\n                \\\"mmol_l\\\": 0.513573,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence decodes\
    \ to the same provider recipe object. Verification covers the current external\
    \ stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\n\
    \  },\n  {\n    \"decision_id\": \"q64\",\n    \"name\": \"MnCl2 x 4 H2O\",\n\
    \    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"MnCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 36,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 100,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\
    \": 0.505293,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q65\",\n    \"name\": \"H3BO3\",\n    \"stage\"\
    : \"External MediaDive 4178 stock only\",\n    \"decision\": \"verified\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.006\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"H3BO3\\\",\\n                \\\"compound_id\\\": 37,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 6,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.006,\\n                \\\"mmol_l\\\": 0.0970246,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence decodes\
    \ to the same provider recipe object. Verification covers the current external\
    \ stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\n\
    \  },\n  {\n    \"decision_id\": \"q66\",\n    \"name\": \"CoCl2 x 6 H2O\",\n\
    \    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.19\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 190,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.19,\\n                \\\"mmol_l\\\
    \": 1.46335,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q67\",\n    \"name\": \"CuCl2 x 2 H2O\",\n\
    \    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.002\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"CuCl2 x 2 H2O\\\",\\n                \\\"compound_id\\\": 39,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 2,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.002,\\n                \\\"mmol_l\\\
    \": 0.0117314,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q68\",\n    \"name\": \"NiCl2 x 6 H2O\",\n\
    \    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.024\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"NiCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 40,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 24,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.024,\\n                \\\"mmol_l\\\
    \": 0.185187,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q69\",\n    \"name\": \"Na2MoO4 x 2 H2O\"\
    ,\n    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.036\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 9,\\n                \\\"compound\\\
    \": \\\"Na2MoO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 36,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.036,\\n                \\\"mmol_l\\\
    \": 0.148791,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q70\",\n    \"name\": \"Distilled water\"\
    ,\n    \"stage\": \"External MediaDive 4178 stock only\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"990\",\n          \"unit\": \"PERCENT_V_V\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"value\": 990,\n      \"unit\"\
    : \"ML\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 10,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 990,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"Provider water is a 990 mL batch\
    \ input, not 990% v/v. Its 1000 mL declared solution volume is separate.\"\n \
    \ },\n  {\n    \"decision_id\": \"q71\",\n    \"name\": \"Provider-declared stock\
    \ volume\",\n    \"stage\": \"External MediaDive 4178 metadata\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Dissolve\
    \ FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining\
    \ salts.\"\n      }\n    ],\n    \"desired\": {\n      \"value\": 1000,\n    \
    \  \"unit\": \"ML\",\n      \"basis\": \"Provider declaration\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"solution4178\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\",\n    \
    \    \"source_locator\": \"$.data.volume\",\n        \"exact_source_quote\": \"\
    \\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"This declaration belongs to the external\
    \ stock and must not be treated as a measured receiving-medium volume or automatic\
    \ proof of NBRC stock equivalence.\"\n  },\n  {\n    \"decision_id\": \"q72\"\
    ,\n    \"name\": \"Placeholder ingredient\",\n    \"stage\": \"External MediaDive\
    \ 4178 generated placeholder\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"interpretation\": \"Not\
    \ an additional reagent; use the actual composition array\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution4178\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4178\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"HCl\\\",\\\
    n                \\\"compound_id\\\": 68,\\n                \\\"solution\\\":\
    \ null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": \\\"25%, 7.7 M\\\",\\n        \
    \        \\\"amount\\\": 10,\\n                \\\"unit\\\": \\\"ml\\\",\\n  \
    \              \\\"g_l\\\": 2.5,\\n                \\\"mmol_l\\\": 68.5683,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The placeholder See source for composition\
    \ is provenance/structure debt, not a quantified ingredient to transfer into the\
    \ medium.\"\n  },\n  {\n    \"decision_id\": \"q73\",\n    \"name\": \"NaOH\"\
    ,\n    \"stage\": \"External MediaDive 5543 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5543\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"NaOH\\\",\\n                \\\"compound_id\\\": 256,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 0.5,\\n                \\\"unit\\\": \\\"g\\\"\
    ,\\n                \\\"g_l\\\": 0.5,\\n                \\\"mmol_l\\\": 12.5009,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence decodes\
    \ to the same provider recipe object. Verification covers the current external\
    \ stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\n\
    \  },\n  {\n    \"decision_id\": \"q74\",\n    \"name\": \"Na2SeO3 x 5 H2O\",\n\
    \    \"stage\": \"External MediaDive 5543 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.003\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"solution5543\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Na2SeO3 x 5 H2O\\\",\\n                \\\"compound_id\\\": 107,\\n  \
    \              \\\"solution\\\": null,\\n                \\\"solution_id\\\":\
    \ null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 3,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.003,\\n                \\\"mmol_l\\\
    \": 0.0114062,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q75\",\n    \"name\": \"Na2WO4 x 2 H2O\",\n\
    \    \"stage\": \"External MediaDive 5543 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.004\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"solution5543\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"Na2WO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 249,\\n   \
    \             \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 4,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.004,\\n                \\\"mmol_l\\\
    \": 0.0121267,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q76\",\n    \"name\": \"Distilled water\"\
    ,\n    \"stage\": \"External MediaDive 5543 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"desired\": {\n      \"value\": \"1\",\n      \"unit\": \"L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution5543\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\",\n\
    \        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q77\",\n    \"name\": \"Provider-declared\
    \ stock volume\",\n    \"stage\": \"External MediaDive 5543 metadata\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": 1000,\n      \"unit\":\
    \ \"ML\",\n      \"basis\": \"Provider declaration\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5543\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5543\",\n        \"source_locator\"\
    : \"$.data.volume\",\n        \"exact_source_quote\": \"\\\"volume\\\": 1000\"\
    ,\n        \"snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"interpretation\": \"This declaration belongs to the external\
    \ stock and must not be treated as a measured receiving-medium volume or automatic\
    \ proof of NBRC stock equivalence.\"\n  },\n  {\n    \"decision_id\": \"q78\"\
    ,\n    \"name\": \"Placeholder ingredient\",\n    \"stage\": \"External MediaDive\
    \ 5543 generated placeholder\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"interpretation\": \"Not\
    \ an additional reagent; use the actual composition array\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5543\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5543\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"NaOH\\\",\\\
    n                \\\"compound_id\\\": 256,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 0.5,\\n                \\\"unit\\\": \\\"g\\\",\\n                \\\"g_l\\\
    \": 0.5,\\n                \\\"mmol_l\\\": 12.5009,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"interpretation\": \"The placeholder See source for composition\
    \ is provenance/structure debt, not a quantified ingredient to transfer into the\
    \ medium.\"\n  },\n  {\n    \"decision_id\": \"q79\",\n    \"name\": \"Cyanocobalamine\"\
    ,\n    \"stage\": \"External MediaDive 6241 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Cyanocobalamine\\\",\\n                \\\"compound_id\\\": 847,\\n  \
    \              \\\"solution\\\": null,\\n                \\\"solution_id\\\":\
    \ null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 10,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\
    \": 0.073779,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q80\",\n    \"name\": \"Thiamine HCl\",\n\
    \    \"stage\": \"External MediaDive 6241 stock only\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"Thiamine HCl\\\",\\n                \\\"compound_id\\\": 1207,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 10,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\
    \": 0.296472,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached exact source-hash evidence\
    \ decodes to the same provider recipe object. Verification covers the current\
    \ external stock amount/basis only; source correspondence to NBRC 1005 is separate.\"\
    \n  },\n  {\n    \"decision_id\": \"q81\",\n    \"name\": \"Biotin\",\n    \"\
    stage\": \"External MediaDive 6241 stock only\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"desired\": {\n      \"value\": 200,\n      \"unit\"\
    : \"MICROGRAM\",\n      \"basis\": \"External 100 mL stock\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution6241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"Biotin\\\"\
    ,\\n                \\\"compound_id\\\": 46,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 200,\\n                \\\"unit\\\": \\\"\\\\u03bcg\\\",\\n              \
    \  \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\n             \
    \   \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"The exact external stock prints 200\
    \ micrograms, not 2000 G_PER_L. This external three-vitamin stock still is not\
    \ the NBRC ten-vitamin mixture.\"\n  },\n  {\n    \"decision_id\": \"q82\",\n\
    \    \"name\": \"Distilled water\",\n    \"stage\": \"External MediaDive 6241\
    \ stock only\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"PERCENT_V_V\"\n \
    \       }\n      }\n    ],\n    \"desired\": {\n      \"make_up_to\": 100,\n \
    \     \"unit\": \"ML\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 100,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      },\n      {\n        \"source_key\": \"solution6241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"source_locator\"\
    : \"$.data.steps[0].step\",\n        \"exact_source_quote\": \"Make up to 100\
    \ ml with distilled water.\",\n        \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"The provider explicitly says make\
    \ up to 100 mL. Its water field and 100 mL declared volume do not support 1000%\
    \ v/v.\"\n  },\n  {\n    \"decision_id\": \"q83\",\n    \"name\": \"Provider-declared\
    \ stock volume\",\n    \"stage\": \"External MediaDive 6241 metadata\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\",\n     \
    \   \"field_path\": \"preparation_notes\",\n        \"stored\": \"Make up to 100\
    \ ml with distilled water.\\n\\nOriginal volume: 100 mL\"\n      }\n    ],\n \
    \   \"desired\": {\n      \"value\": 100,\n      \"unit\": \"ML\",\n      \"basis\"\
    : \"Provider declaration\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 100\",\n        \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"This declaration belongs to the external\
    \ stock and must not be treated as a measured receiving-medium volume or automatic\
    \ proof of NBRC stock equivalence.\"\n  },\n  {\n    \"decision_id\": \"q84\"\
    ,\n    \"name\": \"Placeholder ingredient\",\n    \"stage\": \"External MediaDive\
    \ 6241 generated placeholder\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"interpretation\": \"Not\
    \ an additional reagent; use the actual composition array\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution6241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"Cyanocobalamine\\\
    \",\\n                \\\"compound_id\\\": 847,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 10,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\": 0.073779,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The placeholder See source for composition\
    \ is provenance/structure debt, not a quantified ingredient to transfer into the\
    \ medium.\"\n  },\n  {\n    \"decision_id\": \"q85\",\n    \"name\": \"SL-10 zinc\
    \ identity comparison\",\n    \"stage\": \"NBRC stock versus linked 4178\",\n\
    \    \"decision\": \"conflict\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"solutions[0].term\",\n        \"stored\": {\n   \
    \       \"id\": \"mediadive.solution:4178\",\n          \"label\": \"Trace element\
    \ solution SL-10\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"solutions[0].term\",\n        \"stored\": {\n   \
    \       \"id\": \"mediadive.solution:4178\",\n          \"label\": \"Trace element\
    \ solution SL-10\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"NBRC_ZnCl2\"\
    : {\n        \"value\": 7,\n        \"unit\": \"MG\"\n      },\n      \"linked_4178_ZnCl2\"\
    : {\n        \"value\": 70,\n        \"unit\": \"MG\"\n      }\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1005\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 25:  |  |  | ZnCl 2 | 7 |\
    \ mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">ZnCl<sub>2</sub></td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">7</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">ZnCl<sub>2</sub></td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">7</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"togoM1787original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1787\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 7,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"b053bfd607409733d149e8f5c1d4eccb7c66d480ccec57ee5ae9312b8919276f\"\
    \n      },\n      {\n        \"source_key\": \"solution4178\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/4178\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"ZnCl2\\\"\
    ,\\n                \\\"compound_id\\\": 64,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 70,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.07,\\n                \\\"mmol_l\\\": 0.513573,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"interpretation\": \"The tenfold zinc difference is explicit.\
    \ Similar names and matching other rows do not authenticate this linkage.\"\n\
    \  },\n  {\n    \"decision_id\": \"q86\",\n    \"name\": \"Vitamin mixture identity\
    \ comparison\",\n    \"stage\": \"NBRC stock versus linked 6241\",\n    \"decision\"\
    : \"conflict\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml\"\
    ,\n        \"field_path\": \"solutions[2].term\",\n        \"stored\": {\n   \
    \       \"id\": \"mediadive.solution:6241\",\n          \"label\": \"Vitamin solution\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml\"\
    ,\n        \"field_path\": \"solutions[2].term\",\n        \"stored\": {\n   \
    \       \"id\": \"mediadive.solution:6241\",\n          \"label\": \"Vitamin solution\"\
    \n        }\n      }\n    ],\n    \"desired\": {\n      \"NBRC\": \"Ten vitamin\
    \ species in 1 L stock water\",\n      \"linked_6241\": \"Three vitamin species,\
    \ make up to 100 mL\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"nbrc1005\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\"\
    ,\n        \"source_locator\": \"NBRC 1005 HTML row 43:  |  |  | Biotin | 2 |\
    \ mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Biotin</td>\\n<td align=\\\"right\\\
    \" width=\\\"20%\\\">2</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\\
    n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Biotin</td>\\r\\n<td align=\\\"right\\\" width=\\\"20%\\\"\
    >2</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\n \
    \     },\n      {\n        \"source_key\": \"nbrc1005\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\",\n\
    \        \"source_locator\": \"NBRC 1005 HTML row 49:  |  |  | Ca-pantothenate\
    \ | 5 | mg\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Ca-pantothenate</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">5</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >mg</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Ca-pantothenate</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">5</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">mg</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1005\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1005\",\n\
    \        \"source_locator\": \"NBRC 1005 HTML row 53:  |  |  | Distilled water\
    \ | 1 | L\",\n        \"exact_source_quote\": \"<tr>\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    n<td width=\\\"5%\\\">&nbsp;</td>\\n<td width=\\\"5%\\\">&nbsp;</td>\\n<td colspan=\\\
    \"2\\\" align=\\\"left\\\" width=\\\"50%\\\">Distilled water</td>\\n<td align=\\\
    \"right\\\" width=\\\"20%\\\">1</td>\\n<td align=\\\"left\\\" width=\\\"15%\\\"\
    >L</td>\\n</tr>\",\n        \"snapshot_sha256\": \"fb739fc225eb9bb274a42d3b2ff7f31cf378e8e32894610a4ef578d8525e43f4\"\
    ,\n        \"quotation_normalization\": \"Raw HTML CRLF line breaks normalized\
    \ to LF; original byte-literal row separately preserved.\",\n        \"raw_bytes_quote\"\
    : \"<tr>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td width=\\\"5%\\\">&nbsp;</td>\\\
    r\\n<td width=\\\"5%\\\">&nbsp;</td>\\r\\n<td colspan=\\\"2\\\" align=\\\"left\\\
    \" width=\\\"50%\\\">Distilled water</td>\\r\\n<td align=\\\"right\\\" width=\\\
    \"20%\\\">1</td>\\r\\n<td align=\\\"left\\\" width=\\\"15%\\\">L</td>\\r\\n</tr>\"\
    \n      },\n      {\n        \"source_key\": \"solution6241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"Cyanocobalamine\\\
    \",\\n                \\\"compound_id\\\": 847,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 10,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\": 0.073779,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\n     \
    \ },\n      {\n        \"source_key\": \"solution6241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"Thiamine HCl\\\
    \",\\n                \\\"compound_id\\\": 1207,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 10,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\": 0.296472,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\n     \
    \ },\n      {\n        \"source_key\": \"solution6241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"Biotin\\\"\
    ,\\n                \\\"compound_id\\\": 46,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 200,\\n                \\\"unit\\\": \\\"\\\\u03bcg\\\",\\n              \
    \  \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\n             \
    \   \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"The source does not support replacing\
    \ its ten-vitamin mixture with this three-vitamin formulation; do not transfer\
    \ external stock evidence to the medium.\"\n  }\n]"
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 27 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact medium and stock correspondence
  outcome: concern
  summary: The medium is exactly NBRC 1005/TOGO M1787 with one maintained owner. Solutions
    4178 and 6241 resolve as records but their formulas differ from the named source
    stocks. Solution 5543 agrees with the four Se/W rows; that correspondence does
    not repair dose units or attach evidence to the medium.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - api-4178
  - api-5543
  - api-6241
  - quantity-inventory
- assessment_id: grounding
  area: grounding
  topic: Chemical structures versus labels and current secondary keys
  outcome: concern
  summary: 160 asserted CHEBI slots were inspected across medium and stock layers.
    Canonical labels agree with nonobsolete OLS records. Cobalt/nickel hydrate and
    calcium-pantothenate counterion/stereo problems remain; CHEBI29032 has no current
    MIM index row. The negative lookup is complete, so it does not itself make this
    review partial.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - grounding-inventory
  - primary
  - chebi29032
  - chebi34887
  - chebi35696
- assessment_id: preparation
  area: completeness
  topic: Selective sterilization and stock procedures
  outcome: concern
  summary: Main preparation, delayed sterile additions, main pH 7.2–7.4 and dispensing
    gas ratio are absent. The sulfide stock alone specifies 121°C/15 min, approximate
    pH 7.3, 2 N sulfuric acid and the distinct yellow-color pH 8 observation. Preserve
    unknown gas/percent bases, doses and other sterilization cycles.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - procedure
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: High-metal, complexity and growth scope
  outcome: concern
  summary: The source names the medium for JS_SRB250Lac but supplies no taxonomic
    accession or independent growth result to add. COMPLEX/UNDEFINED and high_metal
    are local classifications, not primary claims. Current metal code aggregates flat
    ingredient values and uses a corpus percentile; the mis-scoped and misunit quantities
    prevent accepting the flag as a scientifically verified concentration classification.
    No population threshold was recomputed.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - record
  - owner-0
  - primary
  - writer-4
  - writer-5
- assessment_id: history-evidence
  area: provenance
  topic: Historical external claims and current writer boundaries
  outcome: supported
  summary: The fourteen attached amount claims authenticate only their exact external
    stocks. Current source bytes match the cited hashes, and decoded recipe snippets
    match despite indentation normalization. Medium history records prior processing
    but does not prove current scientific correctness or a particular historical matching
    mechanism.
  target_ids:
  - CultureMech:008354
  evidence_ids:
  - stock-history
  - record
  - owner-0
findings:
- finding_id: f1
  issue_key: culturemech.008354.wrong-stock-correspondence
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Two resolved stock links select different formulations
  description: Both layers link their NBRC SL-10 to solution 4178 despite 7 versus
    70 mg zinc, and their ten-vitamin stock to three-vitamin solution 6241. These
    are observed formula mismatches, not assertions about the historical matching
    algorithm. Existing external evidence cannot validate the links.
  target_ids:
  - CultureMech:008354
  field_paths:
  - solutions[0].term
  - solutions[2].term
  evidence_ids:
  - primary
  - provider
  - api-4178
  - api-6241
  - quantity-inventory
  - stock-history
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  issue_key: culturemech.008354.flattened-stock-quantities
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Main and stock quantities lose units and stage boundaries
  description: Five distinct water inputs are collapsed to 1093 G_PER_L; stock milligrams
    and liquid milliliter doses are stored as G_PER_L alongside basal ingredients.
    Source resazurin 0.5 g is literal and is not an identified thousandfold error.
    The complete per-stage inventory supplies exact values without assuming measured
    final volume.
  target_ids:
  - CultureMech:008354
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  issue_key: culturemech.008354.hydrate-pantothenate-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Supplied hydrates and calcium pantothenate are misgrounded
  description: CoCl2·6H2O and NiCl2·6H2O are represented by anhydrous structures.
    Calcium pantothenate is assigned an R-pantothenate anion that omits calcium and
    asserts stereochemistry absent from the source. These form problems are separate
    from the current MIM lookup gap.
  target_ids:
  - CultureMech:008354
  field_paths:
  - ingredients[17].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - ingredients[29].term
  - ingredients[29].mediaingredientmech_chebi_term
  evidence_ids:
  - grounding-inventory
  - chebi35696
  - chebi34887
  - chebi29032
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  issue_key: culturemech.008354.current-secondary-gap
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Asserted pantothenate secondary key is absent from the current index
  description: Exact inspection of the pinned complete MIM index found no CHEBI29032
    rows. Its primary OLS term exists; that does not establish asserted secondary
    membership. No unavailable check or historical correspondence is inferred from
    this completed negative lookup.
  target_ids:
  - CultureMech:008354
  field_paths:
  - ingredients[29].mediaingredientmech_chebi_term
  evidence_ids:
  - grounding-inventory
  - chebi29032
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  issue_key: culturemech.008354.missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Required anaerobic and stock preparation is absent
  description: The records lack the main selective-sterilization sequence and the
    distinct neutralized-sulfide procedure. Main pH, gas handling and stock-specific
    cycle/acid conditions must retain their separate scopes and literal ambiguities.
  target_ids:
  - CultureMech:008354
  field_paths:
  - preparation_steps
  - ph_range
  - solutions[3]
  evidence_ids:
  - procedure
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.008354.unverified-classification
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: High-metal classification depends on unreconciled quantities
  description: Both records assert high_metal despite flattened stock quantities and
    unit errors. The current writer is a corpus-relative numerical classifier, not
    source evidence; its existence does not prove historical execution or justify
    a true/false replacement without a corrected analysis.
  target_ids:
  - CultureMech:008354
  field_paths:
  - high_metal
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - writer-4
  - writer-5
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  description: Replace or qualify the incompatible links using exact NBRC stock identities;
    preserve 5543 correspondence separately and retain external stock evidence only
    in its original layer.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008354
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  description: Restore the basal recipe, four stock recipes and receiving doses with
    source units/bases, retain the literal resazurin amount and attach exact per-layer
    evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008354
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  description: Correct confirmed hydrate/counterion mismatches with verified source-specific
    identifiers; preserve unresolved pantothenate stereochemistry without inventing
    a racemate or replacement ID.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008354
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  description: Resolve or remove the unsupported current secondary assertion through
    the maintained mapping workflow; do not create a guessed historical MIM identifier.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008354
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
  description: Add exact source-scoped preparation and evidence; retain unknown cycles,
    percentage bases, titration doses and the separate pH/color statements.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008354
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
- action_id: a6
  description: Reassess classification after quantity and stock corrections, preserving
    the method and comparison population; keep strain naming separate from demonstrated
    growth.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008354
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml
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
- All substantive medium and stock source identities are available. Failed optional
  alternate-provider retrievals remain in the bound catalog and are not treated as
  missing primary evidence.
- No current negative lookup establishes historical MIM validity or invalidity. No
  legacy identifier is asserted in the inspected medium or stock layers.
- Source resazurin is 0.5 g. Main and stock water amounts, percentage/molarity labels,
  sulfide pH/color observations and undefined final volume are preserved without typical-recipe
  substitutions.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-037
- generated-medium
```
