# Source and formulation review: ap11mh_medium (CultureMech:008415)

- Review: 20261021T162629Z-culturemech-008415-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:17:56Z
- Finished UTC: 2026-10-21T16:26:29Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact NBRC 1075 and TOGO M1841 define a main medium plus separately prepared KP, trace-element and vitamin stocks. Both local layers flatten stock ingredients and misrepresent volume/milligram quantities; summed sodium/calcium and the target water total ignore stage boundaries. The two asserted external stock identifiers resolve to different formulations, so their eight verified stock-only amount claims do not authenticate AP11MH. Required preparation, gas and stock-pH context is absent. Supplied-form mismatches and a current secondary-index gap remain distinct from unresolved historical legacy 389 correspondence; that historical check makes the review partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 290; batch 029 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-eight task batches contain 280 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 283 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008415 | data/merge_yaml/merged/AP11MH_medium.yaml | generated | ap11mh_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008415 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008415 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/290/strict.tsv |
| validate-terms | passed | True | CultureMech:008415 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008415 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008415 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical identity of asserted legacy MediaIngredientMech:000389 | unavailable | True | CultureMech:008415 | Complete current index/catalog/tree lookup finished with no exact correspondence, but the historical source mapping required to verify this asserted legacy ID is unavailable. This is separate from the completed current CHEBI:29032 secondary gap. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008415.

The four documented recipes completed; interpret the scope of each separately.

### Complete target/owner ontology and current secondary linkage

grounding: concern. Targets: CultureMech:008415.

39 distinct primary/current-secondary ontology IDs have exact nonobsolete labels. Each layer links 39/40 primary instances (97.50%) and 33/40 current secondary instances (82.50%), on a 0–100 linkage scale, not scientific accuracy. CHEBI:29032 is valid live ontology but absent from the complete pinned MIM index; all other asserted current CHEBI keys have exact rows. Legacy 389 is a separate current absence with unresolved historical correspondence.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008415.

28 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source accession and asserted stock identity

identity: concern. Targets: CultureMech:008415.

TOGO M1841 and NBRC 1075 identify the same named main recipe. The exact standalone stock IDs resolve through the local index and public endpoints, but 6187 has EDTA-based composition instead of NBRC NTA trace stock, and 6241 has three vitamins in 100 ml instead of nine in 1 L. Resolution is not formulation equivalence. KP has no external ID and its inline composition is empty.

### Mixture class and biological claim boundaries

scope: supported. Targets: CultureMech:008415.

Liquid classification is consistent with no agar in the exact source. Yeast extract makes the recipe chemically undefined in part; COMPLEX/SEMI_DEFINED conveys a specified chemical basal recipe with a complex supplement. No target organism, strain, growth outcome, DOI/PMID or measured optimum is asserted. Do not infer them from the title or generic cultivation annotation.

### Exact supplied forms versus stable chemical IDs

grounding: concern. Targets: CultureMech:008415.

Source cobalt and nickel chlorides are hexahydrates, whereas CHEBI:35696 and CHEBI:34887 are anhydrous salts. Source Ca-pantothenate is a calcium salt, unlike the calcium-free anion CHEBI:29032. Source cysteine-HCl does not establish the L configuration of CHEBI:91247. Vitamin B12 is a generic class in this source; the distinct cyanocobalamin in external 6241 must not narrow it. Remaining explicit hydrates agree with their captured generic structural forms; no new ID or amount conversion is inferred.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008415.

