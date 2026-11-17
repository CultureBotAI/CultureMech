# Source and formulation review: anaerobic_tyeg_medium (CultureMech:015413)

- Review: 20261021T152223Z-culturemech-015413-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:15:05Z
- Finished UTC: 2026-10-21T15:22:23Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM684 identity is supported, but main-medium and stock quantities are flattened, receiving stock volumes are represented as solute concentrations, and mineral-stock pH6.5 has displaced main-medium pH7.5.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 268; batch 027 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-six task batches contain 260 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 263 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015413 | data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml | generated | anaerobic_tyeg_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015413 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015413 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/268/strict.tsv |
| validate-terms | passed | True | CultureMech:015413 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015413 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015413 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ684api | unavailable | False | CultureMech:015413 | Exact main JCM684 API and its preserved retry returned503; the old normalization origin cannot be reconstructed from these failures. Complete exact JCM684 primary and scoped parent vitamins were available, so this optional provider-route failure does not prevent assessing the documented primary/record conflicts. |
| Exact source content access: solution4585 | unavailable | False | CultureMech:015413 | Optional provider trace-mineral solution4585 returned503. Exact JCM684 primary supplies the stock recipe and receiving9ml dose; no provider-declared stock volume is fabricated. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015413.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:015413.

29 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 29/31 primary and 29/31 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 31: primary 93.55%; secondary 93.55%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015413.

