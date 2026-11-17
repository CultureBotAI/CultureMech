# Source and formulation review: benzoate_medium (CultureMech:007662)

- Review: 20261021T231134Z-culturemech-007662-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:07:33Z
- Finished UTC: 2026-10-21T23:11:34Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 121 and TOGO M113 confirm the benzoate medium identity and seven nominal solute masses, but 1 L water is stored as 1 g/L and the separate benzoate filter-sterilization step is missing. Current CHEBI identities are supported; the retained legacy MIM000385 mapping cannot be historically authenticated, so review coverage is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 402; batch 041 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty task batches contain 400 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 403 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007662 | data/merge_yaml/merged/BENZOATE_MEDIUM.yaml | generated | benzoate_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007662 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007662 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch041/402/strict.tsv |
| validate-terms | passed | True | CultureMech:007662 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007662 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007662 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical legacy MIM000385 correspondence | unavailable | True | CultureMech:007662 | Current exact lookup completed negatively; the required original legacy mapping remains unavailable. |
| Exact source content access: mediadiveJ121api | unavailable | False | CultureMech:007662 | Optional current MediaDive J121 access returned HTTP 503. Exact JCM121 and TOGO M113 remain available for current formula review; the failure supplies no formulation content. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007662.

The four documented recipes completed; interpret the scope of each separately.

### Exact medium accession and ownership

identity: supported. Targets: CultureMech:007662.

The sole maintained owner is TOGO M113 with original JCM121 identity. The target preserves its formulation and original name; merge provenance and stable ID resolve the contributor without a namesake substitution.

### CHEBI forms and scoped MIM correspondence

grounding: concern. Targets: CultureMech:007662.

The target has six primary links among eight ingredients (75.00% on a 0–100 linkage scale); four current CHEBI-based secondary keys are mapped (50.00%). The fifth secondary assertion uses legacy MediaIngredientMech:000385 and is excluded from that verified current-key count. Exact current labels for all six primary CHEBI terms match, including CHEBI:63051 diammonium hydrogen phosphate. Current lookup absence does not establish that the legacy identity was historically wrong.

### Sterilization, physical state and source limits

completeness: concern. Targets: CultureMech:007662.

Noble agar 20 g and yeast extract support SOLID_AGAR and COMPLEX/UNDEFINED. The records omit the separately filter-sterilized benzoate solution and the applicable default autoclave cycle. Stock strength, volume and pore size are unspecified. No pH, incubation condition or organism growth can be inferred from the title.

### Required historical MIM mapping

provenance: unknown. Targets: CultureMech:007662.

The exact current negative lookup is complete, but the original MIM000385 correspondence was not available in the captured evidence. Preserve the historical link and its uncertainty; do not silently replace it with a guessed mapping or equate CHEBI name agreement with authentication of the old ID.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007662.

19 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007662.

