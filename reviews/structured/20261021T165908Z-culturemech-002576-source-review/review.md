# Source and formulation review: archaeoglobus_profundus_medium (CultureMech:002576)

- Review: 20261021T165908Z-culturemech-002576-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:49:43Z
- Finished UTC: 2026-10-21T16:59:08Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact JCM 214 and the linked JCM 151 Trace minerals subsection define separate main and stock preparations. Both local layers flatten stock amounts and sum magnesium, calcium and sodium across stages, omit the 10 ml stock dose and water contexts, and fail to state a justified final-concentration basis. Most source procedure text survives, but AUTOCLAVE labels a step whose main-medium method is filtration, and trace pH lacks stock placement. Manganese sulfate hydration is unspecified by the source and must not be resolved as anhydrous by label alone. All required primary and current identifier evidence is available.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 300; batch 030 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-nine task batches contain 290 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 293 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002576 | data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml | generated | archaeoglobus_profundus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002576 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002576 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch030/300/strict.tsv |
| validate-terms | passed | True | CultureMech:002576 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002576 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002576 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ214api | unavailable | False | CultureMech:002576 | Optional mediadiveJ214api request returned 503. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred. |
| Exact source content access: jcm151 | unavailable | False | CultureMech:002576 | Optional jcm151 request returned 404. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred. |
| Exact source content access: mediadiveJ214retry | unavailable | False | CultureMech:002576 | Optional mediadiveJ214retry request returned 503. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002576.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary chemical identifiers

grounding: concern. Targets: CultureMech:002576.

23 distinct primary/current-secondary IDs have matching nonobsolete labels. Target direct-ingredient linkage is 23/24 primary (95.83%) and 22/24 current CHEBI-based secondary (91.67%), on a 0–100 linkage scale, not an accuracy score. Current secondary keys without pinned index rows: []. Legacy slot count 0 is separate and does not enter that current-key claim. Supplied-form correspondence is assessed separately.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002576.

17 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact collection medium and source-linked stock

identity: supported. Targets: CultureMech:002576.

JCM214 identifies the exact named main medium and explicitly links JCM151 for Trace minerals. The successful linked historical-route capture supplies that stock; a failed guessed modern route does not establish source absence. The sole normalized JCM owner is resolved by exact merge provenance and stable ID.

### Mixture and biological boundaries

scope: supported. Targets: CultureMech:002576.

Liquid/complex/undefined is compatible with salts plus yeast extract and no agar. Title and archaea filing are source catalogue context, not growth or taxonomic evidence. No organism/strain-specific performance, optimum or paper assertion is added.

### Explicit and unresolved supplied-form boundaries

grounding: concern. Targets: CultureMech:002576.

Source MnSO4·xH2O leaves hydration number unspecified, whereas CHEBI:86360 is anhydrous manganese sulfate. Preserve the hydrated-source qualification and do not invent x or a molarity. Source AlK(SO4)2 does not state a hydrate count, so a dodecahydrate must not be imported from a different Wolin formula. Explicit iron/ammonium nickel hexahydrates, magnesium/calcium hydrates and source Resazurin were checked against their captured structures; neutral resazurin is not contradicted by this source wording.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002576.