41 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Main batch: KH2PO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.730282",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.730282",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "KH 2 PO 4 0.75 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "KH 2 PO 4 0.75 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Main batch: K2HPO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.46056",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.46056",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "K 2 HPO 4 1.5 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "K 2 HPO 4 1.5 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Main batch: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.876339",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.876339",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "NaCl 0.9 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "NaCl 0.9 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main batch: MgCl2 x 6 H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.194742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.194742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "MgCl 2 ·6H 2 O 0.2 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "MgCl 2 ·6H 2 O 0.2 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main batch: NH4Cl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.876339",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.876339",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "NH 4 Cl 0.9 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "NH 4 Cl 0.9 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Main batch: Tryptone",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1.94742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1.94742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "Tryptone (BD-Difco) 2.0 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "Tryptone (BD-Difco) 2.0 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Main batch: Yeast extract",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.94742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.94742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "Yeast extract 2.0 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "Yeast extract 2.0 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Main batch: Glucose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.94742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.94742",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "Glucose 2.0 g",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "Glucose 2.0 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Main batch: Resazurin",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00097371",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00097371",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "Resazurin 1.0 mg",
    "rationale": "Preserve the source batch amount and supplier where specified; listed1.0L water is not a measured final-volume denominator. Local normalized numbers do not authenticate the missing main API. For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct additive g/L term.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe before water row",
        "exact_source_quote": "Resazurin 1.0 mg",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Receiving stock: FeSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "10% FeSO 4 ·7H 2 O solution 5.0 µl",
    "rationale": "Local5 or8G_PER_L misrepresents source volume units and stock strengths. Iron dose is5.0µl, not5ml or5g; sulfide is8.0ml per liter before inoculation. Source percent bases are unspecified: retain10%/5% literally without assuming w/v or computing dissolved mass.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe iron stock or pre-inoculation sulfide addition",
        "exact_source_quote": "10% FeSO 4 ·7H 2 O solution 5.0 µl",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Receiving stock: Na2S x 9 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "5% Na 2 S·9H 2 O solution 8.0 ml",
    "rationale": "Local5 or8G_PER_L misrepresents source volume units and stock strengths. Iron dose is5.0µl, not5ml or5g; sulfide is8.0ml per liter before inoculation. Source percent bases are unspecified: retain10%/5% literally without assuming w/v or computing dissolved mass.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main recipe iron stock or pre-inoculation sulfide addition",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution 8.0 ml",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Trace-mineral stock: Nitrilotriacetic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Nitrilotriacetic acid 12.5 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "Nitrilotriacetic acid 12.5 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Trace-mineral stock: FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "FeCl 2 ·4H 2 O 0.2 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "FeCl 2 ·4H 2 O 0.2 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Trace-mineral stock: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "MnCl 2 ·4H 2 O 0.1 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "MnCl 2 ·4H 2 O 0.1 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Trace-mineral stock: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "CoCl 2 ·6H 2 O 0.02 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.02 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Trace-mineral stock: CaCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "CaCl 2 ·2H 2 O 0.1 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.1 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Trace-mineral stock: ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "ZnCl 2 0.1 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "ZnCl 2 0.1 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Trace-mineral stock: CuCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "CuCl 2 0.2 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "CuCl 2 0.2 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Trace-mineral stock: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "H 3 BO 3 0.01 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "H 3 BO 3 0.01 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Trace-mineral stock: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Na 2 MoO 4 ·2H 2 O 0.01 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.01 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Trace-mineral stock: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.876339",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.876339",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "NaCl 1.0 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "NaCl 1.0 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Trace-mineral stock: Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Na 2 SeO 3 ·5H 2 O 0.02 g within the stock recipe using1.0L water; receiving dose9.0ml.",
    "rationale": "Source stock components are flattened as main-medium concentrations. Keep each component and hydrate within its stock, with water/stock-denominator qualification; do not use undiluted stock amounts at the receiving stage. NaCl also has a distinct0.9g main-batch addition.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace mineral solution table",
        "exact_source_quote": "Na 2 SeO 3 ·5H 2 O 0.02 g",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Linked vitamin stock: Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Biotin 2.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Biotin 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Linked vitamin stock: Folic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Folic acid 2.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Folic acid 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Linked vitamin stock: Pyridoxine hydrochloride",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Pyridoxine·HCl 10.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Pyridoxine·HCl 10.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Linked vitamin stock: Thiamine HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Thiamine·HCl 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Thiamine·HCl 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Linked vitamin stock: Riboflavin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Riboflavin 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Riboflavin 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Linked vitamin stock: Nicotinic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Nicotinic acid 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Nicotinic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Linked vitamin stock: Calcium pantothenate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Calcium pantothenate 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Calcium pantothenate 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Linked vitamin stock: Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Vitamin B 1 2 0.1 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Vitamin B 1 2 0.1 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Linked vitamin stock: p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "p -Aminobenzoic acid 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "p -Aminobenzoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Linked vitamin stock: Lipoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Lipoic acid 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.",
    "rationale": "The local numeric G_PER_L matches undiluted provider stock composition. Provider solution3861 declares1000ml stock volume and these g_l values; none is a JCM684 final-medium concentration. Preserve the stock/receiving boundary and source forms.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace vitamins table only",
        "exact_source_quote": "Lipoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Main source water1.0L; do not treat as final volume.",
    "rationale": "Keep solvent, stock strength and receiving amount at their named preparation stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684 components.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Exact source table/stage boundary",
        "exact_source_quote": "Distilled water 1.0 L Mix components",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Mineral-stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Mineral-stock water1.0L; no measured final-volume statement.",
    "rationale": "Keep solvent, stock strength and receiving amount at their named preparation stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684 components.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Exact source table/stage boundary",
        "exact_source_quote": "Distilled water 1.0 L Dissolve nitrilotriacetic acid",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Vitamin-stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Vitamin-stock water1.0L; provider separately declares1000ml stock volume.",
    "rationale": "Keep solvent, stock strength and receiving amount at their named preparation stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684 components.",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Exact source table/stage boundary",
        "exact_source_quote": "Lipoic acid 5.0 mg Distilled water 1.0 L Trace mineral solution:",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Mineral receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Receive9.0ml of this JCM684 mineral stock.",
    "rationale": "Keep solvent, stock strength and receiving amount at their named preparation stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684 components.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Exact source table/stage boundary",
        "exact_source_quote": "Trace mineral solution (see below) 9.0 ml",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Vitamin receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Receive10.0ml of the JCM197 vitamin stock only.",
    "rationale": "Keep solvent, stock strength and receiving amount at their named preparation stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684 components.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Exact source table/stage boundary",
        "exact_source_quote": "Trace vitamins (see Medium No. 197 ) 10.0 ml",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Main-medium pH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.5,
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.5,
        "decision": "correct"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components and adjust pH to 7.5. Bring to a boil, then cool down and distribute into culture vessels under a N2 gas stream. Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the following solution (autoclaved under a N2 atmosphere) into the medium (per liter):"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components and adjust pH to 7.5. Bring to a boil, then cool down and distribute into culture vessels under a N2 gas stream. Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the following solution (autoclaved under a N2 atmosphere) into the medium (per liter):"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Main-medium preparation pH7.5; stock pH6.5 must remain separate.",
    "rationale": "The prose retains7.5 but top-level ph_value6.5 conflicts; the latter belongs to the mineral stock.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main preparation",
        "exact_source_quote": "Mix components and adjust pH to 7.5.",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Mineral-stock pH and titrant",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "ADJUST_PH",
          "description": "Dissolve nitrilotriacetic acid at first and adjust pH to 6.5 with KOH. Then proceed to add the minerals."
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "ADJUST_PH",
          "description": "Dissolve nitrilotriacetic acid at first and adjust pH to 6.5 with KOH. Then proceed to add the minerals."
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Dissolve NTA first, adjust its stock to pH6.5 with KOH, then add minerals. KOH strength and volume unspecified.",
    "rationale": "Retain the procedure within the stock rather than as an unqualified step of the assembled medium; do not invent titrant quantities.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Trace-mineral stock preparation",
        "exact_source_quote": "Dissolve nitrilotriacetic acid at first and adjust pH to 6.5 with KOH.  Then proceed to add the minerals.",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Main anaerobic preparation and pre-inoculation sulfide",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components and adjust pH to 7.5. Bring to a boil, then cool down and distribute into culture vessels under a N2 gas stream. Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the following solution (autoclaved under a N2 atmosphere) into the medium (per liter):"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components and adjust pH to 7.5. Bring to a boil, then cool down and distribute into culture vessels under a N2 gas stream. Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the following solution (autoclaved under a N2 atmosphere) into the medium (per liter):"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Boil/cool/distribute under N2, seal and autoclave; add separately autoclaved anoxic5% sulfide8ml per liter before inoculation.",
    "rationale": "Local step ends at a colon and omits the quantitative sulfide addition. This source says N2 gas stream/atmosphere without a numerical purity; do not add100% or import the parent197 gas mixture.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "Main and pre-inoculation preparation",
        "exact_source_quote": "Bring to a boil, then cool down and distribute into culture vessels under a N 2 gas stream. Seal with butyl rubber stoppers and autoclave.  Prior to inoculation, add the following solution (autoclaved under a N 2 atmosphere) into the medium (per liter): 5% Na 2 S·9H 2 O solution 8.0 ml",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "JCM stated default sterilization cycle",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components and adjust pH to 7.5. Bring to a boil, then cool down and distribute into culture vessels under a N2 gas stream. Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the following solution (autoclaved under a N2 atmosphere) into the medium (per liter):"
          },
          {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Dissolve nitrilotriacetic acid at first and adjust pH to 6.5 with KOH. Then proceed to add the minerals."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components and adjust pH to 7.5. Bring to a boil, then cool down and distribute into culture vessels under a N2 gas stream. Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the following solution (autoclaved under a N2 atmosphere) into the medium (per liter):"
          },
          {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Dissolve nitrilotriacetic acid at first and adjust pH to 6.5 with KOH. Then proceed to add the minerals."
          }
        ],
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Apply explicitly stated121°C/15min default where JCM684 calls for autoclaving and no different instruction exists.",
    "rationale": "Unlike an assumed standard cycle, this temperature/time is printed in the exact source. Preserve any component-specific exception; parent197 unrelated preparation is outside scope.",
    "source_snippets": [
      {
        "source_key": "jcm684",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684",
        "source_locator": "JCM684 page default instruction",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b",
        "parsed_text_sha256": "2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e"
      }
    ]
  }
]

### Exact source identity and maintained ownership

identity: supported. Targets: CultureMech:015413.

Exact JCM684 title/accession and stable ID resolve the sole explicit normalized owner. All31 ingredient concentrations agree across target and owner; generated-only merge metadata does not constitute source confirmation.

### Claim-level support and exact source stages

