# Source and formulation review: actinotalea_fermentas_medium (CultureMech:008423)

- Review: 20261021T191827Z-culturemech-008423-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:13:53Z
- Finished UTC: 2026-10-21T19:18:27Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC 1084 and TOGO M1849 agree on a batch formulation with 1 L water, 1 mg resazurin and 1.25 mg iron sulfate heptahydrate. Both local layers incorrectly express these as g/L and omit source preparation and the aerobic alternative. Unqualified cysteine-HCl does not establish its asserted L-specific form; historical MediaIngredientMech:000389 correspondence remains unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 342; batch 035 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-four task batches contain 340 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 343 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008423 | data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml | generated | actinotalea_fermentas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008423 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008423 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/342/strict.tsv |
| validate-terms | passed | True | CultureMech:008423 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008423 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008423 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required source-scope verification | unavailable | True | CultureMech:008423 | Required historical correspondence of the retained MediaIngredientMech:000389 cysteine-HCl assertion is not established by the available current catalog/tree. The current exact-key absence check completed; the historical check remains unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008423.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008423.

22 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Main: Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1,
      "source_unit": "L",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The source volume or milligram batch amount is not the local gram-per-liter rate. Preserve exact source unit, hydrate and batch stage; do not invent a measured final volume."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Main: Yeast extract",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 5,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Main: CaCl2·2H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.02,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main: KH2PO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1.5,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main: K2HPO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.21",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.21",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 2.21,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 2.21,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Main: Resazurin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1,
      "source_unit": "mg",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The source volume or milligram batch amount is not the local gram-per-liter rate. Preserve exact source unit, hydrate and batch stage; do not invent a measured final volume."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Main: MgCl2·6H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"MgCl2·6H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.1,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Main: FeSO4·7H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"FeSO4·7H2O\",\n          \"volume\": 1.25,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1.25,
      "source_unit": "mg",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The source volume or milligram batch amount is not the local gram-per-liter rate. Preserve exact source unit, hydrate and batch stage; do not invent a measured final volume."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Main: NaHCO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 0.8,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.8,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Main: (NH4)2SO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.3",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"(NH4)2SO4\",\n          \"volume\": 1.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1.3,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Main: Cellobiose or Cellulose (MN 300)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Cellobiose or Cellulose (MN 300)\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 5,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion. Cellobiose OR cellulose (MN 300) is an alternative at the stated single 5 g input; do not add both."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Main: Cysteine-HCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Cysteine-HCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.5,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "The printed mass agrees numerically but a 1 L water input does not independently establish measured final volume after dissolved solids and separate additions. Preserve the source batch amount with evidence, rather than an unsupported exact final g/L assertion."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Main: NaOH",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": null,
      "source_unit": null,
      "reagent_strength": 8,
      "reagent_unit": "M",
      "final_volume_L": null
    },
    "rationale": "Source gives no fixed receiving dose for this reagent/gas. VARIABLE does not establish the separate 8 M reagent strength or the 100% nitrogen atmosphere; capture those at preparation scope."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Main: N2",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM1849original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"N2\"",
        "snapshot_sha256": "ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef",
        "accessed_at": "2026-10-21T18:58:50.666418Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": null,
      "source_unit": null,
      "reagent_strength": null,
      "reagent_unit": null,
      "final_volume_L": null
    },
    "rationale": "Source gives no fixed receiving dose for this reagent/gas. VARIABLE does not establish the separate 8 M reagent strength or the 100% nitrogen atmosphere; capture those at preparation scope."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Receiving pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Main preparation after Composition",
        "exact_source_quote": "Adjust pH to 7.4",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "pH": 7.4
    },
    "rationale": "This preparation condition is absent from both local layers. Preserve its source stage without asserting an incubation optimum or deriving an unspecified dose."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Adjustment-reagent strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Main preparation after Composition",
        "exact_source_quote": "8 M NaOH",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "reagent_strength_M": 8,
      "dose": "not quantified"
    },
    "rationale": "This preparation condition is absent from both local layers. Preserve its source stage without asserting an incubation optimum or deriving an unspecified dose."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Anaerobic atmosphere",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Main preparation after Composition",
        "exact_source_quote": "100% nitrogen",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "nitrogen_percent": 100,
      "scope": "stated gas atmosphere; no absolute gas volume"
    },
    "rationale": "This preparation condition is absent from both local layers. Preserve its source stage without asserting an incubation optimum or deriving an unspecified dose."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Aerobic alternative: Resazurin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Explicit aerobic alternative sentence",
        "exact_source_quote": "omit resazurin and cysteine-HCl",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "alternative": "aerobic",
      "omitted_component": "Resazurin",
      "do_not_replace_base_amount": true
    },
    "rationale": "The omission applies only to the explicitly stated alternative, not to the base anaerobic formulation. Preserve the branch without fabricating a zero concentration or a species growth assertion."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Aerobic alternative: Cysteine hydrochloride",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Explicit aerobic alternative sentence",
        "exact_source_quote": "omit resazurin and cysteine-HCl",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "alternative": "aerobic",
      "omitted_component": "Cysteine hydrochloride",
      "do_not_replace_base_amount": true
    },
    "rationale": "The omission applies only to the explicitly stated alternative, not to the base anaerobic formulation. Preserve the branch without fabricating a zero concentration or a species growth assertion."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Carbon-source alternative",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[10].preferred_term",
        "stored": "Cellobiose or Cellulose (MN 300)",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[10].preferred_term",
        "stored": "Cellobiose or Cellulose (MN 300)",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Composition carbon-source row",
        "exact_source_quote": "Cellobiose or Cellulose (MN 300) 5 g",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "alternatives": [
        "Cellobiose",
        "Cellulose (MN 300)"
      ],
      "single_batch_amount_g": 5
    },
    "rationale": "The exact OR wording is already retained. Attach evidence and preserve mutually alternative identities; no pure-compound identity is invented for the combined field."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Final-volume basis",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Composition water input",
        "exact_source_quote": "Distilled water 1 L",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "water_input_L": 1,
      "measured_final_volume_L": null
    },
    "rationale": "The source gives a water input, not a final-volume make-up statement. No new concentration denominator is inferred."
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1084",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084",
        "source_locator": "Main preparation: named separate components",
        "exact_source_quote": "sterilized separately by autoclaving under N 2",
        "snapshot_sha256": "5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df",
        "parsed_text_sha256": "4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce",
        "accessed_at": "2026-10-21T18:58:51.598748Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": null,
      "duration_min": null,
      "named_separate_components": [
        "Cellobiose",
        "NaHCO3",
        "cysteine-HCl"
      ]
    },
    "rationale": "Add the stated separate sterilization and atmosphere, but keep cycle numbers unspecified. Do not import a JCM default into this NBRC source or assume that the cellulose alternative has a separately stated process."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:008423.