44 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "KCl",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.34",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.34",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[0], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.34&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q2",
    "label": "MgCl2 x 6 H2O",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[1], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;4.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q3",
    "label": "MgSO4 x 7 H2O",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.45",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.45",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[2], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.45&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis. The local value also combines main and undiluted trace-stock contributions; separate those stages rather than retaining a sum."
  },
  {
    "decision_id": "q4",
    "label": "NH4Cl",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[3], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q5",
    "label": "CaCl2 x 2 H2O",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.24000000000000002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.24000000000000002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[4], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.14&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis. The local value also combines main and undiluted trace-stock contributions; separate those stages rather than retaining a sum."
  },
  {
    "decision_id": "q6",
    "label": "K2HPO4",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.14",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.14",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[5], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.14&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q7",
    "label": "NaCl",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "19.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "19.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[6], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;18.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis. The local value also combines main and undiluted trace-stock contributions; separate those stages rather than retaining a sum."
  },
  {
    "decision_id": "q8",
    "label": "NaHCO3",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[7], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaHCO&lt;sub&gt;3&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q9",
    "label": "Na2SO4",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.7",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.7",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[8], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.7&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q10",
    "label": "Fe(NH4)2(SO4)2 x 6 H2O",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Fe(NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis. The milligram-to-gram arithmetic is consistent, but that alone does not authenticate a final-medium concentration."
  },
  {
    "decision_id": "q11",
    "label": "(NH4)2Ni(SO4)2 x 6 H2O",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[10], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; (NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;Ni(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis. The milligram-to-gram arithmetic is consistent, but that alone does not authenticate a final-medium concentration."
  },
  {
    "decision_id": "q12",
    "label": "Yeast extract",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[12], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q13",
    "label": "Sodium acetate",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[13], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium acetate                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q14",
    "label": "Resazurin",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[14], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis. The milligram-to-gram arithmetic is consistent, but that alone does not authenticate a final-medium concentration."
  },
  {
    "decision_id": "q15",
    "label": "Na2S x 9 H2O",
    "decision": "correct",
    "source_stage": "JCM214 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[15], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Retain this original main amount/unit with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input sum, not an explicit measured final-volume declaration, especially with separately added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for its basis."
  },
  {
    "decision_id": "q16",
    "label": "Nitrilotriacetic acid trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[20], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nitrilotriacetic acid                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q17",
    "label": "MgSO4 x 7 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.45",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.45",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[21], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q18",
    "label": "MnSO4 x n H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[22], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q19",
    "label": "NaCl trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "19.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "19.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[23], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q20",
    "label": "FeSO4 x 7 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[24], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q21",
    "label": "CoSO4 x 7 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[25], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q22",
    "label": "CaCl2 x 2 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.24000000000000002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.24000000000000002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[26], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q23",
    "label": "ZnSO4 x 7 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[27], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q24",
    "label": "CuSO4 x 5 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[28], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q25",
    "label": "AlK(SO4)2 trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[29], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; AlK(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q26",
    "label": "H3BO3 trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[30], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q27",
    "label": "Na2MoO4 x 2 H2O trace stock",
    "decision": "correct",
    "source_stage": "JCM151 Trace minerals only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[31], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      },
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "This amount belongs to the separate JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium dose. It is not a direct main concentration. Preserve source hydration and original units; do not merge full-strength stock amounts with main ingredients."
  },
  {
    "decision_id": "q28",
    "label": "Trace-stock addition",
    "decision": "add",
    "source_stage": "Main stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[11], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace minerals (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=151\"&gt;151&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Restore the exact 10 ml batch dose and full source-specific Trace minerals composition. Do not substitute parent salt base or another named trace recipe."
  },
  {
    "decision_id": "q29",
    "label": "Main water",
    "decision": "add",
    "source_stage": "Main batch",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Restore source 990 ml main water separately from stock water and later sulfide stock volume."
  },
  {
    "decision_id": "q30",
    "label": "Trace-stock water",
    "decision": "add",
    "source_stage": "Trace stock",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Exact source HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7"
      }
    ],
    "interpretation": "Retain 1 L water only inside the Trace minerals preparation; it is not an extra liter added directly to main medium or an explicit measured final stock volume."
  },
  {
    "decision_id": "q31",
    "label": "Main final volume",
    "decision": "not_quantified",
    "source_stage": "Main final-volume limit",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[11], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace minerals (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=151\"&gt;151&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "Known main water plus trace dose sums to 1000 ml, but the source does not declare measured final volume and later sulfide stock volume is unspecified. Do not derive an authenticated denominator from the sum alone."
  },
  {
    "decision_id": "q32",
    "label": "Initial main pH",
    "decision": "evidence_only",
    "source_stage": "Main pH",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      },
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main preparation initial adjustment",
        "exact_source_quote": "adjust pH to 6.9",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "Stored target pH and preparation value agree; attach exact same-layer evidence without treating it as measured final pH."
  },
  {
    "decision_id": "q33",
    "label": "Conditional main pH readjustment",
    "decision": "evidence_only",
    "source_stage": "Late main pH adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main preparation after sulfide addition",
        "exact_source_quote": "pH to 6.9, if necessary.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "Retain the separately conditional 6.9 readjustment after sulfide addition."
  },
  {
    "decision_id": "q34",
    "label": "Main filtration gas ratio",
    "decision": "evidence_only",
    "source_stage": "Main filtration atmosphere",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main preparation filtration sentence",
        "exact_source_quote": "Sterilize by filtration under H 2 -CO 2 (80:20) gas mixture.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "Retain H2/CO2 80:20 at main filtration; no dissolved gas concentration or unstated ratio basis is inferred."
  },
  {
    "decision_id": "q35",
    "label": "Late-addition atmosphere",
    "decision": "evidence_only",
    "source_stage": "Sulfide addition to main",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main aseptic late-addition sentence",
        "exact_source_quote": "H 2 -CO 2 (80:20) atmosphere",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "Preserve this separate main handling atmosphere."
  },
  {
    "decision_id": "q36",
    "label": "Pressure and gas ratio",
    "decision": "evidence_only",
    "source_stage": "Post-inoculation pressure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main final pressure sentence",
        "exact_source_quote": "to 200 kPa H 2 -CO 2 (80:20).",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "Keep 200 kPa and H2/CO2 80:20. The source does not qualify absolute versus gauge pressure; neither qualifier is invented."
  },
  {
    "decision_id": "q37",
    "label": "Sulfide stock nitrogen",
    "decision": "not_quantified",
    "source_stage": "Sulfide stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Separate sulfide-stock sterilization sentence",
        "exact_source_quote": "autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "N2 atmosphere has no explicit purity percentage, quantity or dissolved concentration; do not infer 100%."
  },
  {
    "decision_id": "q38",
    "label": "Sulfide stock strength and dose",
    "decision": "not_quantified",
    "source_stage": "Separate sulfide stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Sulfide stock sentence",
        "exact_source_quote": "Neutralize Na 2 S·9H 2 O solution",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Exact source HTML table row[15], zero-based document row",
        "exact_source_quote": "&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b"
      }
    ],
    "interpretation": "The exact main source supplies a sulfide mass but no stock percentage, volume or neutralization target. The unrelated parent JCM151 sulfide5% recipe is outside the transferred Trace minerals section."
  },
  {
    "decision_id": "q39",
    "label": "Default autoclave cycle scoped to stock",
    "decision": "add",
    "source_stage": "Source-default cycle and explicit exception",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "JCM214 page default header",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Sulfide-stock sentence",
        "exact_source_quote": "autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "Preserve the page default 121°C/15min only with its unless-otherwise-stated scope and the explicit sulfide-stock autoclaving step. Main medium has an explicit filtration exception, so this is not a main autoclave instruction."
  },
  {
    "decision_id": "q40",
    "label": "Main sterilization action mismatch",
    "decision": "correct",
    "source_stage": "Main versus stock methods",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].action",
        "stored": "AUTOCLAVE"
      },
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].action",
        "stored": "AUTOCLAVE"
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main method",
        "exact_source_quote": "Sterilize by filtration under H 2 -CO 2 (80:20) gas mixture.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      },
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Separate sulfide-stock method",
        "exact_source_quote": "autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "The action AUTOCLAVE does not describe main sterilization. Split or explicitly scope main filtration and separate stock autoclaving while retaining the correct descriptive text."
  },
  {
    "decision_id": "q41",
    "label": "Initial trace pH",
    "decision": "correct",
    "source_stage": "Trace-stock pH",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Trace minerals preparation after stock table",
        "exact_source_quote": "adjust pH to 6.5 with KOH solution.",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
        "parsed_text_sha256": "e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9"
      }
    ],
    "interpretation": "Existing numeric text is correct but needs explicit Trace minerals placement; it must not overwrite main pH6.9."
  },
  {
    "decision_id": "q42",
    "label": "Final trace pH",
    "decision": "correct",
    "source_stage": "Trace-stock pH",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Trace minerals preparation after stock table",
        "exact_source_quote": "Adjust final pH to 7.0.",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
        "parsed_text_sha256": "e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9"
      }
    ],
    "interpretation": "Existing numeric text is correct but needs explicit Trace minerals placement; it must not overwrite main pH6.9."
  },
  {
    "decision_id": "q43",
    "label": "H2SO4 adjustment amount",
    "decision": "not_quantified",
    "source_stage": "Main pH reagent",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20)."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm214",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214",
        "source_locator": "Main initial pH adjustment",
        "exact_source_quote": "with H 2 SO 4 .",
        "snapshot_sha256": "693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b",
        "parsed_text_sha256": "339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68"
      }
    ],
    "interpretation": "The source gives neither sulfuric acid strength nor amount; the pH target alone cannot determine either."
  },
  {
    "decision_id": "q44",
    "label": "KOH adjustment amount",
    "decision": "not_quantified",
    "source_stage": "Trace-stock pH reagent",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
      },
      {
        "input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm151linked",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151",
        "source_locator": "Trace-stock initial pH adjustment",
        "exact_source_quote": "with KOH solution.",
        "snapshot_sha256": "6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7",
        "parsed_text_sha256": "e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9"
      }
    ],
    "interpretation": "No KOH strength or volume is specified. Keep this stock-only and do not fabricate a final main concentration."
  }
]