evidence: concern. Targets: CultureMech:015413.

No ingredient amount has attached supporting evidence in either local layer. Every local concentration and scoped source-only quantitative context has an inventory decision with exact quotations and locators. Matching provider transcription receives evidence_only, not verified. Source quantities and provider normalization remain separate.

### Main and stock preparation boundaries

completeness: concern. Targets: CultureMech:015413.

Main pH7.5 and mineral pH6.5 are conflated; stock mineral preparation is at the main root, receiving references/doses are absent, and the sulfide addition sentence is cut off before its quantity. Source default121°C/15min and each stock stage need explicit retention.

### Composition and physical state

scope: supported. Targets: CultureMech:015413.

COMPLEX/UNDEFINED/LIQUID is consistent with tryptone and yeast extract and no agar. Filing and generic cultivation application are not organism evidence.

### Source-specified molecular forms and mixtures

grounding: concern. Targets: CultureMech:015413.

Named mineral hydrates agree with their asserted IDs; generic glucose and vitaminB12 remain generic. Calcium pantothenate primary wording is stereochemically unqualified while CHEBI31345 has a stereospecific structure and D-calcium synonyms. This is unsupported extra specificity to qualify, not proof the supplied material is the wrong enantiomer. Tryptone and yeast extract remain mixtures without invented molecular IDs.

### Growth, taxonomy and graph assertion scope

scope: not_applicable. Targets: CultureMech:015413.

The medium title, bacterial filing and generic Microbial cultivation application are catalog context, not strain-level experimental growth evidence. No organism identifier, growth assertion, phenotype or graph membership is added. No internal variant/reference relationship is asserted in either complete local record.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015413.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained input and current import/merge behavior

provenance: concern. Targets: CultureMech:015413.

Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes.

## Findings

### f1: Separate main amounts, stock compositions and receiving volumes

blocker / open / confirmed; issue key: culturemech.015413.stock-and-volume-collapse.

Both layers flatten31 ingredients. FeSO4 heptahydrate is5G_PER_L where the source adds5µl of10% stock; sodium sulfide nonahydrate is8G_PER_L where the source adds8ml of5% stock per liter. Mineral/vitamin stock amounts are undiluted main entries, and NaCl explicitly sums main and stock values. Bare percent bases and final assembled volume are not established.

### f2: Restore main pH7.5 and keep mineral-stock pH6.5 scoped

major / open / confirmed; issue key: culturemech.015413.preparation-stage-ph.

Top-level ph_value6.5 takes the mineral-stock value despite main preparation explicitly saying7.5. The stock preparation sits at the root, and the main sulfide instruction ends before its8ml/L amount.

### f3: Qualify unsupported pantothenate stereochemistry

minor / open / confirmed; issue key: culturemech.015413.pantothenate-specificity.

JCM197 and provider3861 say calcium pantothenate without D/L qualification; CHEBI31345 resolves correctly but its structure is stereospecific and synonyms include D-calcium pantothenate. Matching labels alone do not establish that source specificity.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct source-native main batch and separate mineral/vitamin stocks with9ml/10ml receiving doses. Preserve iron5µl and sulfide8ml/L stock additions, percent qualifiers and named hydrates. Reassess every concentration against the complete inventory without assuming final volume or percent basis.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent main pH7.5 separately from stock pH6.5/KOH; complete the sulfide addition and its timing/sterilization. Attach the exact source default cycle where applicable and preserve nitrogen context without invented gas proportions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Recover exact supplied-form evidence or qualify the mapping. Do not declare a wrong enantiomer or choose an unverified replacement from a similar label.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch027/268/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/268/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml:1:id: CultureMech:015413<br>./data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml:1:id: CultureMech:015413<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/268/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 36 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/268/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| primary684 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684; Main recipe, pre-inoculation sulfide addition and complete trace-mineral stock | supports | Exact JCM684 primary establishes source stages, original quantities, pH7.5 main medium and pH6.5 mineral-stock preparation; bare10% and5% bases are not specified. |
| vitamin197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins table only, through its Distilled water1.0L row | supports | JCM684 explicitly links this vitamin table. The parent main medium, its gas/pH instructions and its different mineral stock are outside this recipe linkage. |
| vitamin3861 | https://mediadive.dsmz.de/rest/solution/3861; $.data.id/name/volume/recipe, solution3861 Trace vitamins only | supports | Provider-declared vitamin-stock volume1000ml and component g_l corroborate stock composition; they are not final JCM684 concentrations. |
| vitaminJ197 | https://mediadive.dsmz.de/rest/medium/J197; Only solution3861 Trace vitamins; other solutions outside source scope | supports | The accessible parent API supplies the linked vitamin stock, not the unavailable JCM684 main solution or its trace-mineral stock. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49553; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49553 resolves to copper(II) chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term", "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id": "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49553": [{"label": "CuCl2", "match_type": "preferred_term", "identifier": "CHEBI:49553", "preferred_term": "CuCl2", "ontology_id": "CHEBI:49553", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch027/268/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| history-metadata | data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml; data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes. |
| mediadiveJ684api-attempt | https://mediadive.dsmz.de/rest/medium/J684; Preserved exact public retrieval result | context_only | Exact main JCM684 API and its preserved retry returned503; the old normalization origin cannot be reconstructed from these failures. Complete exact JCM684 primary and scoped parent vitamins were available, so this optional provider-route failure does not prevent assessing the documented primary/record conflicts. |
| solution4585-attempt | https://mediadive.dsmz.de/rest/solution/4585; Preserved exact public retrieval result | context_only | Optional provider trace-mineral solution4585 returned503. Exact JCM684 primary supplies the stock recipe and receiving9ml dose; no provider-declared stock volume is fabricated. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Only the exact bound collection/provider sources and pinned identifiers were assessed. Current source differences do not establish source chronology or the exact historical import version.
- Listed water, stock recipe volumes and receiving additions do not establish a measured assembled final volume. No unqualified percent basis, density, unspecified stock strength, sterilization cycle or source-specific replacement identifier is invented.
- Exact main JCM684 API and its preserved retry returned503; the old normalization origin cannot be reconstructed from these failures. Complete exact JCM684 primary and scoped parent vitamins were available, so this optional provider-route failure does not prevent assessing the documented primary/record conflicts.
- Optional provider trace-mineral solution4585 returned503. Exact JCM684 primary supplies the stock recipe and receiving9ml dose; no provider-declared stock volume is fabricated.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152223Z-culturemech-015413-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobic_tyeg_medium (CultureMech:015413)'
started_at: '2026-10-21T15:15:05Z'
finished_at: '2026-10-21T15:22:23Z'
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
summary: JCM684 identity is supported, but main-medium and stock quantities are flattened,
  receiving stock volumes are represented as solute concentrations, and mineral-stock
  pH6.5 has displaced main-medium pH7.5.
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
  - path: data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
    sha256: 0f2cca20afe46baf71b27a942d55d9bc18e4f744e2a9b52e05099cb493a148ba
    role: target
  - path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
    sha256: 6e5e169a6e43d33fa0386d9ad375bdc90ff7b61bb756ddd71f213c66dd06ad37
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/specialized/anaerobic_tyeg_medium.yaml.md
    sha256: a4d74f120a59ea34d462814c8b342f917791fcbcc4de8696cb1e22d63506eaa9
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
  selection: Task review 268; batch 027 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-six task batches
    contain 260 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 263 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015413
