# Source and formulation review: belh1_medium (CultureMech:010333)

- Review: 20261021T231346Z-culturemech-010333-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:07:32Z
- Finished UTC: 2026-10-21T23:13:46Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 874 and exact TOGO M913 establish BELH1 identity, but water, resazurin and six stock doses have incorrect stored units. The empty trace stock omits its named JCM 439 composition, and stage-specific pH, gas and sterilization instructions are missing. Only the named trace subsection transfers from M439; its local cobalt and nickel hydrate grounding also needs correction.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 401; batch 041 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty task batches contain 400 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 403 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010333 | data/merge_yaml/merged/BELH1_MEDIUM.yaml | generated | belh1_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010333 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010333 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch041/401/strict.tsv |
| validate-terms | passed | True | CultureMech:010333 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010333 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010333 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ874api | unavailable | False | CultureMech:010333 | Optional current MediaDive J874 access returned HTTP 503. Complete JCM874 and exact TOGO source content are available; the failed response is not formula evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010333.

The four documented recipes completed; interpret the scope of each separately.

### Exact source and stock boundaries

identity: supported. Targets: CultureMech:010333.

BELH1 is TOGO M913, whose original source is JCM 874. The sole maintained contributor is resolved by exact ID and merge provenance. M439/JCM439 contributes only its named trace subsection, not its basal recipe, other stocks, organism title or high_metal annotation.

### Current identifiers and source chemical forms

grounding: concern. Targets: CultureMech:010333.

The target has 12/13 primary and 8/13 current CHEBI-based secondary ingredient links (92.31% and 61.54% on a 0–100 linkage scale). Exact current labels are resolved in the grounding inventory; these metrics do not measure correctness. The dependency’s supplied cobalt/nickel hexahydrates differ from its existing anhydrous terms. No legacy MIM assertion occurs in target or owner. Missing stock or mixture grounding is kept unresolved, not guessed.

### Stage-specific preparation and classifications

completeness: concern. Targets: CultureMech:010333.

The source specifies pH 7.5, N2:CO2 4:1, cooling, distinct autoclaved versus filter-sterilized additions, gas storage and butyl-stopper handling. None is encoded as preparation steps. COMPLEX/UNDEFINED and LIQUID are consistent with yeast extract and this recipe. No growth temperature, pressure or organism growth is inferred from BELH1 or the stock-parent title.

### Claims and source access limits

evidence: supported. Targets: CultureMech:010333.

Current JCM and exact structured TOGO sources supply direct scoped formulation evidence. No attached target/owner historical amount claims require raw authentication. Retained historical reports and parent history are derivative/context evidence only. Optional MediaDive access failure does not make the adequately sourced current formulation unavailable.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010333.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010333.