12 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 12/14 primary and 9/14 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding. The legacy cysteine key remains historically unresolved separately; current CHEBI-based rows do not authenticate it.

Instance coverage on a 0–100 percent scale, denominator 14: primary 85.71%; secondary 64.29%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008423.

19 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact record and accession identity

identity: supported. Targets: CultureMech:008423.

CultureMech:008423, its exact single bacterial maintained owner, TOGO M1849 and NBRC 1084 agree on this recipe identity. The source spells the medium name as retained locally. No asserted taxonomy identifier or strain-level growth statement is supplied, so the title is not treated as a taxonomy correction or growth experiment.

### Supplied forms versus ontology specificity

grounding: concern. Targets: CultureMech:008423.

Explicit calcium/magnesium/iron hydrates agree with their asserted forms. CHEBI:91247 has L stereochemistry in its definition/InChI/SMILES, while the source says Cysteine-HCl without stereochemistry. This is unresolved supplied-form specificity, not evidence of D or racemic material. K2HPO4 source is not explicitly a hydrate; the matching term formula is retained without adopting a trihydrate synonym. Yeast extract and the carbon-source OR field receive no invented pure-molecule ID.

### Source conditions and aerobic branch

completeness: concern. Targets: CultureMech:008423.

Both local layers omit the 7.4 pH adjustment with 8 M NaOH, explicitly 100% nitrogen atmosphere, separate autoclaving of cellobiose/bicarbonate/cysteine-HCl and the aerobic alternative omitting resazurin/cysteine-HCl. NBRC provides no cycle numbers. Preserve the source branch and carbon-source OR relation without deleting the base ingredients or asserting target-organism growth.

