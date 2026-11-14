# Source and formulation review: aminithiophilus_medium (CultureMech:001636)

- Review: 20261021T143438Z-culturemech-001636-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:22:43Z
- Finished UTC: 2026-10-21T14:34:38Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 503f explicitly assembles six stages into a 1008 mL base medium. Both local layers instead flatten stage and stock concentrations into 34 main ingredients, including unsupported HCl mass conversion from an unqualified percentage. The retained main procedure and pH range are useful, but stock scope and source-only DSM 117064 modifications must remain distinct. Nickel/resazurin forms and one current secondary mapping gap need follow-up; all required current source checks are available.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 247; batch 025 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-four task batches contain 240 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 243 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001636 | data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml | generated | aminithiophilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001636 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001636 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/247/strict.tsv |
| validate-terms | passed | True | CultureMech:001636 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001636 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001636 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Completed exact current secondary-key lookup | passed | True | CultureMech:001636 | The full pinned index scan completed. CHEBI:26833 has no exact mapped preferred-term row; this confirmed current mapping gap is a finding, not an unavailable check. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001636.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001636.

83 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Solution A receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 952 mL Solution A in the base A–F assembly; all six stated doses sum to 1008 mL.",
    "rationale": "These are receiving volumes, not ingredient masses or concentrations. Preserve identifiers 1089–1094 and stage order; do not conflate similarly named stocks in another medium.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1089,\n                        \"amount\": 952,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Solution B receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 25 mL Solution B in the base A–F assembly; all six stated doses sum to 1008 mL.",
    "rationale": "These are receiving volumes, not ingredient masses or concentrations. Preserve identifiers 1089–1094 and stage order; do not conflate similarly named stocks in another medium.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1090,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Solution C receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 1 mL Solution C in the base A–F assembly; all six stated doses sum to 1008 mL.",
    "rationale": "These are receiving volumes, not ingredient masses or concentrations. Preserve identifiers 1089–1094 and stage order; do not conflate similarly named stocks in another medium.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1091,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Solution D receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 mL Solution D in the base A–F assembly; all six stated doses sum to 1008 mL.",
    "rationale": "These are receiving volumes, not ingredient masses or concentrations. Preserve identifiers 1089–1094 and stage order; do not conflate similarly named stocks in another medium.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1092,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Solution E receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 mL Solution E in the base A–F assembly; all six stated doses sum to 1008 mL.",
    "rationale": "These are receiving volumes, not ingredient masses or concentrations. Preserve identifiers 1089–1094 and stage order; do not conflate similarly named stocks in another medium.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 1093,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Solution F receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 mL Solution F in the base A–F assembly; all six stated doses sum to 1008 mL.",
    "rationale": "These are receiving volumes, not ingredient masses or concentrations. Preserve identifiers 1089–1094 and stage order; do not conflate similarly named stocks in another medium.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 1094,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Solution A: KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.210084",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.210084",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.2 g within Solution A. The entire stated stage amount is used in the base, so contribution=0.2/1.008=0.198412698413 g/L. Existing provider-derived 0.210084 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210084,\n                        \"mmol_l\": 1.54377,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Solution A: NH4Cl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.262605",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.262605",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.25 g within Solution A. The entire stated stage amount is used in the base, so contribution=0.25/1.008=0.248015873016 g/L. Existing provider-derived 0.262605 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.262605,\n                        \"mmol_l\": 4.90942,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Solution A: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5.2521",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5.2521",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 5 g within Solution A. The entire stated stage amount is used in the base, so contribution=5/1.008=4.96031746032 g/L. Existing provider-derived 5.2521 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2521,\n                        \"mmol_l\": 89.8717,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Solution A: MgCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.420168",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.420168",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.4 g within Solution A. The entire stated stage amount is used in the base, so contribution=0.4/1.008=0.396825396825 g/L. Existing provider-derived 0.420168 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.420168,\n                        \"mmol_l\": 2.06671,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Solution A: KCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.52521",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.52521",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.5 g within Solution A. The entire stated stage amount is used in the base, so contribution=0.5/1.008=0.496031746032 g/L. Existing provider-derived 0.52521 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.52521,\n                        \"mmol_l\": 7.04507,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Solution A: CaCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.157563",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.157563",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.15 g within Solution A. The entire stated stage amount is used in the base, so contribution=0.15/1.008=0.14880952381 g/L. Existing provider-derived 0.157563 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.157563,\n                        \"mmol_l\": 1.07175,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Solution A: Trace element solution SL-10",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Within Solution A, retain 1 ml of Trace element solution SL-10, exact solution 595.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Solution A: Selenite-tungstate solution",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Within Solution A, retain 1 ml of Selenite-tungstate solution, exact solution 777.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Solution A: Sulfur",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "10.5042",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "10.5042",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 10 g within Solution A. The entire stated stage amount is used in the base, so contribution=10/1.008=9.92063492063 g/L. Existing provider-derived 10.5042 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. Preserve powdered sulfur. An atom-level canonical label with elemental-sulfur synonym is not proof of an incorrect allotrope; current secondary lookup is assessed separately.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.5042,\n                        \"mmol_l\": 327.54,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Solution A: Sodium resazurin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00052521",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00052521",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.50 mL sodium-resazurin stock 0.1% w/v in solution A. It contributes 0.0005 g to the explicit 1008 mL base medium, or 0.000496031746032 g/L; existing 0.00052521 g/L is A-stage normalization.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00052521,\n                        \"mmol_l\": 0.00209105,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Solution A: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 950 mL water within Solution A; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Solution B: Na2CO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 1.25 g within Solution B. The entire stated stage amount is used in the base, so contribution=1.25/1.008=1.24007936508 g/L. Existing provider-derived 50 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Solution B: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 25 mL water within Solution B; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Solution C: Wolin's vitamin solution (10x)",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Within Solution C, retain 1 ml of Wolin's vitamin solution (10x), exact solution 5980. This is 1 mL stock 5980 through solution C; the outer 1 mL receiving dose is the same stock portion, not another 1/1000 dilution.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Solution D: Casamino acids",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 2 g within Solution D. The entire stated stage amount is used in the base, so contribution=2/1.008=1.98412698413 g/L. Existing provider-derived 200 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[4].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Casamino acids\",\n                        \"compound_id\": 101,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 200,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Solution D: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 mL water within Solution D; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[4].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Solution E: Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.2 g within Solution E. The entire stated stage amount is used in the base, so contribution=0.2/1.008=0.198412698413 g/L. Existing provider-derived 20 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[5].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Solution E: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 mL water within Solution E; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[5].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Solution F: Na2S x 9 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.3 g within Solution F. The entire stated stage amount is used in the base, so contribution=0.3/1.008=0.297619047619 g/L. Existing provider-derived 30 g/L is stage strength, not final medium.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[6].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Solution F: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 mL water within Solution F; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[6].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Trace element solution SL-10: HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 10 mL HCl labeled 25% in SL-10, which is explicitly made up to 1000 mL. Percentage basis and density are not supplied; neither 2.5 g/L stock nor its final mass contribution is established.",
    "rationale": "The provider g_l field and local 2.5 g/L are insufficient to repair this unit ambiguity. Decision correct means restore the supported original stock-volume/label representation and remove the unsupported mass assertion; no numerical mass replacement is proposed.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Trace element solution SL-10: FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 1.5 g in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=1.5 g/L stock×0.001 L/1.008 L=0.0014880952381 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Trace element solution SL-10: ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 70 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.07 g/L stock×0.001 L/1.008 L=6.94444444444e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Trace element solution SL-10: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 100 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.1 g/L stock×0.001 L/1.008 L=9.92063492063e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Trace element solution SL-10: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 6 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.006 g/L stock×0.001 L/1.008 L=5.95238095238e-06 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Trace element solution SL-10: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 190 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.19 g/L stock×0.001 L/1.008 L=0.000188492063492 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Trace element solution SL-10: CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 2 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.002 g/L stock×0.001 L/1.008 L=1.98412698413e-06 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Trace element solution SL-10: NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 24 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.024 g/L stock×0.001 L/1.008 L=2.38095238095e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Trace element solution SL-10: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 36 mg in Trace element solution SL-10, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.036000000000000004 g/L stock×0.001 L/1.008 L=3.57142857143e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Trace element solution SL-10: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 990 mL water within Trace element solution SL-10; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Selenite-tungstate solution: NaOH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.5 g in Selenite-tungstate solution, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.5 g/L stock×0.001 L/1.008 L=0.000496031746032 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[8].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Selenite-tungstate solution: Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 3 mg in Selenite-tungstate solution, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.003 g/L stock×0.001 L/1.008 L=2.97619047619e-06 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[8].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Selenite-tungstate solution: Na2WO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 4 mg in Selenite-tungstate solution, provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.004 g/L stock×0.001 L/1.008 L=3.96825396825e-06 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[8].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Selenite-tungstate solution: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 1000 mL water within Selenite-tungstate solution; water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[8].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Wolin's vitamin solution (10x): Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 20 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.02 g/L stock×0.001 L/1.008 L=1.98412698413e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "Wolin's vitamin solution (10x): Folic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 20 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.02 g/L stock×0.001 L/1.008 L=1.98412698413e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "Wolin's vitamin solution (10x): Pyridoxine hydrochloride",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 100 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.1 g/L stock×0.001 L/1.008 L=9.92063492063e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Wolin's vitamin solution (10x): Thiamine HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001 L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q45",
    "component_or_context": "Wolin's vitamin solution (10x): Riboflavin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001 L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q46",
    "component_or_context": "Wolin's vitamin solution (10x): Nicotinic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001 L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q47",
    "component_or_context": "Wolin's vitamin solution (10x): Calcium D-(+)-pantothenate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001 L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims. Base source explicitly specifies Calcium D-(+)-pantothenate; asserted CHEBI:31345 has D synonyms and stereospecific structure. Do not transfer the branch seven-vitamin stock’s less-specific calcium name to this base assertion.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q48",
    "component_or_context": "Wolin's vitamin solution (10x): Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 1 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.001 g/L stock×0.001 L/1.008 L=9.92063492063e-07 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q49",
    "component_or_context": "Wolin's vitamin solution (10x): p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001 L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q50",
    "component_or_context": "Wolin's vitamin solution (10x): (DL)-alpha-Lipoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001 L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer. SL-10 has an explicit final make-up volume; the selenite and vitamin stocks have listed water 1000 mL and provider volume 1000 mL, so their calculated concentrations are explicitly provider-basis calculations, not independent measured-volume claims. Preserve DL in the source name; generic lipoic acid CHEBI:16494 is not an asserted R-only replacement.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q51",
    "component_or_context": "Wolin's vitamin solution (10x): Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 1000 mL water within Wolin's vitamin solution (10x); water volume is not a g/L solute or independent final-volume proof.",
    "rationale": "Restore the exact named stage, original source amount and unit, water and receiving dose; source-only quantities have no current local numeric assertion. No attached amount evidence is present in either layer.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[9].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q52",
    "component_or_context": "Base final volume",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain explicit 1008 mL final base volume, matching 952+25+1+10+10+10 mL assembly.",
    "rationale": "The primary gives this denominator directly; do not replace it with 1000 mL or apply it to the modified strain branch without a separate branch statement.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 header",
        "exact_source_quote": "Final volume: 1008 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1089,\n                        \"amount\": 952,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1090,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1091,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1092,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 1093,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 1094,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q53",
    "component_or_context": "Solution A stated receiving volume versus liquid entries",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "Retain stated A dose 952 mL and water 950 mL. Its listed liquid inputs total 950+1+1+0.50=952.5 mL; the 0.5 mL discrepancy remains explicit.",
    "rationale": "Do not invent a corrected 952.5 mL A dose or override the explicit 1008 mL final base volume. Source quantities are preserved separately from an independently measured assembled volume.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1089,\n                        \"amount\": 952,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00052521,\n                        \"mmol_l\": 0.00209105,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      },
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q54",
    "component_or_context": "Sodium-resazurin stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "0.1% w/v = 1 g/L sodium-resazurin stock, delivered 0.50 mL.",
    "rationale": "The percentage basis is explicit; source sodium salt identity is separately reviewed. Do not use the free-acid molecular mass.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 Solution A",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q55",
    "component_or_context": "SL-10 final make-up volume",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Make SL-10 up to 1000 mL after dissolving iron in HCl and then adding water and remaining salts.",
    "rationale": "This quantity is retained at the current main preparation root; correct its stock scope rather than treating it as absent. It is not the 1008 mL receiving-medium final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive503fapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503f",
        "source_locator": "$.data.solutions[7].steps[0].step",
        "exact_source_quote": "Finally make up to 1000.00 ml.",
        "snapshot_sha256": "ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7"
      }
    ]
  },
  {
    "quantity_id": "q56",
    "component_or_context": "SL-10 HCl percentage basis",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Preserve25% as an unqualified source label and 10 mL as stock preparation volume.",
    "rationale": "No mass/volume or mass/mass basis or density is established. Neither molecular identity HCl nor the provider calculated2.5 g/L establishes the missing basis.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page2 SL-10 subsection",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q57",
    "component_or_context": "Main A/B gas fractions",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 80% nitrogen/20% carbon dioxide for solution A preparation and dispensing and B autoclaving.",
    "rationale": "Existing main prose carries the source quantity but has no attached evidence. Strip literal HTML markup only during separately authorized owner curation; preserve quantities, gas and stage semantics.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "80% N2 and 20% CO2",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q58",
    "component_or_context": "Main A sparging duration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 30–45 min for A sparging, before sulfur-containing receiving vessels.",
    "rationale": "Existing main prose carries the source quantity but has no attached evidence. Strip literal HTML markup only during separately authorized owner curation; preserve quantities, gas and stage semantics.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q59",
    "component_or_context": "Main A autoclave temperature",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 110°C for solution A; the source does not state this as a universal cycle for every stock.",
    "rationale": "Existing main prose carries the source quantity but has no attached evidence. Strip literal HTML markup only during separately authorized owner curation; preserve quantities, gas and stage semantics.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "110°C",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q60",
    "component_or_context": "Main A autoclave duration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 20 min for A sterilization; do not transfer to B–F without explicit support.",
    "rationale": "Existing main prose carries the source quantity but has no attached evidence. Strip literal HTML markup only during separately authorized owner curation; preserve quantities, gas and stage semantics.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "for 20 min",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q61",
    "component_or_context": "C/D/E/F nitrogen proportion",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 100% nitrogen for C preparation/filter sterilization and D/E/F autoclaving.",
    "rationale": "Existing main prose carries the source quantity but has no attached evidence. Strip literal HTML markup only during separately authorized owner curation; preserve quantities, gas and stage semantics.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "100% N2",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q62",
    "component_or_context": "Complete base pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.2,
          "max": 7.4
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.2,
          "max": 7.4
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain base complete-medium pH 7.2–7.4, adjusted if necessary; existing ph_range and main prose agree.",
    "rationale": "Existing main prose carries the source quantity but has no attached evidence. Strip literal HTML markup only during separately authorized owner curation; preserve quantities, gas and stage semantics.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "7.2 - 7.4",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q63",
    "component_or_context": "B–F unreported sterilization cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes or serum vials containing the appropriate amount of sulfur and autoclave at &lt;b&gt;110°C &lt;/b&gt;for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "C is filtered; B and D–F are autoclaved in their specified atmospheres. Their time/temperature values are not supplied.",
    "rationale": "The only explicit 110°C/20 min cycle belongs to A. Do not infer other cycles or filtration pore size.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "Solution C is prepared under 100% N2 gas and sterilized by filtration.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 main preparation",
        "exact_source_quote": "Solutions D, E, and F are autoclaved under 100% N2 gas.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q64",
    "component_or_context": "Branch exclusions",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For DSM 117064 only, omit base C, D, E and F; do not mix their vitamin/casamino/yeast/sulfide stocks with the replacement branch.",
    "rationale": "This source-only branch is not currently asserted in either local layer. If represented during authorized curation, retain it as a distinct conditional variant, never as a correction to the base or a new organism growth assertion. No measured branch final volume is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q65",
    "component_or_context": "Branch solution B dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For DSM 117064 only, increase B to 50 mL.",
    "rationale": "This source-only branch is not currently asserted in either local layer. If represented during authorized curation, retain it as a distinct conditional variant, never as a correction to the base or a new organism growth assertion. No measured branch final volume is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q66",
    "component_or_context": "Branch literal carbonate concentration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain the source parenthetical 2.50 g/L Na2CO3 exactly as a branch assertion. B stock 50 g/L × 50 mL supplies 2.50 g, but the source supplies no explicit modified final volume; do not silently derive a new g/L or use the base 1008 mL denominator.",
    "rationale": "This source-only branch is not currently asserted in either local layer. If represented during authorized curation, retain it as a distinct conditional variant, never as a correction to the base or a new organism growth assertion. No measured branch final volume is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q67",
    "component_or_context": "Branch DSM 503 D dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For DSM 117064 only, add 1 mL of DSM 503 solution D, the named seven-vitamin stock pathway.",
    "rationale": "This source-only branch is not currently asserted in either local layer. If represented during authorized curation, retain it as a distinct conditional variant, never as a correction to the base or a new organism growth assertion. No measured branch final volume is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q68",
    "component_or_context": "Branch DSM 916 F dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For DSM 117064 only, add 10 mL of DSM 916 solution F, the named ferrous-chloride stock pathway.",
    "rationale": "This source-only branch is not currently asserted in either local layer. If represented during authorized curation, retain it as a distinct conditional variant, never as a correction to the base or a new organism growth assertion. No measured branch final volume is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q69",
    "component_or_context": "Branch pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "For DSM 117064 only, complete-medium pH 7.8–8.0; keep base pH 7.2–7.4 unchanged.",
    "rationale": "This source-only branch is not currently asserted in either local layer. If represented during authorized curation, retain it as a distinct conditional variant, never as a correction to the base or a new organism growth assertion. No measured branch final volume is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q70",
    "component_or_context": "Branch nested DSM 503 D stock transfer",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "DSM 503 D is 1 mL seven-vitamin solution1038; the branch1 mL D portion is that same stock volume, not two successive 1/1000 dilutions.",
    "rationale": "Only the named D dependency is followed. Parent DSM 503 main medium, other solutions and strain contexts are excluded.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      },
      {
        "source_key": "solution5960",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5960",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\": \"Seven vitamins solution\",\n                \"solution_id\": 1038,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "b7410288819afd9c77a60cfa809efc7237b24e136ab252f60c77b17e020cbcee"
      },
      {
        "source_key": "dsmz503",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf",
        "source_locator": "Solution D subsection",
        "exact_source_quote": "Seven vitamins solution 1.00 ml",
        "snapshot_sha256": "2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa",
        "parsed_text_sha256": "89641af386bfdf38f8b9f3306d8937b22511d687ce18efed884f4dda432a49d3"
      }
    ]
  },
  {
    "quantity_id": "q71",
    "component_or_context": "Branch seven-vitamin stock: Vitamin B12",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 100 mg Vitamin B12 with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.1 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q72",
    "component_or_context": "Branch seven-vitamin stock: p-Aminobenzoic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 80 mg p-Aminobenzoic acid with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.08 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 80,\n                \"unit\": \"mg\",\n                \"g_l\": 0.08,\n                \"mmol_l\": 0.583345,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q73",
    "component_or_context": "Branch seven-vitamin stock: D-(+)-biotin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 20 mg D-(+)-biotin with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.02 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"D-(+)-biotin\",\n                \"compound_id\": 1359,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q74",
    "component_or_context": "Branch seven-vitamin stock: Nicotinic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 200 mg Nicotinic acid with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.2 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"mg\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.62456,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q75",
    "component_or_context": "Branch seven-vitamin stock: Calcium pantothenate",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 100 mg Calcium pantothenate with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.1 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Calcium pantothenate\",\n                \"compound_id\": 518,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.209849,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q76",
    "component_or_context": "Branch seven-vitamin stock: Pyridoxine hydrochloride",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 300 mg Pyridoxine hydrochloride with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.3 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 300,\n                \"unit\": \"mg\",\n                \"g_l\": 0.3,\n                \"mmol_l\": 1.45886,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q77",
    "component_or_context": "Branch seven-vitamin stock: Thiamine-HCl x 2 H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 200 mg Thiamine-HCl x 2 H2O with listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this is 0.2 mg delivered per branch batch; branch final g/L remains unresolved.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Thiamine-HCl x 2 H2O\",\n                \"compound_id\": 77,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"mg\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 0.535761,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q78",
    "component_or_context": "Branch seven-vitamin stock: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Source-only branch seven-vitamin stock: 1000 ml Distilled water with listed water 1000 mL and provider stock volume 1000 mL.",
    "rationale": "Keep these original branch stock forms separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign base-specific forms or invented IDs; no target grounding exists for these source-only branch nodes.",
    "source_snippets": [
      {
        "source_key": "solution1038",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1038",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q79",
    "component_or_context": "Branch nested DSM 916 F stock transfer",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "DSM 916 F is 10 mL of ferrous stock 1885, the same volume explicitly transferred in the branch.",
    "rationale": "The 5.2% label is unqualified; direct mass/water details are independently captured below. Do not import the rest of DSM 916.",
    "source_snippets": [
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      },
      {
        "source_key": "solution6570",
        "source_url": "https://mediadive.dsmz.de/rest/solution/6570",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": null,\n                \"compound_id\": null,\n                \"solution\": \"Ferrous chloride solution (5.2%)\",\n                \"solution_id\": 1885,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "0f041c2ff9d8250788f8e0af1560502c33c448135cf2bf9924d75c3e8e8a08e2"
      },
      {
        "source_key": "dsmz916",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf",
        "source_locator": "Solution F subsection",
        "exact_source_quote": "Ferrous chloride solution (5.2%) 10.00 ml",
        "snapshot_sha256": "1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323",
        "parsed_text_sha256": "a3b30458292f598b20d5d89e08de5b2fbe0cfa26f3e1629a7853d03f0fa63366"
      }
    ]
  },
  {
    "quantity_id": "q80",
    "component_or_context": "Branch ferrous stock: FeCl2 x 4 H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 0.52 g FeCl2 x 4 H2O in the separate ferrous stock. Provider volume 10 mL and concentration 52 g/L for FeCl2 tetrahydrate are declared provider quantities; the source lists 0.52 g and 10 mL water.",
    "rationale": "Do not turn a listed water volume into an independently measured final stock volume or use the unqualified5.2% label alone as a percent-basis assertion. Preserve the exact tetrahydrate; no final branch mass concentration is derived.",
    "source_snippets": [
      {
        "source_key": "solution1885",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1885",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.52,\n                \"unit\": \"g\",\n                \"g_l\": 52,\n                \"mmol_l\": 261.554,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "87acf0e8ad2a475568f87f4dad2d241eaf3cb9d7dcaad412929b867cc85ceaab"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q81",
    "component_or_context": "Branch ferrous stock: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 10 ml Distilled water in the separate ferrous stock. Provider volume 10 mL and concentration 52 g/L for FeCl2 tetrahydrate are declared provider quantities; the source lists 0.52 g and 10 mL water.",
    "rationale": "Do not turn a listed water volume into an independently measured final stock volume or use the unqualified5.2% label alone as a percent-basis assertion. Preserve the exact tetrahydrate; no final branch mass concentration is derived.",
    "source_snippets": [
      {
        "source_key": "solution1885",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1885",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "87acf0e8ad2a475568f87f4dad2d241eaf3cb9d7dcaad412929b867cc85ceaab"
      },
      {
        "source_key": "dsmz503f",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf",
        "source_locator": "Page1 explicit DSM 117064 modification",
        "exact_source_quote": "For DSM 117064: Omit solution C, solution D, solution E, and solution F. Increase the\namount of solution B to 50 ml (2.50 g/l Na2CO3). Supplement the medium with 1 ml of\nsolution D of medium 503 and 10 ml of solution F of medium 916. Adjust the pH of the\ncomplete medium to 7.8 - 8.0.",
        "snapshot_sha256": "135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1",
        "parsed_text_sha256": "f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92"
      }
    ]
  },
  {
    "quantity_id": "q82",
    "component_or_context": "Branch ferrous-stock pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain pH 2 with HCl within the ferrous stock, not the branch complete-medium pH 7.8–8.0.",
    "rationale": "Keep stock and receiving-medium pH claims separate. No fixed HCl dose or concentration is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz916",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf",
        "source_locator": "Ferrous chloride solution subsection",
        "exact_source_quote": "Adjust to pH 2 with HCl.",
        "snapshot_sha256": "1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323",
        "parsed_text_sha256": "a3b30458292f598b20d5d89e08de5b2fbe0cfa26f3e1629a7853d03f0fa63366"
      }
    ]
  },
  {
    "quantity_id": "q83",
    "component_or_context": "Branch ferrous HCl dose",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "proposed_source_representation": "HCl receiving quantity and strength are not quantified for this stock pH adjustment.",
    "rationale": "Keep stock and receiving-medium pH claims separate. No fixed HCl dose or concentration is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz916",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf",
        "source_locator": "Ferrous chloride solution subsection",
        "exact_source_quote": "Adjust to pH 2 with HCl.",
        "snapshot_sha256": "1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323",
        "parsed_text_sha256": "a3b30458292f598b20d5d89e08de5b2fbe0cfa26f3e1629a7853d03f0fa63366"
      }
    ]
  }
]

