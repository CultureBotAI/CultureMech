# Source and formulation review: artficial_freshwater_medium_i (CultureMech:002297)

- Review: 20261021T172807Z-culturemech-002297-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T17:21:20Z
- Finished UTC: 2026-10-21T17:28:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM 1124 recipe and its three explicitly linked parent stock sections resolve this freshwater formulation. Both local layers convert solution doses into mass concentrations, flatten undiluted iron, trace and selenite/tungstate stocks, and leave three vitamin stocks empty. Basal amounts also use an undocumented final-volume normalization. Preparation preserves some gas and vessel detail but loses stock placement and source-specific sterilization. Nickel hexahydrate is grounded to anhydrous nickel chloride. Required current primary evidence is available; the failed MediaDive API request is retained as an optional provenance limitation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 306; batch 031 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty task batches contain 300 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 303 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002297 | data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml | generated | artficial_freshwater_medium_i |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002297 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002297 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch031/306/strict.tsv |
| validate-terms | passed | True | CultureMech:002297 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002297 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002297 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ1124api | unavailable | False | CultureMech:002297 | The optional current MediaDive J1124 API returned HTTP 503. Exact JCM 1124 and all linked primary stock sections are available; historical API byte equality is not established. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002297.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary chemical identifiers

grounding: concern. Targets: CultureMech:002297.

23 distinct primary/current-secondary IDs resolve to nonobsolete terms; exact stored/canonical labels are recorded separately in each term evidence item. Target direct-ingredient linkage is 23/23 primary (100.00%) and 23/23 current CHEBI-based secondary (100.00%), on a 0–100 linkage scale, not an accuracy score. Current secondary keys without pinned index rows: []. Legacy slot count 0 is separate and does not enter that current-key claim. Supplied-form correspondence is assessed separately.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002297.

19 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact freshwater source and bounded stock links

identity: supported. Targets: CultureMech:002297.

The sole maintained owner and generated target have the same stable ID and exact JCM 1124 accession. The source explicitly links JCM 187 iron/trace, JCM 403 three vitamin stocks and JCM 431 selenite/tungstate. Similar marine/brackish formulations are not substitutes. The MediaDive namespace describes the JCM source identity; inaccessible current API bytes do not authenticate historical payload equality.

### Defined liquid and biological scope

scope: supported. Targets: CultureMech:002297.

The fully resolved source has chemically specified components and no agar or complex nutrient, compatible with DEFINED/DEFINED/LIQUID. Missing local stock detail is a representation defect, not evidence that the source is undefined. Catalogue title, category and generic cultivation application do not establish an organism, growth condition optimum or performance claim.

### Explicit hydrates and vitamin stereochemical boundaries

grounding: concern. Targets: CultureMech:002297.

The trace source explicitly supplies NiCl2·6H2O, whereas CHEBI:34887 is anhydrous nickel chloride. Other asserted hydrate structures were checked separately. The missing JCM 403 stock explicitly uses DL-calcium pantothenate; the D-specific CHEBI:31345 in a context parent is not transferable proof. Parent-only legacy IDs, including the calcium pantothenate legacy link within the transferred vitamin composition, do not authenticate historical membership or a proposed new grounding. No replacement ID is guessed.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002297.