76 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "Distilled water",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[18], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Both mass units are wrong for source 1 L water. Target 4.0 also sums water from four distinct preparation stages; owner 1.0 collapsed identical rows but still loses their separate roles. Preserve all four source water contexts without combining them as main water."
  },
  {
    "decision_id": "q2",
    "label": "NaCl",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "31.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "31.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[9], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;NaCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;30&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 30,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration. Local 31 combines main 30 g with undiluted trace-stock 1 g; retain them separately and apply only the actual stock dose when a basis is justified."
  },
  {
    "decision_id": "q3",
    "label": "CaCl2·2H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[5], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.15&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration. Local 0.25 combines main 0.15 g with undiluted trace-stock 0.1 g; retain separate stages."
  },
  {
    "decision_id": "q4",
    "label": "NH4Cl",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.54",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.54",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[6], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;NH&lt;sub&gt;4&lt;/sub&gt;Cl&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.54&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.54,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q5",
    "label": "Resazurin",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[14], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Resazurin&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Source gives 1 mg resazurin; local 1 G_PER_L loses the milligram unit. Restore source amount/unit with the original batch context; no final-volume inference."
  },
  {
    "decision_id": "q6",
    "label": "MgCl2·6H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "3.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "3.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[4], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;3.05&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"MgCl2·6H2O\",\n          \"volume\": 3.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q7",
    "label": "Na2S·9H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Na2S·9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q8",
    "label": "Sodium acetate",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.82",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.82",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[11], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Sodium acetate&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.82&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Sodium acetate\",\n          \"volume\": 0.82,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q9",
    "label": "Na2CO3",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[15], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;1.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q10",
    "label": "Na2SO4",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.42",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.42",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[7], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;1.42&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2SO4\",\n          \"volume\": 1.42,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q11",
    "label": "Bacto Yeast Extract (Difco)",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[10], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Bacto Yeast Extract (Difco)&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.02&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Bacto Yeast Extract (Difco)\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q12",
    "label": "Cysteine-HCl",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[17], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Cysteine-HCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Cysteine-HCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q13",
    "label": "Na2S2O3·5H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 main batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.24",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.24",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[8], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;S&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;3&lt;/sub&gt;&amp;middot;5H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;1.24&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Na2S2O3·5H2O\",\n          \"volume\": 1.24,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain the exact original main batch amount with its source unit. The main table lists 1 L water plus stock additions; it does not establish a measured final-volume denominator. Current unqualified G_PER_L needs a stated source batch/nominal basis, not an invented corrected final concentration."
  },
  {
    "decision_id": "q14",
    "label": "KP buffer* dose",
    "decision": "correct",
    "source_stage": "Main stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[3], zero-based document row",
        "exact_source_quote": "&lt;tr&gt;\n                            &lt;td colspan=\"2\" id=\"medium-comp\"&gt;&lt;table width='600' border='0'&gt;&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;KP buffer*&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"KP buffer*\",\n          \"volume\": 5,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a source volume dose in ml, not a mass in grams. Associate it only with its exact NBRC stock formulation; do not retain generic-name external substitutions."
  },
  {
    "decision_id": "q15",
    "label": "Trace element solution** dose",
    "decision": "correct",
    "source_stage": "Main stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[12], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Trace element solution**&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"Trace element solution**\",\n          \"volume\": 2,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a source volume dose in ml, not a mass in grams. Associate it only with its exact NBRC stock formulation; do not retain generic-name external substitutions."
  },
  {
    "decision_id": "q16",
    "label": "Vitamin solution*** dose",
    "decision": "correct",
    "source_stage": "Main stock addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[13], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Vitamin solution***&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[0].items[15]",
        "exact_source_quote": "\"component_name\": \"Vitamin solution***\",\n          \"volume\": 2,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a source volume dose in ml, not a mass in grams. Associate it only with its exact NBRC stock formulation; do not retain generic-name external substitutions."
  },
  {
    "decision_id": "q17",
    "label": "KH2PO4",
    "decision": "correct",
    "source_stage": "KP buffer stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[24], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;53&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 53,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This gram amount belongs to separately prepared KP buffer with 1 L water; main adds 5 ml. It is not an undiluted direct main ingredient. Reconstruct the currently empty KP composition."
  },
  {
    "decision_id": "q18",
    "label": "K2HPO4",
    "decision": "correct",
    "source_stage": "KP buffer stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "106",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "106",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[25], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;106&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 106,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This gram amount belongs to separately prepared KP buffer with 1 L water; main adds 5 ml. It is not an undiluted direct main ingredient. Reconstruct the currently empty KP composition."
  },
  {
    "decision_id": "q19",
    "label": "NaCl",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "31.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "31.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[39], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;NaCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q20",
    "label": "CaCl2·2H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[34], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q21",
    "label": "Na2MoO4·2H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[38], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.024&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4·2H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q22",
    "label": "H3BO3",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[37], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.01&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q23",
    "label": "MnCl2·4H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[32], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;4H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"MnCl2·4H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q24",
    "label": "CoCl2·6H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[33], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.024&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q25",
    "label": "NiCl2·6H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.12",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.12",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[40], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.12&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"NiCl2·6H2O\",\n          \"volume\": 0.12,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q26",
    "label": "CuCl2·2H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[36], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.025&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"CuCl2·2H2O\",\n          \"volume\": 0.025,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q27",
    "label": "ZnCl2",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[35], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;ZnCl&lt;sub&gt;2&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[9]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q28",
    "label": "FeCl3·6H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "1.35",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "1.35",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[31], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;FeCl&lt;sub&gt;3&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;1.35&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[10]",
        "exact_source_quote": "\"component_name\": \"FeCl3·6H2O\",\n          \"volume\": 1.35,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q29",
    "label": "KAl(SO4)2·12H2O",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.018",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.018",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[43], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;KAl(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;middot;12H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.018&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[11]",
        "exact_source_quote": "\"component_name\": \"KAl(SO4)2·12H2O\",\n          \"volume\": 0.018,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q30",
    "label": "Nitrilotriacetic acid (NTA)",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "12.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "12.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[30], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Nitrilotriacetic acid (NTA)&lt;/td&gt;&lt;td width='20%' align='right'&gt;12.8&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[12]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid (NTA)\",\n          \"volume\": 12.8,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q31",
    "label": "Na2WO4",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[42], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.004&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[13]",
        "exact_source_quote": "\"component_name\": \"Na2WO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q32",
    "label": "Na2SeO4",
    "decision": "correct",
    "source_stage": "NBRC 1075 trace-element stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[41], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.004&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[14]",
        "exact_source_quote": "\"component_name\": \"Na2SeO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This exact source amount belongs to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct main concentration and is not the differently formulated external 6187 stock. Preserve the printed salt/hydrate."
  },
  {
    "decision_id": "q33",
    "label": "Biotin",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[49], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Biotin&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q34",
    "label": "p-Aminobenzoic acid",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[56], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;&lt;i&gt;p&lt;/i&gt;-Aminobenzoic acid&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q35",
    "label": "Thiamine-HCl",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[52], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Thiamine-HCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q36",
    "label": "Ca-pantothenate",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[34].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[34].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[55], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Ca-pantothenate&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q37",
    "label": "Pyridoxine-HCl",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[35].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[35].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[51], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Pyridoxine-HCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;10&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q38",
    "label": "Folic acid",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[36].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[36].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[50], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Folic acid&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q39",
    "label": "Vitamin B12",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[37].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[37].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[57], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Vitamin B&lt;sub&gt;12&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.01&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.01,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q40",
    "label": "Riboflavin",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[38].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[38].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[53], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Riboflavin&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q41",
    "label": "Nicotinic acid",
    "decision": "correct",
    "source_stage": "NBRC 1075 vitamin stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[39].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[39].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[54], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Nicotinic acid&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "This is a milligram amount in the separate nine-vitamin stock with 1 L water, not the same numeral in grams per liter of main medium. Main receives 2 ml of this stock; the differently formulated external 6241 does not substitute."
  },
  {
    "decision_id": "q42",
    "label": "Water for KP stock",
    "decision": "correct",
    "source_stage": "Stock water: KP",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[0]",
        "stored": {
          "preferred_term": "KP buffer*",
          "composition": [],
          "concentration": {
            "value": "5",
            "unit": "G_PER_L"
          },
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[0]",
        "stored": {
          "preferred_term": "KP buffer*",
          "composition": [],
          "concentration": {
            "value": "5",
            "unit": "G_PER_L"
          },
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[26], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain 1 L water within this stock preparation. The target sums four waters and owner collapses them; neither retains all four preparation stages. This water is not another 1 L directly added to main medium."
  },
  {
    "decision_id": "q43",
    "label": "Water for trace stock",
    "decision": "correct",
    "source_stage": "Stock water: trace",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[1]",
        "stored": {
          "preferred_term": "Trace element solution**",
          "term": {
            "id": "mediadive.solution:6187",
            "label": "Trace element solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[44], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain 1 L water within this stock preparation. The target sums four waters and owner collapses them; neither retains all four preparation stages. This water is not another 1 L directly added to main medium."
  },
  {
    "decision_id": "q44",
    "label": "Water for vitamin stock",
    "decision": "correct",
    "source_stage": "Stock water: vitamin",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions[2]",
        "stored": {
          "preferred_term": "Vitamin solution***",
          "term": {
            "id": "mediadive.solution:6241",
            "label": "Vitamin solution"
          },
          "concentration": {
            "value": "2",
            "unit": "G_PER_L"
          },
          "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
          "name": "Unknown solution"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[58], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "togoM1841",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6"
      }
    ],
    "interpretation": "Retain 1 L water within this stock preparation. The target sums four waters and owner collapses them; neither retains all four preparation stages. This water is not another 1 L directly added to main medium."
  },
  {
    "decision_id": "q45",
    "label": "Hydrogen gas mixture component",
    "decision": "correct",
    "source_stage": "Main dispensing atmosphere",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main dispensing gas-mixture sentence",
        "exact_source_quote": "H 2 /CO 2 (80/20)",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "VARIABLE alone obscures the explicit H2/CO2 ratio 80/20. Preserve that ratio and its gas-atmosphere stage without assigning dissolved molarity or inventing an unstated percentage basis."
  },
  {
    "decision_id": "q46",
    "label": "Carbon dioxide gas mixture component",
    "decision": "correct",
    "source_stage": "Main dispensing atmosphere",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main dispensing gas-mixture sentence",
        "exact_source_quote": "H 2 /CO 2 (80/20)",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "VARIABLE alone obscures the explicit H2/CO2 ratio 80/20. Preserve that ratio and its gas-atmosphere stage without assigning dissolved molarity or inventing an unstated percentage basis."
  },
  {
    "decision_id": "q47",
    "label": "Nitrogen atmosphere",
    "decision": "not_quantified",
    "source_stage": "KP and separate reductant stock handling",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Separate stock-autoclaving sentence",
        "exact_source_quote": "under a N 2 atmosphere.",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "KP stock preparation",
        "exact_source_quote": "Autoclaved under N 2 .",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "N2 atmosphere is named without a purity percentage, volume or dissolved concentration. Keep it scoped to stock handling; do not infer 100% or a main nutrient dose."
  },
  {
    "decision_id": "q48",
    "label": "NaOH stock pH adjustment",
    "decision": "not_quantified",
    "source_stage": "Trace-stock NTA dissolution",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Trace-stock preparation",
        "exact_source_quote": "adjust pH to 6.5 with NaOH",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "NaOH strength and amount are not specified. VARIABLE is compatible with an unquantified adjustment only when scoped to trace-stock NTA dissolution, not a fixed main ingredient."
  },
  {
    "decision_id": "q49",
    "label": "Main pH unadjusted",
    "decision": "add",
    "source_stage": "Main preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ph_value",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ph_value",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main pH row",
        "exact_source_quote": "pH unajusted",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "Preserve the source statement that main pH is unadjusted. It supplies no numerical main pH; do not replace it with trace-stock pH 6.5 or 7.0."
  },
  {
    "decision_id": "q50",
    "label": "Initial trace-stock pH",
    "decision": "add",
    "source_stage": "Trace-stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Trace-stock preparation paragraph",
        "exact_source_quote": "adjust pH to 6.5 with NaOH",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "Record 6.5 at NTA dissolution before the minerals."
  },
  {
    "decision_id": "q51",
    "label": "Final trace-stock pH",
    "decision": "add",
    "source_stage": "Trace-stock preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Trace-stock preparation paragraph",
        "exact_source_quote": "Final pH 7.0.",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "Record 7.0 for the completed trace stock, not the main medium."
  },
  {
    "decision_id": "q52",
    "label": "Sulfide stock strength",
    "decision": "add",
    "source_stage": "Late-added stock strength",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main separate-stock preparation paragraph",
        "exact_source_quote": "Na 2 S·9H 2 O (5% solution)",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "The source 5% is unqualified; do not convert to g/ml without its mass/volume basis."
  },
  {
    "decision_id": "q53",
    "label": "Cysteine-HCl stock strength",
    "decision": "add",
    "source_stage": "Late-added stock strength",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main separate-stock preparation paragraph",
        "exact_source_quote": "cysteine-HCl (5% solution)",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "The source 5% is unqualified; no independent stock dose follows from it."
  },
  {
    "decision_id": "q54",
    "label": "Carbonate stock strength",
    "decision": "add",
    "source_stage": "Late-added stock strength",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main separate-stock preparation paragraph",
        "exact_source_quote": "10% Na 2 CO 3 solutions",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "The source 10% is unqualified; preserve the filtration stage and do not invent a volume."
  },
  {
    "decision_id": "q55",
    "label": "Sulfide stock dose",
    "decision": "not_quantified",
    "source_stage": "Late-added stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main separate-stock preparation",
        "exact_source_quote": "Na 2 S·9H 2 O (5% solution)",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[16], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      }
    ],
    "interpretation": "Source main mass and an unqualified stock percentage do not define a volume dose without a verified percentage basis. Do not fill a guessed ml value."
  },
  {
    "decision_id": "q56",
    "label": "Cysteine-HCl stock dose",
    "decision": "not_quantified",
    "source_stage": "Late-added stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main separate-stock preparation",
        "exact_source_quote": "cysteine-HCl (5% solution)",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[17], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Cysteine-HCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      }
    ],
    "interpretation": "Source main mass and an unqualified stock percentage do not define a volume dose without a verified percentage basis. Do not fill a guessed ml value."
  },
  {
    "decision_id": "q57",
    "label": "Carbonate stock dose",
    "decision": "not_quantified",
    "source_stage": "Late-added stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main separate-stock preparation",
        "exact_source_quote": "10% Na 2 CO 3 solutions",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[15], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;1.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      }
    ],
    "interpretation": "Source main mass and an unqualified stock percentage do not define a volume dose without a verified percentage basis. Do not fill a guessed ml value."
  },
  {
    "decision_id": "q58",
    "label": "Pressurization",
    "decision": "add",
    "source_stage": "Main culture-vessel pressure",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "Main final preparation sentence",
        "exact_source_quote": "Pressurize the inoculated vessels to 150 kPa with H 2 /CO 2 .",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8",
        "parsed_text_sha256": "8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525"
      }
    ],
    "interpretation": "Retain 150 kPa and the named gas; absolute versus gauge is not stated, so neither qualifier is invented."
  },
  {
    "decision_id": "q59",
    "label": "Stock sterilization and staged addition",
    "decision": "add",
    "source_stage": "Source-specific preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[21], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for KP buffer, vitamin solution, Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;, Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O and cysteine-HCl. Dispense the medium into suitable culture vessels under a stream of H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) and seal with butyl rubber stoppers. Separately autoclave KP buffer, Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O (5% solution) and cysteine-HCl (5% solution) under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Sterilize vitamin and 10% Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt; solutions by filtration. Prior to inoculation, aseptically and anaerobically add KP buffer, vitamin, Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;, Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O and cysteine-HCl solutions. Pressurize the inoculated vessels to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[27], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td  width='90%' colspan='5'&gt;Autoclaved under N&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      }
    ],
    "interpretation": "Retain separately autoclaved KP and reductant stocks under N2, filtered vitamin/carbonate stocks and aseptic anaerobic late addition. No exact sterilization time/temperature is printed on this NBRC page."
  },
  {
    "decision_id": "q60",
    "label": "Unspecified sterilization time and temperature",
    "decision": "not_quantified",
    "source_stage": "Source preparation limits",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "presence": "absent"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[21], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for KP buffer, vitamin solution, Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;, Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O and cysteine-HCl. Dispense the medium into suitable culture vessels under a stream of H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) and seal with butyl rubber stoppers. Separately autoclave KP buffer, Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O (5% solution) and cysteine-HCl (5% solution) under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Sterilize vitamin and 10% Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt; solutions by filtration. Prior to inoculation, aseptically and anaerobically add KP buffer, vitamin, Na&lt;sub&gt;2&lt;/sub&gt;CO&lt;sub&gt;3&lt;/sub&gt;, Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O and cysteine-HCl solutions. Pressurize the inoculated vessels to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[27], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td  width='90%' colspan='5'&gt;Autoclaved under N&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      }
    ],
    "interpretation": "Do not import JCM default 121°C/15 min or other collection conditions into this exact NBRC recipe; the source supplies methods but no cycle numbers."
  },
  {
    "decision_id": "q61",
    "label": "Measured final volume",
    "decision": "not_quantified",
    "source_stage": "Main final-volume limit",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "4.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/merge_yaml/merged/AP11MH_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "KP buffer*",
            "composition": [],
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution**",
            "term": {
              "id": "mediadive.solution:6187",
              "label": "Trace element solution"
            },
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Vitamin solution***",
            "term": {
              "id": "mediadive.solution:6241",
              "label": "Vitamin solution"
            },
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
            "name": "Unknown solution"
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "KP buffer*",
            "composition": [],
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution**",
            "term": {
              "id": "mediadive.solution:6187",
              "label": "Trace element solution"
            },
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_6187_Trace_element_solution.yaml for composition",
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Vitamin solution***",
            "term": {
              "id": "mediadive.solution:6241",
              "label": "Vitamin solution"
            },
            "concentration": {
              "value": "2",
              "unit": "G_PER_L"
            },
            "notes": "See mediadive_6241_Vitamin_solution.yaml for composition",
            "name": "Unknown solution"
          }
        ]
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[18], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[3], zero-based document row",
        "exact_source_quote": "&lt;tr&gt;\n                            &lt;td colspan=\"2\" id=\"medium-comp\"&gt;&lt;table width='600' border='0'&gt;&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;KP buffer*&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[12], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Trace element solution**&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      },
      {
        "source_key": "nbrc1075",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075",
        "source_locator": "NBRC 1075 exact raw HTML table row[13], zero-based document row",
        "exact_source_quote": "&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Vitamin solution***&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;",
        "snapshot_sha256": "0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8"
      }
    ],
    "interpretation": "Main lists 1 L water plus 5, 2 and 2 ml named stocks and other late stocks whose volumes are unspecified. Neither summing all four stock preparations nor summing known doses establishes a measured final volume. Retain original batch quantities and explicit nominal calculations only."
  },
  {
    "decision_id": "q62",
    "label": "solution6187 Na2-EDTA",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.75",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\": \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6187",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\": \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[0].concentration (Na2-EDTA) in MediaDive solution 6187; locator=$.data.recipe[0] (compound_id=34). Provider explicitly reports g_l=0.75. Arithmetic check: 0.75 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.75 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916."
      }
    ]
  },
  {
    "decision_id": "q63",
    "label": "solution6187 Distilled water",
    "decision": "correct",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "1000",
          "unit": "PERCENT_V_V"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Water is a source volume, not 1000% v/v."
  },
  {
    "decision_id": "q64",
    "label": "solution6187 FeCl3 x 6 H2O",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.097",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\": \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6187",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\": \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[2].concentration (FeCl3 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[2] (compound_id=82). Provider explicitly reports g_l=0.097. Arithmetic check: 97 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.097 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916."
      }
    ]
  },
  {
    "decision_id": "q65",
    "label": "solution6187 MnCl2 x 4 H2O",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.041",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\": \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6187",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\": \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[3].concentration (MnCl2 x 4 H2O) in MediaDive solution 6187; locator=$.data.recipe[3] (compound_id=36). Provider explicitly reports g_l=0.041. Arithmetic check: 41 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.041 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916."
      }
    ]
  },
  {
    "decision_id": "q66",
    "label": "solution6187 ZnCl2 x 6 H2O",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6187",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[4].concentration (ZnCl2 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[4] (compound_id=2351). Provider explicitly reports g_l=0.005. Arithmetic check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916."
      }
    ]
  },
  {
    "decision_id": "q67",
    "label": "solution6187 CoCl2 x 6 H2O",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6187",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[5].concentration (CoCl2 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[5] (compound_id=38). Provider explicitly reports g_l=0.002. Arithmetic check: 2 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.002 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916."
      }
    ]
  },
  {
    "decision_id": "q68",
    "label": "solution6187 Na2MoO4 x 2 H2O",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6187",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[6].concentration (Na2MoO4 x 2 H2O) in MediaDive solution 6187; locator=$.data.recipe[6] (compound_id=9). Provider explicitly reports g_l=0.004. Arithmetic check: 4 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.004 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00; response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916."
      }
    ]
  },
  {
    "decision_id": "q69",
    "label": "solution6187 preparation context",
    "decision": "evidence_only",
    "source_stage": "External standalone-stock preparation only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "preparation_notes",
        "stored": "Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing sequence:"
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.steps[0].step encoded JSON string",
        "exact_source_quote": "\"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "The retained local preparation contains the same source water/stock context. It is not a procedure or final volume for AP11MH."
  },
  {
    "decision_id": "q70",
    "label": "solution6187 placeholder ingredient",
    "decision": "unsupported",
    "source_stage": "External stock placeholder context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6187",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6187",
        "source_locator": "$.data.id; complete recipe inspected",
        "exact_source_quote": "\"id\": 6187",
        "snapshot_sha256": "d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916"
      }
    ],
    "interpretation": "The local See source placeholder has no independent quantified ingredient identity; the complete composition already carries actual stock rows. This ancillary record is context only and requires separate curation, not transfer into AP11MH."
  },
  {
    "decision_id": "q71",
    "label": "solution6241 Cyanocobalamine",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
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
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6241",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[0].concentration (Cyanocobalamine) in MediaDive solution 6241; locator=$.data.recipe[0] (compound_id=847). Provider explicitly reports g_l=0.1. Arithmetic check: 10 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 100. Retrieved 2026-10-07T10:01:37.871406+00:00; response SHA256=d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1."
      }
    ]
  },
  {
    "decision_id": "q72",
    "label": "solution6241 Thiamine HCl",
    "decision": "verified",
    "source_stage": "External asserted-stock identity context only",
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
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "Existing attached excerpt, cited response hash, provider g_l and declared stock-volume basis agree for this standalone stock only. This does not verify an AP11MH ingredient, stock dose or formulation match.",
    "attached_existing_evidence": [
      {
        "reference": "https://mediadive.dsmz.de/rest/solution/6241",
        "supports": "SUPPORT",
        "snippet": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }",
        "explanation": "Concentration evidence for composition[1].concentration (Thiamine HCl) in MediaDive solution 6241; locator=$.data.recipe[1] (compound_id=1207). Provider explicitly reports g_l=0.1. Arithmetic check: 10 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: \"volume\": 100. Retrieved 2026-10-07T10:01:37.871406+00:00; response SHA256=d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1."
      }
    ]
  },
  {
    "decision_id": "q73",
    "label": "solution6241 Biotin",
    "decision": "correct",
    "source_stage": "External asserted-stock identity context only",
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
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The API gives 200 µg biotin made up to 100 ml, equivalent to 0.002 g/L in this distinct stock, not local 2000 g/L. This stock is not the NBRC vitamin formulation."
  },
  {
    "decision_id": "q74",
    "label": "solution6241 Distilled water",
    "decision": "correct",
    "source_stage": "External asserted-stock identity context only",
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
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "Water is a source volume, not 1000% v/v."
  },
  {
    "decision_id": "q75",
    "label": "solution6241 preparation context",
    "decision": "evidence_only",
    "source_stage": "External standalone-stock preparation only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml",
        "field_path": "preparation_notes",
        "stored": "Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.steps[0].step encoded JSON string",
        "exact_source_quote": "\"Make up to 100 ml with distilled water.\"",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The retained local preparation contains the same source water/stock context. It is not a procedure or final volume for AP11MH."
  },
  {
    "decision_id": "q76",
    "label": "solution6241 placeholder ingredient",
    "decision": "unsupported",
    "source_stage": "External stock placeholder context only",
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
    "source_snippets": [
      {
        "source_key": "solution6241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6241",
        "source_locator": "$.data.id; complete recipe inspected",
        "exact_source_quote": "\"id\": 6241",
        "snapshot_sha256": "d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1"
      }
    ],
    "interpretation": "The local See source placeholder has no independent quantified ingredient identity; the complete composition already carries actual stock rows. This ancillary record is context only and requires separate curation, not transfer into AP11MH."
  }
]