14 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[0].concentration",
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
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1,
      "unit": "L",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "Water volume is incorrectly represented as a mass rate; retain 1 L without density conversion."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "MgSO4 heptahydrate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "MgSO 4 ·7H 2 O 0.2 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.2,
      "unit": "g",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "Yeast extract 0.5 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 0.5,
      "unit": "g",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "NaCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[3].concentration",
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
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "NaCl 5.0 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 5,
      "unit": "g",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "KH2PO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "KH 2 PO 4 1.2 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 1.2,
      "unit": "g",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Diammonium hydrogen phosphate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "(NH 4 ) 2 HPO 4 3.0 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 3,
      "unit": "g",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Noble agar BD-Difco",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "Agar, Noble (BD-Difco) 20.0 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 20,
      "unit": "g",
      "stage": "nominal main recipe",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Sodium benzoate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Main recipe table",
        "exact_source_quote": "Sodium benzoate 3.0 g",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "amount": 3,
      "unit": "g",
      "stage": "separately filter-sterilized benzoate addition",
      "water_input_L": 1,
      "measured_final_volume": null
    },
    "rationale": "The stored nominal g/L numeral agrees with the batch mass at the printed one-litre water basis. The source does not give a separately measured final volume or benzoate-solution volume, so preserve the nominal basis and exact preparation stage."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Separate benzoate solution volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Preparation",
        "exact_source_quote": "Separately sterilize a solution of sodium benzoate by filtration, and aseptically add it to the medium.",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "stock_volume": null
    },
    "rationale": "The source requires filtration and aseptic addition but does not quantify this parameter; do not introduce a customary value."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Separate benzoate solution strength",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Preparation",
        "exact_source_quote": "Separately sterilize a solution of sodium benzoate by filtration, and aseptically add it to the medium.",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "stock_strength": null
    },
    "rationale": "The source requires filtration and aseptic addition but does not quantify this parameter; do not introduce a customary value."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Filter pore size",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Preparation",
        "exact_source_quote": "Separately sterilize a solution of sodium benzoate by filtration, and aseptically add it to the medium.",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "pore_size": null
    },
    "rationale": "The source requires filtration and aseptic addition but does not quantify this parameter; do not introduce a customary value."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Default autoclave temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "JCM page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 121,
      "scope": "basal preparation; sodium benzoate explicitly excepted"
    },
    "rationale": "Apply only the printed default where no exception is stated. Sodium benzoate must retain its separate filter sterilization."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Default autoclave duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "JCM page default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "duration_min": 15,
      "scope": "basal preparation; sodium benzoate explicitly excepted"
    },
    "rationale": "Apply only the printed default where no exception is stated. Sodium benzoate must retain its separate filter sterilization."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "pH, cultivation temperature and atmosphere",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/merge_yaml/merged/BENZOATE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "temperature_value",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "rationale": ""
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm121",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121",
        "source_locator": "Entire available page",
        "exact_source_quote": "Medium data Medium data Search for medium no. = [121]. Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min. 121   BENZOATE MEDIUM (NH 4 ) 2 HPO 4 3.0 g KH 2 PO 4 1.2 g NaCl 5.0 g MgSO 4 ·7H 2 O 0.2 g Yeast extract 0.5 g Sodium benzoate 3.0 g Agar, Noble (BD-Difco) 20.0 g Distilled water 1.0 L Separately sterilize a solution of sodium benzoate by filtration, and aseptically add it to the medium. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved",
        "snapshot_sha256": "996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93",
        "parsed_text_sha256": "1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d",
        "accessed_at": "2026-10-21T22:43:54.506391Z"
      }
    ],
    "proposed_source_representation": {
      "pH": null,
      "cultivation_temperature": null,
      "atmosphere": null
    },
    "rationale": "The exact source gives no values for these conditions. The 121 °C sterilization temperature is not a cultivation temperature."
  }
]

## Findings

### f1: One litre of water is stored as one gram per litre

major / open / confirmed; issue key: culturemech.007662.water-units.

The primary and exact provider specify water 1 L, while both local layers encode 1 G_PER_L. This dimensional mismatch is independent of the unmeasured final volume after the separate benzoate addition.

### f2: The separate benzoate sterilization stage is missing

major / open / confirmed; issue key: culturemech.007662.benzoate-preparation.

The source explicitly requires filtration and aseptic addition of a separate sodium-benzoate solution. The records have no preparation steps and therefore omit this exception as well as the applicable page default.

### f3: The retained legacy secondary link has unresolved historical correspondence

minor / open / confirmed; issue key: culturemech.007662.legacy-correspondence.