50 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "KH2PO4",
    "decision": "correct",
    "source_stage": "JCM 1124 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.197239",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.197239",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[0], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt; &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore the literal batch amount and original unit with the 960 ml basal-water context. The stored rounded G_PER_L normalization is not authenticated by a declared measured final volume. Do not silently replace batch grams or milligrams by grams per liter."
  },
  {
    "decision_id": "q2",
    "label": "NH4Cl",
    "decision": "correct",
    "source_stage": "JCM 1124 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.246548",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.246548",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[1], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore the literal batch amount and original unit with the 960 ml basal-water context. The stored rounded G_PER_L normalization is not authenticated by a declared measured final volume. Do not silently replace batch grams or milligrams by grams per liter."
  },
  {
    "decision_id": "q3",
    "label": "KCl",
    "decision": "correct",
    "source_stage": "JCM 1124 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.295858",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.295858",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[2], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore the literal batch amount and original unit with the 960 ml basal-water context. The stored rounded G_PER_L normalization is not authenticated by a declared measured final volume. Do not silently replace batch grams or milligrams by grams per liter."
  },
  {
    "decision_id": "q4",
    "label": "NaCl",
    "decision": "correct",
    "source_stage": "JCM 1124 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.93097",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.93097",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[3], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore the literal batch amount and original unit with the 960 ml basal-water context. The stored rounded G_PER_L normalization is not authenticated by a declared measured final volume. Do not silently replace batch grams or milligrams by grams per liter."
  },
  {
    "decision_id": "q5",
    "label": "Na2SO4",
    "decision": "correct",
    "source_stage": "JCM 1124 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.38067",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.38067",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[4], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore the literal batch amount and original unit with the 960 ml basal-water context. The stored rounded G_PER_L normalization is not authenticated by a declared measured final volume. Do not silently replace batch grams or milligrams by grams per liter."
  },
  {
    "decision_id": "q6",
    "label": "Resazurin",
    "decision": "correct",
    "source_stage": "JCM 1124 basal batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.000986193",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.000986193",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[8], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore the literal batch amount and original unit with the 960 ml basal-water context. The stored rounded G_PER_L normalization is not authenticated by a declared measured final volume. Do not silently replace batch grams or milligrams by grams per liter."
  },
  {
    "decision_id": "q7",
    "label": "NaHCO3 stock strength and dose",
    "decision": "correct",
    "source_stage": "Post-cooling stocks or separately late sulfide addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[10], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution*                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "This source row gives a solution strength and liquid addition, not a neat-compound mass. Preserve the printed percentage or molarity and ml dose separately. Percent basis is not stated. Only the late sulfide row is explicitly dosed per liter in the following preparation context; do not infer measured final volume for the earlier additions."
  },
  {
    "decision_id": "q8",
    "label": "MgCl2 x 6 H2O stock strength and dose",
    "decision": "correct",
    "source_stage": "Post-cooling stocks or separately late sulfide addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[11], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1 M MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O solution                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "This source row gives a solution strength and liquid addition, not a neat-compound mass. Preserve the printed percentage or molarity and ml dose separately. Percent basis is not stated. Only the late sulfide row is explicitly dosed per liter in the following preparation context; do not infer measured final volume for the earlier additions."
  },
  {
    "decision_id": "q9",
    "label": "CaCl2 x 2 H2O stock strength and dose",
    "decision": "correct",
    "source_stage": "Post-cooling stocks or separately late sulfide addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[12], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1 M CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O solution                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "This source row gives a solution strength and liquid addition, not a neat-compound mass. Preserve the printed percentage or molarity and ml dose separately. Percent basis is not stated. Only the late sulfide row is explicitly dosed per liter in the following preparation context; do not infer measured final volume for the earlier additions."
  },
  {
    "decision_id": "q10",
    "label": "Fructose stock strength and dose",
    "decision": "correct",
    "source_stage": "Post-cooling stocks or separately late sulfide addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1 M Fructose solution*                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "This source row gives a solution strength and liquid addition, not a neat-compound mass. Preserve the printed percentage or molarity and ml dose separately. Percent basis is not stated. Only the late sulfide row is explicitly dosed per liter in the following preparation context; do not infer measured final volume for the earlier additions."
  },
  {
    "decision_id": "q11",
    "label": "Na2S x 9 H2O stock strength and dose",
    "decision": "correct",
    "source_stage": "Post-cooling stocks or separately late sulfide addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[17], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "This source row gives a solution strength and liquid addition, not a neat-compound mass. Preserve the printed percentage or molarity and ml dose separately. Percent basis is not stated. Only the late sulfide row is explicitly dosed per liter in the following preparation context; do not infer measured final volume for the earlier additions."
  },
  {
    "decision_id": "q12",
    "label": "Vitamin solution (see Medium No. 403)",
    "decision": "correct",
    "source_stage": "Three separate filter-sterilized vitamin additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[13], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)*                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "The source adds 1 ml of this distinct stock. The local 1 G_PER_L and empty composition do not represent that dose or formulation. Restore exact named stock scope without importing its parent basal recipe."
  },
  {
    "decision_id": "q13",
    "label": "Thiamine solution (see Medium No. 403)",
    "decision": "correct",
    "source_stage": "Three separate filter-sterilized vitamin additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[14], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)*               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "The source adds 1 ml of this distinct stock. The local 1 G_PER_L and empty composition do not represent that dose or formulation. Restore exact named stock scope without importing its parent basal recipe."
  },
  {
    "decision_id": "q14",
    "label": "Vitamin B12 solution (see Medium No. 403)",
    "decision": "correct",
    "source_stage": "Three separate filter-sterilized vitamin additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[15], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)*      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "The source adds 1 ml of this distinct stock. The local 1 G_PER_L and empty composition do not represent that dose or formulation. Restore exact named stock scope without importing its parent basal recipe."
  },
  {
    "decision_id": "q15",
    "label": "HCl within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron-stock acid component",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q16",
    "label": "FeCl2 x 4 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[17], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q17",
    "label": "ZnCl2 within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[19], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q18",
    "label": "MnCl2 x 4 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[20], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q19",
    "label": "H3BO3 within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[21], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q20",
    "label": "CoCl2 x 6 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[22], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q21",
    "label": "CuCl2 x 2 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[23], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q22",
    "label": "NiCl2 x 6 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[24], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q23",
    "label": "Na2MoO4 x 2 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[25], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q24",
    "label": "NaOH within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Exact source HTML table row[29], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaOH                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q25",
    "label": "Na2SeO3 x 5 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Exact source HTML table row[30], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;3&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q26",
    "label": "Na2WO4 x 2 H2O within stock",
    "decision": "correct",
    "source_stage": "JCM 187 iron/trace or JCM 431 selenite-tungstate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.008",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.008",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Exact source HTML table row[31], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50"
      }
    ],
    "interpretation": "Retain the literal quantity and unit inside its named stock. A full-strength stock amount is not the final-medium concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml dose; converting it to 2.5 g requires an unstated percent basis or density and is not justified."
  },
  {
    "decision_id": "q27",
    "label": "Iron stock addition",
    "decision": "add",
    "source_stage": "Basal stock additions",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[5], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore this explicit 1 ml addition as a named stock with its own composition and preparation context. It is absent from the three vitamin-only local solution descriptors."
  },
  {
    "decision_id": "q28",
    "label": "Trace stock addition",
    "decision": "add",
    "source_stage": "Basal stock additions",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[6], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore this explicit 1 ml addition as a named stock with its own composition and preparation context. It is absent from the three vitamin-only local solution descriptors."
  },
  {
    "decision_id": "q29",
    "label": "Selenite-tungstate stock addition",
    "decision": "add",
    "source_stage": "Basal stock additions",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[7], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Selenite tungstate solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\"&gt;431&lt;/a&gt;)      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Restore this explicit 1 ml addition as a named stock with its own composition and preparation context. It is absent from the three vitamin-only local solution descriptors."
  },
  {
    "decision_id": "q30",
    "label": "Basal water",
    "decision": "add",
    "source_stage": "Main or named-stock water",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Preserve this water amount in its own preparation stage. Do not sum full stock preparations into the receiving medium or assume a measured final volume."
  },
  {
    "decision_id": "q31",
    "label": "Iron-stock water",
    "decision": "add",
    "source_stage": "Main or named-stock water",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[18], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Preserve this water amount in its own preparation stage. Do not sum full stock preparations into the receiving medium or assume a measured final volume."
  },
  {
    "decision_id": "q32",
    "label": "Trace-stock water",
    "decision": "add",
    "source_stage": "Main or named-stock water",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Exact source HTML table row[26], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804"
      }
    ],
    "interpretation": "Preserve this water amount in its own preparation stage. Do not sum full stock preparations into the receiving medium or assume a measured final volume."
  },
  {
    "decision_id": "q33",
    "label": "Selenite-tungstate stock water",
    "decision": "add",
    "source_stage": "Main or named-stock water",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50"
      }
    ],
    "interpretation": "Preserve this water amount in its own preparation stage. Do not sum full stock preparations into the receiving medium or assume a measured final volume."
  },
  {
    "decision_id": "q34",
    "label": "JCM 403 18 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[18], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;4.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q35",
    "label": "JCM 403 19 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[19], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q36",
    "label": "JCM 403 20 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[20], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q37",
    "label": "JCM 403 21 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[21], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; DL-Calcium pantothenate                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q38",
    "label": "JCM 403 22 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[22], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q39",
    "label": "JCM 403 23 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[23], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium phosphate buffer (10 mM, pH 7.1)               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q40",
    "label": "JCM 403 24 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[24], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q41",
    "label": "JCM 403 25 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[25], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium phosphate buffer (25 mM, pH 3.4)               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q42",
    "label": "JCM 403 26 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[26], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q43",
    "label": "JCM 403 27 vitamin-stock component",
    "decision": "add",
    "source_stage": "JCM 403 three stock preparations",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "Exact source HTML table row[27], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61"
      }
    ],
    "interpretation": "Restore the exact component in its own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride forms."
  },
  {
    "decision_id": "q44",
    "label": "Main volume boundary",
    "decision": "not_quantified",
    "source_stage": "Final-medium basis",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[10], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution*                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[17], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Listed liquid inputs are not an explicit measured final-volume declaration. Keep the late sulfide 5 ml per liter instruction separate; do not invent a denominator from all water and stock preparations."
  },
  {
    "decision_id": "q45",
    "label": "Basal gas ratio",
    "decision": "evidence_only",
    "source_stage": "Basal atmosphere",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, add the following solutions (autoclaved or *filter-sterilized):"
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere. After cooling, add the following solutions (autoclaved or *filter-sterilized):"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Initial autoclaving atmosphere",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v)",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      }
    ],
    "interpretation": "The stored 4:1 v/v nitrogen/carbon dioxide atmosphere matches. Attach exact evidence, without converting it to dissolved gas concentration."
  },
  {
    "decision_id": "q46",
    "label": "Vessel example and same gas",
    "decision": "evidence_only",
    "source_stage": "Vessel example",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Aseptically and anaerobically, distribute the medium into culture vessels under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with butyl rubber stoppers. Prior to use, add per liter the following solution to reduce the medium (autoclaved and stored under N2):"
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Aseptically and anaerobically, distribute the medium into culture vessels under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with butyl rubber stoppers. Prior to use, add per liter the following solution to reduce the medium (autoclaved and stored under N2):"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Distribution paragraph",
        "exact_source_quote": "e.g., 20 ml in 60 ml-serum bottles",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Distribution paragraph",
        "exact_source_quote": "under the same gas mixture",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      }
    ],
    "interpretation": "Preserve the explicitly illustrative 20 ml in 60 ml bottle volumes and same 4:1 gas context; neither is a mandatory batch size."
  },
  {
    "decision_id": "q47",
    "label": "Late sulfide dose basis",
    "decision": "correct",
    "source_stage": "Late sulfide",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Aseptically and anaerobically, distribute the medium into culture vessels under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with butyl rubber stoppers. Prior to use, add per liter the following solution to reduce the medium (autoclaved and stored under N2):"
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Aseptically and anaerobically, distribute the medium into culture vessels under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with butyl rubber stoppers. Prior to use, add per liter the following solution to reduce the medium (autoclaved and stored under N2):"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Late-addition paragraph",
        "exact_source_quote": "Prior to use, add per liter the following solution",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Exact source HTML table row[17], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4"
      }
    ],
    "interpretation": "Keep 5 ml per liter of the 5% stock as the explicit late reducing addition. The numeric preparation context survives, but the ingredient mass unit and missing stock linkage do not."
  },
  {
    "decision_id": "q48",
    "label": "Stock nitrogen purity",
    "decision": "not_quantified",
    "source_stage": "Sulfide-stock handling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Aseptically and anaerobically, distribute the medium into culture vessels under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with butyl rubber stoppers. Prior to use, add per liter the following solution to reduce the medium (autoclaved and stored under N2):"
      },
      {
        "input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Aseptically and anaerobically, distribute the medium into culture vessels under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with butyl rubber stoppers. Prior to use, add per liter the following solution to reduce the medium (autoclaved and stored under N2):"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Late sulfide paragraph",
        "exact_source_quote": "autoclaved and stored under N 2",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      }
    ],
    "interpretation": "The source says nitrogen atmosphere but does not quantify purity or gas amount. Do not change this to 100% nitrogen."
  },
  {
    "decision_id": "q49",
    "label": "Default cycle and stock-specific exceptions",
    "decision": "add",
    "source_stage": "Preparation completeness",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      },
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Post-cooling additions",
        "exact_source_quote": "autoclaved or *filter-sterilized",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      }
    ],
    "interpretation": "Retain the source-default 121°C/15 min scope and distinguish starred bicarbonate, vitamins and fructose filtration from unstarred autoclaved stocks. The local combined AUTOCLAVE steps do not enumerate these stage assignments."
  },
  {
    "decision_id": "q50",
    "label": "Main pH and adjustment reagent",
    "decision": "not_quantified",
    "source_stage": "Source limits",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm1124",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124",
        "source_locator": "Main preparation",
        "exact_source_quote": "Mix components thoroughly and autoclave",
        "snapshot_sha256": "eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4",
        "parsed_text_sha256": "4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f"
      }
    ],
    "interpretation": "No main target pH, titration reagent amount, temperature of growth or gas pressure is supplied by this exact source. Do not import parent stock pH or parent cultivation conditions."
  }
]