targets:
- target_id: CultureMech:015413
  path: data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  label: anaerobic_tyeg_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/268/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/268/strict.tsv"
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015413
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
  - CultureMech:015413
- check_id: mediadiveJ684api-source-access
  name: 'Exact source content access: mediadiveJ684api'
  required: false
  status: unavailable
  summary: Exact main JCM684 API and its preserved retry returned503; the old normalization
    origin cannot be reconstructed from these failures. Complete exact JCM684 primary
    and scoped parent vitamins were available, so this optional provider-route failure
    does not prevent assessing the documented primary/record conflicts.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - mediadiveJ684api-attempt
- check_id: solution4585-source-access
  name: 'Exact source content access: solution4585'
  required: false
  status: unavailable
  summary: Optional provider trace-mineral solution4585 returned503. Exact JCM684
    primary supplies the stock recipe and receiving9ml dose; no provider-declared
    stock volume is fabricated.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - solution4585-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:52.564038Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/268/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:54.915145Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/268/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:58.766242Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:16:01.277179Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:22:22Z'
  support: supports
  summary: './data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml:1:id: CultureMech:015413

    ./data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml:1:id: CultureMech:015413

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/268/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:22:22Z'
  support: supports
  summary: 36 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 8bce4df0ad1ade1673cb715be7dba32389095c62c6b7d7e8b058ec75bbcac651
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/268/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: b2dbc6e342fdfed8173e4a6f0303ddd5aa4ec1b2c2cfb2f08d74dc3b4360dc47
- evidence_id: primary684
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684
  locator: Main recipe, pre-inoculation sulfide addition and complete trace-mineral
    stock
  accessed_at: '2026-10-21T15:00:01.162903Z'
  support: supports
  summary: Exact JCM684 primary establishes source stages, original quantities, pH7.5
    main medium and pH6.5 mineral-stock preparation; bare10% and5% bases are not specified.
  snapshot_sha256: e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b
- evidence_id: vitamin197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins table only, through its Distilled water1.0L row
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: JCM684 explicitly links this vitamin table. The parent main medium, its
    gas/pH instructions and its different mineral stock are outside this recipe linkage.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: vitamin3861
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3861
  locator: $.data.id/name/volume/recipe, solution3861 Trace vitamins only
  accessed_at: '2026-10-20T06:58:06.579458Z'
  support: supports
  summary: Provider-declared vitamin-stock volume1000ml and component g_l corroborate
    stock composition; they are not final JCM684 concentrations.
  snapshot_sha256: c6829f83ad6e234909db1d65f45a27c24993e0280ff68c4d7355a8f6344335b9