Current pinned MIM lookup has no MIM000385 match, while the record still asserts it. The exact source and CHEBI63051 establish the ingredient name, not the historical secondary mapping.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained water field to its literal volume and stage, retain the nominal basis of solute amounts, and attach exact source evidence before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the exact basal and benzoate preparation stages. Leave stock volume, strength and pore size unquantified; do not apply autoclaving indiscriminately to benzoate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Recover the original legacy mapping or explicitly preserve its unresolved status; only propose a replacement after exact correspondence is established.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BENZOATE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BENZOATE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BENZOATE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch041/402/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch041/402/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BENZOATE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BENZOATE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BENZOATE_MEDIUM.yaml:1:id: CultureMech:007662<br>./data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml:1:id: CultureMech:007662<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch041/source-preflight-bound/402/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 12 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121; Complete main table and preparation | supports | Exact source formulation and its benzoate exception; no source pH or organism growth assertion. |
| benzoate-prep | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121; Final preparation sentence | supports | Benzoate is filter-sterilized as a separate solution; volume, strength and filter pore size are not stated. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M113; Complete components and comments | supports | Exact M113 provider identifies the original JCM121 source and retains the literal water volume and preparation. The page-only response is a JavaScript shell. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch041/402/grounding-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| history-inventory | /private/tmp/culturemech-review-work-batch041/402/history-inventory.json; Exact local term/history slots and bound source authentication ledger | context_only | Complete exact-field inventory; current metadata, historical evidence and source forms remain distinct. |
| chebi113455 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_113455; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| chebi63051 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63051; Exact OLS identifier, canonical label, obsolete flag, definition and formula | supports | Inspected metadata for every occurrence; source-specific form conclusions remain in the assessment. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact pinned current CHEBI preferred-key rows; metadata source commit/hash | context_only | {"CHEBI:113455": [{"label": "Na-benzoate", "match_type": "preferred_term", "identifier": "CHEBI:113455", "preferred_term": "Na-benzoate", "ontology_id": "CHEBI:113455", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| legacy-current-lookup | /private/tmp/culturemech-review-work-batch041/source-preflight-bound/402/evidence-context-original.json; legacy_mim_lookup and exact pinned current MIM catalog/tree/index | context_only | Exact MediaIngredientMech:000385 has no matching object, identifier text occurrence, tree filename or local index row in the captured current snapshot. This completed negative lookup does not establish historical invalidity. |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Exact current pinned snapshot; legacy identity search only | supports | Current snapshot content is used only for exact identifier correspondence, not historical equivalence or medium formulation. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Exact current pinned snapshot; legacy identity search only | supports | Current snapshot content is used only for exact identifier correspondence, not historical equivalence or medium formulation. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, migration and guarded merge logic are inspected implementation context. Both target and maintained owner retain the water-unit defect and legacy key; the history is not a replay proving which current function caused them. |
| writer-1 | scripts/migrate_legacy_mim_to_chebi.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, migration and guarded merge logic are inspected implementation context. Both target and maintained owner retain the water-unit defect and legacy key; the history is not a replay proving which current function caused them. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, migration and guarded merge logic are inspected implementation context. Both target and maintained owner retain the water-unit defect and legacy key; the history is not a replay proving which current function caused them. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, migration and guarded merge logic are inspected implementation context. Both target and maintained owner retain the water-unit defect and legacy key; the history is not a replay proving which current function caused them. |
| history-metadata | data/merge_yaml/merged/BENZOATE_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml", "events": 9, "timestamp_issues": []}] |
| mediadiveJ121api-attempt | https://mediadive.dsmz.de/rest/medium/J121; Preserved exact public retrieval result | context_only | Optional current MediaDive J121 access returned HTTP 503. Exact JCM121 and TOGO M113 remain available for current formula review; the failure supplies no formulation content. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch041/402/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Partial coverage is caused by unresolved historical MIM000385 correspondence, not by optional MediaDive failure. No original historical legacy mapping was fabricated from current CHEBI metadata.
- Optional current MediaDive J121 access returned HTTP 503. Exact JCM121 and TOGO M113 remain available for current formula review; the failure supplies no formulation content.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T231134Z-culturemech-007662-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: benzoate_medium (CultureMech:007662)'
started_at: '2026-10-21T23:07:33Z'
finished_at: '2026-10-21T23:11:34Z'
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
summary: JCM 121 and TOGO M113 confirm the benzoate medium identity and seven nominal
  solute masses, but 1 L water is stored as 1 g/L and the separate benzoate filter-sterilization
  step is missing. Current CHEBI identities are supported; the retained legacy MIM000385
  mapping cannot be historically authenticated, so review coverage is partial.
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
  - path: data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
    sha256: 97706875019f80380a3895a2b04532b3564020a7fa11a01ce2af8a813dacfe7a
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
    sha256: 5eec3fa8d253eb09cfd2891fbc58db08628d11db16e3f2efb80767bc741ac2c9
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BENZOATE_MEDIUM.md
    sha256: fc34166c62f4e6925c6d147185a3fab4e0c93621ac1a0757ff91eddc560cbf8a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.md
    sha256: 5bec80140ff2bc41b5319601c348a4e8fd15ae1757868c41b7d7399e72784e79
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
  selection: Task review 402; batch 041 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty task batches contain
    400 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 403 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007662
targets:
- target_id: CultureMech:007662
  path: data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  label: benzoate_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BENZOATE_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch041/402/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch041/402/strict.tsv"
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007662
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
  - CultureMech:007662
- check_id: historical-mim000385
  name: Historical legacy MIM000385 correspondence
  required: true
  status: unavailable
  summary: Current exact lookup completed negatively; the required original legacy
    mapping remains unavailable.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - legacy-current-lookup
  - history-inventory
- check_id: mediadiveJ121api-source-access
  name: 'Exact source content access: mediadiveJ121api'
  required: false
  status: unavailable
  summary: Optional current MediaDive J121 access returned HTTP 503. Exact JCM121
    and TOGO M113 remain available for current formula review; the failure supplies
    no formulation content.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - mediadiveJ121api-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:45.835898Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BENZOATE_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch041/402/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:46.803334Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-041/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch041/402/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:47.869021Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BENZOATE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:07:48.553454Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:11:33Z'
  support: supports
  summary: './data/merge_yaml/merged/BENZOATE_MEDIUM.yaml:1:id: CultureMech:007662

    ./data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml:1:id: CultureMech:007662

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/source-preflight-bound/402/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:11:33Z'
  support: supports
  summary: 12 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 42253733351bb1c3704138f6c9d40c5e68d45a322a7a1ea204bb977122416562
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121
  locator: Complete main table and preparation
  accessed_at: '2026-10-21T22:43:54.506391Z'
  support: supports
  summary: Exact source formulation and its benzoate exception; no source pH or organism
    growth assertion.
  quote: Distilled water 1.0 L
  snapshot_sha256: 996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93
- evidence_id: benzoate-prep
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121
  locator: Final preparation sentence
  accessed_at: '2026-10-21T22:43:54.506391Z'
  support: supports
  summary: Benzoate is filter-sterilized as a separate solution; volume, strength
    and filter pore size are not stated.
  quote: Separately sterilize a solution of sodium benzoate by filtration, and aseptically
    add it to the medium.
  snapshot_sha256: 996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M113
  locator: Complete components and comments
  accessed_at: '2026-10-21T22:43:53.799875Z'
  support: supports
  summary: Exact M113 provider identifies the original JCM121 source and retains the
    literal water volume and preparation. The page-only response is a JavaScript shell.
  snapshot_sha256: 4e2f876e7dc9722ce0e4f37a814d818a57b6370450b383b11a53041d8cf111a8
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/402/grounding-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 23498b1d6c9ea71df6f12ea55a317113dfe88b3e7fc59c420c6841f41d9126cc
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/402/history-inventory.json
  locator: Exact local term/history slots and bound source authentication ledger
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Complete exact-field inventory; current metadata, historical evidence and
    source forms remain distinct.
  snapshot_sha256: 6bba1725b13c4e55b273975ba8f8fe1680dfa219c7386b8b85c93da1d0575a30
- evidence_id: chebi113455
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_113455
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T11:55:11.910151Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: ae57ed1c4e8ffdd7909332b3bbe6dcc356a0f03ae779de5a761626ccb6cebfba
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63051
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63051
  locator: Exact OLS identifier, canonical label, obsolete flag, definition and formula
  accessed_at: '2026-10-21T17:04:23.306517Z'
  support: supports
  summary: Inspected metadata for every occurrence; source-specific form conclusions
    remain in the assessment.
  snapshot_sha256: d463939ff68b0686dd62097e1ed8578ca61de590f460afb0ecddef1c74a95afa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact pinned current CHEBI preferred-key rows; metadata source commit/hash
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: '{"CHEBI:113455": [{"label": "Na-benzoate", "match_type": "preferred_term",
    "identifier": "CHEBI:113455", "preferred_term": "Na-benzoate", "ontology_id":
    "CHEBI:113455", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: legacy-current-lookup
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/source-preflight-bound/402/evidence-context-original.json
  locator: legacy_mim_lookup and exact pinned current MIM catalog/tree/index
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Exact MediaIngredientMech:000385 has no matching object, identifier text
    occurrence, tree filename or local index row in the captured current snapshot.
    This completed negative lookup does not establish historical invalidity.
  snapshot_sha256: e15684b38665d9c5e10180e801e02a6d7a2a535b1285704d0a7889bd36379f7b
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Exact current pinned snapshot; legacy identity search only
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Current snapshot content is used only for exact identifier correspondence,
    not historical equivalence or medium formulation.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Exact current pinned snapshot; legacy identity search only
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Current snapshot content is used only for exact identifier correspondence,
    not historical equivalence or medium formulation.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Current importer, migration and guarded merge logic are inspected implementation
    context. Both target and maintained owner retain the water-unit defect and legacy
    key; the history is not a replay proving which current function caused them.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Current importer, migration and guarded merge logic are inspected implementation
    context. Both target and maintained owner retain the water-unit defect and legacy
    key; the history is not a replay proving which current function caused them.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Current importer, migration and guarded merge logic are inspected implementation
    context. Both target and maintained owner retain the water-unit defect and legacy
    key; the history is not a replay proving which current function caused them.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Current importer, migration and guarded merge logic are inspected implementation
    context. Both target and maintained owner retain the water-unit defect and legacy
    key; the history is not a replay proving which current function caused them.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BENZOATE_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml", "events": 9,
    "timestamp_issues": []}]'
- evidence_id: mediadiveJ121api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J121
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:43:53.269843Z'
  support: context_only
  summary: Optional current MediaDive J121 access returned HTTP 503. Exact JCM121
    and TOGO M113 remain available for current formula review; the failure supplies
    no formulation content.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch041/402/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:11:33Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7eeeb19dc9f22ba55f948039da80a4fcdfc9e492011af956f85ddbf5eddbf33b
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact medium accession and ownership
  outcome: supported
  summary: The sole maintained owner is TOGO M113 with original JCM121 identity. The
    target preserves its formulation and original name; merge provenance and stable
    ID resolve the contributor without a namesake substitution.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - provider
- assessment_id: grounding
  area: grounding
  topic: CHEBI forms and scoped MIM correspondence
  outcome: concern
  summary: The target has six primary links among eight ingredients (75.00% on a 0–100
    linkage scale); four current CHEBI-based secondary keys are mapped (50.00%). The
    fifth secondary assertion uses legacy MediaIngredientMech:000385 and is excluded
    from that verified current-key count. Exact current labels for all six primary
    CHEBI terms match, including CHEBI:63051 diammonium hydrogen phosphate. Current
    lookup absence does not establish that the legacy identity was historically wrong.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - grounding-inventory
  - mim
  - legacy-current-lookup
  - mimPinnedCatalog
  - mimPinnedTree
  - primary
- assessment_id: preparation
  area: completeness
  topic: Sterilization, physical state and source limits
  outcome: concern
  summary: Noble agar 20 g and yeast extract support SOLID_AGAR and COMPLEX/UNDEFINED.
    The records omit the separately filter-sterilized benzoate solution and the applicable
    default autoclave cycle. Stock strength, volume and pore size are unspecified.
    No pH, incubation condition or organism growth can be inferred from the title.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - primary
  - benzoate-prep
  - record
  - owner-0
  - quantity-inventory
- assessment_id: historical-legacy
  area: provenance
  topic: Required historical MIM mapping
  outcome: unknown
  summary: The exact current negative lookup is complete, but the original MIM000385
    correspondence was not available in the captured evidence. Preserve the historical
    link and its uncertainty; do not silently replace it with a guessed mapping or
    equate CHEBI name agreement with authentication of the old ID.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - legacy-current-lookup
  - history-inventory
  - grounding-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 19 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 14 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007662
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1,\n      \"unit\"\
    : \"L\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"Water\
    \ volume is incorrectly represented as a mass rate; retain 1 L without density\
    \ conversion.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"MgSO4 heptahydrate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"MgSO 4 ·7H 2 O 0.2 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.2,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"The\
    \ stored nominal g/L numeral agrees with the batch mass at the printed one-litre\
    \ water basis. The source does not give a separately measured final volume or\
    \ benzoate-solution volume, so preserve the nominal basis and exact preparation\
    \ stage.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 0.5 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 0.5,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"The\
    \ stored nominal g/L numeral agrees with the batch mass at the printed one-litre\
    \ water basis. The source does not give a separately measured final volume or\
    \ benzoate-solution volume, so preserve the nominal basis and exact preparation\
    \ stage.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"NaCl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"NaCl 5.0 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 5,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"The\
    \ stored nominal g/L numeral agrees with the batch mass at the printed one-litre\
    \ water basis. The source does not give a separately measured final volume or\
    \ benzoate-solution volume, so preserve the nominal basis and exact preparation\
    \ stage.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"KH2PO4\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"KH 2 PO 4 1.2 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 1.2,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"The\
    \ stored nominal g/L numeral agrees with the batch mass at the printed one-litre\
    \ water basis. The source does not give a separately measured final volume or\
    \ benzoate-solution volume, so preserve the nominal basis and exact preparation\
    \ stage.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Diammonium hydrogen phosphate\",\n    \"decision\": \"evidence_only\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"(NH 4 ) 2 HPO 4 3.0 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 3,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"The\
    \ stored nominal g/L numeral agrees with the batch mass at the printed one-litre\
    \ water basis. The source does not give a separately measured final volume or\
    \ benzoate-solution volume, so preserve the nominal basis and exact preparation\
    \ stage.\"\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Noble agar BD-Difco\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"Agar, Noble (BD-Difco) 20.0 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 20,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"nominal main recipe\",\n      \"water_input_L\":\
    \ 1,\n      \"measured_final_volume\": null\n    },\n    \"rationale\": \"The\
    \ stored nominal g/L numeral agrees with the batch mass at the printed one-litre\
    \ water basis. The source does not give a separately measured final volume or\
    \ benzoate-solution volume, so preserve the nominal basis and exact preparation\
    \ stage.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Sodium benzoate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"\"\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Main recipe table\",\n        \"exact_source_quote\"\
    : \"Sodium benzoate 3.0 g\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"amount\": 3,\n      \"unit\"\
    : \"g\",\n      \"stage\": \"separately filter-sterilized benzoate addition\"\
    ,\n      \"water_input_L\": 1,\n      \"measured_final_volume\": null\n    },\n\
    \    \"rationale\": \"The stored nominal g/L numeral agrees with the batch mass\
    \ at the printed one-litre water basis. The source does not give a separately\
    \ measured final volume or benzoate-solution volume, so preserve the nominal basis\
    \ and exact preparation stage.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n  \
    \  \"component_or_context\": \"Separate benzoate solution volume\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"not_quantified\",\n    \
    \    \"rationale\": \"\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm121\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Preparation\",\n        \"exact_source_quote\"\
    : \"Separately sterilize a solution of sodium benzoate by filtration, and aseptically\
    \ add it to the medium.\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_volume\": null\n   \
    \ },\n    \"rationale\": \"The source requires filtration and aseptic addition\
    \ but does not quantify this parameter; do not introduce a customary value.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\": \"Separate\
    \ benzoate solution strength\",\n    \"decision\": \"not_quantified\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm121\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Preparation\",\n        \"exact_source_quote\"\
    : \"Separately sterilize a solution of sodium benzoate by filtration, and aseptically\
    \ add it to the medium.\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_strength\": null\n \
    \   },\n    \"rationale\": \"The source requires filtration and aseptic addition\
    \ but does not quantify this parameter; do not introduce a customary value.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\": \"Filter\
    \ pore size\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n \
    \       \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm121\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Preparation\",\n        \"exact_source_quote\"\
    : \"Separately sterilize a solution of sodium benzoate by filtration, and aseptically\
    \ add it to the medium.\",\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pore_size\": null\n    },\n\
    \    \"rationale\": \"The source requires filtration and aseptic addition but\
    \ does not quantify this parameter; do not introduce a customary value.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\": \"Default autoclave\
    \ temperature\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"JCM page default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 121,\n  \
    \    \"scope\": \"basal preparation; sodium benzoate explicitly excepted\"\n \
    \   },\n    \"rationale\": \"Apply only the printed default where no exception\
    \ is stated. Sodium benzoate must retain its separate filter sterilization.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\": \"Default\
    \ autoclave duration\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n \
    \       \"decision\": \"add\",\n        \"rationale\": \"\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm121\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"JCM page default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"duration_min\": 15,\n    \
    \  \"scope\": \"basal preparation; sodium benzoate explicitly excepted\"\n   \
    \ },\n    \"rationale\": \"Apply only the printed default where no exception is\
    \ stated. Sodium benzoate must retain its separate filter sterilization.\"\n \
    \ },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\": \"pH,\
    \ cultivation temperature and atmosphere\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"not_quantified\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"temperature_value\",\n        \"stored\": null,\n    \
    \    \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BENZOATE_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n \
    \       \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"not_quantified\",\n        \"rationale\": \"\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"not_quantified\",\n        \"rationale\": \"\"\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm121\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=121\"\
    ,\n        \"source_locator\": \"Entire available page\",\n        \"exact_source_quote\"\
    : \"Medium data Medium data Search for medium no. = [121]. Unless otherwise stated,\
    \ sterilize media by autoclaving at 121°C for 15 min. 121   BENZOATE MEDIUM (NH\
    \ 4 ) 2 HPO 4 3.0 g KH 2 PO 4 1.2 g NaCl 5.0 g MgSO 4 ·7H 2 O 0.2 g Yeast extract\
    \ 0.5 g Sodium benzoate 3.0 g Agar, Noble (BD-Difco) 20.0 g Distilled water 1.0\
    \ L Separately sterilize a solution of sodium benzoate by filtration, and aseptically\
    \ add it to the medium. Copyright © 2026 Microbe Division (JCM) - All Rights Reserved\"\
    ,\n        \"snapshot_sha256\": \"996e6afe7de84640af426696cfa42ebf6c0dce940f129c1e2906923d33cedc93\"\
    ,\n        \"parsed_text_sha256\": \"1b1b234f3ec49f1a881b4e462bc637f006e606a7a5b5152a265a9744b19ee90d\"\
    ,\n        \"accessed_at\": \"2026-10-21T22:43:54.506391Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pH\": null,\n      \"cultivation_temperature\"\
    : null,\n      \"atmosphere\": null\n    },\n    \"rationale\": \"The exact source\
    \ gives no values for these conditions. The 121 °C sterilization temperature is\
    \ not a cultivation temperature.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: culturemech.007662.water-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: One litre of water is stored as one gram per litre
  description: The primary and exact provider specify water 1 L, while both local
    layers encode 1 G_PER_L. This dimensional mismatch is independent of the unmeasured
    final volume after the separate benzoate addition.
  target_ids:
  - CultureMech:007662
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
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
  issue_key: culturemech.007662.benzoate-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The separate benzoate sterilization stage is missing
  description: The source explicitly requires filtration and aseptic addition of a
    separate sodium-benzoate solution. The records have no preparation steps and therefore
    omit this exception as well as the applicable page default.
  target_ids:
  - CultureMech:007662
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary
  - benzoate-prep
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
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
  issue_key: culturemech.007662.legacy-correspondence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The retained legacy secondary link has unresolved historical correspondence
  description: Current pinned MIM lookup has no MIM000385 match, while the record
    still asserts it. The exact source and CHEBI63051 establish the ingredient name,
    not the historical secondary mapping.
  target_ids:
  - CultureMech:007662
  field_paths:
  - ingredients[5].mediaingredientmech_term
  evidence_ids:
  - record
  - owner-0
  - legacy-current-lookup
  - grounding-inventory
  - history-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
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
  description: Correct the maintained water field to its literal volume and stage,
    retain the nominal basis of solute amounts, and attach exact source evidence before
    regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007662
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
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
  description: Add the exact basal and benzoate preparation stages. Leave stock volume,
    strength and pore size unquantified; do not apply autoclaving indiscriminately
    to benzoate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007662
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
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
  description: Recover the original legacy mapping or explicitly preserve its unresolved
    status; only propose a replacement after exact correspondence is established.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007662
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M113_Benzoate_Medium.yaml
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
- Partial coverage is caused by unresolved historical MIM000385 correspondence, not
  by optional MediaDive failure. No original historical legacy mapping was fabricated
  from current CHEBI metadata.
- Optional current MediaDive J121 access returned HTTP 503. Exact JCM121 and TOGO
  M113 remain available for current formula review; the failure supplies no formulation
  content.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-041
- generated-medium
```