### Composition and application limits

scope: supported. Targets: CultureMech:008423.

COMPLEX/UNDEFINED is compatible with the yeast-extract component, and LIQUID with this base formulation. The generic microbial-cultivation application does not establish species-specific growth, an optimum or an aerobic/anaerobic phenotype. Source alternate preparation is formulation context only.

### Evidence and maintained-input ownership

provenance: concern. Targets: CultureMech:008423.

Neither target nor owner attaches claim-level amount evidence, despite recoverable exact primary/provider support. Source URLs and import/enrichment history establish provenance but do not prove amounts, gas scope or chemical specificity. Append later authorized clarification, preserve stable ID and regenerate only from the maintained owner after correction.

## Findings

### f1: Water and two milligram inputs have gram-rate units

blocker / open / confirmed; issue key: culturemech.008423.water-indicator-iron-units.

Both layers encode 1 L water as 1 G_PER_L, 1 mg resazurin as 1 G_PER_L and 1.25 mg FeSO4·7H2O as 1.25 G_PER_L. Other masses have an unestablished final-volume denominator.

### f2: Preparation and the explicit aerobic alternative are missing

major / open / confirmed; issue key: culturemech.008423.preparation-and-alternative.

Both layers omit source pH/reagent strength, 100% nitrogen preparation, separate sterilization and aerobic omissions.

### f3: Cysteine stereochemistry and historical linkage need qualification

minor / open / confirmed; issue key: culturemech.008423.cysteine-specificity-and-history.

The source unqualified Cysteine-HCl does not establish the current L-specific term; the retained legacy000389 mapping is absent from the complete current snapshot but its historical correspondence is unresolved.

## Recommended Actions And Acceptance Checks

### a1

Restore exact water/milligram batch units, preserve other source masses with their actual basis and attach claim-level evidence. Keep cellobiose OR cellulose and the explicit hydrate; do not infer final rates from an unmeasured final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add exact source-scoped preparation and the conditional aerobic omission branch with evidence. Retain unprovided cycle numbers as unknown and avoid a growth/phenotype assertion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Seek source/supplier form and historical legacy mapping evidence; document unresolved specificity without inventing a D/racemic replacement or declaring historical identity invalid from a current absence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch035/342/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/342/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml:1:id: CultureMech:008423<br>./data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml:1:id: CultureMech:008423<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/342/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 17 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/342/evidence-context-original.json; Complete frozen source context and full local objects | context_only | Frozen target/owner objects match freshly inspected records. Source interpretations are assessed against actual bound capture bytes; historical limitations remain separate. |
| primary | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084; Complete Composition and preparation, Medium No.1084 | supports | Exact primary supplies the masses, water input, carbon-source alternatives, pH/NaOH, 100% nitrogen and aerobic omissions; no numerical sterilization cycle or measured final volume is stated. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849; meta, components[0] and comments[0]/comments[2] | supports | Exact provider agrees with NBRC 1084. Source generic title is preserved without a taxonomic correction or growth inference. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch035/342/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91247 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91247 resolves to L-cysteine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml; data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml", "events": 9, "timestamp_issues": []}] |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned current catalog/tree exact legacy lookup | supports | Current absence of MediaIngredientMech:000389 is a completed negative lookup, not proof of historical invalidity. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned current catalog/tree exact legacy lookup | supports | Current absence of MediaIngredientMech:000389 is a completed negative lookup, not proof of historical invalidity. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer has unit-specific parsing and source-section handling; stock/volume heuristics do not make an unstated final volume measured. Current cleanup preserves conflicting duplicates. The historical default/conversion events must not be blamed on uninspected earlier code or overwritten; repair the maintained input with exact source units and conditions. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer has unit-specific parsing and source-section handling; stock/volume heuristics do not make an unstated final volume measured. Current cleanup preserves conflicting duplicates. The historical default/conversion events must not be blamed on uninspected earlier code or overwritten; repair the maintained input with exact source units and conditions. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required historical correspondence of the retained MediaIngredientMech:000389 cysteine-HCl assertion is not established by the available current catalog/tree. The current exact-key absence check completed; the historical check remains unavailable.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191827Z-culturemech-008423-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: actinotalea_fermentas_medium (CultureMech:008423)'
started_at: '2026-10-21T19:13:53Z'
finished_at: '2026-10-21T19:18:27Z'
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
summary: NBRC 1084 and TOGO M1849 agree on a batch formulation with 1 L water, 1 mg
  resazurin and 1.25 mg iron sulfate heptahydrate. Both local layers incorrectly express
  these as g/L and omit source preparation and the aerobic alternative. Unqualified
  cysteine-HCl does not establish its asserted L-specific form; historical MediaIngredientMech:000389
  correspondence remains unresolved.
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
  - path: data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
    sha256: a426de415bd4f4c2091167b117913f960c066a036cd1079f1d4b298785f88541
    role: target
  - path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
    sha256: 248c9f50441d6d77ec696f347568721427ad54740fddc2caea42e71686899ea3
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 342; batch 035 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-four task batches
    contain 340 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 343 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008423