41 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "935",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "935",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "Distilled water 935.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 935,
      "unit": "ml",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "Volume was stored as a mass rate; retain the literal basal water input without density conversion."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "Yeast extract 1.0 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "NaCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "70",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "70",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "NaCl 70.0 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 70,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "CaCl2 dihydrate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.1 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.1,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "KH2PO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "KH 2 PO 4 0.1 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.1,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "NH4Cl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "NH 4 Cl 1.0 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "K2HPO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "K 2 HPO 4 0.1 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.1,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Resazurin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "Resazurin 1.0 mg",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1,
      "unit": "mg",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The source mass is 1 mg = 0.001 g, not the stored 1 g/L. Preserve the batch basis."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "KCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "KCl 0.1 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.1,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Na2S2O3 pentahydrate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Main table",
        "exact_source_quote": "Na 2 S 2 O 3 ·5H 2 O 5.0 g",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 5,
      "unit": "g",
      "stage": "basal recipe",
      "measured_final_volume": null
    },
    "rationale": "The nominal mass numeral agrees, but g/L requires an explicit recipe basis. The staged additions do not establish a measured final volume; attach current claim-level evidence without automatic renormalization."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "KOH titrant amount",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation",
        "exact_source_quote": "adjust pH to 7.5 with KOH",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "titrant": "KOH",
      "dose": null,
      "endpoint_pH": 7.5
    },
    "rationale": "VARIABLE is compatible with an unquantified titration; do not invent a titrant mass or molarity."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "CO2 atmosphere",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Basal autoclaving",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "gas": "CO2",
      "N2_CO2_ratio": [
        4,
        1
      ],
      "basis": "v/v",
      "absolute_gas_amount": null
    },
    "rationale": "The gas ratio is explicit; neither absolute gas volume nor dissolved concentration is given. Keep VARIABLE distinct from the missing atmosphere instruction."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "N2 atmosphere",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Basal autoclaving",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "gas": "N2",
      "N2_CO2_ratio": [
        4,
        1
      ],
      "basis": "v/v",
      "absolute_gas_amount": null
    },
    "rationale": "The gas ratio is explicit; neither absolute gas volume nor dissolved concentration is given. Keep VARIABLE distinct from the missing atmosphere instruction."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Trace element stock addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "Trace element solution (see Medium No. 439 ) 10.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "dose": 10,
      "unit": "ml",
      "strength": null,
      "stage": "basal addition",
      "denominator": "printed recipe; final volume not measured"
    },
    "rationale": "A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition and addition stage; percent basis is not printed, so no w/v or molarity conversion is justified."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "NaHCO3 addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "8% NaHCO 3 solution* 25.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "dose": 25,
      "unit": "ml",
      "strength": {
        "value": 8,
        "unit": "percent",
        "basis": null
      },
      "stage": "post-cooling; filter-sterilized",
      "denominator": "printed recipe; final volume not measured"
    },
    "rationale": "A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition and addition stage; percent basis is not printed, so no w/v or molarity conversion is justified."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "NaHCO3 stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "8% NaHCO 3 solution* 25.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "strength": {
        "value": 8,
        "unit": "percent",
        "basis": null
      },
      "stock_batch_volume": null,
      "stage": "post-cooling; filter-sterilized"
    },
    "rationale": "The strength exists only in the display name while composition is empty. Represent it explicitly without inventing a stock batch volume, percentage basis or hydrate replacement."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "MgCl2 hexahydrate addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "15% MgCl 2 ·6H 2 O solution 20.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "dose": 20,
      "unit": "ml",
      "strength": {
        "value": 15,
        "unit": "percent",
        "basis": null
      },
      "stage": "post-cooling; autoclaved",
      "denominator": "printed recipe; final volume not measured"
    },
    "rationale": "A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition and addition stage; percent basis is not printed, so no w/v or molarity conversion is justified."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "MgCl2 hexahydrate stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "15% MgCl 2 ·6H 2 O solution 20.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "strength": {
        "value": 15,
        "unit": "percent",
        "basis": null
      },
      "stock_batch_volume": null,
      "stage": "post-cooling; autoclaved"
    },
    "rationale": "The strength exists only in the display name while composition is empty. Represent it explicitly without inventing a stock batch volume, percentage basis or hydrate replacement."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Glucose addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "1 M Glucose solution 20.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "dose": 20,
      "unit": "ml",
      "strength": {
        "value": 1,
        "unit": "M"
      },
      "stage": "post-cooling; autoclaved",
      "denominator": "printed recipe; final volume not measured"
    },
    "rationale": "A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition and addition stage; percent basis is not printed, so no w/v or molarity conversion is justified."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Glucose stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "1 M Glucose solution 20.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "strength": {
        "value": 1,
        "unit": "M"
      },
      "stock_batch_volume": null,
      "stage": "post-cooling; autoclaved"
    },
    "rationale": "The strength exists only in the display name while composition is empty. Represent it explicitly without inventing a stock batch volume, percentage basis or hydrate replacement."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Na2S nonahydrate addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution 8.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "dose": 8,
      "unit": "ml",
      "strength": {
        "value": 5,
        "unit": "percent",
        "basis": null
      },
      "stage": "final addition per liter",
      "denominator": "per liter"
    },
    "rationale": "A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition and addition stage; percent basis is not printed, so no w/v or molarity conversion is justified."
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Na2S nonahydrate stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution 8.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "strength": {
        "value": 5,
        "unit": "percent",
        "basis": null
      },
      "stock_batch_volume": null,
      "stage": "final addition per liter"
    },
    "rationale": "The strength exists only in the display name while composition is empty. Represent it explicitly without inventing a stock batch volume, percentage basis or hydrate replacement."
  },
  {
    "quantity_id": "q23",
    "component_or_context": "L-cysteine HCl monohydrate addition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "5% L-Cysteine·HCl·H 2 O solution 10.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "dose": 10,
      "unit": "ml",
      "strength": {
        "value": 5,
        "unit": "percent",
        "basis": null
      },
      "stage": "final addition per liter",
      "denominator": "per liter"
    },
    "rationale": "A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition and addition stage; percent basis is not printed, so no w/v or molarity conversion is justified."
  },
  {
    "quantity_id": "q24",
    "component_or_context": "L-cysteine HCl monohydrate stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[5].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Staged solution tables",
        "exact_source_quote": "5% L-Cysteine·HCl·H 2 O solution 10.0 ml",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "strength": {
        "value": 5,
        "unit": "percent",
        "basis": null
      },
      "stock_batch_volume": null,
      "stage": "final addition per liter"
    },
    "rationale": "The strength exists only in the display name while composition is empty. Represent it explicitly without inventing a stock batch volume, percentage basis or hydrate replacement."
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Trace stock HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "HCl (25%) 12.5 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 12.5,
      "unit": "ml",
      "stage": "trace-stock batch",
      "HCl_strength": {
        "value": 25,
        "unit": "percent",
        "basis": null
      },
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Trace stock Na2MoO4 dihydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 36,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Trace stock Boric acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "H 3 BO 3 30.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 30,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Trace stock FeSO4 heptahydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "FeSO 4 ·7H 2 O 2.1 g",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 2.1,
      "unit": "g",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Trace stock MnCl2 tetrahydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "MnCl 2 ·4H 2 O 100.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 100,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Trace stock CoCl2 hexahydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "CoCl 2 ·6H 2 O 190.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 190,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Trace stock NiCl2 hexahydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "NiCl 2 ·6H 2 O 24.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 24,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Trace stock ZnSO4 heptahydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "144",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 144.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 144,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Trace stock CuCl2 dihydrate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "CuCl 2 ·2H 2 O 2.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 2,
      "unit": "mg",
      "stage": "trace-stock batch",
      "HCl_strength": null,
      "receiving_dose": {
        "value": 10,
        "unit": "ml",
        "source": "JCM874"
      }
    },
    "rationale": "The named stock is absent from BELH1 and its parent components are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic only, not a receiving-medium rate. HCl plus listed water does not declare a measured one-litre final stock."
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Trace stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "988.0",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution subsection",
        "exact_source_quote": "Distilled water 987.0 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 987,
      "unit": "ml",
      "stage": "trace stock only",
      "final_volume": null
    },
    "rationale": "The parent water 988 G_PER_L is a mixed basal/stock quantity, explicitly excluded from transfer. Do not simply replace that entire parent field with 987; separate the parent stages and add only the 987 ml stock input to this dependency."
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Trace HCl percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml",
        "field_path": "ingredients[12].preferred_term",
        "stored": "HCl (25%)",
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "Trace element solution",
        "exact_source_quote": "HCl (25%) 12.5 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b",
        "accessed_at": "2026-10-21T13:13:22.895121Z"
      }
    ],
    "proposed_source_representation": {
      "value": 25,
      "unit": "percent",
      "basis": null,
      "dose_ml": 12.5
    },
    "rationale": "The percentage is explicit but its basis is not. Do not convert to molarity or infer stock final volume."
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Basal pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation/default exception scope",
        "exact_source_quote": "adjust pH to 7.5 with KOH",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "pH": 7.5,
      "stage": "before autoclaving"
    },
    "rationale": "Preserve the explicitly named stage. The default cycle does not override filter sterilization, and a per-liter dose is not proof of a measured assembled volume."
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Autoclave temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation/default exception scope",
        "exact_source_quote": "autoclaving at 121°C for 15 min",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 121,
      "stage": "default only where no exception"
    },
    "rationale": "Preserve the explicitly named stage. The default cycle does not override filter sterilization, and a per-liter dose is not proof of a measured assembled volume."
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Autoclave duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation/default exception scope",
        "exact_source_quote": "autoclaving at 121°C for 15 min",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "duration_min": 15,
      "stage": "default only where no exception"
    },
    "rationale": "Preserve the explicitly named stage. The default cycle does not override filter sterilization, and a per-liter dose is not proof of a measured assembled volume."
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Basal gas ratio",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation/default exception scope",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "N2": 4,
      "CO2": 1,
      "basis": "v/v",
      "stage": "basal autoclaving"
    },
    "rationale": "Preserve the explicitly named stage. The default cycle does not override filter sterilization, and a per-liter dose is not proof of a measured assembled volume."
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Bicarbonate storage gas",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation/default exception scope",
        "exact_source_quote": "*filter-sterilized and stored under N 2 -CO 2 , 4:1, v/v",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "N2": 4,
      "CO2": 1,
      "basis": "v/v",
      "stage": "filter-sterilized bicarbonate storage"
    },
    "rationale": "Preserve the explicitly named stage. The default cycle does not override filter sterilization, and a per-liter dose is not proof of a measured assembled volume."
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Final addition denominator",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BELH1_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm874",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874",
        "source_locator": "Preparation/default exception scope",
        "exact_source_quote": "Finally, add per liter",
        "snapshot_sha256": "538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73",
        "parsed_text_sha256": "651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0",
        "accessed_at": "2026-10-21T22:43:54.692902Z"
      }
    ],
    "proposed_source_representation": {
      "denominator_L": 1,
      "stage": "only final cysteine and sulfide additions"
    },
    "rationale": "Preserve the explicitly named stage. The default cycle does not override filter sterilization, and a per-liter dose is not proof of a measured assembled volume."
  }
]