### Exact sole maintained source

ownership: supported. Targets: CultureMech:002576.

The normalized JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM owner owns correction. Entire target and owner content/history and exact current writers were read. No recipe, history or generated artifact was changed.

## Findings

### f1: Trace-stock ingredients and main concentrations have been combined

blocker / open / confirmed; issue key: cm002576-flattened-stock.

The exact JCM151 Trace minerals composition is flat in both layers. Mg sulfate6.45, calcium0.24000000000000002 and NaCl19 combine main amounts with full-strength stock amounts. The 10ml stock dose and main990ml/stock1L water contexts are absent; the resulting formulation differs materially from the source.

### f2: Action and stock-pH placement obscure the explicit main method

major / open / confirmed; issue key: cm002576-preparation-method.

The main recipe is explicitly filter sterilized, but a combined root step is labelled AUTOCLAVE. Autoclaving belongs to the separate sulfide stock. A second root step contains Trace minerals pH6.5 then7.0 without naming the stock. Main pH6.9, gas ratio and unqualified200kPa text are otherwise retained.

### f3: Unspecified manganese hydrate is represented as anhydrous

major / open / confirmed; issue key: cm002576-hydration-specificity.

The transferred source prints MnSO4·xH2O; current CHEBI:86360 has anhydrous MnSO4 structure. The hydrate count is unavailable in the source, so no exact hydrate ID or molecular-weight conversion can be chosen. Other explicit hydrate labels and neutral Resazurin are not implicated by this finding.

### f4: Supported preparation and ingredient statements lack claim evidence

minor / open / confirmed; issue key: cm002576-evidence.