targets:
- target_id: CultureMech:008423
  path: data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  label: actinotalea_fermentas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/342/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/342/strict.tsv"
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008423
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
  - CultureMech:008423
- check_id: legacy-historical-correspondence
  name: Required source-scope verification
  required: true
  status: unavailable
  summary: Required historical correspondence of the retained MediaIngredientMech:000389
    cysteine-HCl assertion is not established by the available current catalog/tree.
    The current exact-key absence check completed; the historical check remains unavailable.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - mimPinnedCatalog
  - mimPinnedTree
  - record
  - owner-0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:16.016226Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/342/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:17.187156Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/342/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:18.521991Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:19.374682Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:18:26Z'
  support: supports
  summary: './data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml:1:id: CultureMech:008423

    ./data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml:1:id: CultureMech:008423

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/342/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:18:26Z'
  support: supports
  summary: 17 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 14aeb7d71dd8b51839584f683ddcdb25fbab608cb3c68862cf8a1366996f8daf
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/342/evidence-context-original.json
  locator: Complete frozen source context and full local objects
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: Frozen target/owner objects match freshly inspected records. Source interpretations
    are assessed against actual bound capture bytes; historical limitations remain
    separate.
  snapshot_sha256: b8081dc3c7faf80acfcdda25ea792d8b011d3b9c67941bba5724d710964c448c