### Maintained source and generated boundaries

ownership: supported. Targets: CultureMech:008415.

The sole normalized ap11mh_medium.yaml owns future recipe correction. Exact current TOGO section parsing, solution matching and cleanup/merge code were inspected without execution. The two external stocks are context and must not be forced to fit this source. No record or history is changed.

## Findings

### f1: Flattened stock stages, summed duplicates and lost units change the recipe

blocker / open / confirmed; issue key: cm008415-stages-and-units.

Both layers mix KP, trace and vitamin strengths into main ingredients. Main NaCl 31 combines 30 g main with 1 g undiluted trace stock; calcium 0.25 similarly combines 0.15 g and 0.1 g. Target water 4.0 sums four 1 L preparations, while owner 1.0 collapses them without restoring stages; both use mass units. Resazurin 1 mg and all nine vitamin milligram amounts are stored with unchanged numerals in G_PER_L. Stock additions 5/2/2 ml are instead G_PER_L.

### f2: The two external stock links resolve to different formulations

blocker / open / confirmed; issue key: cm008415-wrong-stock-identities.

The referenced 6187 stock is EDTA-based with seven rows; NBRC 1075 trace stock is NTA-based with fifteen rows including water. Referenced 6241 has three vitamins in 100 ml; NBRC 1075 defines nine in 1 L. Their generic labels and eight internally supported amount attachments do not establish source equivalence. The local references resolve, so this is scientific wrong-stock identity rather than an absent-file schema failure.

### f3: Hydrate and calcium-salt mismatches persist despite valid IDs

major / open / confirmed; issue key: cm008415-forms.

CoCl2·6H2O and NiCl2·6H2O are linked to anhydrous CHEBI:35696/CHEBI:34887. Ca-pantothenate is linked to the calcium-free (R)-pantothenate anion. The source cysteine-HCl wording additionally leaves the L stereochemical specificity unestablished. Distinguish confirmed formula mismatches from that narrower unresolved specificity.

### f4: Source gas, separate-stock preparation and stock-pH context are missing

major / open / confirmed; issue key: cm008415-preparation.

Neither layer retains preparation_steps or main unadjusted-pH context. Source specifies H2/CO2 (80/20), separately sterilized stocks, unqualified 5%/10% strengths, trace pH 6.5 then 7.0 and pressure 150 kPa. VARIABLE gases/NaOH do not preserve those stages. No cycle temperature/time, percent basis, N2 purity or absolute/gauge pressure is supplied.

### f5: Current secondary gap and unresolved legacy correspondence are distinct

minor / open / confirmed; issue key: cm008415-secondary-provenance.

CHEBI:29032 is a valid live primary term but has no exact current MIM-index row for its asserted secondary membership. Legacy MediaIngredientMech:000389 is absent from the complete current index/catalog/tree; its historical mapping remains unavailable. A current miss neither proves historical invalidity nor supplies a replacement.

### f6: No main-layer claim evidence accompanies later partial cleanup

minor / open / confirmed; issue key: cm008415-evidence-generated-state.

Neither target nor owner attaches amount/preparation evidence. Owner water changed after target generation, but both representations remain source-incomplete; Unknown solution placeholders hide missing/incorrect stock identity. Current writer behavior and later cleanup notes are not a replay of historical source processing.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the exact main/KP/trace/vitamin stages in the maintained owner, restore original units and each source water context, split duplicate contributions and preserve source stock doses. Do not guess measured final concentration or double-count expanded stocks.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Remove or qualify unsupported external correspondence and represent the exact NBRC stocks with source-backed local identities/composition. Preserve valid standalone stock evidence as scoped context; do not modify those stocks merely to make them fit this medium.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Ground exact supplied hydrates and calcium salt from primary/structure evidence, and qualify unstated stereochemistry without guessing identifiers or converting masses using an unsupported form.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Restore exact preparation and condition scopes, keeping stock pH separate from main pH, explicit gas ratios separate from dissolved amounts, and unknown bases or cycle numbers unresolved.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Qualify or resolve the current secondary membership and obtain exact historical legacy correspondence before retaining an unqualified legacy link. Preserve original history and do not substitute a nearby mapping.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