No attached amount/preparation claim connects the main and trace quantities to their distinct source sections. Historical import and duplicate-cleanup notes cannot authenticate final concentrations or expand the parent-source scope.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the exact source stock and dose, split contributions and preserve original quantities/water stages. Establish the source basis before final-medium concentration conversion; do not transfer unrelated parent ingredients.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Separate or explicitly scope main filtration, sulfide-stock autoclaving and trace-stock pH. Keep the main exception to JCM defaults and avoid inventing pressure qualifiers or stock purity/strength.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the source hydrate qualification and unresolved x, grounding only the justified chemical specificity. Do not infer monohydrate from a different mineral recipe or from a MIM synonym.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach narrow source/version/stage evidence after correction, preserve historical events and regenerate only from separately authorized maintained-input changes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch030/300/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch030/300/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml:1:id: CultureMech:002576<br>./data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml:1:id: CultureMech:002576<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch030/source-preflight-bound/300/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 30 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214; Complete exact JCM214 table and preparation, including default header and explicit main exception | supports | Exact ARCHAEOGLOBUS PROFUNDUS recipe. Main filtration, separately autoclaved sulfide, gas ratios and pressure remain distinct. |
| trace | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Trace minerals table and its following pH paragraph only | supports | The exact link from JCM214 resolves JCM151. Only its Trace minerals subsection transfers; no salt base, sulfur, peptone, citric acid, parent growth conditions or parent sulfide5% context transfers. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Exact label validity is separate from source chemical-form support. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:26710 resolves to sodium chloride. Exact label validity is separate from source chemical-form support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31206 resolves to ammonium chloride. Exact label validity is separate from source chemical-form support. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Exact label validity is separate from source chemical-form support. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Exact label validity is separate from source chemical-form support. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32149 resolves to sodium sulfate. Exact label validity is separate from source chemical-form support. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32588 resolves to potassium chloride. Exact label validity is separate from source chemical-form support. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:32954 resolves to sodium acetate. Exact label validity is separate from source chemical-form support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:33118 resolves to boric acid. Exact label validity is separate from source chemical-form support. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Exact label validity is separate from source chemical-form support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Exact label validity is separate from source chemical-form support. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| chebi76181 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Exact label validity is separate from source chemical-form support. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Exact label validity is separate from source chemical-form support. |
| chebi86149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Exact label validity is separate from source chemical-form support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Exact label validity is separate from source chemical-form support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Exact label validity is separate from source chemical-form support. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86360 resolves to manganese(II) sulfate. Exact label validity is separate from source chemical-form support. |
| chebi86463 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86463; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:86463 resolves to potassium aluminium sulfate. Exact label validity is separate from source chemical-form support. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:8806 resolves to Resazurin. Exact label validity is separate from source chemical-form support. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS ID, canonical label, obsolete flag and supplied-form annotations | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Exact label validity is separate from source chemical-form support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent snapshot metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76181": [{"label": "Fe(NH4)2(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76181", "preferred_term": "Fe(NH4)2(SO4)2 x 6 H2O", "ontology_id": "CHEBI:76181", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86463": [{"label": "AlK(SO4)2", "match_type": "preferred_term", "identifier": "CHEBI:86463", "preferred_term": "AlK(SO4)2", "ontology_id": "CHEBI:86463", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": []} |
| history-metadata | data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml", "events": 8, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, cleanup and merge behavior is scoped context only. Observed cross-stage sums and historical notes are separate from current code, which was not executed or used as a historical replay. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, cleanup and merge behavior is scoped context only. Observed cross-stage sums and historical notes are separate from current code, which was not executed or used as a historical replay. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, cleanup and merge behavior is scoped context only. Observed cross-stage sums and historical notes are separate from current code, which was not executed or used as a historical replay. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch030/300/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| mediadiveJ214api-attempt | https://mediadive.dsmz.de/rest/medium/J214; Preserved exact public retrieval result | context_only | Optional mediadiveJ214api request returned 503. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred. |
| jcm151-attempt | https://jcm.brc.riken.jp/medium/151; Preserved exact public retrieval result | context_only | Optional jcm151 request returned 404. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred. |
| mediadiveJ214retry-attempt | https://mediadive.dsmz.de/rest/medium/J214; Preserved exact public retrieval result | context_only | Optional mediadiveJ214retry request returned 503. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Optional mediadiveJ214api request returned 503. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred.
- Optional jcm151 request returned 404. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred.
- Optional mediadiveJ214retry request returned 503. Exact JCM214 and its actual linked JCM151 route are available, so this failed attempt does not make the required source unavailable. Historical API payload equality is not inferred.
- Completed current-source review. JCM151 transfers only Trace minerals and its following pH paragraph; salt base, sulfur treatment, peptone, parent growth conditions and parent sulfide5% are excluded. Main final volume, pressure gauge/absolute status, sulfide stock strength/dose and manganese hydrate count remain explicitly unresolved.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T165908Z-culturemech-002576-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: archaeoglobus_profundus_medium (CultureMech:002576)'
started_at: '2026-10-21T16:49:43Z'
finished_at: '2026-10-21T16:59:08Z'
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
summary: Exact JCM 214 and the linked JCM 151 Trace minerals subsection define separate
  main and stock preparations. Both local layers flatten stock amounts and sum magnesium,
  calcium and sodium across stages, omit the 10 ml stock dose and water contexts,
  and fail to state a justified final-concentration basis. Most source procedure text
  survives, but AUTOCLAVE labels a step whose main-medium method is filtration, and
  trace pH lacks stock placement. Manganese sulfate hydration is unspecified by the
  source and must not be resolved as anhydrous by label alone. All required primary
  and current identifier evidence is available.
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
  - path: data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
    sha256: f4a5cff52157564a2ebadb61ecadc59e822059f70a2f96a23fc03284c5d407df
    role: target
  - path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
    sha256: b55ce604fa0e5f2b45a81cb53716b2fe9b443239e2fb912e378f102d920f0156
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml.md
    sha256: b872c7f75384f32e731ac5bcf4592c88f11e528e53b110fbbff253ad11f95ec1
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 300; batch 030 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-nine task batches
    contain 290 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 293 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002576
targets:
- target_id: CultureMech:002576
  path: data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  label: archaeoglobus_profundus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch030/300/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch030/300/strict.tsv"
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002576
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
  - CultureMech:002576
- check_id: mediadiveJ214api-source-access
  name: 'Exact source content access: mediadiveJ214api'
  required: false
  status: unavailable
  summary: Optional mediadiveJ214api request returned 503. Exact JCM214 and its actual
    linked JCM151 route are available, so this failed attempt does not make the required
    source unavailable. Historical API payload equality is not inferred.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - mediadiveJ214api-attempt
- check_id: jcm151-source-access
  name: 'Exact source content access: jcm151'
  required: false
  status: unavailable
  summary: Optional jcm151 request returned 404. Exact JCM214 and its actual linked
    JCM151 route are available, so this failed attempt does not make the required
    source unavailable. Historical API payload equality is not inferred.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - jcm151-attempt
- check_id: mediadiveJ214retry-source-access
  name: 'Exact source content access: mediadiveJ214retry'
  required: false
  status: unavailable
  summary: Optional mediadiveJ214retry request returned 503. Exact JCM214 and its
    actual linked JCM151 route are available, so this failed attempt does not make
    the required source unavailable. Historical API payload equality is not inferred.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - mediadiveJ214retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:16.093211Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch030/300/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:18.270171Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch030/300/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:23.010072Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:24.608999Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:59:05Z'
  support: supports
  summary: './data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml:1:id:
    CultureMech:002576

    ./data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml:1:id: CultureMech:002576

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/source-preflight-bound/300/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:59:05Z'
  support: supports
  summary: 30 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 9cdfd090792871876282978b591b4e173ce6d56ea16b44265f5d301ed1482d47
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214
  locator: Complete exact JCM214 table and preparation, including default header and
    explicit main exception
  accessed_at: '2026-10-21T16:34:01.380600Z'
  support: supports
  summary: Exact ARCHAEOGLOBUS PROFUNDUS recipe. Main filtration, separately autoclaved
    sulfide, gas ratios and pressure remain distinct.
  quote: Sterilize by filtration under H 2 -CO 2 (80:20) gas mixture.
  snapshot_sha256: 693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b
- evidence_id: trace
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  locator: Trace minerals table and its following pH paragraph only
  accessed_at: '2026-10-21T09:01:28.851101Z'
  support: supports
  summary: The exact link from JCM214 resolves JCM151. Only its Trace minerals subsection
    transfers; no salt base, sulfur, peptone, citric acid, parent growth conditions
    or parent sulfide5% context transfers.
  quote: 'Trace minerals: Nitrilotriacetic acid 1.5 g'
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: CHEBI:32954 resolves to sodium acetate. Exact label validity is separate
    from source chemical-form support.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Exact label validity is separate from
    source chemical-form support.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Exact label validity is
    separate from source chemical-form support.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76181
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T09:28:27.017914Z'
  support: supports
  summary: CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Exact label
    validity is separate from source chemical-form support.
  snapshot_sha256: 1ca5b1ee73ce8d8fd35e60c7f45baacd870b6f5fdce0a02345be62e7622dbaa5
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:08.844455Z'
  support: supports
  summary: CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Exact label
    validity is separate from source chemical-form support.
  snapshot_sha256: 930d93c33f6115f19153868ae36f0153b69406fd555708237a7ccccfb010cd97
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: CHEBI:86360 resolves to manganese(II) sulfate. Exact label validity is
    separate from source chemical-form support.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: chebi86463
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86463
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T11:01:47.791068Z'
  support: supports
  summary: CHEBI:86463 resolves to potassium aluminium sulfate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: 59060418cddd95e8401be3d2518a69fbcd26a4f4e6f0597b2c8c03834a87812e
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Exact label validity is separate from
    source chemical-form support.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS ID, canonical label, obsolete flag and supplied-form annotations
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Exact label validity
    is separate from source chemical-form support.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent snapshot metadata
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O",
    "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4\u00b7H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4\u00b7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label":
    "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term":
    "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type":
    "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate",
    "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term":
    "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76181": [{"label":
    "Fe(NH4)2(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76181",
    "preferred_term": "Fe(NH4)2(SO4)2 x 6 H2O", "ontology_id": "CHEBI:76181", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier":
    "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term":
    "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O",
    "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86463": [{"label": "AlK(SO4)2", "match_type": "preferred_term",
    "identifier": "CHEBI:86463", "preferred_term": "AlK(SO4)2", "ontology_id": "CHEBI:86463",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id":
    "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys":
    []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml; data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: Current importer, cleanup and merge behavior is scoped context only. Observed
    cross-stage sums and historical notes are separate from current code, which was
    not executed or used as a historical replay.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: Current importer, cleanup and merge behavior is scoped context only. Observed
    cross-stage sums and historical notes are separate from current code, which was
    not executed or used as a historical replay.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: Current importer, cleanup and merge behavior is scoped context only. Observed
    cross-stage sums and historical notes are separate from current code, which was
    not executed or used as a historical replay.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/300/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:59:05Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 99bde66e0c235d2bd598aa5a3c44b0efdd323944daa43d83ba1f3f63efdfc6d3
- evidence_id: mediadiveJ214api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J214
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:33:59.585655Z'
  support: context_only
  summary: Optional mediadiveJ214api request returned 503. Exact JCM214 and its actual
    linked JCM151 route are available, so this failed attempt does not make the required
    source unavailable. Historical API payload equality is not inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: jcm151-attempt
  kind: database
  reference: https://jcm.brc.riken.jp/medium/151
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:38:11.086819Z'
  support: context_only
  summary: Optional jcm151 request returned 404. Exact JCM214 and its actual linked
    JCM151 route are available, so this failed attempt does not make the required
    source unavailable. Historical API payload equality is not inferred.
  snapshot_sha256: 80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880
- evidence_id: mediadiveJ214retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J214
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:38:12.107025Z'
  support: context_only
  summary: Optional mediadiveJ214retry request returned 503. Exact JCM214 and its
    actual linked JCM151 route are available, so this failed attempt does not make
    the required source unavailable. Historical API payload equality is not inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary chemical identifiers
  outcome: concern
  summary: '23 distinct primary/current-secondary IDs have matching nonobsolete labels.
    Target direct-ingredient linkage is 23/24 primary (95.83%) and 22/24 current CHEBI-based
    secondary (91.67%), on a 0–100 linkage scale, not an accuracy score. Current secondary
    keys without pinned index rows: []. Legacy slot count 0 is separate and does not
    enter that current-key claim. Supplied-form correspondence is assessed separately.'
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi26710
  - chebi31206
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32149
  - chebi32312
  - chebi32588
  - chebi32954
  - chebi33118
  - chebi44557
  - chebi75213
  - chebi75836
  - chebi76181
  - chebi76209
  - chebi86149
  - chebi86158
  - chebi86345
  - chebi86360
  - chebi86463
  - chebi8806
  - chebi91244
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 17 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact collection medium and source-linked stock
  outcome: supported
  summary: JCM214 identifies the exact named main medium and explicitly links JCM151
    for Trace minerals. The successful linked historical-route capture supplies that
    stock; a failed guessed modern route does not establish source absence. The sole
    normalized JCM owner is resolved by exact merge provenance and stable ID.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace
- assessment_id: classification
  area: scope
  topic: Mixture and biological boundaries
  outcome: supported
  summary: Liquid/complex/undefined is compatible with salts plus yeast extract and
    no agar. Title and archaea filing are source catalogue context, not growth or
    taxonomic evidence. No organism/strain-specific performance, optimum or paper
    assertion is added.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: forms
  area: grounding
  topic: Explicit and unresolved supplied-form boundaries
  outcome: concern
  summary: Source MnSO4·xH2O leaves hydration number unspecified, whereas CHEBI:86360
    is anhydrous manganese sulfate. Preserve the hydrated-source qualification and
    do not invent x or a molarity. Source AlK(SO4)2 does not state a hydrate count,
    so a dodecahydrate must not be imported from a different Wolin formula. Explicit
    iron/ammonium nickel hexahydrates, magnesium/calcium hydrates and source Resazurin
    were checked against their captured structures; neutral resazurin is not contradicted
    by this source wording.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - primary
  - trace
  - chebi86360
  - chebi86463
  - chebi76181
  - chebi86149
  - chebi8806
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 44 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"KCl\",\n    \"\
    decision\": \"correct\",\n    \"source_stage\": \"JCM214 main batch\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.34\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.34\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[0], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> KCl           \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.34&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"label\": \"MgCl2\
    \ x 6 H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main\
    \ batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[1], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;4.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"label\": \"MgSO4\
    \ x 7 H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main\
    \ batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.45\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.45\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[2], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.45&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis. The local value also combines main and undiluted trace-stock contributions;\
    \ separate those stages rather than retaining a sum.\"\n  },\n  {\n    \"decision_id\"\
    : \"q4\",\n    \"label\": \"NH4Cl\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"JCM214 main batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n        }\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[3], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl\
    \                                                </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"label\": \"CaCl2\
    \ x 2 H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main\
    \ batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24000000000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24000000000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[4], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.14&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis. The local value also combines main and undiluted trace-stock contributions;\
    \ separate those stages rather than retaining a sum.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"label\": \"K2HPO4\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"JCM214 main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.14\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.14\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[5], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.14&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"label\": \"NaCl\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[6], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaCl          \
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;18.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis. The local value also combines main and undiluted trace-stock contributions;\
    \ separate those stages rather than retaining a sum.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"label\": \"NaHCO3\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"JCM214 main batch\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[7], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaHCO<sub>3</sub>\
    \                                               </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"label\": \"Na2SO4\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[8], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>\
    \                                            </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;2.7&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"label\": \"Fe(NH4)2(SO4)2\
    \ x 6 H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main\
    \ batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[9], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Fe(NH<sub>4</sub>)<sub>2</sub>(SO<sub>4</sub>)<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis. The milligram-to-gram arithmetic is consistent, but that alone does\
    \ not authenticate a final-medium concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"label\": \"(NH4)2Ni(SO4)2 x 6 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"JCM214 main batch\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[10], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> (NH<sub>4</sub>)<sub>2</sub>Ni(SO<sub>4</sub>)<sub>2</sub>&#183;6H<sub>2</sub>O\
    \                </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis. The milligram-to-gram arithmetic is consistent, but that alone does\
    \ not authenticate a final-medium concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"label\": \"Yeast extract\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"JCM214 main batch\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[12], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)\
    \                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"label\": \"Sodium\
    \ acetate\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main\
    \ batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[13], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Sodium acetate\
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"label\": \"Resazurin\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM214 main batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[14], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Resazurin     \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> mg  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis. The milligram-to-gram arithmetic is consistent, but that alone does\
    \ not authenticate a final-medium concentration.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"label\": \"Na2S x 9 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"JCM214 main batch\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[15], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>S&#183;9H<sub>2</sub>O\
    \                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain this original main amount/unit\
    \ with its source batch basis. Main 990 ml water plus 10 ml trace is a listed-input\
    \ sum, not an explicit measured final-volume declaration, especially with separately\
    \ added sulfide stock of unspecified volume. Existing G_PER_L needs evidence for\
    \ its basis.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"label\": \"Nitrilotriacetic\
    \ acid trace stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    JCM151 Trace minerals only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[20], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Nitrilotriacetic\
    \ acid                                   </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q17\",\n    \"label\": \"MgSO4 x 7 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.45\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.45\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[21], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q18\",\n    \"label\": \"MnSO4 x n H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[22], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> MnSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O\
    \                           </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q19\",\n    \"label\": \"NaCl trace stock\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace minerals\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[23], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> NaCl          \
    \                                          </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q20\",\n    \"label\": \"FeSO4 x 7 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[24], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q21\",\n    \"label\": \"CoSO4 x 7 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[25], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CoSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q22\",\n    \"label\": \"CaCl2 x 2 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24000000000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24000000000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[26], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q23\",\n    \"label\": \"ZnSO4 x 7 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[27], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q24\",\n    \"label\": \"CuSO4 x 5 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[28], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O\
    \                                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q25\",\n    \"label\": \"AlK(SO4)2 trace stock\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace minerals\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[29], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> AlK(SO<sub>4</sub>)<sub>2</sub>\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q26\",\n    \"label\": \"H3BO3 trace stock\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace minerals\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[30], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>\
    \                                             </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10% ALIGN=RIGHT>\
    \ g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q27\",\n    \"label\": \"Na2MoO4 x 2 H2O trace\
    \ stock\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"JCM151 Trace\
    \ minerals only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm151linked\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[31], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O\
    \                             </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      },\n      {\n        \"source_key\": \"jcm151linked\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\",\n        \"source_locator\"\
    : \"Exact source HTML table row[32], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       \
    \  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"This amount belongs to the separate\
    \ JCM151 Trace minerals stock, with 1 L stock water and a 10 ml receiving-medium\
    \ dose. It is not a direct main concentration. Preserve source hydration and original\
    \ units; do not merge full-strength stock amounts with main ingredients.\"\n \
    \ },\n  {\n    \"decision_id\": \"q28\",\n    \"label\": \"Trace-stock addition\"\
    ,\n    \"decision\": \"add\",\n    \"source_stage\": \"Main stock addition\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[11], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Trace minerals\
    \ (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=151\\\">151</a>)    \
    \              </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the exact 10 ml batch dose\
    \ and full source-specific Trace minerals composition. Do not substitute parent\
    \ salt base or another named trace recipe.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q29\",\n    \"label\": \"Main water\",\n    \"decision\": \"add\",\n    \"\
    source_stage\": \"Main batch\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore source 990 ml main water\
    \ separately from stock water and later sulfide stock volume.\"\n  },\n  {\n \
    \   \"decision_id\": \"q30\",\n    \"label\": \"Trace-stock water\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"Trace stock\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm151linked\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[32], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Distilled water\
    \                                         </TD><TD WIDTH=15% ALIGN=RIGHT><font\
    \ size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD WIDTH=10%\
    \ ALIGN=RIGHT> L  </TD></TR>\",\n        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 1 L water only inside the\
    \ Trace minerals preparation; it is not an extra liter added directly to main\
    \ medium or an explicit measured final stock volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q31\",\n    \"label\": \"Main final volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Main final-volume limit\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm214\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Exact source HTML table row[11], zero-based document\
    \ row\",\n        \"exact_source_quote\": \"<TR><TD WIDTH=75%> Trace minerals\
    \ (see Medium No. <a href=\\\"/cgi-bin/jcm/jcm_grmd?GRMD=151\\\">151</a>)    \
    \              </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[16], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD\
    \ WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"Known main water plus trace dose\
    \ sums to 1000 ml, but the source does not declare measured final volume and later\
    \ sulfide stock volume is unspecified. Do not derive an authenticated denominator\
    \ from the sum alone.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"label\"\
    : \"Initial main pH\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Main pH\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.9\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.9\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main preparation initial adjustment\",\n    \
    \    \"exact_source_quote\": \"adjust pH to 6.9\",\n        \"snapshot_sha256\"\
    : \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\",\n    \
    \    \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"Stored target pH and preparation\
    \ value agree; attach exact same-layer evidence without treating it as measured\
    \ final pH.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"label\": \"Conditional\
    \ main pH readjustment\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Late main pH adjustment\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps[0].description\",\n        \"stored\": \"Mix\
    \ ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by\
    \ filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main preparation after sulfide addition\",\n\
    \        \"exact_source_quote\": \"pH to 6.9, if necessary.\",\n        \"snapshot_sha256\"\
    : \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\",\n    \
    \    \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the separately conditional\
    \ 6.9 readjustment after sulfide addition.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q34\",\n    \"label\": \"Main filtration gas ratio\",\n    \"decision\": \"\
    evidence_only\",\n    \"source_stage\": \"Main filtration atmosphere\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main preparation filtration sentence\",\n   \
    \     \"exact_source_quote\": \"Sterilize by filtration under H 2 -CO 2 (80:20)\
    \ gas mixture.\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain H2/CO2 80:20 at main filtration;\
    \ no dissolved gas concentration or unstated ratio basis is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q35\",\n    \"label\": \"Late-addition atmosphere\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"Sulfide addition\
    \ to main\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main aseptic late-addition sentence\",\n    \
    \    \"exact_source_quote\": \"H 2 -CO 2 (80:20) atmosphere\",\n        \"snapshot_sha256\"\
    : \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\",\n    \
    \    \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve this separate main handling\
    \ atmosphere.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"label\": \"Pressure\
    \ and gas ratio\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"Post-inoculation pressure\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main final pressure sentence\",\n        \"exact_source_quote\"\
    : \"to 200 kPa H 2 -CO 2 (80:20).\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"Keep 200 kPa and H2/CO2 80:20. The\
    \ source does not qualify absolute versus gauge pressure; neither qualifier is\
    \ invented.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"label\": \"Sulfide\
    \ stock nitrogen\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\"\
    : \"Sulfide stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Mix ingredients\
    \ except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize by filtration\
    \ under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution and autoclave\
    \ under a N2 atmosphere. Aseptically and anaerobically add the sterile Na2S x\
    \ 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust pH\
    \ to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Separate sulfide-stock sterilization sentence\"\
    ,\n        \"exact_source_quote\": \"autoclave under a N 2 atmosphere.\",\n  \
    \      \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"N2 atmosphere has no explicit purity\
    \ percentage, quantity or dissolved concentration; do not infer 100%.\"\n  },\n\
    \  {\n    \"decision_id\": \"q38\",\n    \"label\": \"Sulfide stock strength and\
    \ dose\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Separate\
    \ sulfide stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Sulfide stock sentence\",\n        \"exact_source_quote\"\
    : \"Neutralize Na 2 S·9H 2 O solution\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Exact source HTML table row[15], zero-based document row\",\n        \"exact_source_quote\"\
    : \"<TR><TD WIDTH=75%> Na<sub>2</sub>S&#183;9H<sub>2</sub>O                  \
    \                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD\
    \ WIDTH=10% ALIGN=RIGHT> g  </TD></TR>\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    \n      }\n    ],\n    \"interpretation\": \"The exact main source supplies a\
    \ sulfide mass but no stock percentage, volume or neutralization target. The unrelated\
    \ parent JCM151 sulfide5% recipe is outside the transferred Trace minerals section.\"\
    \n  },\n  {\n    \"decision_id\": \"q39\",\n    \"label\": \"Default autoclave\
    \ cycle scoped to stock\",\n    \"decision\": \"add\",\n    \"source_stage\":\
    \ \"Source-default cycle and explicit exception\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm214\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"JCM214 page default header\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Sulfide-stock sentence\",\n        \"exact_source_quote\": \"autoclave under\
    \ a N 2 atmosphere.\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the page default 121°C/15min\
    \ only with its unless-otherwise-stated scope and the explicit sulfide-stock autoclaving\
    \ step. Main medium has an explicit filtration exception, so this is not a main\
    \ autoclave instruction.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n    \"label\"\
    : \"Main sterilization action mismatch\",\n    \"decision\": \"correct\",\n  \
    \  \"source_stage\": \"Main versus stock methods\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].action\",\n        \"stored\"\
    : \"AUTOCLAVE\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].action\",\n        \"stored\"\
    : \"AUTOCLAVE\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main method\",\n        \"exact_source_quote\"\
    : \"Sterilize by filtration under H 2 -CO 2 (80:20) gas mixture.\",\n        \"\
    snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      },\n      {\n        \"source_key\": \"jcm214\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\",\n        \"source_locator\"\
    : \"Separate sulfide-stock method\",\n        \"exact_source_quote\": \"autoclave\
    \ under a N 2 atmosphere.\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"The action AUTOCLAVE does not describe\
    \ main sterilization. Split or explicitly scope main filtration and separate stock\
    \ autoclaving while retaining the correct descriptive text.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q41\",\n    \"label\": \"Initial trace pH\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Trace-stock pH\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm151linked\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Trace minerals preparation after stock table\"\
    ,\n        \"exact_source_quote\": \"adjust pH to 6.5 with KOH solution.\",\n\
    \        \"snapshot_sha256\": \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\"\
    ,\n        \"parsed_text_sha256\": \"e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing numeric text is correct\
    \ but needs explicit Trace minerals placement; it must not overwrite main pH6.9.\"\
    \n  },\n  {\n    \"decision_id\": \"q42\",\n    \"label\": \"Final trace pH\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"Trace-stock pH\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm151linked\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Trace minerals preparation after stock table\"\
    ,\n        \"exact_source_quote\": \"Adjust final pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\",\n    \
    \    \"parsed_text_sha256\": \"e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing numeric text is correct\
    \ but needs explicit Trace minerals placement; it must not overwrite main pH6.9.\"\
    \n  },\n  {\n    \"decision_id\": \"q43\",\n    \"label\": \"H2SO4 adjustment\
    \ amount\",\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Main\
    \ pH reagent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients except Na2S x 9H2O and adjust pH to 6.9 with H2SO4. Sterilize\
    \ by filtration under H2-CO2 (80:20) gas mixture. Neutralize Na2S x 9H2O solution\
    \ and autoclave under a N2 atmosphere. Aseptically and anaerobically add the sterile\
    \ Na2S x 9H2O solution to the medium under a H2-CO2 (80:20) atmosphere and readjust\
    \ pH to 6.9, if necessary. Pressurize inoculated bottle to 200 kPa H2-CO2 (80:20).\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm214\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=214\"\
    ,\n        \"source_locator\": \"Main initial pH adjustment\",\n        \"exact_source_quote\"\
    : \"with H 2 SO 4 .\",\n        \"snapshot_sha256\": \"693053f81a8196583da08c77e62cbf7d7d6788e302687168bd9a6313efb5735b\"\
    ,\n        \"parsed_text_sha256\": \"339a668ac47257d1c6a95c8bf574b7c20327c431964bbf91cceef83121d77d68\"\
    \n      }\n    ],\n    \"interpretation\": \"The source gives neither sulfuric\
    \ acid strength nor amount; the pH target alone cannot determine either.\"\n \
    \ },\n  {\n    \"decision_id\": \"q44\",\n    \"label\": \"KOH adjustment amount\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"Trace-stock\
    \ pH reagent\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm151linked\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151\"\
    ,\n        \"source_locator\": \"Trace-stock initial pH adjustment\",\n      \
    \  \"exact_source_quote\": \"with KOH solution.\",\n        \"snapshot_sha256\"\
    : \"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7\",\n    \
    \    \"parsed_text_sha256\": \"e3a9beb9f7ed9f3f7cd979a7b62d3ce76bbc3bf11c2623b8031be160b3c08db9\"\
    \n      }\n    ],\n    \"interpretation\": \"No KOH strength or volume is specified.\
    \ Keep this stock-only and do not fabricate a final main concentration.\"\n  }\n\
    ]"
- assessment_id: ownership
  area: ownership
  topic: Exact sole maintained source
  outcome: supported
  summary: The normalized JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM owner owns correction.
    Entire target and owner content/history and exact current writers were read. No
    recipe, history or generated artifact was changed.
  target_ids:
  - CultureMech:002576
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: cm002576-flattened-stock
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Trace-stock ingredients and main concentrations have been combined
  description: The exact JCM151 Trace minerals composition is flat in both layers.
    Mg sulfate6.45, calcium0.24000000000000002 and NaCl19 combine main amounts with
    full-strength stock amounts. The 10ml stock dose and main990ml/stock1L water contexts
    are absent; the resulting formulation differs materially from the source.
  target_ids:
  - CultureMech:002576
  field_paths:
  - ingredients[*].concentration
  - ingredients[2].notes
  - ingredients[4].notes
  - ingredients[6].notes
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  issue_key: cm002576-preparation-method
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Action and stock-pH placement obscure the explicit main method
  description: The main recipe is explicitly filter sterilized, but a combined root
    step is labelled AUTOCLAVE. Autoclaving belongs to the separate sulfide stock.
    A second root step contains Trace minerals pH6.5 then7.0 without naming the stock.
    Main pH6.9, gas ratio and unqualified200kPa text are otherwise retained.
  target_ids:
  - CultureMech:002576
  field_paths:
  - preparation_steps[0].action
  - preparation_steps[1]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  issue_key: cm002576-hydration-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Unspecified manganese hydrate is represented as anhydrous
  description: The transferred source prints MnSO4·xH2O; current CHEBI:86360 has anhydrous
    MnSO4 structure. The hydrate count is unavailable in the source, so no exact hydrate
    ID or molecular-weight conversion can be chosen. Other explicit hydrate labels
    and neutral Resazurin are not implicated by this finding.
  target_ids:
  - CultureMech:002576
  field_paths:
  - ingredients[16].term
  - ingredients[16].preferred_term
  evidence_ids:
  - trace
  - chebi86360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  issue_key: cm002576-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Supported preparation and ingredient statements lack claim evidence
  description: No attached amount/preparation claim connects the main and trace quantities
    to their distinct source sections. Historical import and duplicate-cleanup notes
    cannot authenticate final concentrations or expand the parent-source scope.
  target_ids:
  - CultureMech:002576
  field_paths:
  - ingredients[*].evidence
  - references
  - preparation_steps
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace
  - history-metadata
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  description: Reconstruct the exact source stock and dose, split contributions and
    preserve original quantities/water stages. Establish the source basis before final-medium
    concentration conversion; do not transfer unrelated parent ingredients.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002576
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  description: Separate or explicitly scope main filtration, sulfide-stock autoclaving
    and trace-stock pH. Keep the main exception to JCM defaults and avoid inventing
    pressure qualifiers or stock purity/strength.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002576
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  description: Retain the source hydrate qualification and unresolved x, grounding
    only the justified chemical specificity. Do not infer monohydrate from a different
    mineral recipe or from a MIM synonym.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002576
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
  description: Attach narrow source/version/stage evidence after correction, preserve
    historical events and regenerate only from separately authorized maintained-input
    changes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002576
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml
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
- Optional mediadiveJ214api request returned 503. Exact JCM214 and its actual linked
  JCM151 route are available, so this failed attempt does not make the required source
  unavailable. Historical API payload equality is not inferred.
- Optional jcm151 request returned 404. Exact JCM214 and its actual linked JCM151
  route are available, so this failed attempt does not make the required source unavailable.
  Historical API payload equality is not inferred.
- Optional mediadiveJ214retry request returned 503. Exact JCM214 and its actual linked
  JCM151 route are available, so this failed attempt does not make the required source
  unavailable. Historical API payload equality is not inferred.
- Completed current-source review. JCM151 transfers only Trace minerals and its following
  pH paragraph; salt base, sulfur treatment, peptone, parent growth conditions and
  parent sulfide5% are excluded. Main final volume, pressure gauge/absolute status,
  sulfide stock strength/dose and manganese hydrate count remain explicitly unresolved.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-030
- generated-medium
```