- evidence_id: primary
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084
  locator: Complete Composition and preparation, Medium No.1084
  accessed_at: '2026-10-21T18:58:51.598748Z'
  support: supports
  summary: Exact primary supplies the masses, water input, carbon-source alternatives,
    pH/NaOH, 100% nitrogen and aerobic omissions; no numerical sterilization cycle
    or measured final volume is stated.
  snapshot_sha256: 5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849
  locator: meta, components[0] and comments[0]/comments[2]
  accessed_at: '2026-10-21T18:58:50.666418Z'
  support: supports
  summary: Exact provider agrees with NBRC 1084. Source generic title is preserved
    without a taxonomic correction or growth inference.
  snapshot_sha256: ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/342/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 9b8cc8f60c8e21a46e7b9d662b3d96e0d19a16c8d2d6f6e11cf11a056559cca7
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
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
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
- evidence_id: chebi91247
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91247
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:41.606984Z'
  support: supports
  summary: CHEBI:91247 resolves to L-cysteine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 8ff9a3639e1afba34c0d40072292486ff792c7b63a496d189a1cfeb2e6574890
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T19:18:26Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id":
    "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806":
    [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806",
    "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml; data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml", "events":
    9, "timestamp_issues": []}]'
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned current catalog/tree exact legacy lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Current absence of MediaIngredientMech:000389 is a completed negative lookup,
    not proof of historical invalidity.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned current catalog/tree exact legacy lookup
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Current absence of MediaIngredientMech:000389 is a completed negative lookup,
    not proof of historical invalidity.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: Current importer has unit-specific parsing and source-section handling;
    stock/volume heuristics do not make an unstated final volume measured. Current
    cleanup preserves conflicting duplicates. The historical default/conversion events
    must not be blamed on uninspected earlier code or overwritten; repair the maintained
    input with exact source units and conditions.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:18:26Z'
  support: context_only
  summary: Current importer has unit-specific parsing and source-section handling;
    stock/volume heuristics do not make an unstated final volume measured. Current
    cleanup preserves conflicting duplicates. The historical default/conversion events
    must not be blamed on uninspected earlier code or overwritten; repair the maintained
    input with exact source units and conditions.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 22 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Main: Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1,\n    \
    \  \"source_unit\": \"L\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The source\
    \ volume or milligram batch amount is not the local gram-per-liter rate. Preserve\
    \ exact source unit, hydrate and batch stage; do not invent a measured final volume.\"\
    \n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"Main:\
    \ Yeast extract\",\n    \"decision\": \"unsupported\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 5,\n    \
    \  \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Main: CaCl2·2H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2·2H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.02,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Main: KH2PO4\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1.5,\n  \
    \    \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Main: K2HPO4\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.21\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.21\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 2.21,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 2.21,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Main: Resazurin\",\n    \"decision\": \"correct\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1,\n    \
    \  \"source_unit\": \"mg\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The source\
    \ volume or milligram batch amount is not the local gram-per-liter rate. Preserve\
    \ exact source unit, hydrate and batch stage; do not invent a measured final volume.\"\
    \n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"Main:\
    \ MgCl2·6H2O\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2·6H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.1,\n  \
    \    \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Main: FeSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4·7H2O\\\",\\n          \\\"volume\\\": 1.25,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1.25,\n \
    \     \"source_unit\": \"mg\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The source\
    \ volume or milligram batch amount is not the local gram-per-liter rate. Preserve\
    \ exact source unit, hydrate and batch stage; do not invent a measured final volume.\"\
    \n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\": \"Main:\
    \ NaHCO3\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 0.8,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.8,\n  \
    \    \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Main: (NH4)2SO4\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2SO4\\\",\\n          \\\"volume\\\": 1.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1.3,\n  \
    \    \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed\
    \ mass agrees numerically but a 1 L water input does not independently establish\
    \ measured final volume after dissolved solids and separate additions. Preserve\
    \ the source batch amount with evidence, rather than an unsupported exact final\
    \ g/L assertion.\"\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Main: Cellobiose or Cellulose (MN 300)\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[10].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Cellobiose or Cellulose (MN 300)\\\",\\n     \
    \     \\\"volume\\\": 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\",\n    \
    \    \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"source_amount\": 5,\n      \"source_unit\"\
    : \"g\",\n      \"reagent_strength\": null,\n      \"reagent_unit\": null,\n \
    \     \"final_volume_L\": null\n    },\n    \"rationale\": \"The printed mass\
    \ agrees numerically but a 1 L water input does not independently establish measured\
    \ final volume after dissolved solids and separate additions. Preserve the source\
    \ batch amount with evidence, rather than an unsupported exact final g/L assertion.\
    \ Cellobiose OR cellulose (MN 300) is an alternative at the stated single 5 g\
    \ input; do not add both.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"\
    component_or_context\": \"Main: Cysteine-HCl\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[11].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Cysteine-HCl\\\",\\n          \\\"volume\\\":\
    \ 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\",\n        \"\
    accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"source_amount\": 0.5,\n      \"source_unit\": \"g\",\n      \"reagent_strength\"\
    : null,\n      \"reagent_unit\": null,\n      \"final_volume_L\": null\n    },\n\
    \    \"rationale\": \"The printed mass agrees numerically but a 1 L water input\
    \ does not independently establish measured final volume after dissolved solids\
    \ and separate additions. Preserve the source batch amount with evidence, rather\
    \ than an unsupported exact final g/L assertion.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q13\",\n    \"component_or_context\": \"Main: NaOH\",\n    \"decision\": \"\
    not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"conc_value\\\": 8,\\\
    n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": null,\n \
    \     \"source_unit\": null,\n      \"reagent_strength\": 8,\n      \"reagent_unit\"\
    : \"M\",\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"Source\
    \ gives no fixed receiving dose for this reagent/gas. VARIABLE does not establish\
    \ the separate 8 M reagent strength or the 100% nitrogen atmosphere; capture those\
    \ at preparation scope.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Main: N2\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1849original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1849\",\n\
    \        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"N2\\\"\",\n        \"snapshot_sha256\": \"ec0d94bc6e1ac9af27a5b5899cfedb3b974bf475e4734afc9523d8dd192f9cef\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.666418Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": null,\n \
    \     \"source_unit\": null,\n      \"reagent_strength\": null,\n      \"reagent_unit\"\
    : null,\n      \"final_volume_L\": null\n    },\n    \"rationale\": \"Source gives\
    \ no fixed receiving dose for this reagent/gas. VARIABLE does not establish the\
    \ separate 8 M reagent strength or the 100% nitrogen atmosphere; capture those\
    \ at preparation scope.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Receiving pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Main preparation after Composition\",\n     \
    \   \"exact_source_quote\": \"Adjust pH to 7.4\",\n        \"snapshot_sha256\"\
    : \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\",\n    \
    \    \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pH\": 7.4\n    },\n    \"\
    rationale\": \"This preparation condition is absent from both local layers. Preserve\
    \ its source stage without asserting an incubation optimum or deriving an unspecified\
    \ dose.\"\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Adjustment-reagent strength\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Main preparation after Composition\",\n     \
    \   \"exact_source_quote\": \"8 M NaOH\",\n        \"snapshot_sha256\": \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\"\
    ,\n        \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"reagent_strength_M\": 8,\n\
    \      \"dose\": \"not quantified\"\n    },\n    \"rationale\": \"This preparation\
    \ condition is absent from both local layers. Preserve its source stage without\
    \ asserting an incubation optimum or deriving an unspecified dose.\"\n  },\n \
    \ {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"Anaerobic\
    \ atmosphere\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Main preparation after Composition\",\n     \
    \   \"exact_source_quote\": \"100% nitrogen\",\n        \"snapshot_sha256\": \"\
    5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\",\n        \"\
    parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"nitrogen_percent\": 100,\n\
    \      \"scope\": \"stated gas atmosphere; no absolute gas volume\"\n    },\n\
    \    \"rationale\": \"This preparation condition is absent from both local layers.\
    \ Preserve its source stage without asserting an incubation optimum or deriving\
    \ an unspecified dose.\"\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Aerobic alternative: Resazurin\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Explicit aerobic alternative sentence\",\n  \
    \      \"exact_source_quote\": \"omit resazurin and cysteine-HCl\",\n        \"\
    snapshot_sha256\": \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\"\
    ,\n        \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"alternative\": \"aerobic\"\
    ,\n      \"omitted_component\": \"Resazurin\",\n      \"do_not_replace_base_amount\"\
    : true\n    },\n    \"rationale\": \"The omission applies only to the explicitly\
    \ stated alternative, not to the base anaerobic formulation. Preserve the branch\
    \ without fabricating a zero concentration or a species growth assertion.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"Aerobic\
    \ alternative: Cysteine hydrochloride\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Explicit aerobic alternative sentence\",\n  \
    \      \"exact_source_quote\": \"omit resazurin and cysteine-HCl\",\n        \"\
    snapshot_sha256\": \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\"\
    ,\n        \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"alternative\": \"aerobic\"\
    ,\n      \"omitted_component\": \"Cysteine hydrochloride\",\n      \"do_not_replace_base_amount\"\
    : true\n    },\n    \"rationale\": \"The omission applies only to the explicitly\
    \ stated alternative, not to the base anaerobic formulation. Preserve the branch\
    \ without fabricating a zero concentration or a species growth assertion.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\": \"Carbon-source\
    \ alternative\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].preferred_term\",\n        \"stored\"\
    : \"Cellobiose or Cellulose (MN 300)\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].preferred_term\",\n        \"stored\"\
    : \"Cellobiose or Cellulose (MN 300)\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Composition carbon-source row\",\n        \"\
    exact_source_quote\": \"Cellobiose or Cellulose (MN 300) 5 g\",\n        \"snapshot_sha256\"\
    : \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\",\n    \
    \    \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"alternatives\": [\n      \
    \  \"Cellobiose\",\n        \"Cellulose (MN 300)\"\n      ],\n      \"single_batch_amount_g\"\
    : 5\n    },\n    \"rationale\": \"The exact OR wording is already retained. Attach\
    \ evidence and preserve mutually alternative identities; no pure-compound identity\
    \ is invented for the combined field.\"\n  },\n  {\n    \"quantity_id\": \"q21\"\
    ,\n    \"component_or_context\": \"Final-volume basis\",\n    \"decision\": \"\
    not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"\
    https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\",\n   \
    \     \"source_locator\": \"Composition water input\",\n        \"exact_source_quote\"\
    : \"Distilled water 1 L\",\n        \"snapshot_sha256\": \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\"\
    ,\n        \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"water_input_L\": 1,\n    \
    \  \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"The source\
    \ gives a water input, not a final-volume make-up statement. No new concentration\
    \ denominator is inferred.\"\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"\
    component_or_context\": \"Autoclave cycle\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"nbrc1084\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1084\"\
    ,\n        \"source_locator\": \"Main preparation: named separate components\"\
    ,\n        \"exact_source_quote\": \"sterilized separately by autoclaving under\
    \ N 2\",\n        \"snapshot_sha256\": \"5eedd5253a34be80dee727da72dae741f74d94c026619b1586ad946e958471df\"\
    ,\n        \"parsed_text_sha256\": \"4ccb5a1b92c96de5c085cabccc89dc6af5435b00557e93fc7ebc406405a362ce\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:51.598748Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": null,\n \
    \     \"duration_min\": null,\n      \"named_separate_components\": [\n      \
    \  \"Cellobiose\",\n        \"NaHCO3\",\n        \"cysteine-HCl\"\n      ]\n \
    \   },\n    \"rationale\": \"Add the stated separate sterilization and atmosphere,\
    \ but keep cycle numbers unspecified. Do not import a JCM default into this NBRC\
    \ source or assume that the cellulose alternative has a separately stated process.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '12 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 12/14
    primary and 9/14 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding. The legacy cysteine key remains historically
    unresolved separately; current CHEBI-based rows do not authenticate it.'
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi17997
  - chebi32139
  - chebi32145
  - chebi62946
  - chebi63036
  - chebi75836
  - chebi86158
  - chebi86345
  - chebi8806
  - chebi91247
  details: 'Instance coverage on a 0–100 percent scale, denominator 14: primary 85.71%;
    secondary 64.29%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 19 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact record and accession identity
  outcome: supported
  summary: CultureMech:008423, its exact single bacterial maintained owner, TOGO M1849
    and NBRC 1084 agree on this recipe identity. The source spells the medium name
    as retained locally. No asserted taxonomy identifier or strain-level growth statement
    is supplied, so the title is not treated as a taxonomy correction or growth experiment.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - provider