### Primary IDs and exact current CHEBI-based secondary mappings

grounding: concern. Targets: CultureMech:001636.

32 distinct asserted primary IDs have matching nonobsolete labels in both layers. Target has 32/34 primary links and 30/34 current secondary links; 29/30 asserted secondary keys have exact pinned mapped rows, with CHEBI:26833 absent. These 94.12% primary and 85.29% verified-secondary instance metrics have denominator 34 and scale 0–100; they measure linkage, not scientific accuracy. No legacy secondary key is asserted.

### Source accession and maintained ownership

identity: supported. Targets: CultureMech:001636.

CM001636 and its exact maintained owner resolve to DSMZ 503f, not DSMZ 503. The target and owner retain the same 34 ingredient assertions, pH and preparation. Base A–F and DSM 117064-specific modifications are distinct formulations; no new taxon or growth claim is inferred.

### Claim-level amount support and source scope

evidence: concern. Targets: CultureMech:001636.

The local layers have import provenance but no attached amount evidence. The inventory covers every local concentration and scoped source-only quantity using literal excerpts, exact source locators, units, stages and original capture hashes. Provider-declared volume is kept separate from measured assembled final volume.

### Preparation stages, source-only additions and owner differences

completeness: concern. Targets: CultureMech:001636.

The main A–F procedure and final pH are preserved, including sulfur handling, gas fractions, 30–45 min sparging, A 110°C/20 min, separate stock sterilization and B→F addition order. However, named stage compositions/doses are absent, SL-10 final makeup is wrongly at main root, and HTML markup remains literal in prose. Source-only branch stocks and pH remain conditional.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:001636.