### Exact sole maintained input

ownership: supported. Targets: CultureMech:002297.

The normalized artficial_freshwater_medium_i owner owns correction. Entire target/owner fields and histories and exact current writer contexts were read. Generated data are not a curation surface.

## Findings

### f1: Stock concentrations and addition volumes are flattened into main masses

blocker / open / confirmed; issue key: cm002297-stock-stage.

Both layers flatten iron, trace and selenite/tungstate stock quantities and represent several liquid doses as G_PER_L. Three vitamin solutions remain empty 1 G_PER_L stubs. Main and stock waters and the basal 1 ml stock doses are absent, so the formulation cannot be reconstructed faithfully.

### f2: Nickel hexahydrate is grounded to anhydrous nickel chloride

major / open / confirmed; issue key: cm002297-nickel.

The supplied NiCl2·6H2O is explicit in JCM 187, but the asserted CHEBI:34887 structure omits six waters. Correct canonical labels alone cannot repair this chemical-form mismatch.

### f3: Sterilization and buffered-stock details are incompletely represented

major / open / confirmed; issue key: cm002297-procedure.

Gas ratio and vessel example survive, but starred filtration versus stock autoclaving, default cycle and separate buffered vitamin preparations are missing from their proper stages. Parent pH and gas conditions must not be substituted.

### f4: Amount and preparation claims lack same-layer source evidence

minor / open / confirmed; issue key: cm002297-claim-evidence.