- assessment_id: forms
  area: grounding
  topic: Supplied forms versus ontology specificity
  outcome: concern
  summary: Explicit calcium/magnesium/iron hydrates agree with their asserted forms.
    CHEBI:91247 has L stereochemistry in its definition/InChI/SMILES, while the source
    says Cysteine-HCl without stereochemistry. This is unresolved supplied-form specificity,
    not evidence of D or racemic material. K2HPO4 source is not explicitly a hydrate;
    the matching term formula is retained without adopting a trihydrate synonym. Yeast
    extract and the carbon-source OR field receive no invented pure-molecule ID.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - primary
  - provider
  - chebi91247
  - chebi131527
  - chebi75836
  - chebi86158
  - chebi86345
- assessment_id: preparation
  area: completeness
  topic: Source conditions and aerobic branch
  outcome: concern
  summary: Both local layers omit the 7.4 pH adjustment with 8 M NaOH, explicitly
    100% nitrogen atmosphere, separate autoclaving of cellobiose/bicarbonate/cysteine-HCl
    and the aerobic alternative omitting resazurin/cysteine-HCl. NBRC provides no
    cycle numbers. Preserve the source branch and carbon-source OR relation without
    deleting the base ingredients or asserting target-organism growth.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Composition and application limits
  outcome: supported
  summary: COMPLEX/UNDEFINED is compatible with the yeast-extract component, and LIQUID
    with this base formulation. The generic microbial-cultivation application does
    not establish species-specific growth, an optimum or an aerobic/anaerobic phenotype.
    Source alternate preparation is formulation context only.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: provenance
  area: provenance
  topic: Evidence and maintained-input ownership
  outcome: concern
  summary: Neither target nor owner attaches claim-level amount evidence, despite
    recoverable exact primary/provider support. Source URLs and import/enrichment
    history establish provenance but do not prove amounts, gas scope or chemical specificity.
    Append later authorized clarification, preserve stable ID and regenerate only
    from the maintained owner after correction.
  target_ids:
  - CultureMech:008423
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - history-metadata
  - writer-0
  - writer-1