After source-backed correction, attach narrow main/stock/condition evidence with actual hashes/times, use explicit stock names and regenerate separately under authorized gates. Preserve past history and stock-only evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AP11MH_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/ap11mh_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AP11MH_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AP11MH_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch029/290/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/290/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AP11MH_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AP11MH_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AP11MH_medium.yaml:1:id: CultureMech:008415<br>./data/normalized_yaml/bacterial/ap11mh_medium.yaml:1:id: CultureMech:008415<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/290/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 49 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075; Complete exact NBRC 1075 main table, KP/trace/vitamin tables and preparation | supports | Exact AP11MH source has four separate preparation stages. Its main pH is unadjusted; listed water and stock additions do not define a measured final volume. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841; Complete meta, four components sections and every comments object | supports | TOGO maps M1841 to NBRC_M1075, preserves original units and section boundaries, and supplies source-specific preparation comments. This exact JSON, not its JavaScript page, supports provider comparison. |
| prep | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075; Main preparation paragraph after pH | supports | The main gas mixture, separately sterilized stocks, filtration exceptions and pressure are explicit. Pressure is 150 kPa without absolute/gauge qualification. |
| trace-prep | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075; Trace-stock paragraph immediately after its water row | supports | Initial NTA-dissolution pH 6.5 and final stock pH 7.0 belong to trace stock, not the main medium. |
| solution6187 | https://mediadive.dsmz.de/rest/solution/6187; Entire exact solution API: id/name/volume, recipe objects, steps and compound identifiers | supports | Resolved asserted stock identity only. This formulation is not the NBRC 1075 stock with the same generic name. Existing exact amount evidence is verified only inside this local stock. |
| solution6187-local | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; Entire local stock including composition, placeholder ingredients, evidence, preparation, history and references | context_only | Full local dependency inspected as identity-comparison context. It is not a maintained owner or a separately reviewed target; no claim transfers to AP11MH by name. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; Entire exact solution API: id/name/volume, recipe objects, steps and compound identifiers | supports | Resolved asserted stock identity only. This formulation is not the NBRC 1075 stock with the same generic name. Existing exact amount evidence is verified only inside this local stock. |
| solution6241-local | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Entire local stock including composition, placeholder ingredients, evidence, preparation, history and references | context_only | Full local dependency inspected as identity-comparison context. It is not a maintained owner or a separately reviewed target; no claim transfers to AP11MH by name. |
| stock-index | data/normalized_yaml/solutions/mediadive_solution_index.json; Exact index rows mediadive.solution:6187 and 6241 | supports | {"mediadive.solution:6187": {"id": "mediadive.solution:6187", "name": "Trace element solution", "filename": "mediadive_6187_Trace_element_solution.yaml", "ingredient_count": 7}, "mediadive.solution:6241": {"id": "mediadive.solution:6241", "name": "Vitamin solution", "filename": "mediadive_6241_Vitamin_solution.yaml", "ingredient_count": 4}} |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:15377 resolves to water; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:15940 resolves to nicotinic acid; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:15956 resolves to biotin; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:16526 resolves to carbon dioxide; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:17015 resolves to riboflavin; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:176843 resolves to vitamin B12; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:17997 resolves to dinitrogen; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:18276 resolves to dihydrogen; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:26710 resolves to sodium chloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:27470 resolves to folic acid; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi29032 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29032; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:29032 resolves to (R)-pantothenate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:29377 resolves to sodium carbonate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:30753 resolves to 4-aminobenzoic acid; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:30961 resolves to pyridoxine hydrochloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:31206 resolves to ammonium chloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:32145 resolves to sodium hydroxide; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:32149 resolves to sodium sulfate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:32150 resolves to sodium thiosulfate pentahydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:32954 resolves to sodium acetate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:33118 resolves to boric acid; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:34887 resolves to nickel dichloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:35696 resolves to cobalt dichloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:44557 resolves to nitrilotriacetic acid; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:49105 resolves to thiamine hydrochloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:49976 resolves to zinc dichloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi63940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63940; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:63940 resolves to sodium tungstate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:75213 resolves to sodium molybdate dihydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:77775 resolves to sodium selenate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:86158 resolves to calcium chloride dihydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:86254 resolves to iron trichloride hexahydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:8806 resolves to Resazurin; source-specific hydration, salt and stereochemical support is assessed separately. |
| chebi91247 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247; Exact OLS identifier, label, obsolete flag and molecular definition/formula | supports | CHEBI:91247 resolves to L-cysteine hydrochloride; source-specific hydration, salt and stereochemical support is assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete pinned index exact lookup, including zero rows for CHEBI:29032 | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29032": [], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63940": [{"label": "Na2WO4", "match_type": "preferred_term", "identifier": "CHEBI:63940", "preferred_term": "Na2WO4", "ontology_id": "CHEBI:63940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:77775": [{"label": "Na2SeO4", "match_type": "preferred_term", "identifier": "CHEBI:77775", "preferred_term": "Na2SeO4", "ontology_id": "CHEBI:77775", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86254": [{"label": "FeCl3 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": ["CHEBI:29032"]} |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned current catalog/tree exact legacy 389 lookup; tree not truncated | context_only | No exact current legacy 389 correspondence found. Current absence does not authenticate or disprove its historical mapping; no guessed replacement. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned current catalog/tree exact legacy 389 lookup; tree not truncated | context_only | No exact current legacy 389 correspondence found. Current absence does not authenticate or disprove its historical mapping; no guessed replacement. |
| legacy-lookup | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/290/evidence-context-original.json; Full pinned index/catalog/tree exact search counts and hash-pinned records | context_only | {"identifier": "MediaIngredientMech:000389", "lookup_status": "completed_current_snapshot_absence", "index_data_rows": 9077, "index_matches": [], "catalog_rows": 2953, "catalog_matches": [], "catalog_source_key": "mimPinnedCatalog", "catalog_sha256": "474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7", "catalog_accessed_at": "2026-10-21T09:52:30.606764Z", "tree_entries": 7384, "tree_truncated": false, "tree_path_matches": [], "tree_source_key": "mimPinnedTree", "tree_sha256": "71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec", "tree_accessed_at": "2026-10-21T09:51:04.602158Z", "limit": "Current lookup is completed; historical correspondence remains unresolved. This legacy identifier is asserted on the target/owner, so it is distinct from merely unrelated parent context. No replacement mapping is inferred."} |
| history-metadata | data/merge_yaml/merged/AP11MH_medium.yaml; data/normalized_yaml/bacterial/ap11mh_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/ap11mh_medium.yaml", "events": 14, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source section parsing, name-based solution lookup, concentration copying and duplicate/merge handling are inspected context. Current cleanup does not sum differing concentrations. Historical notes record sums and a later identical-water collapse; do not claim current implementation caused the historical outputs. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source section parsing, name-based solution lookup, concentration copying and duplicate/merge handling are inspected context. Current cleanup does not sum differing concentrations. Historical notes record sums and a later identical-water collapse; do not claim current implementation caused the historical outputs. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source section parsing, name-based solution lookup, concentration copying and duplicate/merge handling are inspected context. Current cleanup does not sum differing concentrations. Historical notes record sums and a later identical-water collapse; do not claim current implementation caused the historical outputs. |
| writer-3 | scripts/repair_merged_duplicates.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source section parsing, name-based solution lookup, concentration copying and duplicate/merge handling are inspected context. Current cleanup does not sum differing concentrations. Historical notes record sums and a later identical-water collapse; do not claim current implementation caused the historical outputs. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source section parsing, name-based solution lookup, concentration copying and duplicate/merge handling are inspected context. Current cleanup does not sum differing concentrations. Historical notes record sums and a later identical-water collapse; do not claim current implementation caused the historical outputs. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch029/290/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Partial completion is specifically due to unresolved historical legacy 389 correspondence. Current CHEBI:29032 index absence is a completed lookup, not an unavailable check. The exact NBRC main and all three stock definitions and both wrong external stock identities are otherwise inspectable. No evidence or growth claim is transferred merely because generic stock names agree.
- External 6187/6241 are inspected dependencies, not additional reviewed targets. Their eight amount claims are verified only within their own declared stock bases. Their other anomalies, placeholder/history qualifiers and water/biotin representations are context for safe disambiguation, not authorization to change those files. All primary/source quantities remain separate from unknown measured final volume, percent basis and absolute/gauge pressure.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162629Z-culturemech-008415-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: ap11mh_medium (CultureMech:008415)'
started_at: '2026-10-21T16:17:56Z'
finished_at: '2026-10-21T16:26:29Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact NBRC 1075 and TOGO M1841 define a main medium plus separately prepared
  KP, trace-element and vitamin stocks. Both local layers flatten stock ingredients
  and misrepresent volume/milligram quantities; summed sodium/calcium and the target
  water total ignore stage boundaries. The two asserted external stock identifiers
  resolve to different formulations, so their eight verified stock-only amount claims
  do not authenticate AP11MH. Required preparation, gas and stock-pH context is absent.
  Supplied-form mismatches and a current secondary-index gap remain distinct from
  unresolved historical legacy 389 correspondence; that historical check makes the
  review partial.
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
  - path: data/merge_yaml/merged/AP11MH_medium.yaml
    sha256: 9a0637ccca978c1536521da149ac27484ee0a2ec8b7a60097782a0a7360b17cc
    role: target
  - path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
    sha256: 5a1c16086563b929d8b28015300df2a8983249e3015738810bf76c1956d38dec
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
    role: context
  - path: data/normalized_yaml/solutions/mediadive_solution_index.json
    sha256: 2e43ed2391d0113480837e0756120d71a8dad8a4490010054e67bfb90c66d381
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
  selection: Task review 290; batch 029 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-eight task batches
    contain 280 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 283 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008415
targets:
- target_id: CultureMech:008415
  path: data/merge_yaml/merged/AP11MH_medium.yaml
  label: ap11mh_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AP11MH_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AP11MH_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch029/290/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/290/strict.tsv"
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AP11MH_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AP11MH_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008415
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
  - CultureMech:008415
- check_id: legacy389-historical-correspondence
  name: Historical identity of asserted legacy MediaIngredientMech:000389
  required: true
  status: unavailable
  summary: Complete current index/catalog/tree lookup finished with no exact correspondence,
    but the historical source mapping required to verify this asserted legacy ID is
    unavailable. This is separate from the completed current CHEBI:29032 secondary
    gap.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - legacy-lookup
  - mimPinnedCatalog
  - mimPinnedTree
  - mim
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AP11MH_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/ap11mh_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AP11MH_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:43.061022Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AP11MH_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch029/290/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:44.229315Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/290/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AP11MH_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:45.543336Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AP11MH_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:46.532497Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:26:27Z'
  support: supports
  summary: './data/merge_yaml/merged/AP11MH_medium.yaml:1:id: CultureMech:008415

    ./data/normalized_yaml/bacterial/ap11mh_medium.yaml:1:id: CultureMech:008415

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/290/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:26:27Z'
  support: supports
  summary: 49 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 469f9541c707c37c6e3d281b5102354f0e2c64b169beba4d5ac2d4a95eb5b778
- evidence_id: primary
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075
  locator: Complete exact NBRC 1075 main table, KP/trace/vitamin tables and preparation
  accessed_at: '2026-10-21T16:01:41.386852Z'
  support: supports
  summary: Exact AP11MH source has four separate preparation stages. Its main pH is
    unadjusted; listed water and stock additions do not define a measured final volume.
  quote: Medium No. 1075 Medium AP11MH medium
  snapshot_sha256: 0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841
  locator: Complete meta, four components sections and every comments object
  accessed_at: '2026-10-21T16:01:40.056473Z'
  support: supports
  summary: TOGO maps M1841 to NBRC_M1075, preserves original units and section boundaries,
    and supplies source-specific preparation comments. This exact JSON, not its JavaScript
    page, supports provider comparison.
  snapshot_sha256: 00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6
- evidence_id: prep
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075
  locator: Main preparation paragraph after pH
  accessed_at: '2026-10-21T16:01:41.386852Z'
  support: supports
  summary: The main gas mixture, separately sterilized stocks, filtration exceptions
    and pressure are explicit. Pressure is 150 kPa without absolute/gauge qualification.
  quote: Pressurize the inoculated vessels to 150 kPa with H 2 /CO 2 .
  snapshot_sha256: 0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8
- evidence_id: trace-prep
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075
  locator: Trace-stock paragraph immediately after its water row
  accessed_at: '2026-10-21T16:01:41.386852Z'
  support: supports
  summary: Initial NTA-dissolution pH 6.5 and final stock pH 7.0 belong to trace stock,
    not the main medium.
  quote: First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and
    then add minerals. Final pH 7.0.
  snapshot_sha256: 0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8
- evidence_id: solution6187
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6187
  locator: 'Entire exact solution API: id/name/volume, recipe objects, steps and compound
    identifiers'
  accessed_at: '2026-10-21T14:16:58.890288Z'
  support: supports
  summary: Resolved asserted stock identity only. This formulation is not the NBRC
    1075 stock with the same generic name. Existing exact amount evidence is verified
    only inside this local stock.
  snapshot_sha256: d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916
- evidence_id: solution6187-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: Entire local stock including composition, placeholder ingredients, evidence,
    preparation, history and references
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Full local dependency inspected as identity-comparison context. It is not
    a maintained owner or a separately reviewed target; no claim transfers to AP11MH
    by name.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  locator: 'Entire exact solution API: id/name/volume, recipe objects, steps and compound
    identifiers'
  accessed_at: '2026-10-21T09:46:49.463537Z'
  support: supports
  summary: Resolved asserted stock identity only. This formulation is not the NBRC
    1075 stock with the same generic name. Existing exact amount evidence is verified
    only inside this local stock.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: solution6241-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Entire local stock including composition, placeholder ingredients, evidence,
    preparation, history and references
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Full local dependency inspected as identity-comparison context. It is not
    a maintained owner or a separately reviewed target; no claim transfers to AP11MH
    by name.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: stock-index
  kind: record_content
  reference: data/normalized_yaml/solutions/mediadive_solution_index.json
  locator: Exact index rows mediadive.solution:6187 and 6241
  accessed_at: '2026-10-21T16:26:27Z'
  support: supports
  summary: '{"mediadive.solution:6187": {"id": "mediadive.solution:6187", "name":
    "Trace element solution", "filename": "mediadive_6187_Trace_element_solution.yaml",
    "ingredient_count": 7}, "mediadive.solution:6241": {"id": "mediadive.solution:6241",
    "name": "Vitamin solution", "filename": "mediadive_6241_Vitamin_solution.yaml",
    "ingredient_count": 4}}'
  snapshot_sha256: 2e43ed2391d0113480837e0756120d71a8dad8a4490010054e67bfb90c66d381
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water; source-specific hydration, salt and stereochemical
    support is assessed separately.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin; source-specific hydration, salt and stereochemical
    support is assessed separately.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin; source-specific hydration, salt and
    stereochemical support is assessed separately.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12; source-specific hydration, salt and
    stereochemical support is assessed separately.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen; source-specific hydration, salt and
    stereochemical support is assessed separately.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi18276
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:27.615173Z'
  support: supports
  summary: CHEBI:18276 resolves to dihydrogen; source-specific hydration, salt and
    stereochemical support is assessed separately.
  snapshot_sha256: 47a32d9cfe41e3759385a0e4e002e9fa208fe1511d84e3d0d1f9f1ca9ce6e86d
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid; source-specific hydration, salt and
    stereochemical support is assessed separately.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi29032
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29032
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T16:01:40.896676Z'
  support: supports
  summary: CHEBI:29032 resolves to (R)-pantothenate; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 09b8e88386839f2c0111bf74dfd64335371f99f9e069def6ef7e28d88d0e0d48
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to sodium carbonate; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: CHEBI:32150 resolves to sodium thiosulfate pentahydrate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: CHEBI:32954 resolves to sodium acetate; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid; source-specific hydration, salt and
    stereochemical support is assessed separately.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63940
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T10:07:18.442988Z'
  support: supports
  summary: CHEBI:63940 resolves to sodium tungstate; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: c40f4b9c14d073989f58af77af0f1ffe969948e21d2bbe05a08c919f776aaf5c
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi77775
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:09.354177Z'
  support: supports
  summary: CHEBI:77775 resolves to sodium selenate; source-specific hydration, salt
    and stereochemical support is assessed separately.
  snapshot_sha256: a1a4ab87bbf08908fef7df53a788a85d9f6eee32350f082895e0563d6344c908
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86254
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:30.289392Z'
  support: supports
  summary: CHEBI:86254 resolves to iron trichloride hexahydrate; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: 89afba545ad02f24a850933df154af25dee37357b583f82de13866b44f18d683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate; source-specific
    hydration, salt and stereochemical support is assessed separately.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin; source-specific hydration, salt and stereochemical
    support is assessed separately.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91247
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247
  locator: Exact OLS identifier, label, obsolete flag and molecular definition/formula
  accessed_at: '2026-10-21T09:27:41.606984Z'
  support: supports
  summary: CHEBI:91247 resolves to L-cysteine hydrochloride; source-specific hydration,
    salt and stereochemical support is assessed separately.
  snapshot_sha256: 8ff9a3639e1afba34c0d40072292486ff792c7b63a496d189a1cfeb2e6574890
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete pinned index exact lookup, including zero rows for CHEBI:29032
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water",
    "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956":
    [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956",
    "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label":
    "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29032": [], "CHEBI:29377":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753":
    [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label":
    "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961",
    "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145":
    [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145",
    "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label":
    "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type":
    "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate",
    "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557":
    [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label":
    "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63940": [{"label": "Na2WO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63940", "preferred_term": "Na2WO4", "ontology_id": "CHEBI:63940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:77775": [{"label": "Na2SeO4", "match_type": "preferred_term", "identifier":
    "CHEBI:77775", "preferred_term": "Na2SeO4", "ontology_id": "CHEBI:77775", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86254": [{"label": "FeCl3 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id":
    "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318":
    [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465":
    [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}, "missing_current_keys": ["CHEBI:29032"]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned current catalog/tree exact legacy 389 lookup; tree not
    truncated
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: context_only
  summary: No exact current legacy 389 correspondence found. Current absence does
    not authenticate or disprove its historical mapping; no guessed replacement.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned current catalog/tree exact legacy 389 lookup; tree not
    truncated
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: context_only
  summary: No exact current legacy 389 correspondence found. Current absence does
    not authenticate or disprove its historical mapping; no guessed replacement.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-lookup
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/290/evidence-context-original.json
  locator: Full pinned index/catalog/tree exact search counts and hash-pinned records
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: '{"identifier": "MediaIngredientMech:000389", "lookup_status": "completed_current_snapshot_absence",
    "index_data_rows": 9077, "index_matches": [], "catalog_rows": 2953, "catalog_matches":
    [], "catalog_source_key": "mimPinnedCatalog", "catalog_sha256": "474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7",
    "catalog_accessed_at": "2026-10-21T09:52:30.606764Z", "tree_entries": 7384, "tree_truncated":
    false, "tree_path_matches": [], "tree_source_key": "mimPinnedTree", "tree_sha256":
    "71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec", "tree_accessed_at":
    "2026-10-21T09:51:04.602158Z", "limit": "Current lookup is completed; historical
    correspondence remains unresolved. This legacy identifier is asserted on the target/owner,
    so it is distinct from merely unrelated parent context. No replacement mapping
    is inferred."}'
  snapshot_sha256: b9f4bad35c4c8931ace898637f3eb68c4ed2059fcecfdbb1b4e5b9946657825a
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AP11MH_medium.yaml; data/normalized_yaml/bacterial/ap11mh_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/ap11mh_medium.yaml", "events": 14, "timestamp_issues":
    []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Current source section parsing, name-based solution lookup, concentration
    copying and duplicate/merge handling are inspected context. Current cleanup does
    not sum differing concentrations. Historical notes record sums and a later identical-water
    collapse; do not claim current implementation caused the historical outputs.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Current source section parsing, name-based solution lookup, concentration
    copying and duplicate/merge handling are inspected context. Current cleanup does
    not sum differing concentrations. Historical notes record sums and a later identical-water
    collapse; do not claim current implementation caused the historical outputs.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Current source section parsing, name-based solution lookup, concentration
    copying and duplicate/merge handling are inspected context. Current cleanup does
    not sum differing concentrations. Historical notes record sums and a later identical-water
    collapse; do not claim current implementation caused the historical outputs.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Current source section parsing, name-based solution lookup, concentration
    copying and duplicate/merge handling are inspected context. Current cleanup does
    not sum differing concentrations. Historical notes record sums and a later identical-water
    collapse; do not claim current implementation caused the historical outputs.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Current source section parsing, name-based solution lookup, concentration
    copying and duplicate/merge handling are inspected context. Current cleanup does
    not sum differing concentrations. Historical notes record sums and a later identical-water
    collapse; do not claim current implementation caused the historical outputs.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/290/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:26:27Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 2e9df4f8403a4df6ebe2b81c96ae7f68c8c5c3e38e23a7f17203ed1c1234933b
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Complete target/owner ontology and current secondary linkage
  outcome: concern
  summary: 39 distinct primary/current-secondary ontology IDs have exact nonobsolete
    labels. Each layer links 39/40 primary instances (97.50%) and 33/40 current secondary
    instances (82.50%), on a 0–100 linkage scale, not scientific accuracy. CHEBI:29032
    is valid live ontology but absent from the complete pinned MIM index; all other
    asserted current CHEBI keys have exact rows. Legacy 389 is a separate current
    absence with unresolved historical correspondence.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - record
  - owner-0
  - mim
  - legacy-lookup
  - chebi131527
  - chebi15377
  - chebi15940
  - chebi15956
  - chebi16526
  - chebi17015
  - chebi176843
  - chebi17997
  - chebi18276
  - chebi26710
  - chebi27470
  - chebi29032
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi32145
  - chebi32149
  - chebi32150
  - chebi32954
  - chebi33118
  - chebi34887
  - chebi35696
  - chebi44557
  - chebi49105
  - chebi49976
  - chebi63036
  - chebi63940
  - chebi75213
  - chebi76209
  - chebi77775
  - chebi86158
  - chebi86254
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi86465
  - chebi8806
  - chebi91247
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 28 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact source accession and asserted stock identity
  outcome: concern
  summary: TOGO M1841 and NBRC 1075 identify the same named main recipe. The exact
    standalone stock IDs resolve through the local index and public endpoints, but
    6187 has EDTA-based composition instead of NBRC NTA trace stock, and 6241 has
    three vitamins in 100 ml instead of nine in 1 L. Resolution is not formulation
    equivalence. KP has no external ID and its inline composition is empty.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - stock-index
  - solution6187
  - solution6241
  - solution6187-local
  - solution6241-local
- assessment_id: classification
  area: scope
  topic: Mixture class and biological claim boundaries
  outcome: supported
  summary: Liquid classification is consistent with no agar in the exact source. Yeast
    extract makes the recipe chemically undefined in part; COMPLEX/SEMI_DEFINED conveys
    a specified chemical basal recipe with a complex supplement. No target organism,
    strain, growth outcome, DOI/PMID or measured optimum is asserted. Do not infer
    them from the title or generic cultivation annotation.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
- assessment_id: forms
  area: grounding
  topic: Exact supplied forms versus stable chemical IDs
  outcome: concern
  summary: Source cobalt and nickel chlorides are hexahydrates, whereas CHEBI:35696
    and CHEBI:34887 are anhydrous salts. Source Ca-pantothenate is a calcium salt,
    unlike the calcium-free anion CHEBI:29032. Source cysteine-HCl does not establish
    the L configuration of CHEBI:91247. Vitamin B12 is a generic class in this source;
    the distinct cyanocobalamin in external 6241 must not narrow it. Remaining explicit
    hydrates agree with their captured generic structural forms; no new ID or amount
    conversion is inferred.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - primary
  - provider
  - chebi35696
  - chebi34887
  - chebi29032
  - chebi91247
  - chebi176843
  - solution6241
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 76 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"source_stage\": \"NBRC 1075 main batch\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[18], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Distilled water</td><td width='20%' align='right'>1</td><td\
    \ width='15%' align='left'>L</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Both mass units are wrong for source\
    \ 1 L water. Target 4.0 also sums water from four distinct preparation stages;\
    \ owner 1.0 collapsed identical rows but still loses their separate roles. Preserve\
    \ all four source water contexts without combining them as main water.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"label\": \"NaCl\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"NBRC 1075 main batch\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"31.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"31.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[9], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>NaCl</td><td width='20%' align='right'>30</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 30,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration. Local 31 combines main 30 g with undiluted trace-stock\
    \ 1 g; retain them separately and apply only the actual stock dose when a basis\
    \ is justified.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"label\": \"\
    CaCl2·2H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"NBRC 1075\
    \ main batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[5], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>CaCl<sub>2</sub>&middot;2H<sub>2</sub>O</td><td\
    \ width='20%' align='right'>0.15</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2·2H2O\\\",\\n          \\\"volume\\\": 0.15,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration. Local 0.25 combines main 0.15 g with undiluted trace-stock\
    \ 0.1 g; retain separate stages.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n\
    \    \"label\": \"NH4Cl\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.54\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.54\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[6], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>NH<sub>4</sub>Cl</td><td width='20%' align='right'>0.54</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.54,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"label\"\
    : \"Resazurin\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"NBRC\
    \ 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[14], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Resazurin</td><td width='20%' align='right'>1</td><td\
    \ width='15%' align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Source gives 1 mg resazurin; local\
    \ 1 G_PER_L loses the milligram unit. Restore source amount/unit with the original\
    \ batch context; no final-volume inference.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"label\": \"MgCl2·6H2O\",\n    \"decision\": \"correct\",\n  \
    \  \"source_stage\": \"NBRC 1075 main batch\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3.05\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[4], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>MgCl<sub>2</sub>&middot;6H<sub>2</sub>O</td><td\
    \ width='20%' align='right'>3.05</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2·6H2O\\\",\\n          \\\"volume\\\": 3.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"label\"\
    : \"Na2S·9H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"NBRC\
    \ 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[16], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Na<sub>2</sub>S&middot;9H<sub>2</sub>O</td><td\
    \ width='20%' align='right'>0.5</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S·9H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"label\"\
    : \"Sodium acetate\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    NBRC 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.82\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.82\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[11], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Sodium acetate</td><td width='20%' align='right'>0.82</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sodium acetate\\\",\\n          \\\"volume\\\"\
    : 0.82,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"Retain the exact original main batch amount\
    \ with its source unit. The main table lists 1 L water plus stock additions; it\
    \ does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"label\"\
    : \"Na2CO3\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"NBRC 1075\
    \ main batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[15], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Na<sub>2</sub>CO<sub>3</sub></td><td width='20%'\
    \ align='right'>1.5</td><td width='15%' align='left'>g</td></tr>\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"label\"\
    : \"Na2SO4\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"NBRC 1075\
    \ main batch\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.42\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.42\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[7], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Na<sub>2</sub>SO<sub>4</sub></td><td width='20%'\
    \ align='right'>1.42</td><td width='15%' align='left'>g</td></tr>\",\n       \
    \ \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SO4\\\",\\n          \\\"volume\\\": 1.42,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact original main batch\
    \ amount with its source unit. The main table lists 1 L water plus stock additions;\
    \ it does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"label\"\
    : \"Bacto Yeast Extract (Difco)\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[10], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Bacto Yeast Extract (Difco)</td><td width='20%'\
    \ align='right'>0.02</td><td width='15%' align='left'>g</td></tr>\",\n       \
    \ \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Bacto Yeast Extract (Difco)\\\",\\n          \\\
    \"volume\\\": 0.02,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Retain the exact original main batch amount\
    \ with its source unit. The main table lists 1 L water plus stock additions; it\
    \ does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"label\"\
    : \"Cysteine-HCl\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    NBRC 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[17], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Cysteine-HCl</td><td width='20%' align='right'>0.5</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Cysteine-HCl\\\",\\n          \\\"volume\\\":\
    \ 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"Retain the exact original main batch amount\
    \ with its source unit. The main table lists 1 L water plus stock additions; it\
    \ does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"label\"\
    : \"Na2S2O3·5H2O\",\n    \"decision\": \"correct\",\n    \"source_stage\": \"\
    NBRC 1075 main batch\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.24\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.24\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[8], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub>&middot;5H<sub>2</sub>O</td><td\
    \ width='20%' align='right'>1.24</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S2O3·5H2O\\\",\\n          \\\"volume\\\":\
    \ 1.24,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"Retain the exact original main batch amount\
    \ with its source unit. The main table lists 1 L water plus stock additions; it\
    \ does not establish a measured final-volume denominator. Current unqualified\
    \ G_PER_L needs a stated source batch/nominal basis, not an invented corrected\
    \ final concentration.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"label\"\
    : \"KP buffer* dose\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"Main stock addition\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"solutions[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[3], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr>\\n                 \
    \           <td colspan=\\\"2\\\" id=\\\"medium-comp\\\"><table width='600' border='0'><tr\
    \ height='1px'><td width='5%'>&nbsp;</td><td width='60%' align='left' colspan='4'>KP\
    \ buffer*</td><td width='20%' align='right'>5</td><td width='15%' align='left'>ml</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KP buffer*\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This is a source volume dose in ml,\
    \ not a mass in grams. Associate it only with its exact NBRC stock formulation;\
    \ do not retain generic-name external substitutions.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"label\": \"Trace element solution** dose\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"Main stock addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[12], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Trace element solution**</td><td width='20%'\
    \ align='right'>2</td><td width='15%' align='left'>ml</td></tr>\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution**\\\",\\n          \\\"\
    volume\\\": 2,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This is a source volume dose in ml, not\
    \ a mass in grams. Associate it only with its exact NBRC stock formulation; do\
    \ not retain generic-name external substitutions.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"label\": \"Vitamin solution*** dose\",\n    \"decision\": \"\
    correct\",\n    \"source_stage\": \"Main stock addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[13], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Vitamin solution***</td><td width='20%'\
    \ align='right'>2</td><td width='15%' align='left'>ml</td></tr>\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[0].items[15]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin solution***\\\",\\n          \\\"volume\\\
    \": 2,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a source volume dose in ml, not a mass\
    \ in grams. Associate it only with its exact NBRC stock formulation; do not retain\
    \ generic-name external substitutions.\"\n  },\n  {\n    \"decision_id\": \"q17\"\
    ,\n    \"label\": \"KH2PO4\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"KP buffer stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"53\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"53\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[24], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>KH<sub>2</sub>PO<sub>4</sub></td><td width='20%' align='right'>53</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 53,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This gram amount belongs to separately\
    \ prepared KP buffer with 1 L water; main adds 5 ml. It is not an undiluted direct\
    \ main ingredient. Reconstruct the currently empty KP composition.\"\n  },\n \
    \ {\n    \"decision_id\": \"q18\",\n    \"label\": \"K2HPO4\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"KP buffer stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"106\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"106\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[25], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>K<sub>2</sub>HPO<sub>4</sub></td><td width='20%' align='right'>106</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 106,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This gram amount belongs to separately\
    \ prepared KP buffer with 1 L water; main adds 5 ml. It is not an undiluted direct\
    \ main ingredient. Reconstruct the currently empty KP composition.\"\n  },\n \
    \ {\n    \"decision_id\": \"q19\",\n    \"label\": \"NaCl\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"NBRC 1075 trace-element stock\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"31.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"31.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[39], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>NaCl</td><td width='20%' align='right'>1</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"label\": \"CaCl2·2H2O\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[34], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>CaCl<sub>2</sub>&middot;2H<sub>2</sub>O</td><td width='20%' align='right'>0.1</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2·2H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"label\": \"Na2MoO4·2H2O\",\n    \"decision\": \"correct\",\n\
    \    \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[18].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[38], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Na<sub>2</sub>MoO<sub>4</sub>&middot;2H<sub>2</sub>O</td><td width='20%'\
    \ align='right'>0.024</td><td width='15%' align='left'>g</td></tr>\",\n      \
    \  \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4·2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.024,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This exact source amount belongs to the\
    \ NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct\
    \ main concentration and is not the differently formulated external 6187 stock.\
    \ Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\": \"q22\"\
    ,\n    \"label\": \"H3BO3\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 trace-element stock\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"\
    field_path\": \"solutions[1]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Trace element solution**\",\n          \"term\": {\n            \"id\": \"\
    mediadive.solution:6187\",\n            \"label\": \"Trace element solution\"\n\
    \          },\n          \"concentration\": {\n            \"value\": \"2\",\n\
    \            \"unit\": \"G_PER_L\"\n          },\n          \"notes\": \"See mediadive_6187_Trace_element_solution.yaml\
    \ for composition\",\n          \"name\": \"Unknown solution\"\n        }\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[37], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>H<sub>3</sub>BO<sub>3</sub></td><td width='20%' align='right'>0.01</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"label\": \"MnCl2·4H2O\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[20].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[32], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>MnCl<sub>2</sub>&middot;4H<sub>2</sub>O</td><td width='20%' align='right'>0.1</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2·4H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"label\": \"CoCl2·6H2O\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[21].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[33], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>CoCl<sub>2</sub>&middot;6H<sub>2</sub>O</td><td width='20%' align='right'>0.024</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2·6H2O\\\",\\n          \\\"volume\\\": 0.024,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"label\": \"NiCl2·6H2O\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.12\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[22].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.12\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[40], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>NiCl<sub>2</sub>&middot;6H<sub>2</sub>O</td><td width='20%' align='right'>0.12</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2·6H2O\\\",\\n          \\\"volume\\\": 0.12,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q26\",\n    \"label\": \"CuCl2·2H2O\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[23].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[36], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>CuCl<sub>2</sub>&middot;2H<sub>2</sub>O</td><td width='20%' align='right'>0.025</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2·2H2O\\\",\\n          \\\"volume\\\": 0.025,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q27\",\n    \"label\": \"ZnCl2\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[24].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[35], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>ZnCl<sub>2</sub></td><td width='20%' align='right'>0.1</td><td width='15%'\
    \ align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q28\",\n    \"label\": \"FeCl3·6H2O\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.35\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[25].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.35\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[31], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>FeCl<sub>3</sub>&middot;6H<sub>2</sub>O</td><td width='20%' align='right'>1.35</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl3·6H2O\\\",\\n          \\\"volume\\\": 1.35,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q29\",\n    \"label\": \"KAl(SO4)2·12H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.018\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[26].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.018\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[43], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>KAl(SO<sub>4</sub>)<sub>2</sub>&middot;12H<sub>2</sub>O</td><td\
    \ width='20%' align='right'>0.018</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KAl(SO4)2·12H2O\\\",\\n          \\\"volume\\\"\
    : 0.018,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This exact source amount belongs to the\
    \ NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct\
    \ main concentration and is not the differently formulated external 6187 stock.\
    \ Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\": \"q30\"\
    ,\n    \"label\": \"Nitrilotriacetic acid (NTA)\",\n    \"decision\": \"correct\"\
    ,\n    \"source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.8\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[27].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"12.8\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[30], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Nitrilotriacetic acid (NTA)</td><td width='20%' align='right'>12.8</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid (NTA)\\\",\\n          \\\
    \"volume\\\": 12.8,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This exact source amount belongs to the\
    \ NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a direct\
    \ main concentration and is not the differently formulated external 6187 stock.\
    \ Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\": \"q31\"\
    ,\n    \"label\": \"Na2WO4\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 trace-element stock\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[28].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.004\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"\
    field_path\": \"solutions[1]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Trace element solution**\",\n          \"term\": {\n            \"id\": \"\
    mediadive.solution:6187\",\n            \"label\": \"Trace element solution\"\n\
    \          },\n          \"concentration\": {\n            \"value\": \"2\",\n\
    \            \"unit\": \"G_PER_L\"\n          },\n          \"notes\": \"See mediadive_6187_Trace_element_solution.yaml\
    \ for composition\",\n          \"name\": \"Unknown solution\"\n        }\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[42], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Na<sub>2</sub>WO<sub>4</sub></td><td width='20%' align='right'>0.004</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4\\\",\\n          \\\"volume\\\": 0.004,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q32\",\n    \"label\": \"Na2SeO4\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"NBRC 1075 trace-element stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[29].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[41], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Na<sub>2</sub>SeO<sub>4</sub></td><td width='20%' align='right'>0.004</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO4\\\",\\n          \\\"volume\\\": 0.004,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact source amount belongs\
    \ to the NBRC NTA trace stock with 1 L water; main receives 2 ml. It is not a\
    \ direct main concentration and is not the differently formulated external 6187\
    \ stock. Preserve the printed salt/hydrate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q33\",\n    \"label\": \"Biotin\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"\
    field_path\": \"ingredients[31].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"\
    preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n          \
    \  \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin solution\"\
    \n          },\n          \"concentration\": {\n            \"value\": \"2\",\n\
    \            \"unit\": \"G_PER_L\"\n          },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml\
    \ for composition\",\n          \"name\": \"Unknown solution\"\n        }\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n   \
    \     \"source_locator\": \"NBRC 1075 exact raw HTML table row[49], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Biotin</td><td width='20%' align='right'>2</td><td width='15%' align='left'>mg</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This is a milligram amount in the\
    \ separate nine-vitamin stock with 1 L water, not the same numeral in grams per\
    \ liter of main medium. Main receives 2 ml of this stock; the differently formulated\
    \ external 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q34\"\
    ,\n    \"label\": \"p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n \
    \   \"source_stage\": \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[32].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n     \
    \   \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[56], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'><i>p</i>-Aminobenzoic acid</td><td width='20%' align='right'>1</td><td\
    \ width='15%' align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p-Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 1,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a milligram amount in the separate\
    \ nine-vitamin stock with 1 L water, not the same numeral in grams per liter of\
    \ main medium. Main receives 2 ml of this stock; the differently formulated external\
    \ 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"\
    label\": \"Thiamine-HCl\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[33].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[33].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n     \
    \   \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[52], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Thiamine-HCl</td><td width='20%' align='right'>5</td><td width='15%'\
    \ align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine-HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a milligram amount in the separate\
    \ nine-vitamin stock with 1 L water, not the same numeral in grams per liter of\
    \ main medium. Main receives 2 ml of this stock; the differently formulated external\
    \ 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"\
    label\": \"Ca-pantothenate\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[34].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[34].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n     \
    \   \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[55], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Ca-pantothenate</td><td width='20%' align='right'>5</td><td width='15%'\
    \ align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Ca-pantothenate\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a milligram amount in the separate\
    \ nine-vitamin stock with 1 L water, not the same numeral in grams per liter of\
    \ main medium. Main receives 2 ml of this stock; the differently formulated external\
    \ 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"\
    label\": \"Pyridoxine-HCl\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[35].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[35].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n    \
    \    \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[51], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Pyridoxine-HCl</td><td width='20%' align='right'>10</td><td width='15%'\
    \ align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine-HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a milligram amount in the separate\
    \ nine-vitamin stock with 1 L water, not the same numeral in grams per liter of\
    \ main medium. Main receives 2 ml of this stock; the differently formulated external\
    \ 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"\
    label\": \"Folic acid\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[36].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[36].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n     \
    \   \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[50], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Folic acid</td><td width='20%' align='right'>2</td><td width='15%'\
    \ align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This is a milligram amount in the\
    \ separate nine-vitamin stock with 1 L water, not the same numeral in grams per\
    \ liter of main medium. Main receives 2 ml of this stock; the differently formulated\
    \ external 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q39\"\
    ,\n    \"label\": \"Vitamin B12\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[37].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[37].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n  \
    \      \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"\
    preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n          \
    \  \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin solution\"\
    \n          },\n          \"concentration\": {\n            \"value\": \"2\",\n\
    \            \"unit\": \"G_PER_L\"\n          },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml\
    \ for composition\",\n          \"name\": \"Unknown solution\"\n        }\n  \
    \    }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[57], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Vitamin B<sub>12</sub></td><td width='20%' align='right'>0.01</td><td\
    \ width='15%' align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This is a milligram amount in the\
    \ separate nine-vitamin stock with 1 L water, not the same numeral in grams per\
    \ liter of main medium. Main receives 2 ml of this stock; the differently formulated\
    \ external 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q40\"\
    ,\n    \"label\": \"Riboflavin\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[38].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[38].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n     \
    \   \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[53], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Riboflavin</td><td width='20%' align='right'>5</td><td width='15%'\
    \ align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"This is a milligram amount in the\
    \ separate nine-vitamin stock with 1 L water, not the same numeral in grams per\
    \ liter of main medium. Main receives 2 ml of this stock; the differently formulated\
    \ external 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q41\"\
    ,\n    \"label\": \"Nicotinic acid\",\n    \"decision\": \"correct\",\n    \"\
    source_stage\": \"NBRC 1075 vitamin stock\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"\
    field_path\": \"ingredients[39].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"\
    preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n          \
    \  \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin solution\"\
    \n          },\n          \"concentration\": {\n            \"value\": \"2\",\n\
    \            \"unit\": \"G_PER_L\"\n          },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml\
    \ for composition\",\n          \"name\": \"Unknown solution\"\n        }\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[39].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n   \
    \     \"source_locator\": \"NBRC 1075 exact raw HTML table row[54], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Nicotinic acid</td><td width='20%' align='right'>5</td><td width='15%'\
    \ align='left'>mg</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a milligram amount in the separate\
    \ nine-vitamin stock with 1 L water, not the same numeral in grams per liter of\
    \ main medium. Main receives 2 ml of this stock; the differently formulated external\
    \ 6241 does not substitute.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n    \"\
    label\": \"Water for KP stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Stock water: KP\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"4.0\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"KP buffer*\",\n          \"composition\": [],\n     \
    \     \"concentration\": {\n            \"value\": \"5\",\n            \"unit\"\
    : \"G_PER_L\"\n          },\n          \"name\": \"Unknown solution\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"KP buffer*\",\n          \"composition\": [],\n     \
    \     \"concentration\": {\n            \"value\": \"5\",\n            \"unit\"\
    : \"G_PER_L\"\n          },\n          \"name\": \"Unknown solution\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[26], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Distilled water</td><td width='20%' align='right'>1</td><td width='15%'\
    \ align='left'>L</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 1 L water within this stock\
    \ preparation. The target sums four waters and owner collapses them; neither retains\
    \ all four preparation stages. This water is not another 1 L directly added to\
    \ main medium.\"\n  },\n  {\n    \"decision_id\": \"q43\",\n    \"label\": \"\
    Water for trace stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Stock water: trace\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"4.0\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Trace element solution**\",\n          \"term\": {\n\
    \            \"id\": \"mediadive.solution:6187\",\n            \"label\": \"Trace\
    \ element solution\"\n          },\n          \"concentration\": {\n         \
    \   \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n     \
    \     \"notes\": \"See mediadive_6187_Trace_element_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[44], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Distilled water</td><td width='20%' align='right'>1</td><td width='15%'\
    \ align='left'>L</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 1 L water within this stock\
    \ preparation. The target sums four waters and owner collapses them; neither retains\
    \ all four preparation stages. This water is not another 1 L directly added to\
    \ main medium.\"\n  },\n  {\n    \"decision_id\": \"q44\",\n    \"label\": \"\
    Water for vitamin stock\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Stock water: vitamin\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"4.0\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2]\",\n        \"stored\": {\n        \
    \  \"preferred_term\": \"Vitamin solution***\",\n          \"term\": {\n     \
    \       \"id\": \"mediadive.solution:6241\",\n            \"label\": \"Vitamin\
    \ solution\"\n          },\n          \"concentration\": {\n            \"value\"\
    : \"2\",\n            \"unit\": \"G_PER_L\"\n          },\n          \"notes\"\
    : \"See mediadive_6241_Vitamin_solution.yaml for composition\",\n          \"\
    name\": \"Unknown solution\"\n        }\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\",\n   \
    \     \"field_path\": \"solutions[2]\",\n        \"stored\": {\n          \"preferred_term\"\
    : \"Vitamin solution***\",\n          \"term\": {\n            \"id\": \"mediadive.solution:6241\"\
    ,\n            \"label\": \"Vitamin solution\"\n          },\n          \"concentration\"\
    : {\n            \"value\": \"2\",\n            \"unit\": \"G_PER_L\"\n      \
    \    },\n          \"notes\": \"See mediadive_6241_Vitamin_solution.yaml for composition\"\
    ,\n          \"name\": \"Unknown solution\"\n        }\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"nbrc1075\",\n       \
    \ \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[58], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='5%'>&nbsp;</td><td width='50%' align='left'\
    \ colspan='2'>Distilled water</td><td width='20%' align='right'>1</td><td width='15%'\
    \ align='left'>L</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"togoM1841\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1841\",\n\
    \        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"00f3d13967abfc0e5f8f9ae7e0bfb9294796f46ce8cc1629e30e09a5f34745d6\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 1 L water within this stock\
    \ preparation. The target sums four waters and owner collapses them; neither retains\
    \ all four preparation stages. This water is not another 1 L directly added to\
    \ main medium.\"\n  },\n  {\n    \"decision_id\": \"q45\",\n    \"label\": \"\
    Hydrogen gas mixture component\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"Main dispensing atmosphere\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main dispensing gas-mixture sentence\",\n   \
    \     \"exact_source_quote\": \"H 2 /CO 2 (80/20)\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE alone obscures the explicit\
    \ H2/CO2 ratio 80/20. Preserve that ratio and its gas-atmosphere stage without\
    \ assigning dissolved molarity or inventing an unstated percentage basis.\"\n\
    \  },\n  {\n    \"decision_id\": \"q46\",\n    \"label\": \"Carbon dioxide gas\
    \ mixture component\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"Main dispensing atmosphere\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main dispensing gas-mixture sentence\",\n   \
    \     \"exact_source_quote\": \"H 2 /CO 2 (80/20)\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE alone obscures the explicit\
    \ H2/CO2 ratio 80/20. Preserve that ratio and its gas-atmosphere stage without\
    \ assigning dissolved molarity or inventing an unstated percentage basis.\"\n\
    \  },\n  {\n    \"decision_id\": \"q47\",\n    \"label\": \"Nitrogen atmosphere\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_stage\": \"KP and separate\
    \ reductant stock handling\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"variable\",\n          \"unit\"\
    : \"VARIABLE\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Separate stock-autoclaving sentence\",\n    \
    \    \"exact_source_quote\": \"under a N 2 atmosphere.\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"KP stock preparation\",\n        \"exact_source_quote\"\
    : \"Autoclaved under N 2 .\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    ,\n        \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"N2 atmosphere is named without a\
    \ purity percentage, volume or dissolved concentration. Keep it scoped to stock\
    \ handling; do not infer 100% or a main nutrient dose.\"\n  },\n  {\n    \"decision_id\"\
    : \"q48\",\n    \"label\": \"NaOH stock pH adjustment\",\n    \"decision\": \"\
    not_quantified\",\n    \"source_stage\": \"Trace-stock NTA dissolution\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Trace-stock preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 6.5 with NaOH\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    ,\n        \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"NaOH strength and amount are not\
    \ specified. VARIABLE is compatible with an unquantified adjustment only when\
    \ scoped to trace-stock NTA dissolution, not a fixed main ingredient.\"\n  },\n\
    \  {\n    \"decision_id\": \"q49\",\n    \"label\": \"Main pH unadjusted\",\n\
    \    \"decision\": \"add\",\n    \"source_stage\": \"Main preparation\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main pH row\",\n        \"exact_source_quote\"\
    : \"pH unajusted\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    ,\n        \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"Preserve the source statement that\
    \ main pH is unadjusted. It supplies no numerical main pH; do not replace it with\
    \ trace-stock pH 6.5 or 7.0.\"\n  },\n  {\n    \"decision_id\": \"q50\",\n   \
    \ \"label\": \"Initial trace-stock pH\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Trace-stock preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"presence\": \"absent\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Trace-stock preparation paragraph\",\n      \
    \  \"exact_source_quote\": \"adjust pH to 6.5 with NaOH\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"Record 6.5 at NTA dissolution before\
    \ the minerals.\"\n  },\n  {\n    \"decision_id\": \"q51\",\n    \"label\": \"\
    Final trace-stock pH\",\n    \"decision\": \"add\",\n    \"source_stage\": \"\
    Trace-stock preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"presence\": \"absent\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Trace-stock preparation paragraph\",\n      \
    \  \"exact_source_quote\": \"Final pH 7.0.\",\n        \"snapshot_sha256\": \"\
    0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n        \"\
    parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"Record 7.0 for the completed trace\
    \ stock, not the main medium.\"\n  },\n  {\n    \"decision_id\": \"q52\",\n  \
    \  \"label\": \"Sulfide stock strength\",\n    \"decision\": \"add\",\n    \"\
    source_stage\": \"Late-added stock strength\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n    \
    \    \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n     \
    \   \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main separate-stock preparation paragraph\",\n\
    \        \"exact_source_quote\": \"Na 2 S·9H 2 O (5% solution)\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    ,\n        \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"The source 5% is unqualified; do\
    \ not convert to g/ml without its mass/volume basis.\"\n  },\n  {\n    \"decision_id\"\
    : \"q53\",\n    \"label\": \"Cysteine-HCl stock strength\",\n    \"decision\"\
    : \"add\",\n    \"source_stage\": \"Late-added stock strength\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main separate-stock preparation paragraph\",\n\
    \        \"exact_source_quote\": \"cysteine-HCl (5% solution)\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"The source 5% is unqualified; no\
    \ independent stock dose follows from it.\"\n  },\n  {\n    \"decision_id\": \"\
    q54\",\n    \"label\": \"Carbonate stock strength\",\n    \"decision\": \"add\"\
    ,\n    \"source_stage\": \"Late-added stock strength\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main separate-stock preparation paragraph\",\n\
    \        \"exact_source_quote\": \"10% Na 2 CO 3 solutions\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"The source 10% is unqualified; preserve\
    \ the filtration stage and do not invent a volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q55\",\n    \"label\": \"Sulfide stock dose\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Late-added stock dose\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main separate-stock preparation\",\n        \"\
    exact_source_quote\": \"Na 2 S·9H 2 O (5% solution)\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[16], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Na<sub>2</sub>S&middot;9H<sub>2</sub>O</td><td\
    \ width='20%' align='right'>0.5</td><td width='15%' align='left'>g</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      }\n    ],\n    \"interpretation\": \"Source main mass and an unqualified\
    \ stock percentage do not define a volume dose without a verified percentage basis.\
    \ Do not fill a guessed ml value.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n\
    \    \"label\": \"Cysteine-HCl stock dose\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Late-added stock dose\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main separate-stock preparation\",\n        \"\
    exact_source_quote\": \"cysteine-HCl (5% solution)\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[17], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Cysteine-HCl</td><td width='20%' align='right'>0.5</td><td\
    \ width='15%' align='left'>g</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      }\n    ],\n    \"interpretation\": \"Source main mass and an unqualified\
    \ stock percentage do not define a volume dose without a verified percentage basis.\
    \ Do not fill a guessed ml value.\"\n  },\n  {\n    \"decision_id\": \"q57\",\n\
    \    \"label\": \"Carbonate stock dose\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Late-added stock dose\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main separate-stock preparation\",\n        \"\
    exact_source_quote\": \"10% Na 2 CO 3 solutions\",\n        \"snapshot_sha256\"\
    : \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\",\n    \
    \    \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[15], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Na<sub>2</sub>CO<sub>3</sub></td><td width='20%'\
    \ align='right'>1.5</td><td width='15%' align='left'>g</td></tr>\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      }\n    ],\n    \"interpretation\": \"Source main mass and an unqualified\
    \ stock percentage do not define a volume dose without a verified percentage basis.\
    \ Do not fill a guessed ml value.\"\n  },\n  {\n    \"decision_id\": \"q58\",\n\
    \    \"label\": \"Pressurization\",\n    \"decision\": \"add\",\n    \"source_stage\"\
    : \"Main culture-vessel pressure\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"presence\": \"\
    absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"Main final preparation sentence\",\n        \"\
    exact_source_quote\": \"Pressurize the inoculated vessels to 150 kPa with H 2\
    \ /CO 2 .\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    ,\n        \"parsed_text_sha256\": \"8f14c290259221bfe61edef01d5e81c35a3dc38fc0258b1cdc8f32f76ef2f525\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain 150 kPa and the named gas;\
    \ absolute versus gauge is not stated, so neither qualifier is invented.\"\n \
    \ },\n  {\n    \"decision_id\": \"q59\",\n    \"label\": \"Stock sterilization\
    \ and staged addition\",\n    \"decision\": \"add\",\n    \"source_stage\": \"\
    Source-specific preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"presence\": \"absent\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[21], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='90%' colspan='5'>Mix ingredients except for\
    \ KP buffer, vitamin solution, Na<sub>2</sub>CO<sub>3</sub>, Na<sub>2</sub>S&middot;9H<sub>2</sub>O\
    \ and cysteine-HCl. Dispense the medium into suitable culture vessels under a\
    \ stream of H<sub>2</sub>/CO<sub>2</sub> (80/20) and seal with butyl rubber stoppers.\
    \ Separately autoclave KP buffer, Na<sub>2</sub>S&middot;9H<sub>2</sub>O (5% solution)\
    \ and cysteine-HCl (5% solution) under a N<sub>2</sub> atmosphere. Sterilize vitamin\
    \ and 10% Na<sub>2</sub>CO<sub>3</sub> solutions by filtration. Prior to inoculation,\
    \ aseptically and anaerobically add KP buffer, vitamin, Na<sub>2</sub>CO<sub>3</sub>,\
    \ Na<sub>2</sub>S&middot;9H<sub>2</sub>O and cysteine-HCl solutions. Pressurize\
    \ the inoculated vessels to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[27], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td  width='90%' colspan='5'>Autoclaved under N<sub>2</sub>.</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain separately autoclaved KP and\
    \ reductant stocks under N2, filtered vitamin/carbonate stocks and aseptic anaerobic\
    \ late addition. No exact sterilization time/temperature is printed on this NBRC\
    \ page.\"\n  },\n  {\n    \"decision_id\": \"q60\",\n    \"label\": \"Unspecified\
    \ sterilization time and temperature\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Source preparation limits\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"presence\": \"absent\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[21], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td width='90%' colspan='5'>Mix ingredients except for\
    \ KP buffer, vitamin solution, Na<sub>2</sub>CO<sub>3</sub>, Na<sub>2</sub>S&middot;9H<sub>2</sub>O\
    \ and cysteine-HCl. Dispense the medium into suitable culture vessels under a\
    \ stream of H<sub>2</sub>/CO<sub>2</sub> (80/20) and seal with butyl rubber stoppers.\
    \ Separately autoclave KP buffer, Na<sub>2</sub>S&middot;9H<sub>2</sub>O (5% solution)\
    \ and cysteine-HCl (5% solution) under a N<sub>2</sub> atmosphere. Sterilize vitamin\
    \ and 10% Na<sub>2</sub>CO<sub>3</sub> solutions by filtration. Prior to inoculation,\
    \ aseptically and anaerobically add KP buffer, vitamin, Na<sub>2</sub>CO<sub>3</sub>,\
    \ Na<sub>2</sub>S&middot;9H<sub>2</sub>O and cysteine-HCl solutions. Pressurize\
    \ the inoculated vessels to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[27], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='5%'>&nbsp;</td><td  width='90%' colspan='5'>Autoclaved under N<sub>2</sub>.</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not import JCM default 121°C/15\
    \ min or other collection conditions into this exact NBRC recipe; the source supplies\
    \ methods but no cycle numbers.\"\n  },\n  {\n    \"decision_id\": \"q61\",\n\
    \    \"label\": \"Measured final volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"Main final-volume limit\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/AP11MH_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"KP buffer*\",\n            \"composition\"\
    : [],\n            \"concentration\": {\n              \"value\": \"5\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"Unknown\
    \ solution\"\n          },\n          {\n            \"preferred_term\": \"Trace\
    \ element solution**\",\n            \"term\": {\n              \"id\": \"mediadive.solution:6187\"\
    ,\n              \"label\": \"Trace element solution\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"2\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"notes\": \"See mediadive_6187_Trace_element_solution.yaml\
    \ for composition\",\n            \"name\": \"Unknown solution\"\n          },\n\
    \          {\n            \"preferred_term\": \"Vitamin solution***\",\n     \
    \       \"term\": {\n              \"id\": \"mediadive.solution:6241\",\n    \
    \          \"label\": \"Vitamin solution\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"See mediadive_6241_Vitamin_solution.yaml\
    \ for composition\",\n            \"name\": \"Unknown solution\"\n          }\n\
    \        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ap11mh_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"KP buffer*\",\n            \"composition\"\
    : [],\n            \"concentration\": {\n              \"value\": \"5\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"Unknown\
    \ solution\"\n          },\n          {\n            \"preferred_term\": \"Trace\
    \ element solution**\",\n            \"term\": {\n              \"id\": \"mediadive.solution:6187\"\
    ,\n              \"label\": \"Trace element solution\"\n            },\n     \
    \       \"concentration\": {\n              \"value\": \"2\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"notes\": \"See mediadive_6187_Trace_element_solution.yaml\
    \ for composition\",\n            \"name\": \"Unknown solution\"\n          },\n\
    \          {\n            \"preferred_term\": \"Vitamin solution***\",\n     \
    \       \"term\": {\n              \"id\": \"mediadive.solution:6241\",\n    \
    \          \"label\": \"Vitamin solution\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"2\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"notes\": \"See mediadive_6241_Vitamin_solution.yaml\
    \ for composition\",\n            \"name\": \"Unknown solution\"\n          }\n\
    \        ]\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1075\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\"\
    ,\n        \"source_locator\": \"NBRC 1075 exact raw HTML table row[18], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Distilled water</td><td width='20%' align='right'>1</td><td\
    \ width='15%' align='left'>L</td></tr>\",\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[3], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr>\\n                 \
    \           <td colspan=\\\"2\\\" id=\\\"medium-comp\\\"><table width='600' border='0'><tr\
    \ height='1px'><td width='5%'>&nbsp;</td><td width='60%' align='left' colspan='4'>KP\
    \ buffer*</td><td width='20%' align='right'>5</td><td width='15%' align='left'>ml</td></tr>\"\
    ,\n        \"snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[12], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Trace element solution**</td><td width='20%'\
    \ align='right'>2</td><td width='15%' align='left'>ml</td></tr>\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      },\n      {\n        \"source_key\": \"nbrc1075\",\n        \"source_url\"\
    : \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1075\",\n\
    \        \"source_locator\": \"NBRC 1075 exact raw HTML table row[13], zero-based\
    \ document row\",\n        \"exact_source_quote\": \"<tr height='1px'><td width='5%'>&nbsp;</td><td\
    \ width='60%' align='left' colspan='4'>Vitamin solution***</td><td width='20%'\
    \ align='right'>2</td><td width='15%' align='left'>ml</td></tr>\",\n        \"\
    snapshot_sha256\": \"0f6958a7a09680efccd7161d3cad3d8267c0ace526418f0d158f259d3dceeae8\"\
    \n      }\n    ],\n    \"interpretation\": \"Main lists 1 L water plus 5, 2 and\
    \ 2 ml named stocks and other late stocks whose volumes are unspecified. Neither\
    \ summing all four stock preparations nor summing known doses establishes a measured\
    \ final volume. Retain original batch quantities and explicit nominal calculations\
    \ only.\"\n  },\n  {\n    \"decision_id\": \"q62\",\n    \"label\": \"solution6187\
    \ Na2-EDTA\",\n    \"decision\": \"verified\",\n    \"source_stage\": \"External\
    \ asserted-stock identity context only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.75\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"Na2-EDTA\\\",\\n                \\\"compound_id\\\": 34,\\n          \
    \      \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.75,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.75,\\n                \\\"mmol_l\\\
    \": 2.23078,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6187\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 1,\\\
    n                \\\"compound\\\": \\\"Na2-EDTA\\\",\\n                \\\"compound_id\\\
    \": 34,\\n                \\\"solution\\\": null,\\n                \\\"solution_id\\\
    \": null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 0.75,\\n                \\\"unit\\\
    \": \\\"g\\\",\\n                \\\"g_l\\\": 0.75,\\n                \\\"mmol_l\\\
    \": 2.23078,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"explanation\": \"Concentration evidence for composition[0].concentration\
    \ (Na2-EDTA) in MediaDive solution 6187; locator=$.data.recipe[0] (compound_id=34).\
    \ Provider explicitly reports g_l=0.75. Arithmetic check: 0.75 g * 1 g/g / (1000\
    \ ml / 1000 ml per L) = 0.75 g/L, consistent with the reported value at its precision.\
    \ Evidence supports the provider-declared concentration within this solution,\
    \ not a concentration in a receiving medium or an independently measured final\
    \ volume. Water addition alone is not used to infer a final volume. Additional\
    \ exact excerpt at $.data.volume: \\\"volume\\\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00;\
    \ response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q63\",\n    \"label\": \"\
    solution6187 Distilled water\",\n    \"decision\": \"correct\",\n    \"source_stage\"\
    : \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"PERCENT_V_V\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Water is a source volume, not 1000%\
    \ v/v.\"\n  },\n  {\n    \"decision_id\": \"q64\",\n    \"label\": \"solution6187\
    \ FeCl3 x 6 H2O\",\n    \"decision\": \"verified\",\n    \"source_stage\": \"\
    External asserted-stock identity context only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.097\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"FeCl3 x 6 H2O\\\",\\n                \\\"compound_id\\\": 82,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 97,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.097,\\n                \\\"mmol_l\\\
    \": 0.358866,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6187\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 4,\\\
    n                \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                \\\
    \"compound_id\\\": 82,\\n                \\\"solution\\\": null,\\n          \
    \      \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 97,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.097,\\\
    n                \\\"mmol_l\\\": 0.358866,\\n                \\\"optional\\\"\
    : 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[2].concentration (FeCl3 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[2]\
    \ (compound_id=82). Provider explicitly reports g_l=0.097. Arithmetic check: 97\
    \ mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.097 g/L, consistent with the\
    \ reported value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00;\
    \ response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q65\",\n    \"label\": \"\
    solution6187 MnCl2 x 4 H2O\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.041\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"MnCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 36,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 41,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.041,\\n                \\\"mmol_l\\\
    \": 0.20717,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6187\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 5,\\\
    n                \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                \\\
    \"compound_id\\\": 36,\\n                \\\"solution\\\": null,\\n          \
    \      \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 41,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.041,\\\
    n                \\\"mmol_l\\\": 0.20717,\\n                \\\"optional\\\":\
    \ 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[3].concentration (MnCl2 x 4 H2O) in MediaDive solution 6187; locator=$.data.recipe[3]\
    \ (compound_id=36). Provider explicitly reports g_l=0.041. Arithmetic check: 41\
    \ mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.041 g/L, consistent with the\
    \ reported value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00;\
    \ response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q66\",\n    \"label\": \"\
    solution6187 ZnCl2 x 6 H2O\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"ZnCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 2351,\\n   \
    \             \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 5,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.005,\\n                \\\"mmol_l\\\
    \": 0.0204583,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6187\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 6,\\\
    n                \\\"compound\\\": \\\"ZnCl2 x 6 H2O\\\",\\n                \\\
    \"compound_id\\\": 2351,\\n                \\\"solution\\\": null,\\n        \
    \        \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 5,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.005,\\\
    n                \\\"mmol_l\\\": 0.0204583,\\n                \\\"optional\\\"\
    : 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[4].concentration (ZnCl2 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[4]\
    \ (compound_id=2351). Provider explicitly reports g_l=0.005. Arithmetic check:\
    \ 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L, consistent with the\
    \ reported value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00;\
    \ response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q67\",\n    \"label\": \"\
    solution6187 CoCl2 x 6 H2O\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 2,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.002,\\n                \\\"mmol_l\\\
    \": 0.0154037,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6187\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 7,\\\
    n                \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                \\\
    \"compound_id\\\": 38,\\n                \\\"solution\\\": null,\\n          \
    \      \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 2,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.002,\\\
    n                \\\"mmol_l\\\": 0.0154037,\\n                \\\"optional\\\"\
    : 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[5].concentration (CoCl2 x 6 H2O) in MediaDive solution 6187; locator=$.data.recipe[5]\
    \ (compound_id=38). Provider explicitly reports g_l=0.002. Arithmetic check: 2\
    \ mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.002 g/L, consistent with the\
    \ reported value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00;\
    \ response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q68\",\n    \"label\": \"\
    solution6187 Na2MoO4 x 2 H2O\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"Na2MoO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 4,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.004,\\n                \\\"mmol_l\\\
    \": 0.0165323,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6187\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 8,\\\
    n                \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n               \
    \ \\\"compound_id\\\": 9,\\n                \\\"solution\\\": null,\\n       \
    \         \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 4,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.004,\\\
    n                \\\"mmol_l\\\": 0.0165323,\\n                \\\"optional\\\"\
    : 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[6].concentration (Na2MoO4 x 2 H2O) in MediaDive solution 6187; locator=$.data.recipe[6]\
    \ (compound_id=9). Provider explicitly reports g_l=0.004. Arithmetic check: 4\
    \ mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.004 g/L, consistent with the\
    \ reported value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 1000. Retrieved 2026-10-07T10:01:03.929880+00:00;\
    \ response SHA256=d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q69\",\n    \"label\": \"\
    solution6187 preparation context\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"source_stage\": \"External standalone-stock preparation only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Add to\
    \ 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\\
    r\\nfollowing sequence:\"\n      }\n    ],\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.steps[0].step encoded JSON string\",\n\
    \        \"exact_source_quote\": \"\\\"Add to 1000 ml of distilled water 0.75\
    \ g Na2EDTA and the minerals in exactly the \\\\r\\\\nfollowing sequence:\\\"\"\
    ,\n        \"snapshot_sha256\": \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\
    \n      }\n    ],\n    \"interpretation\": \"The retained local preparation contains\
    \ the same source water/stock context. It is not a procedure or final volume for\
    \ AP11MH.\"\n  },\n  {\n    \"decision_id\": \"q70\",\n    \"label\": \"solution6187\
    \ placeholder ingredient\",\n    \"decision\": \"unsupported\",\n    \"source_stage\"\
    : \"External stock placeholder context only\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6187\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6187\"\
    ,\n        \"source_locator\": \"$.data.id; complete recipe inspected\",\n   \
    \     \"exact_source_quote\": \"\\\"id\\\": 6187\",\n        \"snapshot_sha256\"\
    : \"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The local See source placeholder has no\
    \ independent quantified ingredient identity; the complete composition already\
    \ carries actual stock rows. This ancillary record is context only and requires\
    \ separate curation, not transfer into AP11MH.\"\n  },\n  {\n    \"decision_id\"\
    : \"q71\",\n    \"label\": \"solution6241 Cyanocobalamine\",\n    \"decision\"\
    : \"verified\",\n    \"source_stage\": \"External asserted-stock identity context\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
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
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 2,\\\
    n                \\\"compound\\\": \\\"Cyanocobalamine\\\",\\n               \
    \ \\\"compound_id\\\": 847,\\n                \\\"solution\\\": null,\\n     \
    \           \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 10,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\\
    n                \\\"mmol_l\\\": 0.073779,\\n                \\\"optional\\\"\
    : 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[0].concentration (Cyanocobalamine) in MediaDive solution 6241; locator=$.data.recipe[0]\
    \ (compound_id=847). Provider explicitly reports g_l=0.1. Arithmetic check: 10\
    \ mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.10 g/L, consistent with the reported\
    \ value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 100. Retrieved 2026-10-07T10:01:37.871406+00:00;\
    \ response SHA256=d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q72\",\n    \"label\": \"\
    solution6241 Thiamine HCl\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
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
    \n      }\n    ],\n    \"interpretation\": \"Existing attached excerpt, cited\
    \ response hash, provider g_l and declared stock-volume basis agree for this standalone\
    \ stock only. This does not verify an AP11MH ingredient, stock dose or formulation\
    \ match.\",\n    \"attached_existing_evidence\": [\n      {\n        \"reference\"\
    : \"https://mediadive.dsmz.de/rest/solution/6241\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"{\\n                \\\"recipe_order\\\": 3,\\\
    n                \\\"compound\\\": \\\"Thiamine HCl\\\",\\n                \\\"\
    compound_id\\\": 1207,\\n                \\\"solution\\\": null,\\n          \
    \      \\\"solution_id\\\": null,\\n                \\\"condition\\\": null,\\\
    n                \\\"attribute\\\": null,\\n                \\\"amount\\\": 10,\\\
    n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\\
    n                \\\"mmol_l\\\": 0.296472,\\n                \\\"optional\\\"\
    : 0\\n            }\",\n        \"explanation\": \"Concentration evidence for\
    \ composition[1].concentration (Thiamine HCl) in MediaDive solution 6241; locator=$.data.recipe[1]\
    \ (compound_id=1207). Provider explicitly reports g_l=0.1. Arithmetic check: 10\
    \ mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.10 g/L, consistent with the reported\
    \ value at its precision. Evidence supports the provider-declared concentration\
    \ within this solution, not a concentration in a receiving medium or an independently\
    \ measured final volume. Water addition alone is not used to infer a final volume.\
    \ Additional exact excerpt at $.data.volume: \\\"volume\\\": 100. Retrieved 2026-10-07T10:01:37.871406+00:00;\
    \ response SHA256=d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1.\"\
    \n      }\n    ]\n  },\n  {\n    \"decision_id\": \"q73\",\n    \"label\": \"\
    solution6241 Biotin\",\n    \"decision\": \"correct\",\n    \"source_stage\":\
    \ \"External asserted-stock identity context only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"Biotin\\\",\\n                \\\"compound_id\\\": 46,\\n            \
    \    \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n \
    \               \\\"condition\\\": null,\\n                \\\"attribute\\\":\
    \ null,\\n                \\\"amount\\\": 200,\\n                \\\"unit\\\"\
    : \\\"\\\\u03bcg\\\",\\n                \\\"g_l\\\": null,\\n                \\\
    \"mmol_l\\\": null,\\n                \\\"optional\\\": 0\\n            }\",\n\
    \        \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"The API gives 200 µg biotin made\
    \ up to 100 ml, equivalent to 0.002 g/L in this distinct stock, not local 2000\
    \ g/L. This stock is not the NBRC vitamin formulation.\"\n  },\n  {\n    \"decision_id\"\
    : \"q74\",\n    \"label\": \"solution6241 Distilled water\",\n    \"decision\"\
    : \"correct\",\n    \"source_stage\": \"External asserted-stock identity context\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"PERCENT_V_V\"\n \
    \       }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 100,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"Water is a source volume, not 1000%\
    \ v/v.\"\n  },\n  {\n    \"decision_id\": \"q75\",\n    \"label\": \"solution6241\
    \ preparation context\",\n    \"decision\": \"evidence_only\",\n    \"source_stage\"\
    : \"External standalone-stock preparation only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"Make\
    \ up to 100 ml with distilled water.\\n\\nOriginal volume: 100 mL\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution6241\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\",\n\
    \        \"source_locator\": \"$.data.steps[0].step encoded JSON string\",\n \
    \       \"exact_source_quote\": \"\\\"Make up to 100 ml with distilled water.\\\
    \"\",\n        \"snapshot_sha256\": \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\
    \n      }\n    ],\n    \"interpretation\": \"The retained local preparation contains\
    \ the same source water/stock context. It is not a procedure or final volume for\
    \ AP11MH.\"\n  },\n  {\n    \"decision_id\": \"q76\",\n    \"label\": \"solution6241\
    \ placeholder ingredient\",\n    \"decision\": \"unsupported\",\n    \"source_stage\"\
    : \"External stock placeholder context only\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution6241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/6241\"\
    ,\n        \"source_locator\": \"$.data.id; complete recipe inspected\",\n   \
    \     \"exact_source_quote\": \"\\\"id\\\": 6241\",\n        \"snapshot_sha256\"\
    : \"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The local See source placeholder has no\
    \ independent quantified ingredient identity; the complete composition already\
    \ carries actual stock rows. This ancillary record is context only and requires\
    \ separate curation, not transfer into AP11MH.\"\n  }\n]"
- assessment_id: ownership
  area: ownership
  topic: Maintained source and generated boundaries
  outcome: supported
  summary: The sole normalized ap11mh_medium.yaml owns future recipe correction. Exact
    current TOGO section parsing, solution matching and cleanup/merge code were inspected
    without execution. The two external stocks are context and must not be forced
    to fit this source. No record or history is changed.
  target_ids:
  - CultureMech:008415
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
  - writer-3
  - writer-4
  - stock-index
findings:
- finding_id: f1
  issue_key: cm008415-stages-and-units
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Flattened stock stages, summed duplicates and lost units change the recipe
  description: Both layers mix KP, trace and vitamin strengths into main ingredients.
    Main NaCl 31 combines 30 g main with 1 g undiluted trace stock; calcium 0.25 similarly
    combines 0.15 g and 0.1 g. Target water 4.0 sums four 1 L preparations, while
    owner 1.0 collapses them without restoring stages; both use mass units. Resazurin
    1 mg and all nine vitamin milligram amounts are stored with unchanged numerals
    in G_PER_L. Stock additions 5/2/2 ml are instead G_PER_L.
  target_ids:
  - CultureMech:008415
  field_paths:
  - ingredients[*].concentration
  - ingredients[0:3].notes
  - solutions[*].concentration
  - solutions[0].composition
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  issue_key: cm008415-wrong-stock-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The two external stock links resolve to different formulations
  description: The referenced 6187 stock is EDTA-based with seven rows; NBRC 1075
    trace stock is NTA-based with fifteen rows including water. Referenced 6241 has
    three vitamins in 100 ml; NBRC 1075 defines nine in 1 L. Their generic labels
    and eight internally supported amount attachments do not establish source equivalence.
    The local references resolve, so this is scientific wrong-stock identity rather
    than an absent-file schema failure.
  target_ids:
  - CultureMech:008415
  field_paths:
  - solutions[1].term
  - solutions[1].notes
  - solutions[2].term
  - solutions[2].notes
  evidence_ids:
  - primary
  - provider
  - solution6187
  - solution6241
  - solution6187-local
  - solution6241-local
  - stock-index
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm008415-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Hydrate and calcium-salt mismatches persist despite valid IDs
  description: CoCl2·6H2O and NiCl2·6H2O are linked to anhydrous CHEBI:35696/CHEBI:34887.
    Ca-pantothenate is linked to the calcium-free (R)-pantothenate anion. The source
    cysteine-HCl wording additionally leaves the L stereochemical specificity unestablished.
    Distinguish confirmed formula mismatches from that narrower unresolved specificity.
  target_ids:
  - CultureMech:008415
  field_paths:
  - ingredients[21].term
  - ingredients[22].term
  - ingredients[22].mediaingredientmech_chebi_term
  - ingredients[34].term
  - ingredients[34].mediaingredientmech_chebi_term
  - ingredients[11].term
  evidence_ids:
  - primary
  - provider
  - chebi35696
  - chebi34887
  - chebi29032
  - chebi91247
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  issue_key: cm008415-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source gas, separate-stock preparation and stock-pH context are missing
  description: Neither layer retains preparation_steps or main unadjusted-pH context.
    Source specifies H2/CO2 (80/20), separately sterilized stocks, unqualified 5%/10%
    strengths, trace pH 6.5 then 7.0 and pressure 150 kPa. VARIABLE gases/NaOH do
    not preserve those stages. No cycle temperature/time, percent basis, N2 purity
    or absolute/gauge pressure is supplied.
  target_ids:
  - CultureMech:008415
  field_paths:
  - preparation_steps
  - ph_value
  - ingredients[13:16].concentration
  - ingredients[30].concentration
  evidence_ids:
  - primary
  - prep
  - trace-prep
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  issue_key: cm008415-secondary-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current secondary gap and unresolved legacy correspondence are distinct
  description: CHEBI:29032 is a valid live primary term but has no exact current MIM-index
    row for its asserted secondary membership. Legacy MediaIngredientMech:000389 is
    absent from the complete current index/catalog/tree; its historical mapping remains
    unavailable. A current miss neither proves historical invalidity nor supplies
    a replacement.
  target_ids:
  - CultureMech:008415
  field_paths:
  - ingredients[34].mediaingredientmech_chebi_term
  - ingredients[11].mediaingredientmech_term
  evidence_ids:
  - mim
  - legacy-lookup
  - mimPinnedCatalog
  - mimPinnedTree
  - chebi29032
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: cm008415-evidence-generated-state
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: No main-layer claim evidence accompanies later partial cleanup
  description: Neither target nor owner attaches amount/preparation evidence. Owner
    water changed after target generation, but both representations remain source-incomplete;
    Unknown solution placeholders hide missing/incorrect stock identity. Current writer
    behavior and later cleanup notes are not a replay of historical source processing.
  target_ids:
  - CultureMech:008415
  field_paths:
  - ingredients[*].evidence
  - solutions[*].name
  - curation_history
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - quantity-inventory
  - writer-0
  - writer-1
  - writer-2
  - writer-3
  - writer-4
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  description: Reconstruct the exact main/KP/trace/vitamin stages in the maintained
    owner, restore original units and each source water context, split duplicate contributions
    and preserve source stock doses. Do not guess measured final concentration or
    double-count expanded stocks.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008415
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  description: Remove or qualify unsupported external correspondence and represent
    the exact NBRC stocks with source-backed local identities/composition. Preserve
    valid standalone stock evidence as scoped context; do not modify those stocks
    merely to make them fit this medium.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008415
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  description: Ground exact supplied hydrates and calcium salt from primary/structure
    evidence, and qualify unstated stereochemistry without guessing identifiers or
    converting masses using an unsupported form.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008415
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  description: Restore exact preparation and condition scopes, keeping stock pH separate
    from main pH, explicit gas ratios separate from dissolved amounts, and unknown
    bases or cycle numbers unresolved.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008415
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  description: Qualify or resolve the current secondary membership and obtain exact
    historical legacy correspondence before retaining an unqualified legacy link.
    Preserve original history and do not substitute a nearby mapping.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008415
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
  description: After source-backed correction, attach narrow main/stock/condition
    evidence with actual hashes/times, use explicit stock names and regenerate separately
    under authorized gates. Preserve past history and stock-only evidence.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008415
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ap11mh_medium.yaml
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
- Partial completion is specifically due to unresolved historical legacy 389 correspondence.
  Current CHEBI:29032 index absence is a completed lookup, not an unavailable check.
  The exact NBRC main and all three stock definitions and both wrong external stock
  identities are otherwise inspectable. No evidence or growth claim is transferred
  merely because generic stock names agree.
- External 6187/6241 are inspected dependencies, not additional reviewed targets.
  Their eight amount claims are verified only within their own declared stock bases.
  Their other anomalies, placeholder/history qualifiers and water/biotin representations
  are context for safe disambiguation, not authorization to change those files. All
  primary/source quantities remain separate from unknown measured final volume, percent
  basis and absolute/gauge pressure.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-029
- generated-medium
```