Import and migration histories identify processing events but do not substantiate units, dose basis or stock transfer. All currently stored concentration claims lack exact attached source excerpts.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the exact source stock hierarchy, original dose units and batch contexts in the maintained owner, with narrow claim evidence. Resolve percent basis and final-volume limits explicitly; do not infer density or sum full stocks.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the source hexahydrate and choose only a verified matching primary/secondary identity. Do not derive mass or molarity using anhydrous formula weight.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach source-specific preparation and named-stock evidence while preserving conditional scope, default exceptions and distinct buffer pH values.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve historical bytes and add narrow source/version/stage evidence after separately authorized correction; regenerate the derived record from its owner.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch031/306/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch031/306/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml:1:id: CultureMech:002297<br>./data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml:1:id: CultureMech:002297<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch031/source-preflight-bound/306/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 54 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124; Complete exact medium 1124 table, post-cooling additions and late per-liter sulfide paragraph | supports | JCM 1124 distinguishes basal batch amounts, stock concentrations, addition volumes and the explicitly per-liter late sulfide dose. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; FeCl2 solution and Trace element solution subsections only | supports | Only the explicitly linked stock subsection transfers. Parent basal formulations, gases, pressure, organisms, sulfur and other vitamins do not transfer. |
| jcm403 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403; Vitamin, Thiamine and Vitamin B12 solution subsections only | supports | Only the explicitly linked stock subsection transfers. Parent basal formulations, gases, pressure, organisms, sulfur and other vitamins do not transfer. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; Selenite-tungstate solution subsection only | supports | Only the explicitly linked stock subsection transfers. Parent basal formulations, gases, pressure, organisms, sulfur and other vitamins do not transfer. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Stored labels: ['disodium selenite pentahydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:17883 resolves to hydrogen chloride. Stored labels: ['hydrogen chloride']. Exact label correspondence is separate from source chemical-form support. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:26710 resolves to sodium chloride. Stored labels: ['sodium chloride']. Exact label correspondence is separate from source chemical-form support. |
| chebi28757 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28757; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:28757 resolves to fructose. Stored labels: ['fructose']. Exact label correspondence is separate from source chemical-form support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31206 resolves to ammonium chloride. Stored labels: ['ammonium chloride']. Exact label correspondence is separate from source chemical-form support. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Stored labels: ['sodium hydrogencarbonate']. Exact label correspondence is separate from source chemical-form support. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32145 resolves to sodium hydroxide. Stored labels: ['sodium hydroxide']. Exact label correspondence is separate from source chemical-form support. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32149 resolves to sodium sulfate. Stored labels: ['sodium sulfate']. Exact label correspondence is separate from source chemical-form support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32588 resolves to potassium chloride. Stored labels: ['potassium chloride']. Exact label correspondence is separate from source chemical-form support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:33118 resolves to boric acid. Stored labels: ['boric acid']. Exact label correspondence is separate from source chemical-form support. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:34887 resolves to nickel dichloride. Stored labels: ['nickel dichloride']. Exact label correspondence is separate from source chemical-form support. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:49976 resolves to zinc dichloride. Stored labels: ['zinc dichloride']. Exact label correspondence is separate from source chemical-form support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Stored labels: ['cobalt chloride hexahydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Stored labels: ['potassium dihydrogen phosphate']. Exact label correspondence is separate from source chemical-form support. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Stored labels: ['sodium tungstate dihydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Stored labels: ['sodium molybdate dihydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Stored labels: ['sodium sulfide nonahydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Stored labels: ['calcium chloride dihydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Stored labels: ['iron dichloride tetrahydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Stored labels: ['copper(II) chloride dihydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Stored labels: ['magnesium dichloride hexahydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Stored labels: ['manganese(II) chloride tetrahydrate']. Exact label correspondence is separate from source chemical-form support. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:8806 resolves to Resazurin. Stored labels: ['Resazurin']. Exact label correspondence is separate from source chemical-form support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent snapshot metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28757": [{"label": "Fructose", "match_type": "preferred_term", "identifier": "CHEBI:28757", "preferred_term": "Fructose", "ontology_id": "CHEBI:28757", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": []} |
| history-metadata | data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml; data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml", "events": 9, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, solution migration and formulation-aware merge code are context only. The recorded migration and merge events are historical evidence; current code was not executed or used to infer which implementation produced the older fields. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, solution migration and formulation-aware merge code are context only. The recorded migration and merge events are historical evidence; current code was not executed or used to infer which implementation produced the older fields. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, solution migration and formulation-aware merge code are context only. The recorded migration and merge events are historical evidence; current code was not executed or used to infer which implementation produced the older fields. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch031/306/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| mediadiveJ1124api-attempt | https://mediadive.dsmz.de/rest/medium/J1124; Preserved exact public retrieval result | context_only | The optional current MediaDive J1124 API returned HTTP 503. Exact JCM 1124 and all linked primary stock sections are available; historical API byte equality is not established. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The optional current MediaDive J1124 API returned HTTP 503. Exact JCM 1124 and all linked primary stock sections are available; historical API byte equality is not established.
- Completed current-primary review. Parent-only legacy identifiers do not authenticate transferred stock identity; the source stock compositions themselves are independently available. Main final volume, unqualified percentage bases and nitrogen purity remain unresolved source limits. No source recipe or stored review was changed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172807Z-culturemech-002297-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: artficial_freshwater_medium_i (CultureMech:002297)'
started_at: '2026-10-21T17:21:20Z'
finished_at: '2026-10-21T17:28:07Z'
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
summary: The exact JCM 1124 recipe and its three explicitly linked parent stock sections
  resolve this freshwater formulation. Both local layers convert solution doses into
  mass concentrations, flatten undiluted iron, trace and selenite/tungstate stocks,
  and leave three vitamin stocks empty. Basal amounts also use an undocumented final-volume
  normalization. Preparation preserves some gas and vessel detail but loses stock
  placement and source-specific sterilization. Nickel hexahydrate is grounded to anhydrous
  nickel chloride. Required current primary evidence is available; the failed MediaDive
  API request is retained as an optional provenance limitation.
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
  - path: data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
    sha256: 476bd0f6f3a2789906637b65054bfb48e9abd36bfcd5e2b676acc3cc84bc1040
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
    sha256: 1a5fece2649cec85c820476a37a0a59968f828451a6bc2da7cafe3675cfa298e
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/bacterial/artficial_freshwater_medium_i.yaml.md
    sha256: 435d520aa0c79eeb2037a2fa17100d9a444e666e7c1c18574db9b4b78f37b559
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 306; batch 031 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty task batches contain
    300 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 303 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002297
targets:
- target_id: CultureMech:002297
  path: data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  label: artficial_freshwater_medium_i
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch031/306/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch031/306/strict.tsv"
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002297
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
  - CultureMech:002297
- check_id: mediadiveJ1124api-source-access
  name: 'Exact source content access: mediadiveJ1124api'
  required: false
  status: unavailable
  summary: The optional current MediaDive J1124 API returned HTTP 503. Exact JCM 1124
    and all linked primary stock sections are available; historical API byte equality
    is not established.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - mediadiveJ1124api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:53.669118Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch031/306/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:54.940795Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch031/306/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:56.406504Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:57.332116Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T17:28:06Z'
  support: supports
  summary: './data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml:1:id: CultureMech:002297

    ./data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml:1:id: CultureMech:002297

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/source-preflight-bound/306/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T17:28:06Z'
  support: supports
  summary: 54 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2bb008e94227358fc16f612ac21a03f89428c412be881b6ae1258cb4bd406c71
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124
  locator: Complete exact medium 1124 table, post-cooling additions and late per-liter
    sulfide paragraph
  accessed_at: '2026-10-21T17:05:55.362009Z'
  support: supports
  summary: JCM 1124 distinguishes basal batch amounts, stock concentrations, addition
    volumes and the explicitly per-liter late sulfide dose.
  quote: Prior to use, add per liter the following solution
  snapshot_sha256: eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: FeCl2 solution and Trace element solution subsections only
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: Only the explicitly linked stock subsection transfers. Parent basal formulations,
    gases, pressure, organisms, sulfur and other vitamins do not transfer.
  quote: 'FeCl 2 solution: 25% HCl (7.7 M) 10.0 ml'
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm403
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403
  locator: Vitamin, Thiamine and Vitamin B12 solution subsections only
  accessed_at: '2026-10-21T09:49:56.169277Z'
  support: supports
  summary: Only the explicitly linked stock subsection transfers. Parent basal formulations,
    gases, pressure, organisms, sulfur and other vitamins do not transfer.
  quote: DL-Calcium pantothenate 5.0 mg
  snapshot_sha256: b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: Selenite-tungstate solution subsection only
  accessed_at: '2026-10-21T12:23:19.260180Z'
  support: supports
  summary: Only the explicitly linked stock subsection transfers. Parent basal formulations,
    gases, pressure, organisms, sulfur and other vitamins do not transfer.
  quote: 'Selenite-tungstate solution: NaOH 0.4 g'
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: 'CHEBI:131361 resolves to disodium selenite pentahydrate. Stored labels:
    [''disodium selenite pentahydrate'']. Exact label correspondence is separate from
    source chemical-form support.'
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: 'CHEBI:17883 resolves to hydrogen chloride. Stored labels: [''hydrogen
    chloride'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: 'CHEBI:26710 resolves to sodium chloride. Stored labels: [''sodium chloride''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi28757
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28757
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T09:49:55.504136Z'
  support: supports
  summary: 'CHEBI:28757 resolves to fructose. Stored labels: [''fructose'']. Exact
    label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 76d05e03e00004437e5231331dcf49803064128e054d8be9f70019d2efe44105
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: 'CHEBI:31206 resolves to ammonium chloride. Stored labels: [''ammonium
    chloride'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: 'CHEBI:32139 resolves to sodium hydrogencarbonate. Stored labels: [''sodium
    hydrogencarbonate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: 'CHEBI:32145 resolves to sodium hydroxide. Stored labels: [''sodium hydroxide''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: 'CHEBI:32149 resolves to sodium sulfate. Stored labels: [''sodium sulfate''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: 'CHEBI:32588 resolves to potassium chloride. Stored labels: [''potassium
    chloride'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: 'CHEBI:33118 resolves to boric acid. Stored labels: [''boric acid'']. Exact
    label correspondence is separate from source chemical-form support.'
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: 'CHEBI:34887 resolves to nickel dichloride. Stored labels: [''nickel dichloride''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: 'CHEBI:49976 resolves to zinc dichloride. Stored labels: [''zinc dichloride''].
    Exact label correspondence is separate from source chemical-form support.'
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: 'CHEBI:53503 resolves to cobalt chloride hexahydrate. Stored labels: [''cobalt
    chloride hexahydrate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: 'CHEBI:63036 resolves to potassium dihydrogen phosphate. Stored labels:
    [''potassium dihydrogen phosphate'']. Exact label correspondence is separate from
    source chemical-form support.'
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: 'CHEBI:63939 resolves to sodium tungstate dihydrate. Stored labels: [''sodium
    tungstate dihydrate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: 'CHEBI:75213 resolves to sodium molybdate dihydrate. Stored labels: [''sodium
    molybdate dihydrate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: 'CHEBI:76209 resolves to sodium sulfide nonahydrate. Stored labels: [''sodium
    sulfide nonahydrate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: 'CHEBI:86158 resolves to calcium chloride dihydrate. Stored labels: [''calcium
    chloride dihydrate'']. Exact label correspondence is separate from source chemical-form
    support.'
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: 'CHEBI:86249 resolves to iron dichloride tetrahydrate. Stored labels: [''iron
    dichloride tetrahydrate'']. Exact label correspondence is separate from source
    chemical-form support.'
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: 'CHEBI:86318 resolves to copper(II) chloride dihydrate. Stored labels:
    [''copper(II) chloride dihydrate'']. Exact label correspondence is separate from
    source chemical-form support.'
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: 'CHEBI:86345 resolves to magnesium dichloride hexahydrate. Stored labels:
    [''magnesium dichloride hexahydrate'']. Exact label correspondence is separate
    from source chemical-form support.'
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: 'CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Stored labels:
    [''manganese(II) chloride tetrahydrate'']. Exact label correspondence is separate
    from source chemical-form support.'
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: 'CHEBI:8806 resolves to Resazurin. Stored labels: [''Resazurin'']. Exact
    label correspondence is separate from source chemical-form support.'
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent snapshot metadata
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id":
    "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883":
    [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883",
    "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28757": [{"label":
    "Fructose", "match_type": "preferred_term", "identifier": "CHEBI:28757", "preferred_term":
    "Fructose", "ontology_id": "CHEBI:28757", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label":
    "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term":
    "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213":
    [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label":
    "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249",
    "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806":
    [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806",
    "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml; data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml", "events":
    9, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: Current importer, solution migration and formulation-aware merge code are
    context only. The recorded migration and merge events are historical evidence;
    current code was not executed or used to infer which implementation produced the
    older fields.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: Current importer, solution migration and formulation-aware merge code are
    context only. The recorded migration and merge events are historical evidence;
    current code was not executed or used to infer which implementation produced the
    older fields.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: Current importer, solution migration and formulation-aware merge code are
    context only. The recorded migration and merge events are historical evidence;
    current code was not executed or used to infer which implementation produced the
    older fields.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/306/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T17:28:06Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 6aa0dbc22d87db3bf4e4b5592c443e95584f7d8c77aa839b4f533dae74534252
- evidence_id: mediadiveJ1124api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1124
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:05:52.815162Z'
  support: context_only
  summary: The optional current MediaDive J1124 API returned HTTP 503. Exact JCM 1124
    and all linked primary stock sections are available; historical API byte equality
    is not established.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary chemical identifiers
  outcome: concern
  summary: '23 distinct primary/current-secondary IDs resolve to nonobsolete terms;
    exact stored/canonical labels are recorded separately in each term evidence item.
    Target direct-ingredient linkage is 23/23 primary (100.00%) and 23/23 current
    CHEBI-based secondary (100.00%), on a 0–100 linkage scale, not an accuracy score.
    Current secondary keys without pinned index rows: []. Legacy slot count 0 is separate
    and does not enter that current-key claim. Supplied-form correspondence is assessed
    separately.'
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi17883
  - chebi26710
  - chebi28757
  - chebi31206
  - chebi32139
  - chebi32145
  - chebi32149
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 19 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact freshwater source and bounded stock links
  outcome: supported
  summary: The sole maintained owner and generated target have the same stable ID
    and exact JCM 1124 accession. The source explicitly links JCM 187 iron/trace,
    JCM 403 three vitamin stocks and JCM 431 selenite/tungstate. Similar marine/brackish
    formulations are not substitutes. The MediaDive namespace describes the JCM source
    identity; inaccessible current API bytes do not authenticate historical payload
    equality.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - record
  - owner-0
  - primary
  - jcm187
  - jcm403
  - jcm431
- assessment_id: classification
  area: scope
  topic: Defined liquid and biological scope
  outcome: supported
  summary: The fully resolved source has chemically specified components and no agar
    or complex nutrient, compatible with DEFINED/DEFINED/LIQUID. Missing local stock
    detail is a representation defect, not evidence that the source is undefined.
    Catalogue title, category and generic cultivation application do not establish
    an organism, growth condition optimum or performance claim.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: forms
  area: grounding
  topic: Explicit hydrates and vitamin stereochemical boundaries
  outcome: concern
  summary: The trace source explicitly supplies NiCl2·6H2O, whereas CHEBI:34887 is
    anhydrous nickel chloride. Other asserted hydrate structures were checked separately.
    The missing JCM 403 stock explicitly uses DL-calcium pantothenate; the D-specific
    CHEBI:31345 in a context parent is not transferable proof. Parent-only legacy
    IDs, including the calcium pantothenate legacy link within the transferred vitamin
    composition, do not authenticate historical membership or a proposed new grounding.
    No replacement ID is guessed.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - jcm187
  - jcm403
  - chebi34887
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 50 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"KH2PO4\",\n   \
    \ \"decision\": \"correct\",\n    \"source_stage\": \"JCM 1124 basal batch\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.197239\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.197239\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[0], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>\
    \ </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[9], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the literal batch amount\
    \ and original unit with the 960 ml basal-water context. The stored rounded G_PER_L\
    \ normalization is not authenticated by a declared measured final volume. Do not\
    \ silently replace batch grams or milligrams by grams per liter.\"\n  },\n  {\n\
    \    \"decision_id\": \"q2\",\n    \"label\": \"NH4Cl\",\n    \"decision\": \"\
    correct\",\n    \"source_stage\": \"JCM 1124 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.246548\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.246548\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[1], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl\
    \                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[9], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the literal batch amount\
    \ and original unit with the 960 ml basal-water context. The stored rounded G_PER_L\
    \ normalization is not authenticated by a declared measured final volume. Do not\
    \ silently replace batch grams or milligrams by grams per liter.\"\n  },\n  {\n\
    \    \"decision_id\": \"q3\",\n    \"label\": \"KCl\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"JCM 1124 basal batch\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.295858\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.295858\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[2], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KCl           \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[9], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the literal batch amount\
    \ and original unit with the 960 ml basal-water context. The stored rounded G_PER_L\
    \ normalization is not authenticated by a declared measured final volume. Do not\
    \ silently replace batch grams or milligrams by grams per liter.\"\n  },\n  {\n\
    \    \"decision_id\": \"q4\",\n    \"label\": \"NaCl\",\n    \"decision\": \"\
    correct\",\n    \"source_stage\": \"JCM 1124 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.93097\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.93097\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[3], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaCl          \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[9], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the literal batch amount\
    \ and original unit with the 960 ml basal-water context. The stored rounded G_PER_L\
    \ normalization is not authenticated by a declared measured final volume. Do not\
    \ silently replace batch grams or milligrams by grams per liter.\"\n  },\n  {\n\
    \    \"decision_id\": \"q5\",\n    \"label\": \"Na2SO4\",\n    \"decision\": \"\
    correct\",\n    \"source_stage\": \"JCM 1124 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.38067\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.38067\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[4], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[9], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the literal batch amount\
    \ and original unit with the 960 ml basal-water context. The stored rounded G_PER_L\
    \ normalization is not authenticated by a declared measured final volume. Do not\
    \ silently replace batch grams or milligrams by grams per liter.\"\n  },\n  {\n\
    \    \"decision_id\": \"q6\",\n    \"label\": \"Resazurin\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"JCM 1124 basal batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000986193\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000986193\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[8], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Resazurin     \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[9], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the literal batch amount\
    \ and original unit with the 960 ml basal-water context. The stored rounded G_PER_L\
    \ normalization is not authenticated by a declared measured final volume. Do not\
    \ silently replace batch grams or milligrams by grams per liter.\"\n  },\n  {\n\
    \    \"decision_id\": \"q7\",\n    \"label\": \"NaHCO3 stock strength and dose\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Post-cooling stocks\
    \ or separately late sulfide addition\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[10], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub>\
    \ solution*                                </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"This source row gives a solution\
    \ strength and liquid addition, not a neat-compound mass. Preserve the printed\
    \ percentage or molarity and ml dose separately. Percent basis is not stated.\
    \ Only the late sulfide row is explicitly dosed per liter in the following preparation\
    \ context; do not infer measured final volume for the earlier additions.\"\n \
    \ },\n  {\n    \"decision_id\": \"q8\",\n    \"label\": \"MgCl2 x 6 H2O stock\
    \ strength and dose\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"Post-cooling stocks or separately late sulfide addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[11], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 1 M MgCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \ solution                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"This source row gives a solution\
    \ strength and liquid addition, not a neat-compound mass. Preserve the printed\
    \ percentage or molarity and ml dose separately. Percent basis is not stated.\
    \ Only the late sulfide row is explicitly dosed per liter in the following preparation\
    \ context; do not infer measured final volume for the earlier additions.\"\n \
    \ },\n  {\n    \"decision_id\": \"q9\",\n    \"label\": \"CaCl2 x 2 H2O stock\
    \ strength and dose\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"Post-cooling stocks or separately late sulfide addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[12], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 1 M CaCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \ solution                     </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"This source row gives a solution\
    \ strength and liquid addition, not a neat-compound mass. Preserve the printed\
    \ percentage or molarity and ml dose separately. Percent basis is not stated.\
    \ Only the late sulfide row is explicitly dosed per liter in the following preparation\
    \ context; do not infer measured final volume for the earlier additions.\"\n \
    \ },\n  {\n    \"decision_id\": \"q10\",\n    \"label\": \"Fructose stock strength\
    \ and dose\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Post-cooling\
    \ stocks or separately late sulfide addition\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[16], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 1 M Fructose solution*\
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"This source row gives a solution\
    \ strength and liquid addition, not a neat-compound mass. Preserve the printed\
    \ percentage or molarity and ml dose separately. Percent basis is not stated.\
    \ Only the late sulfide row is explicitly dosed per liter in the following preparation\
    \ context; do not infer measured final volume for the earlier additions.\"\n \
    \ },\n  {\n    \"decision_id\": \"q11\",\n    \"label\": \"Na2S x 9 H2O stock\
    \ strength and dose\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"Post-cooling stocks or separately late sulfide addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[17], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O\
    \ solution                      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This source row gives a solution strength\
    \ and liquid addition, not a neat-compound mass. Preserve the printed percentage\
    \ or molarity and ml dose separately. Percent basis is not stated. Only the late\
    \ sulfide row is explicitly dosed per liter in the following preparation context;\
    \ do not infer measured final volume for the earlier additions.\"\n  },\n  {\n\
    \    \"decision_id\": \"q12\",\n    \"label\": \"Vitamin solution (see Medium\
    \ No. 403)\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"Three separate\
    \ filter-sterilized vitamin additions\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[13], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Vitamin solution\
    \ (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=403\\\">403</a>)*   \
    \             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 1 ml of this distinct\
    \ stock. The local 1 G_PER_L and empty composition do not represent that dose\
    \ or formulation. Restore exact named stock scope without importing its parent\
    \ basal recipe.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"label\": \"\
    Thiamine solution (see Medium No. 403)\",\n    \"decision\": \"correct\",\n  \
    \  \"source_stage\": \"Three separate filter-sterilized vitamin additions\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[14], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Thiamine solution\
    \ (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=403\\\">403</a>)*   \
    \            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 1 ml of this distinct\
    \ stock. The local 1 G_PER_L and empty composition do not represent that dose\
    \ or formulation. Restore exact named stock scope without importing its parent\
    \ basal recipe.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"label\": \"\
    Vitamin B12 solution (see Medium No. 403)\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"Three separate filter-sterilized vitamin additions\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[15], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>\
    \ solution (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=403\\\">403</a>)*\
    \      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 1 ml of this distinct\
    \ stock. The local 1 G_PER_L and empty composition do not represent that dose\
    \ or formulation. Restore exact named stock scope without importing its parent\
    \ basal recipe.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"label\": \"\
    HCl within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    JCM 187 iron-stock acid component\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\",\n\
    \        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[16], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> 25% HCl (7.7 M)\
    \                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"label\"\
    : \"FeCl2 x 4 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[17], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"label\"\
    : \"ZnCl2 within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[19], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>\
    \                                               </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"label\"\
    : \"MnCl2 x 4 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[20], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O\
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"label\"\
    : \"H3BO3 within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[21], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>\
    \                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"label\"\
    : \"CoCl2 x 6 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[22], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"label\"\
    : \"CuCl2 x 2 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[23], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"label\"\
    : \"NiCl2 x 6 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[24], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"label\"\
    : \"Na2MoO4 x 2 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[25], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O\
    \                            </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"label\"\
    : \"NaOH within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[29], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaOH          \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"label\"\
    : \"Na2SeO3 x 5 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[30], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>SeO<sub>3</sub>&#183;5H<sub>2</sub>O\
    \                             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"label\"\
    : \"Na2WO4 x 2 H2O within stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM 187 iron/trace or JCM 431 selenite-tungstate stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.008\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.008\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[31], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>WO<sub>4</sub>&#183;2H<sub>2</sub>O\
    \                              </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the literal quantity and unit\
    \ inside its named stock. A full-strength stock amount is not the final-medium\
    \ concentration. HCl additionally has an explicit 25% (7.7 M) stock and 10 ml\
    \ dose; converting it to 2.5 g requires an unstated percent basis or density and\
    \ is not justified.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"label\"\
    : \"Iron stock addition\",\n    \"decision\": \"add\",\n    \"source_stage\":\
    \ \"Basal stock additions\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[5], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution (see Medium No. <a href=\\\"\
    /cgi-bin/jcm/jcm_grmd?GRMD=187\\\">187</a>)                </TD><TD WIDTH=15%\
    \ ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore this explicit 1 ml addition\
    \ as a named stock with its own composition and preparation context. It is absent\
    \ from the three vitamin-only local solution descriptors.\"\n  },\n  {\n    \"\
    decision_id\": \"q28\",\n    \"label\": \"Trace stock addition\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"Basal stock additions\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1124\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[6], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Trace element solution\
    \ (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=187\\\">187</a>)    \
    \       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore this explicit 1 ml addition\
    \ as a named stock with its own composition and preparation context. It is absent\
    \ from the three vitamin-only local solution descriptors.\"\n  },\n  {\n    \"\
    decision_id\": \"q29\",\n    \"label\": \"Selenite-tungstate stock addition\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Basal stock additions\"\
    ,\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[7], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Selenite tungstate\
    \ solution (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=431\\\">431</a>)\
    \      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore this explicit 1 ml addition\
    \ as a named stock with its own composition and preparation context. It is absent\
    \ from the three vitamin-only local solution descriptors.\"\n  },\n  {\n    \"\
    decision_id\": \"q30\",\n    \"label\": \"Basal water\",\n    \"decision\": \"\
    add\",\n    \"source_stage\": \"Main or named-stock water\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1124\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[9], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this water amount in its\
    \ own preparation stage. Do not sum full stock preparations into the receiving\
    \ medium or assume a measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q31\",\n    \"label\": \"Iron-stock water\",\n    \"decision\": \"add\",\n\
    \    \"source_stage\": \"Main or named-stock water\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[18], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this water amount in its\
    \ own preparation stage. Do not sum full stock preparations into the receiving\
    \ medium or assume a measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q32\",\n    \"label\": \"Trace-stock water\",\n    \"decision\": \"add\",\n\
    \    \"source_stage\": \"Main or named-stock water\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[26], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this water amount in its\
    \ own preparation stage. Do not sum full stock preparations into the receiving\
    \ medium or assume a measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q33\",\n    \"label\": \"Selenite-tungstate stock water\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"Main or named-stock water\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[32], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L        </TD></TR>\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this water amount in its\
    \ own preparation stage. Do not sum full stock preparations into the receiving\
    \ medium or assume a measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q34\",\n    \"label\": \"JCM 403 18 vitamin-stock component\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"JCM 403 three stock preparations\",\n    \"\
    local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm403\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[18], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic\
    \ acid                             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;4.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"label\": \"JCM 403\
    \ 19 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[19], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Biotin                                                \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"label\": \"JCM 403\
    \ 20 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[20], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Nicotinic acid                                        \
    \ </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"label\": \"JCM 403\
    \ 21 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[21], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> DL-Calcium pantothenate                               \
    \ </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"label\": \"JCM 403\
    \ 22 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[22], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q39\",\n    \"label\": \"JCM 403\
    \ 23 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[23], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Sodium phosphate buffer (10 mM, pH 7.1)               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n    \"label\": \"JCM 403\
    \ 24 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[24], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                     </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q41\",\n    \"label\": \"JCM 403\
    \ 25 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[25], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Sodium phosphate buffer (25 mM, pH 3.4)               </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n    \"label\": \"JCM 403\
    \ 26 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[26], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                     \
    \                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact component in its\
    \ own named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs.\
    \ The vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4;\
    \ neither is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q43\",\n    \"label\": \"JCM 403\
    \ 27 vitamin-stock component\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"JCM 403 three stock preparations\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm403\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\",\n        \"source_locator\"\
    : \"Exact source HTML table row[27], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Restore the exact component in its own\
    \ named vitamin, thiamine or B12 stock, retaining original mg/100 ml inputs. The\
    \ vitamin buffer is 10 mM at pH 7.1; the thiamine buffer is 25 mM at pH 3.4; neither\
    \ is a main-medium pH. Preserve DL-calcium pantothenate and explicit hydrochloride\
    \ forms.\"\n  },\n  {\n    \"decision_id\": \"q44\",\n    \"label\": \"Main volume\
    \ boundary\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"\
    Final-medium basis\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[9], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[10], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*                        \
    \        </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[17], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution      \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Listed liquid inputs are not an explicit\
    \ measured final-volume declaration. Keep the late sulfide 5 ml per liter instruction\
    \ separate; do not invent a denominator from all water and stock preparations.\"\
    \n  },\n  {\n    \"decision_id\": \"q45\",\n    \"label\": \"Basal gas ratio\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Basal atmosphere\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere.\
    \ After cooling, add the following solutions (autoclaved or *filter-sterilized):\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix components thoroughly and autoclave under a N2-CO2 (4:1, v/v) gas atmosphere.\
    \ After cooling, add the following solutions (autoclaved or *filter-sterilized):\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1124\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Initial autoclaving atmosphere\",\n        \"\
    exact_source_quote\": \"N 2 -CO 2 (4:1, v/v)\",\n        \"snapshot_sha256\":\
    \ \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\",\n    \
    \    \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored 4:1 v/v nitrogen/carbon\
    \ dioxide atmosphere matches. Attach exact evidence, without converting it to\
    \ dissolved gas concentration.\"\n  },\n  {\n    \"decision_id\": \"q46\",\n \
    \   \"label\": \"Vessel example and same gas\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"Vessel example\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Aseptically and anaerobically, distribute the medium into culture vessels\
    \ under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with\
    \ butyl rubber stoppers. Prior to use, add per liter the following solution to\
    \ reduce the medium (autoclaved and stored under N2):\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Aseptically and anaerobically, distribute the medium into culture vessels\
    \ under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with\
    \ butyl rubber stoppers. Prior to use, add per liter the following solution to\
    \ reduce the medium (autoclaved and stored under N2):\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1124\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Distribution paragraph\",\n        \"exact_source_quote\"\
    : \"e.g., 20 ml in 60 ml-serum bottles\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    ,\n        \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Distribution paragraph\",\n        \"exact_source_quote\": \"under the same\
    \ gas mixture\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    ,\n        \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the explicitly illustrative\
    \ 20 ml in 60 ml bottle volumes and same 4:1 gas context; neither is a mandatory\
    \ batch size.\"\n  },\n  {\n    \"decision_id\": \"q47\",\n    \"label\": \"Late\
    \ sulfide dose basis\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Late sulfide\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Aseptically and anaerobically, distribute the medium into culture vessels\
    \ under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with\
    \ butyl rubber stoppers. Prior to use, add per liter the following solution to\
    \ reduce the medium (autoclaved and stored under N2):\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Aseptically and anaerobically, distribute the medium into culture vessels\
    \ under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with\
    \ butyl rubber stoppers. Prior to use, add per liter the following solution to\
    \ reduce the medium (autoclaved and stored under N2):\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1124\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Late-addition paragraph\",\n        \"exact_source_quote\"\
    : \"Prior to use, add per liter the following solution\",\n        \"snapshot_sha256\"\
    : \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\",\n    \
    \    \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Exact source HTML table row[17], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O solution      \
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>\",\n        \"snapshot_sha256\"\
    : \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Keep 5 ml per liter of the 5% stock as\
    \ the explicit late reducing addition. The numeric preparation context survives,\
    \ but the ingredient mass unit and missing stock linkage do not.\"\n  },\n  {\n\
    \    \"decision_id\": \"q48\",\n    \"label\": \"Stock nitrogen purity\",\n  \
    \  \"decision\": \"not_quantified\",\n    \"source_stage\": \"Sulfide-stock handling\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Aseptically and anaerobically, distribute the medium into culture vessels\
    \ under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with\
    \ butyl rubber stoppers. Prior to use, add per liter the following solution to\
    \ reduce the medium (autoclaved and stored under N2):\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Aseptically and anaerobically, distribute the medium into culture vessels\
    \ under the same gas mixture (e.g., 20 ml in 60 ml-serum bottles) and seal with\
    \ butyl rubber stoppers. Prior to use, add per liter the following solution to\
    \ reduce the medium (autoclaved and stored under N2):\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1124\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\"\
    ,\n        \"source_locator\": \"Late sulfide paragraph\",\n        \"exact_source_quote\"\
    : \"autoclaved and stored under N 2\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    ,\n        \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      }\n    ],\n    \"interpretation\": \"The source says nitrogen atmosphere\
    \ but does not quantify purity or gas amount. Do not change this to 100% nitrogen.\"\
    \n  },\n  {\n    \"decision_id\": \"q49\",\n    \"label\": \"Default cycle and\
    \ stock-specific exceptions\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Preparation completeness\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Page default\",\n        \"exact_source_quote\": \"Unless otherwise stated,\
    \ sterilize media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\"\
    : \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\",\n    \
    \    \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      },\n      {\n        \"source_key\": \"jcm1124\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n        \"source_locator\"\
    : \"Post-cooling additions\",\n        \"exact_source_quote\": \"autoclaved or\
    \ *filter-sterilized\",\n        \"snapshot_sha256\": \"eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\"\
    ,\n        \"parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the source-default 121°C/15\
    \ min scope and distinguish starred bicarbonate, vitamins and fructose filtration\
    \ from unstarred autoclaved stocks. The local combined AUTOCLAVE steps do not\
    \ enumerate these stage assignments.\"\n  },\n  {\n    \"decision_id\": \"q50\"\
    ,\n    \"label\": \"Main pH and adjustment reagent\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Source limits\",\n    \"local_fields\": [],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1124\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1124\",\n \
    \       \"source_locator\": \"Main preparation\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave\",\n        \"snapshot_sha256\": \"\
    eb1a2235a29e4bfe848a98d9be544046042fe59727b6fa3c1202d3a8087015a4\",\n        \"\
    parsed_text_sha256\": \"4b595fa04b97c196f56b790621aa9f3ca8f2b6c5662448bf08b0aeaff86d573f\"\
    \n      }\n    ],\n    \"interpretation\": \"No main target pH, titration reagent\
    \ amount, temperature of growth or gas pressure is supplied by this exact source.\
    \ Do not import parent stock pH or parent cultivation conditions.\"\n  }\n]"
- assessment_id: ownership
  area: ownership
  topic: Exact sole maintained input
  outcome: supported
  summary: The normalized artficial_freshwater_medium_i owner owns correction. Entire
    target/owner fields and histories and exact current writer contexts were read.
    Generated data are not a curation surface.
  target_ids:
  - CultureMech:002297
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: cm002297-stock-stage
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock concentrations and addition volumes are flattened into main masses
  description: Both layers flatten iron, trace and selenite/tungstate stock quantities
    and represent several liquid doses as G_PER_L. Three vitamin solutions remain
    empty 1 G_PER_L stubs. Main and stock waters and the basal 1 ml stock doses are
    absent, so the formulation cannot be reconstructed faithfully.
  target_ids:
  - CultureMech:002297
  field_paths:
  - ingredients[*].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - jcm187
  - jcm403
  - jcm431
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  issue_key: cm002297-nickel
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel chloride
  description: The supplied NiCl2·6H2O is explicit in JCM 187, but the asserted CHEBI:34887
    structure omits six waters. Correct canonical labels alone cannot repair this
    chemical-form mismatch.
  target_ids:
  - CultureMech:002297
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - jcm187
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  issue_key: cm002297-procedure
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Sterilization and buffered-stock details are incompletely represented
  description: Gas ratio and vessel example survive, but starred filtration versus
    stock autoclaving, default cycle and separate buffered vitamin preparations are
    missing from their proper stages. Parent pH and gas conditions must not be substituted.
  target_ids:
  - CultureMech:002297
  field_paths:
  - preparation_steps
  - solutions[*].composition
  evidence_ids:
  - primary
  - jcm403
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  issue_key: cm002297-claim-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Amount and preparation claims lack same-layer source evidence
  description: Import and migration histories identify processing events but do not
    substantiate units, dose basis or stock transfer. All currently stored concentration
    claims lack exact attached source excerpts.
  target_ids:
  - CultureMech:002297
  field_paths:
  - ingredients[*].evidence
  - solutions[*].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  description: Reconstruct the exact source stock hierarchy, original dose units and
    batch contexts in the maintained owner, with narrow claim evidence. Resolve percent
    basis and final-volume limits explicitly; do not infer density or sum full stocks.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002297
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  description: Preserve the source hexahydrate and choose only a verified matching
    primary/secondary identity. Do not derive mass or molarity using anhydrous formula
    weight.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002297
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  description: Attach source-specific preparation and named-stock evidence while preserving
    conditional scope, default exceptions and distinct buffer pH values.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002297
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
  description: Preserve historical bytes and add narrow source/version/stage evidence
    after separately authorized correction; regenerate the derived record from its
    owner.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002297
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml
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
- The optional current MediaDive J1124 API returned HTTP 503. Exact JCM 1124 and all
  linked primary stock sections are available; historical API byte equality is not
  established.
- Completed current-primary review. Parent-only legacy identifiers do not authenticate
  transferred stock identity; the source stock compositions themselves are independently
  available. Main final volume, unqualified percentage bases and nitrogen purity remain
  unresolved source limits. No source recipe or stored review was changed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-031
- generated-medium
```