findings:
- finding_id: f1
  issue_key: culturemech.008423.water-indicator-iron-units
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Water and two milligram inputs have gram-rate units
  description: Both layers encode 1 L water as 1 G_PER_L, 1 mg resazurin as 1 G_PER_L
    and 1.25 mg FeSO4·7H2O as 1.25 G_PER_L. Other masses have an unestablished final-volume
    denominator.
  target_ids:
  - CultureMech:008423
  field_paths:
  - ingredients[0].concentration
  - ingredients[5].concentration
  - ingredients[7].concentration
  - ingredients
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
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
  issue_key: culturemech.008423.preparation-and-alternative
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and the explicit aerobic alternative are missing
  description: Both layers omit source pH/reagent strength, 100% nitrogen preparation,
    separate sterilization and aerobic omissions.
  target_ids:
  - CultureMech:008423
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: Native P3.5 is elevated to major because omitted sterilization
    boundaries, atmosphere and alternative composition materially alter this source
    recipe.
- finding_id: f3
  issue_key: culturemech.008423.cysteine-specificity-and-history
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Cysteine stereochemistry and historical linkage need qualification
  description: The source unqualified Cysteine-HCl does not establish the current
    L-specific term; the retained legacy000389 mapping is absent from the complete
    current snapshot but its historical correspondence is unresolved.
  target_ids:
  - CultureMech:008423
  field_paths:
  - ingredients[11].term
  - ingredients[11].mediaingredientmech_term
  evidence_ids:
  - primary
  - chebi91247
  - mimPinnedCatalog
  - mimPinnedTree
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
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
  description: Restore exact water/milligram batch units, preserve other source masses
    with their actual basis and attach claim-level evidence. Keep cellobiose OR cellulose
    and the explicit hydrate; do not infer final rates from an unmeasured final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008423
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
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
  description: Add exact source-scoped preparation and the conditional aerobic omission
    branch with evidence. Retain unprovided cycle numbers as unknown and avoid a growth/phenotype
    assertion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008423
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
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
  description: Seek source/supplier form and historical legacy mapping evidence; document
    unresolved specificity without inventing a D/racemic replacement or declaring
    historical identity invalid from a current absence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008423
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/actinotalea_fermentas_medium.yaml
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
- Required historical correspondence of the retained MediaIngredientMech:000389 cysteine-HCl
  assertion is not established by the available current catalog/tree. The current
  exact-key absence check completed; the historical check remains unavailable.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-035
- generated-medium
```