- evidence_id: vitaminJ197
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J197
  locator: Only solution3861 Trace vitamins; other solutions outside source scope
  accessed_at: '2026-10-21T09:49:11.793511Z'
  support: supports
  summary: The accessible parent API supplies the linked vitamin stock, not the unavailable
    JCM684 main solution or its trace-mineral stock.
  snapshot_sha256: 779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
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
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
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
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
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
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
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
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
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
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
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
- evidence_id: chebi49553
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49553
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:07:17.608864Z'
  support: supports
  summary: CHEBI:49553 resolves to copper(II) chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 55d84961ae8c483bc2364cb9c5f159267161b61a3c77c93632021c6f4ea1810d
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
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
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
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
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
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
  accessed_at: '2026-10-21T15:22:22Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940":
    [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494":
    [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label":
    "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label":
    "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31345": [{"label": "Calcium pantothenate", "match_type": "preferred_term",
    "identifier": "CHEBI:31345", "preferred_term": "Calcium pantothenate", "ontology_id":
    "CHEBI:31345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic
    acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49553":
    [{"label": "CuCl2", "match_type": "preferred_term", "identifier": "CHEBI:49553",
    "preferred_term": "CuCl2", "ontology_id": "CHEBI:49553", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label":
    "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249",
    "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type":
    "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id":
    "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/268/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 3c0f5e4b67ac617213f0d6bc9cbe04bae7890cd53e17c0ed50ac0eb84e62a82a
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml; data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:22:22Z'
  support: context_only
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: mediadiveJ684api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J684
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:59:59.202888Z'
  support: context_only
  summary: Exact main JCM684 API and its preserved retry returned503; the old normalization
    origin cannot be reconstructed from these failures. Complete exact JCM684 primary
    and scoped parent vitamins were available, so this optional provider-route failure
    does not prevent assessing the documented primary/record conflicts.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution4585-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4585
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:04:29.870191Z'
  support: context_only
  summary: Optional provider trace-mineral solution4585 returned503. Exact JCM684
    primary supplies the stock recipe and receiving9ml dose; no provider-declared
    stock volume is fabricated.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '29 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 29/31
    primary and 29/31 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi131527
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17234
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi33118
  - chebi44557
  - chebi49105
  - chebi49553
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86345
  - chebi86368
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 31: primary 93.55%;
    secondary 93.55%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 41 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Main batch: KH2PO4\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.730282\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.730282\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"KH 2 PO 4 0.75 g\",\n    \"rationale\": \"Preserve the source batch amount\
    \ and supplier where specified; listed1.0L water is not a measured final-volume\
    \ denominator. Local normalized numbers do not authenticate the missing main API.\
    \ For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium\
    \ and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a\
    \ direct additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"KH 2 PO 4 0.75 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Main batch: K2HPO4\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.46056\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.46056\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"K 2 HPO 4 1.5 g\",\n    \"rationale\": \"Preserve the source batch amount\
    \ and supplier where specified; listed1.0L water is not a measured final-volume\
    \ denominator. Local normalized numbers do not authenticate the missing main API.\
    \ For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium\
    \ and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a\
    \ direct additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"K 2 HPO 4 1.5 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Main batch: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.876339\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1.876339\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"NaCl 0.9 g\",\n    \"rationale\": \"Preserve the source batch amount and supplier\
    \ where specified; listed1.0L water is not a measured final-volume denominator.\
    \ Local normalized numbers do not authenticate the missing main API. For NaCl,\
    \ the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and\
    \ stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct\
    \ additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"NaCl 0.9 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Main batch: MgCl2 x 6 H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.194742\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.194742\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"MgCl 2 ·6H 2 O 0.2 g\",\n    \"rationale\": \"Preserve the source batch amount\
    \ and supplier where specified; listed1.0L water is not a measured final-volume\
    \ denominator. Local normalized numbers do not authenticate the missing main API.\
    \ For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium\
    \ and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a\
    \ direct additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"MgCl 2 ·6H 2 O 0.2 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Main batch: NH4Cl\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.876339\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.876339\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"NH 4 Cl 0.9 g\",\n    \"rationale\": \"Preserve the source batch amount and\
    \ supplier where specified; listed1.0L water is not a measured final-volume denominator.\
    \ Local normalized numbers do not authenticate the missing main API. For NaCl,\
    \ the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and\
    \ stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct\
    \ additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"NH 4 Cl 0.9 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Main batch: Tryptone\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.94742\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.94742\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Tryptone (BD-Difco) 2.0 g\",\n    \"rationale\": \"Preserve the source batch\
    \ amount and supplier where specified; listed1.0L water is not a measured final-volume\
    \ denominator. Local normalized numbers do not authenticate the missing main API.\
    \ For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium\
    \ and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a\
    \ direct additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"Tryptone (BD-Difco) 2.0 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Main batch: Yeast extract\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.94742\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.94742\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Yeast extract 2.0 g\",\n    \"rationale\": \"Preserve the source batch amount\
    \ and supplier where specified; listed1.0L water is not a measured final-volume\
    \ denominator. Local normalized numbers do not authenticate the missing main API.\
    \ For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium\
    \ and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a\
    \ direct additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"Yeast extract 2.0 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Main batch: Glucose\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.94742\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[8].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1.94742\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Glucose 2.0 g\",\n    \"rationale\": \"Preserve the source batch amount and\
    \ supplier where specified; listed1.0L water is not a measured final-volume denominator.\
    \ Local normalized numbers do not authenticate the missing main API. For NaCl,\
    \ the local1.876339 value explicitly sums0.876339 and1.0 across main-medium and\
    \ stock contexts; the mineral-stock1.0g belongs in its own stock, not as a direct\
    \ additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"Glucose 2.0 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Main batch: Resazurin\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00097371\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"unsupported\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00097371\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Resazurin 1.0 mg\",\n    \"rationale\": \"Preserve the source batch amount\
    \ and supplier where specified; listed1.0L water is not a measured final-volume\
    \ denominator. Local normalized numbers do not authenticate the missing main API.\
    \ For NaCl, the local1.876339 value explicitly sums0.876339 and1.0 across main-medium\
    \ and stock contexts; the mineral-stock1.0g belongs in its own stock, not as a\
    \ direct additive g/L term.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe before water row\",\n        \"exact_source_quote\"\
    : \"Resazurin 1.0 mg\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Receiving stock: FeSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"10% FeSO 4 ·7H 2 O solution 5.0 µl\",\n    \"rationale\": \"Local5 or8G_PER_L\
    \ misrepresents source volume units and stock strengths. Iron dose is5.0µl, not5ml\
    \ or5g; sulfide is8.0ml per liter before inoculation. Source percent bases are\
    \ unspecified: retain10%/5% literally without assuming w/v or computing dissolved\
    \ mass.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe iron stock or pre-inoculation sulfide\
    \ addition\",\n        \"exact_source_quote\": \"10% FeSO 4 ·7H 2 O solution 5.0\
    \ µl\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Receiving stock: Na2S x 9 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5% Na 2 S·9H 2 O solution 8.0 ml\",\n    \"rationale\": \"Local5 or8G_PER_L\
    \ misrepresents source volume units and stock strengths. Iron dose is5.0µl, not5ml\
    \ or5g; sulfide is8.0ml per liter before inoculation. Source percent bases are\
    \ unspecified: retain10%/5% literally without assuming w/v or computing dissolved\
    \ mass.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main recipe iron stock or pre-inoculation sulfide\
    \ addition\",\n        \"exact_source_quote\": \"5% Na 2 S·9H 2 O solution 8.0\
    \ ml\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: Nitrilotriacetic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[11].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Nitrilotriacetic acid 12.5 g within the stock recipe using1.0L water; receiving\
    \ dose9.0ml.\",\n    \"rationale\": \"Source stock components are flattened as\
    \ main-medium concentrations. Keep each component and hydrate within its stock,\
    \ with water/stock-denominator qualification; do not use undiluted stock amounts\
    \ at the receiving stage. NaCl also has a distinct0.9g main-batch addition.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"Nitrilotriacetic acid 12.5 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"FeCl 2 ·4H 2 O 0.2 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"FeCl 2 ·4H 2 O 0.2 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"MnCl 2 ·4H 2 O 0.1 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"MnCl 2 ·4H 2 O 0.1 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"CoCl 2 ·6H 2 O 0.02 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"CoCl 2 ·6H 2 O 0.02 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: CaCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"CaCl 2 ·2H 2 O 0.1 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"CaCl 2 ·2H 2 O 0.1 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"ZnCl 2 0.1 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"ZnCl 2 0.1 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: CuCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"CuCl 2 0.2 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"CuCl 2 0.2 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"H 3 BO 3 0.01 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"H 3 BO 3 0.01 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Na 2 MoO 4 ·2H 2 O 0.01 g within the stock recipe using1.0L water; receiving\
    \ dose9.0ml.\",\n    \"rationale\": \"Source stock components are flattened as\
    \ main-medium concentrations. Keep each component and hydrate within its stock,\
    \ with water/stock-denominator qualification; do not use undiluted stock amounts\
    \ at the receiving stage. NaCl also has a distinct0.9g main-batch addition.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"Na 2 MoO 4 ·2H 2 O 0.01 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.876339\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1.876339\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"NaCl 1.0 g within the stock recipe using1.0L water; receiving dose9.0ml.\"\
    ,\n    \"rationale\": \"Source stock components are flattened as main-medium concentrations.\
    \ Keep each component and hydrate within its stock, with water/stock-denominator\
    \ qualification; do not use undiluted stock amounts at the receiving stage. NaCl\
    \ also has a distinct0.9g main-batch addition.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"NaCl 1.0 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Trace-mineral stock: Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Na 2 SeO 3 ·5H 2 O 0.02 g within the stock recipe using1.0L water; receiving\
    \ dose9.0ml.\",\n    \"rationale\": \"Source stock components are flattened as\
    \ main-medium concentrations. Keep each component and hydrate within its stock,\
    \ with water/stock-denominator qualification; do not use undiluted stock amounts\
    \ at the receiving stage. NaCl also has a distinct0.9g main-batch addition.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace mineral solution table\",\n        \"exact_source_quote\"\
    : \"Na 2 SeO 3 ·5H 2 O 0.02 g\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Biotin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[21].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Biotin 2.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\",\n\
    \    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Biotin 2.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Folic acid\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[22].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Folic acid 2.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Folic acid 2.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Pyridoxine hydrochloride\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Pyridoxine·HCl 10.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Pyridoxine·HCl 10.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Thiamine HCl\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[24].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Thiamine·HCl 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Thiamine·HCl 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Riboflavin\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Riboflavin 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Riboflavin 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Nicotinic acid\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[26].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Nicotinic acid 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Nicotinic acid 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Calcium pantothenate\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[27].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Calcium pantothenate 5.0 mg in linked vitamin stock; receive10.0ml stock in\
    \ JCM684.\",\n    \"rationale\": \"The local numeric G_PER_L matches undiluted\
    \ provider stock composition. Provider solution3861 declares1000ml stock volume\
    \ and these g_l values; none is a JCM684 final-medium concentration. Preserve\
    \ the stock/receiving boundary and source forms.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"Trace vitamins table only\",\n        \"exact_source_quote\": \"Calcium pantothenate\
    \ 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Vitamin B12\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[28].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Vitamin B 1 2 0.1 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Vitamin B 1 2 0.1 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: p-Aminobenzoic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[29].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"p -Aminobenzoic acid 5.0 mg in linked vitamin stock; receive10.0ml stock in\
    \ JCM684.\",\n    \"rationale\": \"The local numeric G_PER_L matches undiluted\
    \ provider stock composition. Provider solution3861 declares1000ml stock volume\
    \ and these g_l values; none is a JCM684 final-medium concentration. Preserve\
    \ the stock/receiving boundary and source forms.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"Trace vitamins table only\",\n        \"exact_source_quote\": \"p -Aminobenzoic\
    \ acid 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Linked vitamin stock: Lipoic acid\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n        \"\
    field_path\": \"ingredients[30].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Lipoic acid 5.0 mg in linked vitamin stock; receive10.0ml stock in JCM684.\"\
    ,\n    \"rationale\": \"The local numeric G_PER_L matches undiluted provider stock\
    \ composition. Provider solution3861 declares1000ml stock volume and these g_l\
    \ values; none is a JCM684 final-medium concentration. Preserve the stock/receiving\
    \ boundary and source forms.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace vitamins table only\",\n        \"exact_source_quote\"\
    : \"Lipoic acid 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Main source water1.0L; do not treat as final volume.\",\n    \"rationale\"\
    : \"Keep solvent, stock strength and receiving amount at their named preparation\
    \ stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684\
    \ components.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Exact source table/stage boundary\",\n      \
    \  \"exact_source_quote\": \"Distilled water 1.0 L Mix components\",\n       \
    \ \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Mineral-stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Mineral-stock water1.0L; no measured final-volume statement.\",\n    \"rationale\"\
    : \"Keep solvent, stock strength and receiving amount at their named preparation\
    \ stage. Do not use the parent JCM197 basal formulation or mineral recipe as JCM684\
    \ components.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Exact source table/stage boundary\",\n      \
    \  \"exact_source_quote\": \"Distilled water 1.0 L Dissolve nitrilotriacetic acid\"\
    ,\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Vitamin-stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Vitamin-stock water1.0L; provider separately declares1000ml stock volume.\"\
    ,\n    \"rationale\": \"Keep solvent, stock strength and receiving amount at their\
    \ named preparation stage. Do not use the parent JCM197 basal formulation or mineral\
    \ recipe as JCM684 components.\",\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Exact source table/stage boundary\",\n      \
    \  \"exact_source_quote\": \"Lipoic acid 5.0 mg Distilled water 1.0 L Trace mineral\
    \ solution:\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Mineral receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Receive9.0ml of this JCM684 mineral stock.\",\n    \"rationale\": \"Keep solvent,\
    \ stock strength and receiving amount at their named preparation stage. Do not\
    \ use the parent JCM197 basal formulation or mineral recipe as JCM684 components.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Exact source table/stage boundary\",\n      \
    \  \"exact_source_quote\": \"Trace mineral solution (see below) 9.0 ml\",\n  \
    \      \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"Vitamin receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Receive10.0ml of the JCM197 vitamin stock only.\",\n    \"rationale\": \"\
    Keep solvent, stock strength and receiving amount at their named preparation stage.\
    \ Do not use the parent JCM197 basal formulation or mineral recipe as JCM684 components.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm684\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Exact source table/stage boundary\",\n      \
    \  \"exact_source_quote\": \"Trace vitamins (see Medium No. 197 ) 10.0 ml\",\n\
    \        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"Main-medium pH\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5,\n        \"\
    decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5,\n        \"\
    decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components and adjust pH to 7.5. Bring to a boil, then\
    \ cool down and distribute into culture vessels under a N2 gas stream. Seal with\
    \ butyl rubber stoppers and autoclave. Prior to inoculation, add the following\
    \ solution (autoclaved under a N2 atmosphere) into the medium (per liter):\"\n\
    \        },\n        \"decision\": \"evidence_only\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components and adjust pH to 7.5. Bring to a boil, then\
    \ cool down and distribute into culture vessels under a N2 gas stream. Seal with\
    \ butyl rubber stoppers and autoclave. Prior to inoculation, add the following\
    \ solution (autoclaved under a N2 atmosphere) into the medium (per liter):\"\n\
    \        },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"\
    proposed_source_representation\": \"Main-medium preparation pH7.5; stock pH6.5\
    \ must remain separate.\",\n    \"rationale\": \"The prose retains7.5 but top-level\
    \ ph_value6.5 conflicts; the latter belongs to the mineral stock.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\",\n        \"source_locator\"\
    : \"Main preparation\",\n        \"exact_source_quote\": \"Mix components and\
    \ adjust pH to 7.5.\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Mineral-stock pH and titrant\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n\
    \          \"step_number\": 2,\n          \"action\": \"ADJUST_PH\",\n       \
    \   \"description\": \"Dissolve nitrilotriacetic acid at first and adjust pH to\
    \ 6.5 with KOH. Then proceed to add the minerals.\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n\
    \          \"step_number\": 2,\n          \"action\": \"ADJUST_PH\",\n       \
    \   \"description\": \"Dissolve nitrilotriacetic acid at first and adjust pH to\
    \ 6.5 with KOH. Then proceed to add the minerals.\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Dissolve\
    \ NTA first, adjust its stock to pH6.5 with KOH, then add minerals. KOH strength\
    \ and volume unspecified.\",\n    \"rationale\": \"Retain the procedure within\
    \ the stock rather than as an unqualified step of the assembled medium; do not\
    \ invent titrant quantities.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Trace-mineral stock preparation\",\n        \"\
    exact_source_quote\": \"Dissolve nitrilotriacetic acid at first and adjust pH\
    \ to 6.5 with KOH.  Then proceed to add the minerals.\",\n        \"snapshot_sha256\"\
    : \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\",\n    \
    \    \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Main anaerobic preparation and pre-inoculation sulfide\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components and adjust pH to 7.5. Bring to a boil, then\
    \ cool down and distribute into culture vessels under a N2 gas stream. Seal with\
    \ butyl rubber stoppers and autoclave. Prior to inoculation, add the following\
    \ solution (autoclaved under a N2 atmosphere) into the medium (per liter):\"\n\
    \        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n    \
    \      \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n          \"\
    description\": \"Mix components and adjust pH to 7.5. Bring to a boil, then cool\
    \ down and distribute into culture vessels under a N2 gas stream. Seal with butyl\
    \ rubber stoppers and autoclave. Prior to inoculation, add the following solution\
    \ (autoclaved under a N2 atmosphere) into the medium (per liter):\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Boil/cool/distribute under N2, seal and autoclave; add separately autoclaved\
    \ anoxic5% sulfide8ml per liter before inoculation.\",\n    \"rationale\": \"\
    Local step ends at a colon and omits the quantitative sulfide addition. This source\
    \ says N2 gas stream/atmosphere without a numerical purity; do not add100% or\
    \ import the parent197 gas mixture.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"Main and pre-inoculation preparation\",\n   \
    \     \"exact_source_quote\": \"Bring to a boil, then cool down and distribute\
    \ into culture vessels under a N 2 gas stream. Seal with butyl rubber stoppers\
    \ and autoclave.  Prior to inoculation, add the following solution (autoclaved\
    \ under a N 2 atmosphere) into the medium (per liter): 5% Na 2 S·9H 2 O solution\
    \ 8.0 ml\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"JCM stated default sterilization cycle\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_TYEG_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components and adjust pH to 7.5. Bring to\
    \ a boil, then cool down and distribute into culture vessels under a N2 gas stream.\
    \ Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the\
    \ following solution (autoclaved under a N2 atmosphere) into the medium (per liter):\"\
    \n          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"ADJUST_PH\",\n            \"description\": \"Dissolve nitrilotriacetic acid\
    \ at first and adjust pH to 6.5 with KOH. Then proceed to add the minerals.\"\n\
    \          }\n        ],\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components and adjust pH to 7.5. Bring to\
    \ a boil, then cool down and distribute into culture vessels under a N2 gas stream.\
    \ Seal with butyl rubber stoppers and autoclave. Prior to inoculation, add the\
    \ following solution (autoclaved under a N2 atmosphere) into the medium (per liter):\"\
    \n          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"ADJUST_PH\",\n            \"description\": \"Dissolve nitrilotriacetic acid\
    \ at first and adjust pH to 6.5 with KOH. Then proceed to add the minerals.\"\n\
    \          }\n        ],\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": \"Apply explicitly stated121°C/15min default\
    \ where JCM684 calls for autoclaving and no different instruction exists.\",\n\
    \    \"rationale\": \"Unlike an assumed standard cycle, this temperature/time\
    \ is printed in the exact source. Preserve any component-specific exception; parent197\
    \ unrelated preparation is outside scope.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm684\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=684\"\
    ,\n        \"source_locator\": \"JCM684 page default instruction\",\n        \"\
    exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"e525065e3e9a570d0356a81666f6b5217b81414a99a631dadaf381a3ce51793b\"\
    ,\n        \"parsed_text_sha256\": \"2af95361a14d3eb848869817ee7ca99b8c34d619cc24ea3a3cac89ce24da479e\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact source identity and maintained ownership
  outcome: supported
  summary: Exact JCM684 title/accession and stable ID resolve the sole explicit normalized
    owner. All31 ingredient concentrations agree across target and owner; generated-only
    merge metadata does not constitute source confirmation.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - primary684
  - vitamin197
  - vitamin3861
  - vitaminJ197
- assessment_id: evidence
  area: evidence
  topic: Claim-level support and exact source stages
  outcome: concern
  summary: No ingredient amount has attached supporting evidence in either local layer.
    Every local concentration and scoped source-only quantitative context has an inventory
    decision with exact quotations and locators. Matching provider transcription receives
    evidence_only, not verified. Source quantities and provider normalization remain
    separate.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - quantity-inventory
  - primary684
  - vitamin197
  - vitamin3861
  - vitaminJ197
- assessment_id: preparation
  area: completeness
  topic: Main and stock preparation boundaries
  outcome: concern
  summary: Main pH7.5 and mineral pH6.5 are conflated; stock mineral preparation is
    at the main root, receiving references/doses are absent, and the sulfide addition
    sentence is cut off before its quantity. Source default121°C/15min and each stock
    stage need explicit retention.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - quantity-inventory
  - primary684
  - vitamin197
  - vitamin3861
  - vitaminJ197
- assessment_id: classification
  area: scope
  topic: Composition and physical state
  outcome: supported
  summary: COMPLEX/UNDEFINED/LIQUID is consistent with tryptone and yeast extract
    and no agar. Filing and generic cultivation application are not organism evidence.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - primary684
  - vitamin197
  - vitamin3861
  - vitaminJ197
- assessment_id: forms
  area: grounding
  topic: Source-specified molecular forms and mixtures
  outcome: concern
  summary: Named mineral hydrates agree with their asserted IDs; generic glucose and
    vitaminB12 remain generic. Calcium pantothenate primary wording is stereochemically
    unqualified while CHEBI31345 has a stereospecific structure and D-calcium synonyms.
    This is unsupported extra specificity to qualify, not proof the supplied material
    is the wrong enantiomer. Tryptone and yeast extract remain mixtures without invented
    molecular IDs.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - primary684
  - vitamin197
  - vitamin3861
  - vitaminJ197
- assessment_id: growth
  area: scope
  topic: Growth, taxonomy and graph assertion scope
  outcome: not_applicable
  summary: The medium title, bacterial filing and generic Microbial cultivation application
    are catalog context, not strain-level experimental growth evidence. No organism
    identifier, growth assertion, phenotype or graph membership is added. No internal
    variant/reference relationship is asserted in either complete local record.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - primary684
  - vitamin197
  - vitamin3861
  - vitaminJ197
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: writer
  area: provenance
  topic: Maintained input and current import/merge behavior
  outcome: concern
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  target_ids:
  - CultureMech:015413
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: culturemech.015413.stock-and-volume-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Separate main amounts, stock compositions and receiving volumes
  description: Both layers flatten31 ingredients. FeSO4 heptahydrate is5G_PER_L where
    the source adds5µl of10% stock; sodium sulfide nonahydrate is8G_PER_L where the
    source adds8ml of5% stock per liter. Mineral/vitamin stock amounts are undiluted
    main entries, and NaCl explicitly sums main and stock values. Bare percent bases
    and final assembled volume are not established.
  target_ids:
  - CultureMech:015413
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - primary684
  - vitamin197
  - vitamin3861
  - quantity-inventory
  - bound-owner-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
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
  issue_key: culturemech.015413.preparation-stage-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore main pH7.5 and keep mineral-stock pH6.5 scoped
  description: Top-level ph_value6.5 takes the mineral-stock value despite main preparation
    explicitly saying7.5. The stock preparation sits at the root, and the main sulfide
    instruction ends before its8ml/L amount.
  target_ids:
  - CultureMech:015413
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - primary684
  - vitamin197
  - vitamin3861
  - quantity-inventory
  - bound-owner-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
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
  issue_key: culturemech.015413.pantothenate-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify unsupported pantothenate stereochemistry
  description: JCM197 and provider3861 say calcium pantothenate without D/L qualification;
    CHEBI31345 resolves correctly but its structure is stereospecific and synonyms
    include D-calcium pantothenate. Matching labels alone do not establish that source
    specificity.
  target_ids:
  - CultureMech:015413
  field_paths:
  - ingredients[27].term
  - ingredients[27].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - primary684
  - vitamin197
  - vitamin3861
  - quantity-inventory
  - bound-owner-context
  - chebi31345
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
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
  description: Reconstruct source-native main batch and separate mineral/vitamin stocks
    with9ml/10ml receiving doses. Preserve iron5µl and sulfide8ml/L stock additions,
    percent qualifiers and named hydrates. Reassess every concentration against the
    complete inventory without assuming final volume or percent basis.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015413
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
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
  description: Represent main pH7.5 separately from stock pH6.5/KOH; complete the
    sulfide addition and its timing/sterilization. Attach the exact source default
    cycle where applicable and preserve nitrogen context without invented gas proportions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015413
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
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
  description: Recover exact supplied-form evidence or qualify the mapping. Do not
    declare a wrong enantiomer or choose an unverified replacement from a similar
    label.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015413
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_tyeg_medium.yaml
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
- Only the exact bound collection/provider sources and pinned identifiers were assessed.
  Current source differences do not establish source chronology or the exact historical
  import version.
- Listed water, stock recipe volumes and receiving additions do not establish a measured
  assembled final volume. No unqualified percent basis, density, unspecified stock
  strength, sterilization cycle or source-specific replacement identifier is invented.
- Exact main JCM684 API and its preserved retry returned503; the old normalization
  origin cannot be reconstructed from these failures. Complete exact JCM684 primary
  and scoped parent vitamins were available, so this optional provider-route failure
  does not prevent assessing the documented primary/record conflicts.
- Optional provider trace-mineral solution4585 returned503. Exact JCM684 primary supplies
  the stock recipe and receiving9ml dose; no provider-declared stock volume is fabricated.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-027
- generated-medium
```