COMPLEX/UNDEFINED and LIQUID are consistent with base casamino acids, yeast extract and no gelling agent. The branch omits these complex additions, so these base classifications must not automatically be transferred to the branch. Source name and generic application do not prove growth.

### Supplied forms and chemical specificity

grounding: concern. Targets: CultureMech:001636.

Nickel chloride is explicitly hexahydrate but CHEBI:34887 is anhydrous Cl2Ni; sodium resazurin is mapped to sodium-free CHEBI:8806. Base calcium D-(+)-pantothenate agrees with the D synonyms/stereospecific CHEBI:31345; generic CHEBI:16494 does not contradict the retained DL-lipoic name. CHEBI:26833 has elemental-sulfur synonyms; powder context does not prove an incorrect atom/allotrope mapping. The current secondary-key absence is separate from primary identity. Vitamin B12 remains generic; no specific vitamer or mixture identity is invented.

### Growth, organism taxonomy and graph claims

scope: not_applicable. Targets: CultureMech:001636.

The title, generic Microbial cultivation application and catalog Aerobic flags are not experimental growth or taxonomy evidence. No growth assertions, current taxonomy IDs or graph membership are added. Explicit source strain qualifiers remain formulation scope only.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001636.

21 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Authoritative inputs and current writer scope

provenance: concern. Targets: CultureMech:001636.

Current MediaDive code separates first-stage ingredients and stock references but still gathers preparation from every API solution at the main root. Current cleanup flags disagreeing duplicate values; current lossless merge preserves scientific differences. The current code is not evidence of a particular old execution. Repair the exact normalized owner and review source-stage import handling before separately authorized regeneration.

## Findings

### f1: Stage and stock concentrations replace the assembled medium

blocker / open / confirmed; issue key: culturemech.001636.a-through-f-stock-collapse.

Both layers flatten 34 concentration assertions from separate A, B, D, E, F, SL-10, selenite and vitamin stocks. Primary final volume is explicitly 1008 mL; A’s 952 mL provider normalization and full-strength B–F/stock values are not final-medium concentrations. The stage graph, dose and separate water rows are missing.

### f2: HCl mass conversion lacks a specified percentage basis

major / open / confirmed; issue key: culturemech.001636.hcl-unqualified-percent-mass.

ingredients[12] stores 2.5 g/L HCl, matching a provider calculation, while the primary specifies 10 mL HCl 25% in SL-10 with no percentage basis or density. This cannot establish that mass concentration, even before the separate stock/main stage error.

### f3: Nickel hydration and sodium-resazurin form are not preserved

major / open / confirmed; issue key: culturemech.001636.source-salt-and-hydrate-forms.

Source NiCl2 x 6H2O is grounded to anhydrous CHEBI:34887 in primary and current secondary fields; source sodium resazurin is grounded to sodium-free CHEBI:8806. Other retained generic identities are not declared wrong merely because their source names include powder or DL context.

### f4: SL-10 preparation is represented as main-medium preparation

major / open / confirmed; issue key: culturemech.001636.stock-preparation-scope.

The second root preparation step dissolves iron in HCl and makes up to 1000 mL; this belongs to SL-10, not the 1008 mL main assembly. Main prose names A–F but their structured compositions and doses are absent. The primary also contains a separate DSM 117064 branch; if represented, its replacements/pH must stay conditional.

### f5: The asserted sulfur secondary key lacks a current pinned mapping

minor / open / confirmed; issue key: culturemech.001636.sulfur-current-secondary-gap.

CHEBI:26833 resolves in OLS with the canonical sulfur atom label and elemental-sulfur synonyms, but the complete pinned MIM preferred-term index has no mapped row for that exact secondary key. This is a completed negative lookup, not source unavailability or proof of wrong primary sulfur identity.

## Recommended Actions And Acceptance Checks

### a1

Restore the exact A–F stage graph and named nested stocks with all source amounts/water and receiving doses in the normalized owner. Correct flattened values with the explicit base 1008 mL denominator where justified; retain source/provider limits for individual stock volumes and A’s 952 versus 952.5 mL entries. Attach narrow evidence and regenerate only after authorized curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore exact 10 mL HCl 25% source representation at SL-10 scope and keep percentage basis unresolved unless exact-source evidence supplies it. Remove the unsupported mass assertion only through authorized owner curation; do not invent density or a numerical replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify exact salt/hydrate replacements in the normalized owner without inventing an uninspected identifier, preserve source masses, and never use the anhydrous/free-acid molecular mass for supplied forms. Preserve valid D-pantothenate, generic B12, DL-lipoic and elemental-sulfur context.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve the useful main sequence and move the exact SL-10 procedure to its stock scope. Preserve A-only 110°C/20 min and distinct B–F sterilization limits; clean literal HTML without changing values. Keep any recovered DSM 117064 branch separate, including named DSM 503 D and DSM 916 F dependencies, without importing either parent medium or inferring branch final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Reconcile the current secondary mapping using exact MIM evidence; do not substitute an adjacent sulfur species or delete a valid primary identifier based solely on the current mapping gap. Preserve powdered source context and append provenance clarification during authorized owner curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/aminithiophilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch025/247/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/247/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml:1:id: CultureMech:001636<br>./data/normalized_yaml/bacterial/aminithiophilus_medium.yaml:1:id: CultureMech:001636<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/247/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 54 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/247/evidence-context-original.json; Complete frozen target/owners, source stages, exact secondary lookup and ignored-inclusive relationships | context_only | Full captured records re-read and compared by exact equality with fresh inspected records. Context is supporting provenance; exact bound primary/provider captures independently support scientific claims. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf; Pages 1–3: explicit final volume, A–F assembly, all stock tables, main procedure and DSM 117064 branch | supports | Primary base final volume is explicitly 1008 mL. Six receiving amounts sum to that number; stock compositions and their receiving doses remain separate. The DSM 117064 modification is a source-only branch, not the base recipe or a growth assertion. |
| provider | https://mediadive.dsmz.de/rest/medium/503f; data.medium and all ten solutions: 1088–1094,595,777,5980 | supports | Provider declares the same base final volume and stage graph. Existing local values correspond to its separate A, B, D, E, F and nested stock g_l fields, not the complete 1008 mL medium. Provider HCl g_l=2.5 does not establish the missing percentage basis. |
| seven-vitamin-dependency | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf; Solution D and Seven vitamins solution only | supports | Only solution D and its named seven-vitamin stock are transferred by the explicit DSM 117064 cross-reference. Parent basal medium and other DSM 503 branches are excluded. |
| ferrous-dependency | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf; Solution F and Ferrous chloride solution subsection only | supports | Only solution F, its ferrous chloride stock and stock pH instruction are transferred by the explicit cross-reference. Parent medium and other stock recipes are not added to this branch. |
| seven-vitamin-provider | https://mediadive.dsmz.de/rest/solution/1038; data.recipe complete eight rows | supports | Exact stock 1038 contains seven vitamin solutes and water. Compound names and forms, including unqualified calcium pantothenate and thiamine hydrochloride dihydrate, are retained separately from base stock 5980. |
| ferrous-provider | https://mediadive.dsmz.de/rest/solution/1885; data.recipe and steps | supports | Exact stock 1885 specifies ferrous chloride tetrahydrate0.52 g and water 10 mL with adjustment to pH2. Its5.2% name does not independently establish a percent basis or measured final volume. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch025/247/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:131361 resolves to canonical disodium selenite pentahydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:15940 resolves to canonical nicotinic acid; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:15956 resolves to canonical biotin; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:16494 resolves to canonical lipoic acid; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:17015 resolves to canonical riboflavin; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:176843 resolves to canonical vitamin B12; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:17883 resolves to canonical hydrogen chloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:26710 resolves to canonical sodium chloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:26833 resolves to canonical sulfur atom; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:27470 resolves to canonical folic acid; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:29377 resolves to canonical sodium carbonate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:30753 resolves to canonical 4-aminobenzoic acid; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:30961 resolves to canonical pyridoxine hydrochloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:31206 resolves to canonical ammonium chloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:31345 resolves to canonical Calcium pantothenate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:32145 resolves to canonical sodium hydroxide; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:32588 resolves to canonical potassium chloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:33118 resolves to canonical boric acid; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:34887 resolves to canonical nickel dichloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:49105 resolves to canonical thiamine hydrochloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:49976 resolves to canonical zinc dichloride; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:53503 resolves to canonical cobalt chloride hexahydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:63036 resolves to canonical potassium dihydrogen phosphate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:63939 resolves to canonical sodium tungstate dihydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:75213 resolves to canonical sodium molybdate dihydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:76209 resolves to canonical sodium sulfide nonahydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:86158 resolves to canonical calcium chloride dihydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:86249 resolves to canonical iron dichloride tetrahydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:86318 resolves to canonical copper(II) chloride dihydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:86345 resolves to canonical magnesium dichloride hexahydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:86368 resolves to canonical manganese(II) chloride tetrahydrate; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact obo_id, label, definition, synonyms, formula and stereochemical metadata | supports | CHEBI:8806 resolves to canonical Resazurin; this verifies metadata, not all source-form equivalence. Source-specific forms are assessed separately. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Full exact-key scan of pinned index; adjacent source commit and hash | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833": [], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/aminithiophilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml", "events": 10, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Only exact per-record bound captures are used. Current collection and provider differences do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently establish a measured final mixture volume. No density, percent basis, exact hydration, default sterilization cycle or stock volume is invented.
- All required current primary/provider and named dependency checks completed. No historical legacy-secondary assertion requires unavailable correspondence; the completed sulfur current-index negative result is not a reason for partial coverage. Source-only branch final volume, HCl percentage basis and unspecified sterilization cycles remain explicit scientific limits.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143438Z-culturemech-001636-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aminithiophilus_medium (CultureMech:001636)'
started_at: '2026-10-21T14:22:43Z'
finished_at: '2026-10-21T14:34:38Z'
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
summary: DSMZ 503f explicitly assembles six stages into a 1008 mL base medium. Both
  local layers instead flatten stage and stock concentrations into 34 main ingredients,
  including unsupported HCl mass conversion from an unqualified percentage. The retained
  main procedure and pH range are useful, but stock scope and source-only DSM 117064
  modifications must remain distinct. Nickel/resazurin forms and one current secondary
  mapping gap need follow-up; all required current source checks are available.
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
  - path: data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
    sha256: 8b147f23df3bd5e4d351d85d930e20fb5dc55b335c168cc334930de138cbddec
    role: target
  - path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
    sha256: 18a192a332fe94909766099f07a27200f1af06ae03531aae79049dc679fa167b
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
  selection: Task review 247; batch 025 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-four task batches
    contain 240 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 243 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001636