## Findings

### f1: Water, resazurin and stock doses have incorrect units

major / open / confirmed; issue key: culturemech.010333.amount-units.

The source gives 935 ml water and 1 mg resazurin, while both local layers store 935 and 1 G_PER_L. Six liquid stock additions are also stored as mass rates. These dimensional errors are separate from the unknown measured final volume.

### f2: The six named stocks have empty compositions

major / open / confirmed; issue key: culturemech.010333.stock-composition.

All six solutions use Unknown solution placeholders and empty composition arrays. The available exact sources support the trace constituents and the other stated strengths, but not invented percent bases or batch volumes.

### f3: The named trace stock loses cobalt and nickel hydration

major / open / confirmed; issue key: culturemech.010333.trace-hydrates.

M439 ingredients[17] and [18] name explicit hexahydrates but point to cobalt dichloride and nickel dichloride. The named stock transfer makes supplied-form specificity relevant even though the receiving solution is currently empty.

### f4: The source preparation stages are missing

major / open / confirmed; issue key: culturemech.010333.preparation.

Missing pH, atmosphere, cooling and separate sterilization/storage instructions prevent faithful interpretation of the six additions. This is a formulation-stage omission, not a request to invent a routine protocol.

## Recommended Actions And Acceptance Checks

### a1

Correct maintained amounts to source units and stages, keeping original batch amounts and explicit final per-litre additions distinct; attach exact current evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent exact stock composition, dose and stage; resolve M439 only to the trace subsection and preserve its separate water input.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve exact hydrated terms from authoritative ontology evidence before reuse, preserving all other parent recipe scope. Do not invent replacement identifiers.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add the exact source sequence and exceptions. Retain unqualified percentage bases and unknown measured final volume; do not apply the default autoclave cycle to bicarbonate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BELH1_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BELH1_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BELH1_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch041/401/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch041/401/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BELH1_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BELH1_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BELH1_MEDIUM.yaml:1:id: CultureMech:010333<br>./data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml:1:id: CultureMech:010333<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch041/source-preflight-bound/401/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 30 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| trace-owner | data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml; Full parent read; only ingredients[12:21] and separately identified trace water are transferred | context_only | The parent is a source dependency, not a contributor to BELH1. Its basal ingredients, other stocks, gas, pH, receiving doses and high_metal flag are exclusion context. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874; Complete table and staged preparation | supports | Exact current primary confirms M913 original accession JCM 874, basal amounts and late additions. |
| trace-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439; Trace element solution subsection only | supports | The named trace subsection contains HCl, eight salts and water; none of the parent medium or other stock instructions transfers. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M913; Complete components and comments | supports | Exact provider separately retains basal, post-cooling and final addition components; the JavaScript page itself is not formulation evidence. |
| trace-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439; $.components[3] only | supports | Only the trace-element component is relevant to the receiving M913 formulation. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch041/401/grounding-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| history-inventory | /private/tmp/culturemech-review-work-batch041/401/history-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact pinned current CHEBI preferred-key rows; metadata source commit/hash | context_only | {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32035": [{"label": "KOH", "match_type": "preferred_term", "identifier": "CHEBI:32035", "preferred_term": "KOH", "ontology_id": "CHEBI:32035", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer and guarded merger are captured implementation context, not a replay of the historical import. Wrong units and empty stocks exist in both maintained owner and target; do not assign their historical cause to current code without execution evidence. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer and guarded merger are captured implementation context, not a replay of the historical import. Wrong units and empty stocks exist in both maintained owner and target; do not assign their historical cause to current code without execution evidence. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer and guarded merger are captured implementation context, not a replay of the historical import. Wrong units and empty stocks exist in both maintained owner and target; do not assign their historical cause to current code without execution evidence. |
| history-metadata | data/merge_yaml/merged/BELH1_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| mediadiveJ874api-attempt | https://mediadive.dsmz.de/rest/medium/J874; Preserved exact public retrieval result | context_only | Optional current MediaDive J874 access returned HTTP 503. Complete JCM874 and exact TOGO source content are available; the failed response is not formula evidence. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch041/401/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Optional current MediaDive J874 access returned HTTP 503. Complete JCM874 and exact TOGO source content are available; the failed response is not formula evidence.
- The M439 parent was read in full for exclusion and provenance context. Only ingredients[12] through [20], the source trace water and named receiving stock are quantitatively transferred; other parent ingredients, eight parent doses, gases, pH and high_metal flag are excluded from this single-record formulation assessment.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T231346Z-culturemech-010333-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: belh1_medium (CultureMech:010333)'
started_at: '2026-10-21T23:07:32Z'
finished_at: '2026-10-21T23:13:46Z'
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
summary: JCM 874 and exact TOGO M913 establish BELH1 identity, but water, resazurin
  and six stock doses have incorrect stored units. The empty trace stock omits its
  named JCM 439 composition, and stage-specific pH, gas and sterilization instructions
  are missing. Only the named trace subsection transfers from M439; its local cobalt
  and nickel hydrate grounding also needs correction.
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
  - path: data/merge_yaml/merged/BELH1_MEDIUM.yaml
    sha256: 4160c184a6d0104903083faa00b281b4d219cd6c0376f5e85ee1ea3b886e2c33
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    sha256: 61b72e39e60ca8f44e869309dd78d47a3277760d3bf16ffaaaac30da77fab6b0
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
    sha256: 129fe67a47c71b93714571d979ff1fe812c9fe55bf71ed579304901ed894df1a
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BELH1_MEDIUM.md
    sha256: 5d3311288954f340ae9d19279448015f997be1abe5708e98c02834277cba9f9c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.md
    sha256: b64e3213b70e037d2f22e037ce17153d05ae9f95351762c8084e7049333ee303
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
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
  selection: Task review 401; batch 041 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty task batches contain
    400 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 403 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010333
targets:
- target_id: CultureMech:010333
  path: data/merge_yaml/merged/BELH1_MEDIUM.yaml
  label: belh1_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BELH1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BELH1_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch041/401/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch041/401/strict.tsv"
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BELH1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BELH1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010333
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
  - CultureMech:010333
- check_id: mediadiveJ874api-source-access
  name: 'Exact source content access: mediadiveJ874api'
  required: false
  status: unavailable
  summary: Optional current MediaDive J874 access returned HTTP 503. Complete JCM874
    and exact TOGO source content are available; the failed response is not formula
    evidence.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - mediadiveJ874api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BELH1_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BELH1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:41.791288Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BELH1_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch041/401/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:42.751333Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch041/401/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BELH1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:44.361739Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BELH1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:45.192095Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:10:29Z'
  support: supports
  summary: './data/merge_yaml/merged/BELH1_MEDIUM.yaml:1:id: CultureMech:010333

    ./data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml:1:id: CultureMech:010333

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/source-preflight-bound/401/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:10:29Z'
  support: supports
  summary: 30 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2734b97205522ffcdb4e8472c70001ea3ab6aa7e9c2f7aa45fdcb158b3681c12
- evidence_id: trace-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
  locator: Full parent read; only ingredients[12:21] and separately identified trace
    water are transferred
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: The parent is a source dependency, not a contributor to BELH1. Its basal
    ingredients, other stocks, gas, pH, receiving doses and high_metal flag are exclusion
    context.
  snapshot_sha256: 61b72e39e60ca8f44e869309dd78d47a3277760d3bf16ffaaaac30da77fab6b0
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874
  locator: Complete table and staged preparation
  accessed_at: '2026-10-21T22:43:54.692902Z'
  support: supports
  summary: Exact current primary confirms M913 original accession JCM 874, basal amounts
    and late additions.
  quote: Distilled water 935.0 ml
  snapshot_sha256: 538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73
- evidence_id: trace-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439
  locator: Trace element solution subsection only
  accessed_at: '2026-10-21T13:13:22.895121Z'
  support: supports
  summary: The named trace subsection contains HCl, eight salts and water; none of
    the parent medium or other stock instructions transfers.
  quote: 'Trace element solution: HCl (25%) 12.5 ml'
  snapshot_sha256: 2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M913
  locator: Complete components and comments
  accessed_at: '2026-10-21T22:43:53.886594Z'
  support: supports
  summary: Exact provider separately retains basal, post-cooling and final addition
    components; the JavaScript page itself is not formulation evidence.
  snapshot_sha256: 2e680c92c62f0dfce8cb70b3e0352f18629681b50159abbe0dd6b12304dec219
- evidence_id: trace-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M439
  locator: $.components[3] only
  accessed_at: '2026-10-21T13:13:19.779835Z'
  support: supports
  summary: Only the trace-element component is relevant to the receiving M913 formulation.
  snapshot_sha256: 8f66c42a9c785a07759e4c017d8253f0acb25d377dce0f49e79a7c9b800ba35c
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/401/grounding-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: e9b88dc101a3bd97f53b09499beb95699e4e8de6d4584a6e2f43a5636412c710
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/401/history-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 03fb8d4fb7b8ac4bdeaab84043a98c0a644ff820cc47fc5212937463667f15ac
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32035
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T06:57:47.017507Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 6ed3df00965b4707265cfced80411c4b1937b727f8c2093addbc467f88ce2ec8
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact pinned current CHEBI preferred-key rows; metadata source commit/hash
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: '{"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label":
    "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32035": [{"label": "KOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32035", "preferred_term": "KOH", "ontology_id": "CHEBI:32035",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label":
    "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term":
    "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Current importer and guarded merger are captured implementation context,
    not a replay of the historical import. Wrong units and empty stocks exist in both
    maintained owner and target; do not assign their historical cause to current code
    without execution evidence.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Current importer and guarded merger are captured implementation context,
    not a replay of the historical import. Wrong units and empty stocks exist in both
    maintained owner and target; do not assign their historical cause to current code
    without execution evidence.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Current importer and guarded merger are captured implementation context,
    not a replay of the historical import. Wrong units and empty stocks exist in both
    maintained owner and target; do not assign their historical cause to current code
    without execution evidence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BELH1_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml", "events": 12, "timestamp_issues":
    []}]'
- evidence_id: mediadiveJ874api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J874
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:43:53.348988Z'
  support: context_only
  summary: Optional current MediaDive J874 access returned HTTP 503. Complete JCM874
    and exact TOGO source content are available; the failed response is not formula
    evidence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/401/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:10:29Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 69cddd0b12c08750ecbe924e1f145daa76fdc03d29749d7f3647a805776615ac
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source and stock boundaries
  outcome: supported
  summary: BELH1 is TOGO M913, whose original source is JCM 874. The sole maintained
    contributor is resolved by exact ID and merge provenance. M439/JCM439 contributes
    only its named trace subsection, not its basal recipe, other stocks, organism
    title or high_metal annotation.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - provider
  - trace-primary
  - trace-provider
  - trace-owner
- assessment_id: grounding
  area: grounding
  topic: Current identifiers and source chemical forms
  outcome: concern
  summary: The target has 12/13 primary and 8/13 current CHEBI-based secondary ingredient
    links (92.31% and 61.54% on a 0–100 linkage scale). Exact current labels are resolved
    in the grounding inventory; these metrics do not measure correctness. The dependency’s
    supplied cobalt/nickel hexahydrates differ from its existing anhydrous terms.
    No legacy MIM assertion occurs in target or owner. Missing stock or mixture grounding
    is kept unresolved, not guessed.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - grounding-inventory
  - mim
  - primary
  - trace-primary
  - trace-owner
- assessment_id: conditions
  area: completeness
  topic: Stage-specific preparation and classifications
  outcome: concern
  summary: The source specifies pH 7.5, N2:CO2 4:1, cooling, distinct autoclaved versus
    filter-sterilized additions, gas storage and butyl-stopper handling. None is encoded
    as preparation steps. COMPLEX/UNDEFINED and LIQUID are consistent with yeast extract
    and this recipe. No growth temperature, pressure or organism growth is inferred
    from BELH1 or the stock-parent title.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - primary
  - record
  - owner-0
  - quantity-inventory
- assessment_id: evidence-scope
  area: evidence
  topic: Claims and source access limits
  outcome: supported
  summary: Current JCM and exact structured TOGO sources supply direct scoped formulation
    evidence. No attached target/owner historical amount claims require raw authentication.
    Retained historical reports and parent history are derivative/context evidence
    only. Optional MediaDive access failure does not make the adequately sourced current
    formulation unavailable.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - primary
  - provider
  - trace-primary
  - history-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 41 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010333
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n \
    \       \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"935\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"935\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 935.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 935,\n      \"unit\"\
    : \"ml\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"Volume was stored as a mass rate; retain\
    \ the literal basal water input without density conversion.\"\n  },\n  {\n   \
    \ \"quantity_id\": \"q2\",\n    \"component_or_context\": \"Yeast extract\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      }\n   \
    \ ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.0 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"NaCl\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"70\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"70\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"NaCl 70.0 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 70,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"CaCl2\
    \ dihydrate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n \
    \       \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"CaCl 2 ·2H 2 O 0.1 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\": \"KH2PO4\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"KH 2 PO 4 0.1 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\": \"NH4Cl\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n      }\n   \
    \ ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"NH 4 Cl 1.0 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"K2HPO4\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"K 2 HPO 4 0.1 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\": \"Resazurin\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    correct\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n    ],\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Resazurin 1.0 mg\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The source mass is 1 mg = 0.001 g, not the\
    \ stored 1 g/L. Preserve the batch basis.\"\n  },\n  {\n    \"quantity_id\": \"\
    q9\",\n    \"component_or_context\": \"KCl\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"KCl 0.1 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\": \"Na2S2O3\
    \ pentahydrate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Na 2 S 2 O 3 ·5H 2 O 5.0 g\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 5,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"basal recipe\",\n      \"measured_final_volume\"\
    : null\n    },\n    \"rationale\": \"The nominal mass numeral agrees, but g/L\
    \ requires an explicit recipe basis. The staged additions do not establish a measured\
    \ final volume; attach current claim-level evidence without automatic renormalization.\"\
    \n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\": \"KOH\
    \ titrant amount\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    \"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    \"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm874\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 7.5 with KOH\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"titrant\": \"KOH\",\n    \
    \  \"dose\": null,\n      \"endpoint_pH\": 7.5\n    },\n    \"rationale\": \"\
    VARIABLE is compatible with an unquantified titration; do not invent a titrant\
    \ mass or molarity.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"CO2 atmosphere\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    \"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    \"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm874\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Basal autoclaving\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"gas\": \"CO2\",\n      \"\
    N2_CO2_ratio\": [\n        4,\n        1\n      ],\n      \"basis\": \"v/v\",\n\
    \      \"absolute_gas_amount\": null\n    },\n    \"rationale\": \"The gas ratio\
    \ is explicit; neither absolute gas volume nor dissolved concentration is given.\
    \ Keep VARIABLE distinct from the missing atmosphere instruction.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q13\",\n    \"component_or_context\": \"N2 atmosphere\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n        \"decision\"\
    : \"not_quantified\",\n        \"rationale\": \"\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n\
    \        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    \"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm874\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Basal autoclaving\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"gas\": \"N2\",\n      \"N2_CO2_ratio\"\
    : [\n        4,\n        1\n      ],\n      \"basis\": \"v/v\",\n      \"absolute_gas_amount\"\
    : null\n    },\n    \"rationale\": \"The gas ratio is explicit; neither absolute\
    \ gas volume nor dissolved concentration is given. Keep VARIABLE distinct from\
    \ the missing atmosphere instruction.\"\n  },\n  {\n    \"quantity_id\": \"q14\"\
    ,\n    \"component_or_context\": \"Trace element stock addition\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"Trace element solution (see Medium No. 439 ) 10.0 ml\",\n        \"snapshot_sha256\"\
    : \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\",\n    \
    \    \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose\": 10,\n      \"unit\"\
    : \"ml\",\n      \"strength\": null,\n      \"stage\": \"basal addition\",\n \
    \     \"denominator\": \"printed recipe; final volume not measured\"\n    },\n\
    \    \"rationale\": \"A liquid stock dose is stored as G_PER_L. Preserve the source\
    \ volume, composition and addition stage; percent basis is not printed, so no\
    \ w/v or molarity conversion is justified.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q15\",\n    \"component_or_context\": \"NaHCO3 addition\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"8% NaHCO 3 solution* 25.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose\": 25,\n      \"unit\"\
    : \"ml\",\n      \"strength\": {\n        \"value\": 8,\n        \"unit\": \"\
    percent\",\n        \"basis\": null\n      },\n      \"stage\": \"post-cooling;\
    \ filter-sterilized\",\n      \"denominator\": \"printed recipe; final volume\
    \ not measured\"\n    },\n    \"rationale\": \"A liquid stock dose is stored as\
    \ G_PER_L. Preserve the source volume, composition and addition stage; percent\
    \ basis is not printed, so no w/v or molarity conversion is justified.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\": \"NaHCO3 stock\
    \ strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[1].composition\",\n        \"stored\": [],\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"8% NaHCO 3 solution* 25.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"strength\": {\n        \"\
    value\": 8,\n        \"unit\": \"percent\",\n        \"basis\": null\n      },\n\
    \      \"stock_batch_volume\": null,\n      \"stage\": \"post-cooling; filter-sterilized\"\
    \n    },\n    \"rationale\": \"The strength exists only in the display name while\
    \ composition is empty. Represent it explicitly without inventing a stock batch\
    \ volume, percentage basis or hydrate replacement.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q17\",\n    \"component_or_context\": \"MgCl2 hexahydrate addition\",\n  \
    \  \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\": \"solutions[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"15% MgCl 2 ·6H 2 O solution 20.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose\": 20,\n      \"unit\"\
    : \"ml\",\n      \"strength\": {\n        \"value\": 15,\n        \"unit\": \"\
    percent\",\n        \"basis\": null\n      },\n      \"stage\": \"post-cooling;\
    \ autoclaved\",\n      \"denominator\": \"printed recipe; final volume not measured\"\
    \n    },\n    \"rationale\": \"A liquid stock dose is stored as G_PER_L. Preserve\
    \ the source volume, composition and addition stage; percent basis is not printed,\
    \ so no w/v or molarity conversion is justified.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q18\",\n    \"component_or_context\": \"MgCl2 hexahydrate stock strength\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\": \"solutions[2].composition\"\
    ,\n        \"stored\": [],\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"15% MgCl 2 ·6H 2 O solution 20.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"strength\": {\n        \"\
    value\": 15,\n        \"unit\": \"percent\",\n        \"basis\": null\n      },\n\
    \      \"stock_batch_volume\": null,\n      \"stage\": \"post-cooling; autoclaved\"\
    \n    },\n    \"rationale\": \"The strength exists only in the display name while\
    \ composition is empty. Represent it explicitly without inventing a stock batch\
    \ volume, percentage basis or hydrate replacement.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q19\",\n    \"component_or_context\": \"Glucose addition\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"1 M Glucose solution 20.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose\": 20,\n      \"unit\"\
    : \"ml\",\n      \"strength\": {\n        \"value\": 1,\n        \"unit\": \"\
    M\"\n      },\n      \"stage\": \"post-cooling; autoclaved\",\n      \"denominator\"\
    : \"printed recipe; final volume not measured\"\n    },\n    \"rationale\": \"\
    A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition\
    \ and addition stage; percent basis is not printed, so no w/v or molarity conversion\
    \ is justified.\"\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Glucose stock strength\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"1 M Glucose solution 20.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"strength\": {\n        \"\
    value\": 1,\n        \"unit\": \"M\"\n      },\n      \"stock_batch_volume\":\
    \ null,\n      \"stage\": \"post-cooling; autoclaved\"\n    },\n    \"rationale\"\
    : \"The strength exists only in the display name while composition is empty. Represent\
    \ it explicitly without inventing a stock batch volume, percentage basis or hydrate\
    \ replacement.\"\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Na2S nonahydrate addition\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"5% Na 2 S·9H 2 O solution 8.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose\": 8,\n      \"unit\"\
    : \"ml\",\n      \"strength\": {\n        \"value\": 5,\n        \"unit\": \"\
    percent\",\n        \"basis\": null\n      },\n      \"stage\": \"final addition\
    \ per liter\",\n      \"denominator\": \"per liter\"\n    },\n    \"rationale\"\
    : \"A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition\
    \ and addition stage; percent basis is not printed, so no w/v or molarity conversion\
    \ is justified.\"\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Na2S nonahydrate stock strength\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"5% Na 2 S·9H 2 O solution 8.0 ml\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"strength\": {\n        \"\
    value\": 5,\n        \"unit\": \"percent\",\n        \"basis\": null\n      },\n\
    \      \"stock_batch_volume\": null,\n      \"stage\": \"final addition per liter\"\
    \n    },\n    \"rationale\": \"The strength exists only in the display name while\
    \ composition is empty. Represent it explicitly without inventing a stock batch\
    \ volume, percentage basis or hydrate replacement.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q23\",\n    \"component_or_context\": \"L-cysteine HCl monohydrate addition\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"correct\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n        \"\
    field_path\": \"solutions[5].concentration\",\n        \"stored\": {\n       \
    \   \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"\
    decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm874\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\",\n  \
    \      \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"5% L-Cysteine·HCl·H 2 O solution 10.0 ml\",\n        \"snapshot_sha256\":\
    \ \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\",\n    \
    \    \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"dose\": 10,\n      \"unit\"\
    : \"ml\",\n      \"strength\": {\n        \"value\": 5,\n        \"unit\": \"\
    percent\",\n        \"basis\": null\n      },\n      \"stage\": \"final addition\
    \ per liter\",\n      \"denominator\": \"per liter\"\n    },\n    \"rationale\"\
    : \"A liquid stock dose is stored as G_PER_L. Preserve the source volume, composition\
    \ and addition stage; percent basis is not printed, so no w/v or molarity conversion\
    \ is justified.\"\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"L-cysteine HCl monohydrate stock strength\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Staged solution tables\",\n        \"exact_source_quote\"\
    : \"5% L-Cysteine·HCl·H 2 O solution 10.0 ml\",\n        \"snapshot_sha256\":\
    \ \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\",\n    \
    \    \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"strength\": {\n        \"\
    value\": 5,\n        \"unit\": \"percent\",\n        \"basis\": null\n      },\n\
    \      \"stock_batch_volume\": null,\n      \"stage\": \"final addition per liter\"\
    \n    },\n    \"rationale\": \"The strength exists only in the display name while\
    \ composition is empty. Represent it explicitly without inventing a stock batch\
    \ volume, percentage basis or hydrate replacement.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q25\",\n    \"component_or_context\": \"Trace stock HCl\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"HCl (25%) 12.5 ml\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 12.5,\n      \"\
    unit\": \"ml\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\"\
    : {\n        \"value\": 25,\n        \"unit\": \"percent\",\n        \"basis\"\
    : null\n      },\n      \"receiving_dose\": {\n        \"value\": 10,\n      \
    \  \"unit\": \"ml\",\n        \"source\": \"JCM874\"\n      }\n    },\n    \"\
    rationale\": \"The named stock is absent from BELH1 and its parent components\
    \ are flattened as G_PER_L. Retain original batch units; mg to g is arithmetic\
    \ only, not a receiving-medium rate. HCl plus listed water does not declare a\
    \ measured one-litre final stock.\"\n  },\n  {\n    \"quantity_id\": \"q26\",\n\
    \    \"component_or_context\": \"Trace stock Na2MoO4 dihydrate\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 36.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 36,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\": \"Trace\
    \ stock Boric acid\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n \
    \       \"field_path\": \"solutions[0].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"H 3 BO 3 30.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 30,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\": \"Trace\
    \ stock FeSO4 heptahydrate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"FeSO 4 ·7H 2 O 2.1 g\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 2.1,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\": \"Trace\
    \ stock MnCl2 tetrahydrate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"MnCl 2 ·4H 2 O 100.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 100,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\": \"Trace\
    \ stock CoCl2 hexahydrate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"CoCl 2 ·6H 2 O 190.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 190,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\": \"Trace\
    \ stock NiCl2 hexahydrate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"NiCl 2 ·6H 2 O 24.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 24,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\": \"Trace\
    \ stock ZnSO4 heptahydrate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"144\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 144.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 144,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\": \"Trace\
    \ stock CuCl2 dihydrate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"CuCl 2 ·2H 2 O 2.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 2,\n      \"unit\"\
    : \"mg\",\n      \"stage\": \"trace-stock batch\",\n      \"HCl_strength\": null,\n\
    \      \"receiving_dose\": {\n        \"value\": 10,\n        \"unit\": \"ml\"\
    ,\n        \"source\": \"JCM874\"\n      }\n    },\n    \"rationale\": \"The named\
    \ stock is absent from BELH1 and its parent components are flattened as G_PER_L.\
    \ Retain original batch units; mg to g is arithmetic only, not a receiving-medium\
    \ rate. HCl plus listed water does not declare a measured one-litre final stock.\"\
    \n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\": \"Trace\
    \ stock water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[0].composition\",\n        \"stored\": [],\n       \
    \ \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"988.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution subsection\",\n      \
    \  \"exact_source_quote\": \"Distilled water 987.0 ml\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 987,\n      \"unit\"\
    : \"ml\",\n      \"stage\": \"trace stock only\",\n      \"final_volume\": null\n\
    \    },\n    \"rationale\": \"The parent water 988 G_PER_L is a mixed basal/stock\
    \ quantity, explicitly excluded from transfer. Do not simply replace that entire\
    \ parent field with 987; separate the parent stages and add only the 987 ml stock\
    \ input to this dependency.\"\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"\
    component_or_context\": \"Trace HCl percentage\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].preferred_term\",\n        \"stored\"\
    : \"HCl (25%)\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"Trace element solution\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 12.5 ml\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:13:22.895121Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"value\": 25,\n      \"unit\"\
    : \"percent\",\n      \"basis\": null,\n      \"dose_ml\": 12.5\n    },\n    \"\
    rationale\": \"The percentage is explicit but its basis is not. Do not convert\
    \ to molarity or infer stock final volume.\"\n  },\n  {\n    \"quantity_id\":\
    \ \"q36\",\n    \"component_or_context\": \"Basal pH\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm874\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\",\n        \"source_locator\"\
    : \"Preparation/default exception scope\",\n        \"exact_source_quote\": \"\
    adjust pH to 7.5 with KOH\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pH\": 7.5,\n      \"stage\"\
    : \"before autoclaving\"\n    },\n    \"rationale\": \"Preserve the explicitly\
    \ named stage. The default cycle does not override filter sterilization, and a\
    \ per-liter dose is not proof of a measured assembled volume.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q37\",\n    \"component_or_context\": \"Autoclave temperature\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\",\n        \"rationale\"\
    : \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Preparation/default exception scope\",\n    \
    \    \"exact_source_quote\": \"autoclaving at 121°C for 15 min\",\n        \"\
    snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 121,\n  \
    \    \"stage\": \"default only where no exception\"\n    },\n    \"rationale\"\
    : \"Preserve the explicitly named stage. The default cycle does not override filter\
    \ sterilization, and a per-liter dose is not proof of a measured assembled volume.\"\
    \n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\": \"Autoclave\
    \ duration\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm874\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\",\n        \"source_locator\"\
    : \"Preparation/default exception scope\",\n        \"exact_source_quote\": \"\
    autoclaving at 121°C for 15 min\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"duration_min\": 15,\n    \
    \  \"stage\": \"default only where no exception\"\n    },\n    \"rationale\":\
    \ \"Preserve the explicitly named stage. The default cycle does not override filter\
    \ sterilization, and a per-liter dose is not proof of a measured assembled volume.\"\
    \n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\": \"Basal\
    \ gas ratio\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm874\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\",\n        \"source_locator\"\
    : \"Preparation/default exception scope\",\n        \"exact_source_quote\": \"\
    N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"N2\": 4,\n      \"CO2\": 1,\n\
    \      \"basis\": \"v/v\",\n      \"stage\": \"basal autoclaving\"\n    },\n \
    \   \"rationale\": \"Preserve the explicitly named stage. The default cycle does\
    \ not override filter sterilization, and a per-liter dose is not proof of a measured\
    \ assembled volume.\"\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Bicarbonate storage gas\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Preparation/default exception scope\",\n    \
    \    \"exact_source_quote\": \"*filter-sterilized and stored under N 2 -CO 2 ,\
    \ 4:1, v/v\",\n        \"snapshot_sha256\": \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\"\
    ,\n        \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"N2\": 4,\n      \"CO2\": 1,\n\
    \      \"basis\": \"v/v\",\n      \"stage\": \"filter-sterilized bicarbonate storage\"\
    \n    },\n    \"rationale\": \"Preserve the explicitly named stage. The default\
    \ cycle does not override filter sterilization, and a per-liter dose is not proof\
    \ of a measured assembled volume.\"\n  },\n  {\n    \"quantity_id\": \"q41\",\n\
    \    \"component_or_context\": \"Final addition denominator\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BELH1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm874\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=874\"\
    ,\n        \"source_locator\": \"Preparation/default exception scope\",\n    \
    \    \"exact_source_quote\": \"Finally, add per liter\",\n        \"snapshot_sha256\"\
    : \"538dbb901153c44ddc63dfc1d23cbdfab8c5778aa80ff36c7684df05eff6db73\",\n    \
    \    \"parsed_text_sha256\": \"651566cff586d4c7ba126b0faff90b08f6173927bfc73fc35534cf617d583ba0\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.692902Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"denominator_L\": 1,\n    \
    \  \"stage\": \"only final cysteine and sulfide additions\"\n    },\n    \"rationale\"\
    : \"Preserve the explicitly named stage. The default cycle does not override filter\
    \ sterilization, and a per-liter dose is not proof of a measured assembled volume.\"\
    \n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.010333.amount-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water, resazurin and stock doses have incorrect units
  description: The source gives 935 ml water and 1 mg resazurin, while both local
    layers store 935 and 1 G_PER_L. Six liquid stock additions are also stored as
    mass rates. These dimensional errors are separate from the unknown measured final
    volume.
  target_ids:
  - CultureMech:010333
  field_paths:
  - ingredients[0].concentration
  - ingredients[7].concentration
  - solutions
  evidence_ids:
  - primary
  - record
  - owner-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.010333.stock-composition
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The six named stocks have empty compositions
  description: All six solutions use Unknown solution placeholders and empty composition
    arrays. The available exact sources support the trace constituents and the other
    stated strengths, but not invented percent bases or batch volumes.
  target_ids:
  - CultureMech:010333
  field_paths:
  - solutions
  evidence_ids:
  - primary
  - trace-primary
  - trace-owner
  - record
  - owner-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    role: maintained trace-stock dependency only
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.010333.trace-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The named trace stock loses cobalt and nickel hydration
  description: M439 ingredients[17] and [18] name explicit hexahydrates but point
    to cobalt dichloride and nickel dichloride. The named stock transfer makes supplied-form
    specificity relevant even though the receiving solution is currently empty.
  target_ids:
  - CultureMech:010333
  field_paths:
  - solutions[0].composition
  evidence_ids:
  - trace-primary
  - trace-owner
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    role: maintained trace-stock dependency only
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.010333.preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The source preparation stages are missing
  description: Missing pH, atmosphere, cooling and separate sterilization/storage
    instructions prevent faithful interpretation of the six additions. This is a formulation-stage
    omission, not a request to invent a routine protocol.
  target_ids:
  - CultureMech:010333
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - primary
  - record
  - owner-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
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
  description: Correct maintained amounts to source units and stages, keeping original
    batch amounts and explicit final per-litre additions distinct; attach exact current
    evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010333
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
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
  description: Represent exact stock composition, dose and stage; resolve M439 only
    to the trace subsection and preserve its separate water input.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010333
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    role: maintained trace-stock dependency only
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
  description: Resolve exact hydrated terms from authoritative ontology evidence before
    reuse, preserving all other parent recipe scope. Do not invent replacement identifiers.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010333
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.yaml
    role: maintained trace-stock dependency only
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
  description: Add the exact source sequence and exceptions. Retain unqualified percentage
    bases and unknown measured final volume; do not apply the default autoclave cycle
    to bicarbonate.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010333
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M913_BELH1_Medium.yaml
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
- Optional current MediaDive J874 access returned HTTP 503. Complete JCM874 and exact
  TOGO source content are available; the failed response is not formula evidence.
- The M439 parent was read in full for exclusion and provenance context. Only ingredients[12]
  through [20], the source trace water and named receiving stock are quantitatively
  transferred; other parent ingredients, eight parent doses, gases, pH and high_metal
  flag are excluded from this single-record formulation assessment.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-041
- generated-medium
```