targets:
- target_id: CultureMech:001636
  path: data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  label: aminithiophilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch025/247/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/247/strict.tsv"
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001636
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
  - CultureMech:001636
- check_id: current-secondary-exact-lookup
  name: Completed exact current secondary-key lookup
  required: true
  status: passed
  summary: The full pinned index scan completed. CHEBI:26833 has no exact mapped preferred-term
    row; this confirmed current mapping gap is a finding, not an unavailable check.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - mim
  - chebi26833
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:41.973097Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch025/247/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:43.917367Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/247/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:46.618731Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:47.915433Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:34:37Z'
  support: supports
  summary: './data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml:1:id: CultureMech:001636

    ./data/normalized_yaml/bacterial/aminithiophilus_medium.yaml:1:id: CultureMech:001636

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/247/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:34:37Z'
  support: supports
  summary: 54 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 98411c6b1410861f966bdee60b8736d42f2c1b8d2059a74b99f23b811b5352e8
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/247/evidence-context-original.json
  locator: Complete frozen target/owners, source stages, exact secondary lookup and
    ignored-inclusive relationships
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Full captured records re-read and compared by exact equality with fresh
    inspected records. Context is supporting provenance; exact bound primary/provider
    captures independently support scientific claims.
  snapshot_sha256: ecb76bc45bb0ec86e75fd46d60529ae7f07ce63d9c890a4754b2b6405edd33e9
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf
  locator: 'Pages 1–3: explicit final volume, A–F assembly, all stock tables, main
    procedure and DSM 117064 branch'
  accessed_at: '2026-10-21T14:01:45.812678Z'
  support: supports
  summary: Primary base final volume is explicitly 1008 mL. Six receiving amounts
    sum to that number; stock compositions and their receiving doses remain separate.
    The DSM 117064 modification is a source-only branch, not the base recipe or a
    growth assertion.
  snapshot_sha256: 135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/503f
  locator: 'data.medium and all ten solutions: 1088–1094,595,777,5980'
  accessed_at: '2026-10-21T14:01:43.148721Z'
  support: supports
  summary: Provider declares the same base final volume and stage graph. Existing
    local values correspond to its separate A, B, D, E, F and nested stock g_l fields,
    not the complete 1008 mL medium. Provider HCl g_l=2.5 does not establish the missing
    percentage basis.
  snapshot_sha256: ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7
- evidence_id: seven-vitamin-dependency
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf
  locator: Solution D and Seven vitamins solution only
  accessed_at: '2026-10-21T14:02:49.283551Z'
  support: supports
  summary: Only solution D and its named seven-vitamin stock are transferred by the
    explicit DSM 117064 cross-reference. Parent basal medium and other DSM 503 branches
    are excluded.
  snapshot_sha256: 2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa
- evidence_id: ferrous-dependency
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf
  locator: Solution F and Ferrous chloride solution subsection only
  accessed_at: '2026-10-21T14:02:49.294153Z'
  support: supports
  summary: Only solution F, its ferrous chloride stock and stock pH instruction are
    transferred by the explicit cross-reference. Parent medium and other stock recipes
    are not added to this branch.
  snapshot_sha256: 1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323
- evidence_id: seven-vitamin-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1038
  locator: data.recipe complete eight rows
  accessed_at: '2026-10-21T14:03:59.147423Z'
  support: supports
  summary: Exact stock 1038 contains seven vitamin solutes and water. Compound names
    and forms, including unqualified calcium pantothenate and thiamine hydrochloride
    dihydrate, are retained separately from base stock 5980.
  snapshot_sha256: d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa
- evidence_id: ferrous-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1885
  locator: data.recipe and steps
  accessed_at: '2026-10-21T14:03:59.147620Z'
  support: supports
  summary: Exact stock 1885 specifies ferrous chloride tetrahydrate0.52 g and water
    10 mL with adjustment to pH2. Its5.2% name does not independently establish a
    percent basis or measured final volume.
  snapshot_sha256: 87acf0e8ad2a475568f87f4dad2d241eaf3cb9d7dcaad412929b867cc85ceaab
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/247/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 1c4e43e8e2b795141be76d0889469f24170835913bd80210dac2dd6499aa2faf
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: CHEBI:131361 resolves to canonical disodium selenite pentahydrate; this
    verifies metadata, not all source-form equivalence. Source-specific forms are
    assessed separately.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to canonical nicotinic acid; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to canonical biotin; this verifies metadata, not all
    source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to canonical lipoic acid; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to canonical riboflavin; this verifies metadata, not
    all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to canonical vitamin B12; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to canonical hydrogen chloride; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to canonical sodium chloride; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi26833
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:04.114839Z'
  support: supports
  summary: CHEBI:26833 resolves to canonical sulfur atom; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to canonical folic acid; this verifies metadata, not
    all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to canonical sodium carbonate; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to canonical 4-aminobenzoic acid; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to canonical pyridoxine hydrochloride; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to canonical ammonium chloride; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to canonical Calcium pantothenate; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to canonical sodium hydroxide; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to canonical potassium chloride; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to canonical boric acid; this verifies metadata, not
    all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to canonical nickel dichloride; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to canonical thiamine hydrochloride; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to canonical zinc dichloride; this verifies metadata,
    not all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to canonical cobalt chloride hexahydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to canonical potassium dihydrogen phosphate; this
    verifies metadata, not all source-form equivalence. Source-specific forms are
    assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to canonical sodium tungstate dihydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to canonical sodium molybdate dihydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to canonical sodium sulfide nonahydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to canonical calcium chloride dihydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to canonical iron dichloride tetrahydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to canonical copper(II) chloride dihydrate; this verifies
    metadata, not all source-form equivalence. Source-specific forms are assessed
    separately.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to canonical magnesium dichloride hexahydrate; this
    verifies metadata, not all source-form equivalence. Source-specific forms are
    assessed separately.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to canonical manganese(II) chloride tetrahydrate;
    this verifies metadata, not all source-form equivalence. Source-specific forms
    are assessed separately.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact obo_id, label, definition, synonyms, formula and stereochemical metadata
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to canonical Resazurin; this verifies metadata, not
    all source-form equivalence. Source-specific forms are assessed separately.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Full exact-key scan of pinned index; adjacent source commit and hash
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label":
    "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label":
    "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term":
    "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833": [], "CHEBI:27470":
    [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470",
    "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type":
    "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label":
    "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term":
    "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl",
    "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier":
    "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
  search_scope: Entire pinned CSV parsed, including every row; no ignore-filtered
    search or fuzzy name replacement.
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/aminithiophilus_medium.yaml", "events": 10, "timestamp_issues":
    []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:37Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 83 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Solution A receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 952 mL Solution A in the base A–F assembly; all six stated doses sum\
    \ to 1008 mL.\",\n    \"rationale\": \"These are receiving volumes, not ingredient\
    \ masses or concentrations. Preserve identifiers 1089–1094 and stage order; do\
    \ not conflate similarly named stocks in another medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    solution\\\": \\\"Solution A\\\",\\n                        \\\"solution_id\\\"\
    : 1089,\\n                        \\\"amount\\\": 952,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Solution B receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 25 mL Solution B in the base A–F assembly; all six stated doses sum\
    \ to 1008 mL.\",\n    \"rationale\": \"These are receiving volumes, not ingredient\
    \ masses or concentrations. Preserve identifiers 1089–1094 and stage order; do\
    \ not conflate similarly named stocks in another medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Solution B\\\",\\n                        \\\"solution_id\\\"\
    : 1090,\\n                        \\\"amount\\\": 25,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Solution C receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1 mL Solution C in the base A–F assembly; all six stated doses sum\
    \ to 1008 mL.\",\n    \"rationale\": \"These are receiving volumes, not ingredient\
    \ masses or concentrations. Preserve identifiers 1089–1094 and stage order; do\
    \ not conflate similarly named stocks in another medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    solution\\\": \\\"Solution C\\\",\\n                        \\\"solution_id\\\"\
    : 1091,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n\
    \                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Solution D receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL Solution D in the base A–F assembly; all six stated doses sum\
    \ to 1008 mL.\",\n    \"rationale\": \"These are receiving volumes, not ingredient\
    \ masses or concentrations. Preserve identifiers 1089–1094 and stage order; do\
    \ not conflate similarly named stocks in another medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    solution\\\": \\\"Solution D\\\",\\n                        \\\"solution_id\\\"\
    : 1092,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Solution E receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL Solution E in the base A–F assembly; all six stated doses sum\
    \ to 1008 mL.\",\n    \"rationale\": \"These are receiving volumes, not ingredient\
    \ masses or concentrations. Preserve identifiers 1089–1094 and stage order; do\
    \ not conflate similarly named stocks in another medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    solution\\\": \\\"Solution E\\\",\\n                        \\\"solution_id\\\"\
    : 1093,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Solution F receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL Solution F in the base A–F assembly; all six stated doses sum\
    \ to 1008 mL.\",\n    \"rationale\": \"These are receiving volumes, not ingredient\
    \ masses or concentrations. Preserve identifiers 1089–1094 and stage order; do\
    \ not conflate similarly named stocks in another medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Solution F\\\",\\n                        \\\"solution_id\\\"\
    : 1094,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Solution A: KH2PO4\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.210084\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.210084\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.2 g within Solution A. The entire stated stage amount is used in\
    \ the base, so contribution=0.2/1.008=0.198412698413 g/L. Existing provider-derived\
    \ 0.210084 g/L is stage strength, not final medium.\",\n    \"rationale\": \"\
    Restore the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.210084,\\n           \
    \             \\\"mmol_l\\\": 1.54377,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Solution A: NH4Cl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.262605\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.262605\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.25 g within Solution A. The entire stated stage amount is used in\
    \ the base, so contribution=0.25/1.008=0.248015873016 g/L. Existing provider-derived\
    \ 0.262605 g/L is stage strength, not final medium.\",\n    \"rationale\": \"\
    Restore the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 0.25,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.262605,\\n     \
    \                   \\\"mmol_l\\\": 4.90942,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Solution A: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2521\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"5.2521\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 5 g within Solution A. The entire stated stage amount is used in the\
    \ base, so contribution=5/1.008=4.96031746032 g/L. Existing provider-derived 5.2521\
    \ g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore the\
    \ exact named stage, original source amount and unit, water and receiving dose;\
    \ source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 5.2521,\\n             \
    \           \\\"mmol_l\\\": 89.8717,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Solution A: MgCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.420168\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.420168\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.4 g within Solution A. The entire stated stage amount is used in\
    \ the base, so contribution=0.4/1.008=0.396825396825 g/L. Existing provider-derived\
    \ 0.420168 g/L is stage strength, not final medium.\",\n    \"rationale\": \"\
    Restore the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.4,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.420168,\\\
    n                        \\\"mmol_l\\\": 2.06671,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Solution A: KCl\",\n    \"decision\": \"correct\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.52521\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.52521\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.5 g within Solution A. The entire stated stage amount is used in\
    \ the base, so contribution=0.5/1.008=0.496031746032 g/L. Existing provider-derived\
    \ 0.52521 g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.52521,\\n            \
    \            \\\"mmol_l\\\": 7.04507,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Solution A: CaCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.157563\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.157563\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.15 g within Solution A. The entire stated stage amount is used in\
    \ the base, so contribution=0.15/1.008=0.14880952381 g/L. Existing provider-derived\
    \ 0.157563 g/L is stage strength, not final medium.\",\n    \"rationale\": \"\
    Restore the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.15,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.157563,\\\
    n                        \\\"mmol_l\\\": 1.07175,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Solution A: Trace element solution SL-10\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Within Solution A, retain 1 ml of Trace element solution SL-10, exact solution\
    \ 595.\",\n    \"rationale\": \"Restore the exact named stage, original source\
    \ amount and unit, water and receiving dose; source-only quantities have no current\
    \ local numeric assertion. No attached amount evidence is present in either layer.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"solution\\\": \\\"Trace element solution SL-10\\\",\\n            \
    \            \\\"solution_id\\\": 595,\\n                        \\\"amount\\\"\
    : 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Solution A: Selenite-tungstate solution\",\n    \"decision\": \"add\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Within Solution A, retain 1 ml of Selenite-tungstate solution, exact solution\
    \ 777.\",\n    \"rationale\": \"Restore the exact named stage, original source\
    \ amount and unit, water and receiving dose; source-only quantities have no current\
    \ local numeric assertion. No attached amount evidence is present in either layer.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"solution\\\": \\\"Selenite-tungstate solution\\\",\\n             \
    \           \\\"solution_id\\\": 777,\\n                        \\\"amount\\\"\
    : 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Solution A: Sulfur\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.5042\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"10.5042\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 g within Solution A. The entire stated stage amount is used in the\
    \ base, so contribution=10/1.008=9.92063492063 g/L. Existing provider-derived\
    \ 10.5042 g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer. Preserve powdered sulfur. An atom-level\
    \ canonical label with elemental-sulfur synonym is not proof of an incorrect allotrope;\
    \ current secondary lookup is assessed separately.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\": 80,\\\
    n                        \\\"condition\\\": \\\"\\\",\\n                     \
    \   \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"amount\\\
    \": 10,\\n                        \\\"unit\\\": \\\"g\\\",\\n                \
    \        \\\"g_l\\\": 10.5042,\\n                        \\\"mmol_l\\\": 327.54,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Solution A: Sodium resazurin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00052521\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.00052521\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.50 mL sodium-resazurin stock 0.1% w/v in solution A. It contributes\
    \ 0.0005 g to the explicit 1008 mL base medium, or 0.000496031746032 g/L; existing\
    \ 0.00052521 g/L is A-stage normalization.\",\n    \"rationale\": \"Restore the\
    \ exact named stage, original source amount and unit, water and receiving dose;\
    \ source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.00052521,\\n        \
    \                \\\"mmol_l\\\": 0.00209105,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Solution A: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 950 mL water within Solution A; water volume is not a g/L solute or\
    \ independent final-volume proof.\",\n    \"rationale\": \"Restore the exact named\
    \ stage, original source amount and unit, water and receiving dose; source-only\
    \ quantities have no current local numeric assertion. No attached amount evidence\
    \ is present in either layer.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 950,\\n                        \\\"unit\\\": \\\"ml\\\",\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Solution B: Na2CO3\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1.25 g within Solution B. The entire stated stage amount is used in\
    \ the base, so contribution=1.25/1.008=1.24007936508 g/L. Existing provider-derived\
    \ 50 g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"amount\\\": 1.25,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 50,\\n           \
    \             \\\"mmol_l\\\": 471.752,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Solution B: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 25 mL water within Solution B; water volume is not a g/L solute or\
    \ independent final-volume proof.\",\n    \"rationale\": \"Restore the exact named\
    \ stage, original source amount and unit, water and receiving dose; source-only\
    \ quantities have no current local numeric assertion. No attached amount evidence\
    \ is present in either layer.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 25,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Solution C: Wolin's vitamin solution (10x)\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Within Solution C, retain 1 ml of Wolin's vitamin solution (10x), exact solution\
    \ 5980. This is 1 mL stock 5980 through solution C; the outer 1 mL receiving dose\
    \ is the same stock portion, not another 1/1000 dilution.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Solution D: Casamino acids\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 2 g within Solution D. The entire stated stage amount is used in the\
    \ base, so contribution=2/1.008=1.98412698413 g/L. Existing provider-derived 200\
    \ g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore the\
    \ exact named stage, original source amount and unit, water and receiving dose;\
    \ source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Casamino acids\\\",\\n                        \\\"compound_id\\\
    \": 101,\\n                        \\\"amount\\\": 2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 200,\\n  \
    \                      \\\"optional\\\": 0\\n                    }\",\n      \
    \  \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Solution D: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL water within Solution D; water volume is not a g/L solute or\
    \ independent final-volume proof.\",\n    \"rationale\": \"Restore the exact named\
    \ stage, original source amount and unit, water and receiving dose; source-only\
    \ quantities have no current local numeric assertion. No attached amount evidence\
    \ is present in either layer.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[4].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 10,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Solution E: Yeast extract\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.2 g within Solution E. The entire stated stage amount is used in\
    \ the base, so contribution=0.2/1.008=0.198412698413 g/L. Existing provider-derived\
    \ 20 g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n  \
    \                      \\\"optional\\\": 0\\n                    }\",\n      \
    \  \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Solution E: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL water within Solution E; water volume is not a g/L solute or\
    \ independent final-volume proof.\",\n    \"rationale\": \"Restore the exact named\
    \ stage, original source amount and unit, water and receiving dose; source-only\
    \ quantities have no current local numeric assertion. No attached amount evidence\
    \ is present in either layer.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 10,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Solution F: Na2S x 9 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.3 g within Solution F. The entire stated stage amount is used in\
    \ the base, so contribution=0.3/1.008=0.297619047619 g/L. Existing provider-derived\
    \ 30 g/L is stage strength, not final medium.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\n  \
    \                      \\\"mmol_l\\\": 124.905,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Solution F: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL water within Solution F; water volume is not a g/L solute or\
    \ independent final-volume proof.\",\n    \"rationale\": \"Restore the exact named\
    \ stage, original source amount and unit, water and receiving dose; source-only\
    \ quantities have no current local numeric assertion. No attached amount evidence\
    \ is present in either layer.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 10,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: HCl\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 10 mL HCl labeled 25% in SL-10, which is explicitly made up to 1000\
    \ mL. Percentage basis and density are not supplied; neither 2.5 g/L stock nor\
    \ its final mass contribution is established.\",\n    \"rationale\": \"The provider\
    \ g_l field and local 2.5 g/L are insufficient to repair this unit ambiguity.\
    \ Decision correct means restore the supported original stock-volume/label representation\
    \ and remove the unsupported mass assertion; no numerical mass replacement is\
    \ proposed.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"HCl\\\",\\n                   \
    \     \\\"compound_id\\\": 68,\\n                        \\\"attribute\\\": \\\
    \"25%\\\",\\n                        \\\"amount\\\": 10,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 2.5,\\\
    n                        \\\"mmol_l\\\": 68.5683,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: FeCl2 x 4 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1.5 g in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=1.5 g/L stock×0.001 L/1.008\
    \ L=0.0014880952381 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"FeCl2 x 4 H2O\\\",\\n                        \\\"\
    compound_id\\\": 260,\\n                        \\\"amount\\\": 1.5,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 1.5,\\n                        \\\"mmol_l\\\": 7.54482,\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: ZnCl2\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 70 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.07 g/L stock×0.001 L/1.008\
    \ L=6.94444444444e-05 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"ZnCl2\\\",\\n                        \\\"compound_id\\\
    \": 64,\\n                        \\\"amount\\\": 70,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.07,\\n\
    \                        \\\"mmol_l\\\": 0.513573,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 100 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.1 g/L stock×0.001 L/1.008\
    \ L=9.92063492063e-05 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"\
    compound_id\\\": 36,\\n                        \\\"amount\\\": 100,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.505293,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: H3BO3\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 6 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.006 g/L stock×0.001 L/1.008\
    \ L=5.95238095238e-06 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\
    \": 37,\\n                        \\\"amount\\\": 6,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.006,\\n\
    \                        \\\"mmol_l\\\": 0.0970246,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 190 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.19 g/L stock×0.001 L/1.008\
    \ L=0.000188492063492 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 38,\\n                        \\\"amount\\\": 190,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.19,\\n                        \\\"mmol_l\\\": 1.46335,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: CuCl2 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 2 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.002 g/L stock×0.001 L/1.008\
    \ L=1.98412698413e-06 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 39,\\n                        \\\"amount\\\": 2,\\n         \
    \               \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\"\
    : 0.002,\\n                        \\\"mmol_l\\\": 0.0117314,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: NiCl2 x 6 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 24 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.024 g/L stock×0.001 L/1.008\
    \ L=2.38095238095e-05 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 40,\\n                        \\\"amount\\\": 24,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.024,\\n                        \\\"mmol_l\\\": 0.185187,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 36 mg in Trace element solution SL-10, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.036000000000000004 g/L\
    \ stock×0.001 L/1.008 L=3.57142857143e-05 g/L base; retain stock formula separately.\"\
    ,\n    \"rationale\": \"Restore the exact named stage, original source amount\
    \ and unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 9,\\n                        \\\"amount\\\
    \": 36,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.036,\\n                        \\\"mmol_l\\\": 0.148791,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Trace element solution SL-10: Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 990 mL water within Trace element solution SL-10; water volume is not\
    \ a g/L solute or independent final-volume proof.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 990,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"Selenite-tungstate solution: NaOH\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.5 g in Selenite-tungstate solution, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.5 g/L stock×0.001 L/1.008\
    \ L=0.000496031746032 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[8].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"NaOH\\\",\\n                        \\\"compound_id\\\
    \": 256,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n\
    \                        \\\"mmol_l\\\": 12.5009,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"Selenite-tungstate solution: Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[22].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 3 mg in Selenite-tungstate solution, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.003 g/L stock×0.001 L/1.008\
    \ L=2.97619047619e-06 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[8].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\
    \"compound_id\\\": 107,\\n                        \\\"amount\\\": 3,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.003,\\n                        \\\"mmol_l\\\": 0.0114062,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Selenite-tungstate solution: Na2WO4 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 4 mg in Selenite-tungstate solution, provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.004 g/L stock×0.001 L/1.008\
    \ L=3.96825396825e-06 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[8].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 249,\\n                        \\\"amount\\\": 4,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.004,\\n                        \\\"mmol_l\\\": 0.0121267,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\": \"\
    Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Selenite-tungstate solution: Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1000 mL water within Selenite-tungstate solution; water volume is not\
    \ a g/L solute or independent final-volume proof.\",\n    \"rationale\": \"Restore\
    \ the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[8].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Biotin\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[24].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 20 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.02 g/L stock×0.001\
    \ L/1.008 L=1.98412698413e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Biotin\\\",\\n                \
    \        \\\"compound_id\\\": 46,\\n                        \\\"amount\\\": 20,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.0818632,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Folic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 20 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.02 g/L stock×0.001\
    \ L/1.008 L=1.98412698413e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Folic acid\\\",\\n            \
    \            \\\"compound_id\\\": 138,\\n                        \\\"amount\\\"\
    : 20,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.0453104,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Pyridoxine hydrochloride\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 100 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.1 g/L stock×0.001\
    \ L/1.008 L=9.92063492063e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"Pyridoxine hydrochloride\\\",\\\
    n                        \\\"compound_id\\\": 519,\\n                        \\\
    \"amount\\\": 100,\\n                        \\\"unit\\\": \\\"mg\\\",\\n    \
    \                    \\\"g_l\\\": 0.1,\\n                        \\\"mmol_l\\\"\
    : 0.486287,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Thiamine HCl\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[27].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001\
    \ L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"Thiamine HCl\\\",\\n          \
    \              \\\"compound_id\\\": 1207,\\n                        \\\"amount\\\
    \": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.148236,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Riboflavin\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[28].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001\
    \ L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Riboflavin\\\",\\n            \
    \            \\\"compound_id\\\": 136,\\n                        \\\"amount\\\"\
    : 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.132837,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Nicotinic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[29].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001\
    \ L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"Nicotinic acid\\\",\\n        \
    \                \\\"compound_id\\\": 139,\\n                        \\\"amount\\\
    \": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.406141,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q47\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Calcium D-(+)-pantothenate\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[30].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001\
    \ L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims. Base source explicitly specifies Calcium D-(+)-pantothenate; asserted\
    \ CHEBI:31345 has D synonyms and stereospecific structure. Do not transfer the\
    \ branch seven-vitamin stock’s less-specific calcium name to this base assertion.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[9].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Calcium D-(+)-pantothenate\\\",\\n              \
    \          \\\"compound_id\\\": 1512,\\n                        \\\"amount\\\"\
    : 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.209846,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q48\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Vitamin B12\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[31].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL stock.\
    \ With the explicitly named1 mL transfer, contribution=0.001 g/L stock×0.001 L/1.008\
    \ L=9.92063492063e-07 g/L base; retain stock formula separately.\",\n    \"rationale\"\
    : \"Restore the exact named stage, original source amount and unit, water and\
    \ receiving dose; source-only quantities have no current local numeric assertion.\
    \ No attached amount evidence is present in either layer. SL-10 has an explicit\
    \ final make-up volume; the selenite and vitamin stocks have listed water 1000\
    \ mL and provider volume 1000 mL, so their calculated concentrations are explicitly\
    \ provider-basis calculations, not independent measured-volume claims.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503fapi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n \
    \       \"source_locator\": \"$.data.solutions[9].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.001,\\n\
    \                        \\\"mmol_l\\\": 0.00073779,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q49\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): p-Aminobenzoic acid\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[32].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001\
    \ L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"p-Aminobenzoic acid\\\",\\n   \
    \                     \\\"compound_id\\\": 47,\\n                        \\\"\
    amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n       \
    \                 \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\"\
    : 0.364591,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q50\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): (DL)-alpha-Lipoic acid\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\",\n        \"\
    field_path\": \"ingredients[33].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 50 mg in Wolin's vitamin solution (10x), provider-declared 1000 mL\
    \ stock. With the explicitly named1 mL transfer, contribution=0.05 g/L stock×0.001\
    \ L/1.008 L=4.96031746032e-05 g/L base; retain stock formula separately.\",\n\
    \    \"rationale\": \"Restore the exact named stage, original source amount and\
    \ unit, water and receiving dose; source-only quantities have no current local\
    \ numeric assertion. No attached amount evidence is present in either layer. SL-10\
    \ has an explicit final make-up volume; the selenite and vitamin stocks have listed\
    \ water 1000 mL and provider volume 1000 mL, so their calculated concentrations\
    \ are explicitly provider-basis calculations, not independent measured-volume\
    \ claims. Preserve DL in the source name; generic lipoic acid CHEBI:16494 is not\
    \ an asserted R-only replacement.\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"(DL)-alpha-Lipoic acid\\\",\\n\
    \                        \\\"compound_id\\\": 252,\\n                        \\\
    \"amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n     \
    \                   \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\"\
    : 0.24233,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q51\",\n    \"component_or_context\"\
    : \"Wolin's vitamin solution (10x): Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1000 mL water within Wolin's vitamin solution (10x); water volume is\
    \ not a g/L solute or independent final-volume proof.\",\n    \"rationale\": \"\
    Restore the exact named stage, original source amount and unit, water and receiving\
    \ dose; source-only quantities have no current local numeric assertion. No attached\
    \ amount evidence is present in either layer.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q52\",\n    \"component_or_context\"\
    : \"Base final volume\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve compounds of solution A except sulfur\
    \ and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials containing the appropriate amount of sulfur and autoclave at\
    \ <b>110°C </b>for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration.\
    \ Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium\
    \ appropriate amounts of solutions B to F are added to the sterile solution A\
    \ in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if\
    \ necessary.\"\n          },\n          {\n            \"step_number\": 2,\n \
    \           \"action\": \"DISSOLVE\",\n            \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve compounds of solution A except sulfur\
    \ and sparge it with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Distribute under the same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials containing the appropriate amount of sulfur and autoclave at\
    \ <b>110°C </b>for 20 min. Solution B is autoclaved under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solution C is prepared under 100% N2 gas and sterilized by filtration.\
    \ Solutions D, E, and F are autoclaved under 100% N2 gas. To complete the medium\
    \ appropriate amounts of solutions B to F are added to the sterile solution A\
    \ in the sequence as indicated. Adjust pH of complete medium to 7.2 - 7.4, if\
    \ necessary.\"\n          },\n          {\n            \"step_number\": 2,\n \
    \           \"action\": \"DISSOLVE\",\n            \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain explicit\
    \ 1008 mL final base volume, matching 952+25+1+10+10+10 mL assembly.\",\n    \"\
    rationale\": \"The primary gives this denominator directly; do not replace it\
    \ with 1000 mL or apply it to the modified strain branch without a separate branch\
    \ statement.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1008 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    solution\\\": \\\"Solution A\\\",\\n                        \\\"solution_id\\\"\
    : 1089,\\n                        \\\"amount\\\": 952,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Solution B\\\",\\n                        \\\"solution_id\\\"\
    : 1090,\\n                        \\\"amount\\\": 25,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    solution\\\": \\\"Solution C\\\",\\n                        \\\"solution_id\\\"\
    : 1091,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n\
    \                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    solution\\\": \\\"Solution D\\\",\\n                        \\\"solution_id\\\"\
    : 1092,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    solution\\\": \\\"Solution E\\\",\\n                        \\\"solution_id\\\"\
    : 1093,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Solution F\\\",\\n                        \\\"solution_id\\\"\
    : 1094,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q53\",\n    \"component_or_context\"\
    : \"Solution A stated receiving volume versus liquid entries\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain stated A dose 952 mL and water 950 mL. Its listed liquid inputs total\
    \ 950+1+1+0.50=952.5 mL; the 0.5 mL discrepancy remains explicit.\",\n    \"rationale\"\
    : \"Do not invent a corrected 952.5 mL A dose or override the explicit 1008 mL\
    \ final base volume. Source quantities are preserved separately from an independently\
    \ measured assembled volume.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"solution\\\": \\\"Solution A\\\",\\n            \
    \            \\\"solution_id\\\": 1089,\\n                        \\\"amount\\\
    \": 952,\\n                        \\\"unit\\\": \\\"ml\\\",\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-10\\\",\\n                       \
    \ \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n  \
    \                      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.00052521,\\n        \
    \                \\\"mmol_l\\\": 0.00209105,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503fapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 950,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q54\",\n    \"component_or_context\"\
    : \"Sodium-resazurin stock strength\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.1% w/v = 1 g/L sodium-resazurin stock, delivered 0.50 mL.\",\n    \"rationale\"\
    : \"The percentage basis is explicit; source sodium salt identity is separately\
    \ reviewed. Do not use the free-acid molecular mass.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n       \
    \ \"source_locator\": \"Page1 Solution A\",\n        \"exact_source_quote\": \"\
    Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q55\",\n    \"component_or_context\"\
    : \"SL-10 final make-up volume\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Make SL-10 up to\
    \ 1000 mL after dissolving iron in HCl and then adding water and remaining salts.\"\
    ,\n    \"rationale\": \"This quantity is retained at the current main preparation\
    \ root; correct its stock scope rather than treating it as absent. It is not the\
    \ 1008 mL receiving-medium final volume.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503fapi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503f\",\n        \"source_locator\": \"\
    $.data.solutions[7].steps[0].step\",\n        \"exact_source_quote\": \"Finally\
    \ make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"ab10e0bed27ed8fc4a0303112fcf53fe33fa2c9985ffee693e0c103a4d3d8aa7\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q56\",\n    \"component_or_context\"\
    : \"SL-10 HCl percentage basis\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve25% as an unqualified source label and 10 mL as stock preparation\
    \ volume.\",\n    \"rationale\": \"No mass/volume or mass/mass basis or density\
    \ is established. Neither molecular identity HCl nor the provider calculated2.5\
    \ g/L establishes the missing basis.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page2 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q57\",\n    \"component_or_context\"\
    : \"Main A/B gas fractions\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 80% nitrogen/20% carbon dioxide for solution A preparation and dispensing\
    \ and B autoclaving.\",\n    \"rationale\": \"Existing main prose carries the\
    \ source quantity but has no attached evidence. Strip literal HTML markup only\
    \ during separately authorized owner curation; preserve quantities, gas and stage\
    \ semantics.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"80% N2 and 20% CO2\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q58\",\n    \"component_or_context\"\
    : \"Main A sparging duration\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 30–45 min for A sparging, before sulfur-containing receiving vessels.\"\
    ,\n    \"rationale\": \"Existing main prose carries the source quantity but has\
    \ no attached evidence. Strip literal HTML markup only during separately authorized\
    \ owner curation; preserve quantities, gas and stage semantics.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n       \
    \ \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"30 - 45 min\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q59\",\n    \"component_or_context\"\
    : \"Main A autoclave temperature\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 110°C for solution A; the source does not state this as a universal\
    \ cycle for every stock.\",\n    \"rationale\": \"Existing main prose carries\
    \ the source quantity but has no attached evidence. Strip literal HTML markup\
    \ only during separately authorized owner curation; preserve quantities, gas and\
    \ stage semantics.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"110°C\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q60\",\n    \"component_or_context\"\
    : \"Main A autoclave duration\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 20 min for A sterilization; do not transfer to B–F without explicit\
    \ support.\",\n    \"rationale\": \"Existing main prose carries the source quantity\
    \ but has no attached evidence. Strip literal HTML markup only during separately\
    \ authorized owner curation; preserve quantities, gas and stage semantics.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz503f\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"for 20 min\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q61\",\n    \"component_or_context\"\
    : \"C/D/E/F nitrogen proportion\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 100% nitrogen for C preparation/filter sterilization and D/E/F autoclaving.\"\
    ,\n    \"rationale\": \"Existing main prose carries the source quantity but has\
    \ no attached evidence. Strip literal HTML markup only during separately authorized\
    \ owner curation; preserve quantities, gas and stage semantics.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n       \
    \ \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"100% N2\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q62\",\n    \"component_or_context\"\
    : \"Complete base pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.2,\n          \"max\": 7.4\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.2,\n          \"max\": 7.4\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Retain base complete-medium\
    \ pH 7.2–7.4, adjusted if necessary; existing ph_range and main prose agree.\"\
    ,\n    \"rationale\": \"Existing main prose carries the source quantity but has\
    \ no attached evidence. Strip literal HTML markup only during separately authorized\
    \ owner curation; preserve quantities, gas and stage semantics.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n       \
    \ \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"7.2 - 7.4\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q63\",\n    \"component_or_context\"\
    : \"B–F unreported sterilization cycle\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve compounds of solution A except sulfur and sparge it with 80% N2 and\
    \ 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Distribute under the\
    \ same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ the appropriate amount of sulfur and autoclave at <b>110°C </b>for 20 min. Solution\
    \ B is autoclaved under 80% N2 and 20% CO2 gas atmosphere. Solution C is prepared\
    \ under 100% N2 gas and sterilized by filtration. Solutions D, E, and F are autoclaved\
    \ under 100% N2 gas. To complete the medium appropriate amounts of solutions B\
    \ to F are added to the sterile solution A in the sequence as indicated. Adjust\
    \ pH of complete medium to 7.2 - 7.4, if necessary.\",\n        \"decision\":\
    \ \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"C is filtered; B and D–F are autoclaved in their specified atmospheres. Their\
    \ time/temperature values are not supplied.\",\n    \"rationale\": \"The only\
    \ explicit 110°C/20 min cycle belongs to A. Do not infer other cycles or filtration\
    \ pore size.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"Solution C is prepared under 100% N2 gas and sterilized by filtration.\",\n\
    \        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 main preparation\",\n        \"exact_source_quote\"\
    : \"Solutions D, E, and F are autoclaved under 100% N2 gas.\",\n        \"snapshot_sha256\"\
    : \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\",\n    \
    \    \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q64\",\n    \"component_or_context\"\
    : \"Branch exclusions\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For DSM 117064 only, omit base C, D, E and F; do not mix their vitamin/casamino/yeast/sulfide\
    \ stocks with the replacement branch.\",\n    \"rationale\": \"This source-only\
    \ branch is not currently asserted in either local layer. If represented during\
    \ authorized curation, retain it as a distinct conditional variant, never as a\
    \ correction to the base or a new organism growth assertion. No measured branch\
    \ final volume is inferred.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q65\",\n    \"component_or_context\"\
    : \"Branch solution B dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For DSM 117064 only, increase B to 50 mL.\",\n    \"rationale\": \"This source-only\
    \ branch is not currently asserted in either local layer. If represented during\
    \ authorized curation, retain it as a distinct conditional variant, never as a\
    \ correction to the base or a new organism growth assertion. No measured branch\
    \ final volume is inferred.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q66\",\n    \"component_or_context\"\
    : \"Branch literal carbonate concentration\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain the source parenthetical 2.50 g/L Na2CO3 exactly as a branch assertion.\
    \ B stock 50 g/L × 50 mL supplies 2.50 g, but the source supplies no explicit\
    \ modified final volume; do not silently derive a new g/L or use the base 1008\
    \ mL denominator.\",\n    \"rationale\": \"This source-only branch is not currently\
    \ asserted in either local layer. If represented during authorized curation, retain\
    \ it as a distinct conditional variant, never as a correction to the base or a\
    \ new organism growth assertion. No measured branch final volume is inferred.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz503f\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q67\",\n    \"component_or_context\"\
    : \"Branch DSM 503 D dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For DSM 117064 only, add 1 mL of DSM 503 solution D, the named seven-vitamin\
    \ stock pathway.\",\n    \"rationale\": \"This source-only branch is not currently\
    \ asserted in either local layer. If represented during authorized curation, retain\
    \ it as a distinct conditional variant, never as a correction to the base or a\
    \ new organism growth assertion. No measured branch final volume is inferred.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz503f\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q68\",\n    \"component_or_context\"\
    : \"Branch DSM 916 F dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For DSM 117064 only, add 10 mL of DSM 916 solution F, the named ferrous-chloride\
    \ stock pathway.\",\n    \"rationale\": \"This source-only branch is not currently\
    \ asserted in either local layer. If represented during authorized curation, retain\
    \ it as a distinct conditional variant, never as a correction to the base or a\
    \ new organism growth assertion. No measured branch final volume is inferred.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz503f\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q69\",\n    \"component_or_context\"\
    : \"Branch pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"For DSM 117064 only, complete-medium pH 7.8–8.0; keep base pH 7.2–7.4 unchanged.\"\
    ,\n    \"rationale\": \"This source-only branch is not currently asserted in either\
    \ local layer. If represented during authorized curation, retain it as a distinct\
    \ conditional variant, never as a correction to the base or a new organism growth\
    \ assertion. No measured branch final volume is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n       \
    \ \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n        \"\
    exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q70\",\n    \"component_or_context\"\
    : \"Branch nested DSM 503 D stock transfer\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"DSM 503 D is 1 mL seven-vitamin solution1038; the branch1 mL D portion is\
    \ that same stock volume, not two successive 1/1000 dilutions.\",\n    \"rationale\"\
    : \"Only the named D dependency is followed. Parent DSM 503 main medium, other\
    \ solutions and strain contexts are excluded.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      },\n      {\n        \"source_key\": \"solution5960\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5960\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 1,\\n                \\\"compound\\\": null,\\n     \
    \           \\\"compound_id\\\": null,\\n                \\\"solution\\\": \\\"\
    Seven vitamins solution\\\",\\n                \\\"solution_id\\\": 1038,\\n \
    \               \\\"condition\\\": null,\\n                \\\"attribute\\\":\
    \ null,\\n                \\\"amount\\\": 1,\\n                \\\"unit\\\": \\\
    \"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\"\
    : null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"b7410288819afd9c77a60cfa809efc7237b24e136ab252f60c77b17e020cbcee\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf\",\n        \"\
    source_locator\": \"Solution D subsection\",\n        \"exact_source_quote\":\
    \ \"Seven vitamins solution 1.00 ml\",\n        \"snapshot_sha256\": \"2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa\"\
    ,\n        \"parsed_text_sha256\": \"89641af386bfdf38f8b9f3306d8937b22511d687ce18efed884f4dda432a49d3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q71\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: Vitamin B12\",\n    \"decision\": \"add\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 100 mg Vitamin B12 with listed water\
    \ 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this\
    \ is 0.1 mg delivered per branch batch; branch final g/L remains unresolved.\"\
    ,\n    \"rationale\": \"Keep these original branch stock forms separate from base\
    \ Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly\
    \ dihydrate. Do not assign base-specific forms or invented IDs; no target grounding\
    \ exists for these source-only branch nodes.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"solution1038\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\": \"\
    $.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n                \\\"\
    recipe_order\\\": 1,\\n                \\\"compound\\\": \\\"Vitamin B12\\\",\\\
    n                \\\"compound_id\\\": 18,\\n                \\\"solution\\\":\
    \ null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 100,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.1,\\n                \\\"mmol_l\\\": 0.073779,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q72\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: p-Aminobenzoic acid\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 80 mg p-Aminobenzoic acid with listed\
    \ water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer\
    \ this is 0.08 mg delivered per branch batch; branch final g/L remains unresolved.\"\
    ,\n    \"rationale\": \"Keep these original branch stock forms separate from base\
    \ Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly\
    \ dihydrate. Do not assign base-specific forms or invented IDs; no target grounding\
    \ exists for these source-only branch nodes.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"solution1038\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\": \"\
    $.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n                \\\"\
    recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"p-Aminobenzoic acid\\\
    \",\\n                \\\"compound_id\\\": 47,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 80,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.08,\\n                \\\"mmol_l\\\": 0.583345,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q73\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: D-(+)-biotin\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 20 mg D-(+)-biotin with listed water\
    \ 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer this\
    \ is 0.02 mg delivered per branch batch; branch final g/L remains unresolved.\"\
    ,\n    \"rationale\": \"Keep these original branch stock forms separate from base\
    \ Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly\
    \ dihydrate. Do not assign base-specific forms or invented IDs; no target grounding\
    \ exists for these source-only branch nodes.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"solution1038\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\": \"\
    $.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n                \\\"\
    recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"D-(+)-biotin\\\"\
    ,\\n                \\\"compound_id\\\": 1359,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 20,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\": 0.0818632,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q74\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: Nicotinic acid\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 200 mg Nicotinic acid with listed\
    \ water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer\
    \ this is 0.2 mg delivered per branch batch; branch final g/L remains unresolved.\"\
    ,\n    \"rationale\": \"Keep these original branch stock forms separate from base\
    \ Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly\
    \ dihydrate. Do not assign base-specific forms or invented IDs; no target grounding\
    \ exists for these source-only branch nodes.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"solution1038\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\": \"\
    $.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n                \\\"\
    recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"Nicotinic acid\\\"\
    ,\\n                \\\"compound_id\\\": 139,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 200,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\": 1.62456,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q75\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: Calcium pantothenate\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 100 mg Calcium pantothenate with listed\
    \ water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer\
    \ this is 0.1 mg delivered per branch batch; branch final g/L remains unresolved.\"\
    ,\n    \"rationale\": \"Keep these original branch stock forms separate from base\
    \ Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly\
    \ dihydrate. Do not assign base-specific forms or invented IDs; no target grounding\
    \ exists for these source-only branch nodes.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"solution1038\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\": \"\
    $.data.recipe[4]\",\n        \"exact_source_quote\": \"{\\n                \\\"\
    recipe_order\\\": 5,\\n                \\\"compound\\\": \\\"Calcium pantothenate\\\
    \",\\n                \\\"compound_id\\\": 518,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 100,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\": 0.209849,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q76\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: Pyridoxine hydrochloride\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 300 mg Pyridoxine hydrochloride with\
    \ listed water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL\
    \ transfer this is 0.3 mg delivered per branch batch; branch final g/L remains\
    \ unresolved.\",\n    \"rationale\": \"Keep these original branch stock forms\
    \ separate from base Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl\
    \ is explicitly dihydrate. Do not assign base-specific forms or invented IDs;\
    \ no target grounding exists for these source-only branch nodes.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution1038\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\"\
    : \"$.data.recipe[5]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 6,\\n                \\\"compound\\\": \\\"Pyridoxine\
    \ hydrochloride\\\",\\n                \\\"compound_id\\\": 519,\\n          \
    \      \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 300,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.3,\\n                \\\"mmol_l\\\
    \": 1.45886,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q77\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: Thiamine-HCl x 2 H2O\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 200 mg Thiamine-HCl x 2 H2O with listed\
    \ water 1000 mL and provider stock volume 1000 mL. At the explicit 1 mL transfer\
    \ this is 0.2 mg delivered per branch batch; branch final g/L remains unresolved.\"\
    ,\n    \"rationale\": \"Keep these original branch stock forms separate from base\
    \ Wolin 10x: calcium pantothenate is unqualified here and thiamine-HCl is explicitly\
    \ dihydrate. Do not assign base-specific forms or invented IDs; no target grounding\
    \ exists for these source-only branch nodes.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"solution1038\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/1038\",\n        \"source_locator\": \"\
    $.data.recipe[6]\",\n        \"exact_source_quote\": \"{\\n                \\\"\
    recipe_order\\\": 7,\\n                \\\"compound\\\": \\\"Thiamine-HCl x 2\
    \ H2O\\\",\\n                \\\"compound_id\\\": 77,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 200,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\": 0.535761,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q78\",\n    \"component_or_context\"\
    : \"Branch seven-vitamin stock: Distilled water\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Source-only branch seven-vitamin stock: 1000 ml Distilled water with listed\
    \ water 1000 mL and provider stock volume 1000 mL.\",\n    \"rationale\": \"Keep\
    \ these original branch stock forms separate from base Wolin 10x: calcium pantothenate\
    \ is unqualified here and thiamine-HCl is explicitly dihydrate. Do not assign\
    \ base-specific forms or invented IDs; no target grounding exists for these source-only\
    \ branch nodes.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution1038\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/1038\"\
    ,\n        \"source_locator\": \"$.data.recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"d85a7d6a5e176981afec2e03863d4829bdb84e8a36d156b3a90e6ca8f34e32fa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q79\",\n    \"component_or_context\"\
    : \"Branch nested DSM 916 F stock transfer\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"DSM 916 F is 10 mL of ferrous stock 1885, the same volume explicitly transferred\
    \ in the branch.\",\n    \"rationale\": \"The 5.2% label is unqualified; direct\
    \ mass/water details are independently captured below. Do not import the rest\
    \ of DSM 916.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz503f\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\"\
    ,\n        \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n \
    \       \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D,\
    \ solution E, and solution F. Increase the\\namount of solution B to 50 ml (2.50\
    \ g/l Na2CO3). Supplement the medium with 1 ml of\\nsolution D of medium 503 and\
    \ 10 ml of solution F of medium 916. Adjust the pH of the\\ncomplete medium to\
    \ 7.8 - 8.0.\",\n        \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      },\n      {\n        \"source_key\": \"solution6570\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/6570\",\n        \"source_locator\"\
    : \"$.data.recipe[0]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": null,\\n     \
    \           \\\"compound_id\\\": null,\\n                \\\"solution\\\": \\\"\
    Ferrous chloride solution (5.2%)\\\",\\n                \\\"solution_id\\\": 1885,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 10,\\n                \\\"unit\\\":\
    \ \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"0f041c2ff9d8250788f8e0af1560502c33c448135cf2bf9924d75c3e8e8a08e2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz916\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf\",\n    \
    \    \"source_locator\": \"Solution F subsection\",\n        \"exact_source_quote\"\
    : \"Ferrous chloride solution (5.2%) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323\",\n    \
    \    \"parsed_text_sha256\": \"a3b30458292f598b20d5d89e08de5b2fbe0cfa26f3e1629a7853d03f0fa63366\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q80\",\n    \"component_or_context\"\
    : \"Branch ferrous stock: FeCl2 x 4 H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 0.52 g FeCl2 x 4 H2O in the separate ferrous stock. Provider volume\
    \ 10 mL and concentration 52 g/L for FeCl2 tetrahydrate are declared provider\
    \ quantities; the source lists 0.52 g and 10 mL water.\",\n    \"rationale\":\
    \ \"Do not turn a listed water volume into an independently measured final stock\
    \ volume or use the unqualified5.2% label alone as a percent-basis assertion.\
    \ Preserve the exact tetrahydrate; no final branch mass concentration is derived.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution1885\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/1885\",\n\
    \        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"FeCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 260,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.52,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 52,\\n                \\\"mmol_l\\\
    \": 261.554,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"87acf0e8ad2a475568f87f4dad2d241eaf3cb9d7dcaad412929b867cc85ceaab\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q81\",\n    \"component_or_context\"\
    : \"Branch ferrous stock: Distilled water\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain 10 ml Distilled water in the separate ferrous stock. Provider volume\
    \ 10 mL and concentration 52 g/L for FeCl2 tetrahydrate are declared provider\
    \ quantities; the source lists 0.52 g and 10 mL water.\",\n    \"rationale\":\
    \ \"Do not turn a listed water volume into an independently measured final stock\
    \ volume or use the unqualified5.2% label alone as a percent-basis assertion.\
    \ Preserve the exact tetrahydrate; no final branch mass concentration is derived.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution1885\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/1885\",\n\
    \        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 10,\\n                \\\"unit\\\":\
    \ \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"87acf0e8ad2a475568f87f4dad2d241eaf3cb9d7dcaad412929b867cc85ceaab\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503f\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503f.pdf\",\n   \
    \     \"source_locator\": \"Page1 explicit DSM 117064 modification\",\n      \
    \  \"exact_source_quote\": \"For DSM 117064: Omit solution C, solution D, solution\
    \ E, and solution F. Increase the\\namount of solution B to 50 ml (2.50 g/l Na2CO3).\
    \ Supplement the medium with 1 ml of\\nsolution D of medium 503 and 10 ml of solution\
    \ F of medium 916. Adjust the pH of the\\ncomplete medium to 7.8 - 8.0.\",\n \
    \       \"snapshot_sha256\": \"135789b812e593100b3ae79019bc5d27e13bc61df0b50521a64e7ab7772488e1\"\
    ,\n        \"parsed_text_sha256\": \"f3d396b978354563e6b6a2724825124d964322282f3ce11e4cd8cacd69502f92\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q82\",\n    \"component_or_context\"\
    : \"Branch ferrous-stock pH\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Retain pH 2 with HCl within the ferrous stock, not the branch complete-medium\
    \ pH 7.8–8.0.\",\n    \"rationale\": \"Keep stock and receiving-medium pH claims\
    \ separate. No fixed HCl dose or concentration is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz916\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf\",\n        \"\
    source_locator\": \"Ferrous chloride solution subsection\",\n        \"exact_source_quote\"\
    : \"Adjust to pH 2 with HCl.\",\n        \"snapshot_sha256\": \"1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323\"\
    ,\n        \"parsed_text_sha256\": \"a3b30458292f598b20d5d89e08de5b2fbe0cfa26f3e1629a7853d03f0fa63366\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q83\",\n    \"component_or_context\"\
    : \"Branch ferrous HCl dose\",\n    \"decision\": \"not_quantified\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINITHIOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminithiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"not_quantified\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"HCl receiving quantity and strength are not quantified for this stock pH adjustment.\"\
    ,\n    \"rationale\": \"Keep stock and receiving-medium pH claims separate. No\
    \ fixed HCl dose or concentration is inferred.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz916\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium916.pdf\"\
    ,\n        \"source_locator\": \"Ferrous chloride solution subsection\",\n   \
    \     \"exact_source_quote\": \"Adjust to pH 2 with HCl.\",\n        \"snapshot_sha256\"\
    : \"1d30f1d600caf1028c7e856727fee639d3e6a360d1066d14efa5e90207b21323\",\n    \
    \    \"parsed_text_sha256\": \"a3b30458292f598b20d5d89e08de5b2fbe0cfa26f3e1629a7853d03f0fa63366\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Primary IDs and exact current CHEBI-based secondary mappings
  outcome: concern
  summary: 32 distinct asserted primary IDs have matching nonobsolete labels in both
    layers. Target has 32/34 primary links and 30/34 current secondary links; 29/30
    asserted secondary keys have exact pinned mapped rows, with CHEBI:26833 absent.
    These 94.12% primary and 85.29% verified-secondary instance metrics have denominator
    34 and scale 0–100; they measure linkage, not scientific accuracy. No legacy secondary
    key is asserted.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - owner-0
  - mim
  - chebi131361
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi26833
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32145
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
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
- assessment_id: identity
  area: identity
  topic: Source accession and maintained ownership
  outcome: supported
  summary: CM001636 and its exact maintained owner resolve to DSMZ 503f, not DSMZ
    503. The target and owner retain the same 34 ingredient assertions, pH and preparation.
    Base A–F and DSM 117064-specific modifications are distinct formulations; no new
    taxon or growth claim is inferred.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - primary
  - provider
  - seven-vitamin-dependency
  - ferrous-dependency
- assessment_id: evidence
  area: evidence
  topic: Claim-level amount support and source scope
  outcome: concern
  summary: The local layers have import provenance but no attached amount evidence.
    The inventory covers every local concentration and scoped source-only quantity
    using literal excerpts, exact source locators, units, stages and original capture
    hashes. Provider-declared volume is kept separate from measured assembled final
    volume.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - seven-vitamin-dependency
  - ferrous-dependency
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, source-only additions and owner differences
  outcome: concern
  summary: The main A–F procedure and final pH are preserved, including sulfur handling,
    gas fractions, 30–45 min sparging, A 110°C/20 min, separate stock sterilization
    and B→F addition order. However, named stage compositions/doses are absent, SL-10
    final makeup is wrongly at main root, and HTML markup remains literal in prose.
    Source-only branch stocks and pH remain conditional.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - seven-vitamin-dependency
  - ferrous-dependency
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are consistent with base casamino acids, yeast
    extract and no gelling agent. The branch omits these complex additions, so these
    base classifications must not automatically be transferred to the branch. Source
    name and generic application do not prove growth.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - primary
  - provider
  - seven-vitamin-dependency
  - ferrous-dependency
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical specificity
  outcome: concern
  summary: Nickel chloride is explicitly hexahydrate but CHEBI:34887 is anhydrous
    Cl2Ni; sodium resazurin is mapped to sodium-free CHEBI:8806. Base calcium D-(+)-pantothenate
    agrees with the D synonyms/stereospecific CHEBI:31345; generic CHEBI:16494 does
    not contradict the retained DL-lipoic name. CHEBI:26833 has elemental-sulfur synonyms;
    powder context does not prove an incorrect atom/allotrope mapping. The current
    secondary-key absence is separate from primary identity. Vitamin B12 remains generic;
    no specific vitamer or mixture identity is invented.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - primary
  - provider
  - seven-vitamin-dependency
  - ferrous-dependency
- assessment_id: growth
  area: scope
  topic: Growth, organism taxonomy and graph claims
  outcome: not_applicable
  summary: The title, generic Microbial cultivation application and catalog Aerobic
    flags are not experimental growth or taxonomy evidence. No growth assertions,
    current taxonomy IDs or graph membership are added. Explicit source strain qualifiers
    remain formulation scope only.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - primary
  - provider
  - seven-vitamin-dependency
  - ferrous-dependency
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 21 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: writer
  area: provenance
  topic: Authoritative inputs and current writer scope
  outcome: concern
  summary: Current MediaDive code separates first-stage ingredients and stock references
    but still gathers preparation from every API solution at the main root. Current
    cleanup flags disagreeing duplicate values; current lossless merge preserves scientific
    differences. The current code is not evidence of a particular old execution. Repair
    the exact normalized owner and review source-stage import handling before separately
    authorized regeneration.
  target_ids:
  - CultureMech:001636
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: culturemech.001636.a-through-f-stock-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stage and stock concentrations replace the assembled medium
  description: Both layers flatten 34 concentration assertions from separate A, B,
    D, E, F, SL-10, selenite and vitamin stocks. Primary final volume is explicitly
    1008 mL; A’s 952 mL provider normalization and full-strength B–F/stock values
    are not final-medium concentrations. The stage graph, dose and separate water
    rows are missing.
  target_ids:
  - CultureMech:001636
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
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
  issue_key: culturemech.001636.hcl-unqualified-percent-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: HCl mass conversion lacks a specified percentage basis
  description: ingredients[12] stores 2.5 g/L HCl, matching a provider calculation,
    while the primary specifies 10 mL HCl 25% in SL-10 with no percentage basis or
    density. This cannot establish that mass concentration, even before the separate
    stock/main stage error.
  target_ids:
  - CultureMech:001636
  field_paths:
  - ingredients[12].concentration
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.001636.source-salt-and-hydrate-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydration and sodium-resazurin form are not preserved
  description: Source NiCl2 x 6H2O is grounded to anhydrous CHEBI:34887 in primary
    and current secondary fields; source sodium resazurin is grounded to sodium-free
    CHEBI:8806. Other retained generic identities are not declared wrong merely because
    their source names include powder or DL context.
  target_ids:
  - CultureMech:001636
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - record
  - primary
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.001636.stock-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SL-10 preparation is represented as main-medium preparation
  description: The second root preparation step dissolves iron in HCl and makes up
    to 1000 mL; this belongs to SL-10, not the 1008 mL main assembly. Main prose names
    A–F but their structured compositions and doses are absent. The primary also contains
    a separate DSM 117064 branch; if represented, its replacements/pH must stay conditional.
  target_ids:
  - CultureMech:001636
  field_paths:
  - preparation_steps[1]
  - preparation_steps[0]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.001636.sulfur-current-secondary-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The asserted sulfur secondary key lacks a current pinned mapping
  description: CHEBI:26833 resolves in OLS with the canonical sulfur atom label and
    elemental-sulfur synonyms, but the complete pinned MIM preferred-term index has
    no mapped row for that exact secondary key. This is a completed negative lookup,
    not source unavailability or proof of wrong primary sulfur identity.
  target_ids:
  - CultureMech:001636
  field_paths:
  - ingredients[6].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - mim
  - chebi26833
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.2
  native_severity: P3.2
  normalization_reason: P3.2 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore the exact A–F stage graph and named nested stocks with all
    source amounts/water and receiving doses in the normalized owner. Correct flattened
    values with the explicit base 1008 mL denominator where justified; retain source/provider
    limits for individual stock volumes and A’s 952 versus 952.5 mL entries. Attach
    narrow evidence and regenerate only after authorized curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
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
  description: Restore exact 10 mL HCl 25% source representation at SL-10 scope and
    keep percentage basis unresolved unless exact-source evidence supplies it. Remove
    the unsupported mass assertion only through authorized owner curation; do not
    invent density or a numerical replacement.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
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
  description: Verify exact salt/hydrate replacements in the normalized owner without
    inventing an uninspected identifier, preserve source masses, and never use the
    anhydrous/free-acid molecular mass for supplied forms. Preserve valid D-pantothenate,
    generic B12, DL-lipoic and elemental-sulfur context.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
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
  description: Preserve the useful main sequence and move the exact SL-10 procedure
    to its stock scope. Preserve A-only 110°C/20 min and distinct B–F sterilization
    limits; clean literal HTML without changing values. Keep any recovered DSM 117064
    branch separate, including named DSM 503 D and DSM 916 F dependencies, without
    importing either parent medium or inferring branch final volume.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
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
  description: Reconcile the current secondary mapping using exact MIM evidence; do
    not substitute an adjacent sulfur species or delete a valid primary identifier
    based solely on the current mapping gap. Preserve powdered source context and
    append provenance clarification during authorized owner curation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001636
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminithiophilus_medium.yaml
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
- Only exact per-record bound captures are used. Current collection and provider differences
  do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently
  establish a measured final mixture volume. No density, percent basis, exact hydration,
  default sterilization cycle or stock volume is invented.
- All required current primary/provider and named dependency checks completed. No
  historical legacy-secondary assertion requires unavailable correspondence; the completed
  sulfur current-index negative result is not a reason for partial coverage. Source-only
  branch final volume, HCl percentage basis and unspecified sterilization cycles remain
  explicit scientific limits.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-025
- generated-medium
```
