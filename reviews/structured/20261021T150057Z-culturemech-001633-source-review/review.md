# Source and formulation review: ammonifex_thiophilus_medium (CultureMech:001633)

- Review: 20261021T150057Z-culturemech-001633-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:47:43Z
- Finished UTC: 2026-10-21T15:00:57Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 503c is identifiable and its preparation prose survives, but 33 stock-strength values are flattened into direct medium concentrations and the A–F hierarchy is absent. Reconstruct the stock doses, correct sodium-resazurin/nickel forms, and reassess the unsupported high-metal annotation without inventing a measured final volume.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 253; batch 026 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-five task batches contain 250 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 253 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001633 | data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml | generated | ammonifex_thiophilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001633 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001633 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/253/strict.tsv |
| validate-terms | passed | True | CultureMech:001633 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001633 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001633 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001633.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:001633.

33 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 33/33 primary and 31/33 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 33: primary 100.00%; secondary 93.94%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001633.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact medium and maintained owner

identity: supported. Targets: CultureMech:001633.

CultureMech:001633, DSMZ/MediaDive 503c and the sole maintained owner agree in identity. The target retains the owner’s 33 direct ingredients, two preparation steps and high_metal flag; the extra merge event does not repair their scientific representation. No organism, strain-specific growth, DOI or PMID is asserted by this record; the name and generic cultivation application do not supply new growth evidence.

### A–F hierarchy and conditional arithmetic

consistency: concern. Targets: CultureMech:001633.

The source combines A 922 mL, B 50 mL, C 10 mL, D 1 mL, E 10 mL and F 10 mL. B/C/E/F contain respectively 2.5 g carbonate, 2 g formate, 2 g thiosulfate pentahydrate and 0.3 g sulfide nonahydrate; their local 50/200/200/30 g/L values are stock strengths. SL-10 and selenite-tungstate are dosed within A; vitamins are dosed through D. Solution A lists 920 + 1 + 1 + 0.5 = 922.5 mL liquid additions but declares 922 mL. All calculations therefore preserve nominal provider bases and source aliquots rather than claim measured final concentrations.

### Preserved instructions with missing stock structure

completeness: concern. Targets: CultureMech:001633.

The first local step preserves the complete source gas/sterilization sequence, including filtration of D/E despite its broad AUTOCLAVE action. A–F are not represented as identifiable local stock objects, and SL-10’s 1000 mL makeup instruction is incorrectly attached to the main sequence. Restore stage identity and structured actions while retaining the already-present filtration, gas fractions, sequence and conditional pH endpoint. The source supplies no autoclave temperature/duration or quantified pH-adjustment reagent.

### Source salts, hydrates and stereochemistry

grounding: concern. Targets: CultureMech:001633.

Sodium resazurin is grounded to neutral CHEBI:8806 (C12H7NO4), without a secondary slot; nickel hexahydrate uses anhydrous CHEBI:34887 in both slots. These supplied forms require reconciliation. Calcium D-(+)-pantothenate is compatible with the captured D-specific structure/synonyms of CHEBI:31345; generic stereounspecified CHEBI:16494 does not falsely assert a single DL-lipoic enantiomer. No extra hydrate or stereoisomer is inferred for source names that do not specify one. HCl 25% lacks a stated percent basis/density, so the provider’s 2.5 g/L is not independently confirmed as a mass conversion.

### Defined liquid formulation and high-metal flag

scope: concern. Targets: CultureMech:001633.

DEFINED/DEFINED and LIQUID agree with the named chemical recipe and noncomplex provider metadata. The high_metal:true assertion is not established: the schema describes a millimolar percentile threshold, but the inspected analyzer treats g/L as a numeric proxy without molecular-weight conversion and defaults native G_PER_L units to factor one, while consuming only direct ingredients. The flattened stock strengths make this record particularly unsuitable for such a classification. No corrected total, percentile or replacement Boolean is inferred without a separately authorized source-aware calculation.

### Current import and merge behavior

provenance: concern. Targets: CultureMech:001633.

Current MediaDive composition parsing handles only the primary solution and separately preserves stock additions, while preparation parsing still aggregates solution-specific steps. Current formulation merging requires compatible formulation content. Reconcile the maintained owner and its nested stock definitions before regenerating; these current code observations do not reconstruct the historical import run.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001633.

60 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main sol. 503c: Solution A",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1063,\n                        \"amount\": 922,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Main sol. 503c table; Solution A row",
        "exact_source_quote": "Solution A                                                     922.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 922 ml in Main sol. 503c, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 503c: Solution B",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1067,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Main sol. 503c table; Solution B row",
        "exact_source_quote": "Solution B                                                      50.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 ml in Main sol. 503c, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 503c: Solution C",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1068,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Main sol. 503c table; Solution C row",
        "exact_source_quote": "Solution C                                                      10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Main sol. 503c, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 503c: Solution D",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1065,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Main sol. 503c table; Solution D row",
        "exact_source_quote": "Solution D                                                       1.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1 ml in Main sol. 503c, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 503c: Solution E",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 1069,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Main sol. 503c table; Solution E row",
        "exact_source_quote": "Solution E                                                      10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Main sol. 503c, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 503c: Solution F",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 1070,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Main sol. 503c table; Solution F row",
        "exact_source_quote": "Solution F                                                      10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Main sol. 503c, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A: KH2PO4",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "0.21692",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.21692,\n                        \"mmol_l\": 1.594,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; KH2PO4 row",
        "exact_source_quote": "KH2PO4                                                           0.20          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.2 g in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.21692",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.21692",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: NH4Cl",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": {
      "value": "0.27115",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.27115,\n                        \"mmol_l\": 5.06917,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; NH4Cl row",
        "exact_source_quote": "NH4Cl                                                            0.25          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.25 g in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.27115",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.27115",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: NaCl",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "local": {
      "value": "1.0846",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.0846,\n                        \"mmol_l\": 18.5592,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; NaCl row",
        "exact_source_quote": "NaCl                                                             1.00          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1 g in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.0846",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.0846",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: MgCl2 x 6 H2O",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "local": {
      "value": "0.433839",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.433839,\n                        \"mmol_l\": 2.13396,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; MgCl2 x 6 H2O row",
        "exact_source_quote": "MgCl2 x 6 H2O                                                    0.40          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.4 g in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.433839",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.433839",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: KCl",
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "local": {
      "value": "0.542299",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.542299,\n                        \"mmol_l\": 7.2743,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; KCl row",
        "exact_source_quote": "KCl                                                              0.50          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.5 g in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.542299",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.542299",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: CaCl2 x 2 H2O",
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "local": {
      "value": "0.16269",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.16269,\n                        \"mmol_l\": 1.10662,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; CaCl2 x 2 H2O row",
        "exact_source_quote": "CaCl2 x 2 H2O                                                    0.15          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.15 g in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16269",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16269",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: Trace element solution SL-10",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; Trace element solution SL-10 row",
        "exact_source_quote": "Trace element solution SL-10                                     1.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1 ml in Solution A, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A: Selenite-tungstate solution",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; Selenite-tungstate solution row",
        "exact_source_quote": "Selenite-tungstate solution                                      1.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1 ml in Solution A, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A: Sodium resazurin",
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "local": {
      "value": "0.000542299",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000542299,\n                        \"mmol_l\": 0.00215909,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; Sodium resazurin (0.1% w/v) row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v)                                      0.50        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.5 ml in Solution A, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000542299",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.000542299",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "The provider divides Solution A source grams by its nominal 0.922 L basis; main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve printed rounding and do not silently choose a measured stock or final denominator. For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source A batch."
  },
  {
    "ingredient_or_context": "Solution A: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 920,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution A table; Distilled water row",
        "exact_source_quote": "Distilled water                                                920.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 920 ml in Solution A, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution B: Na2CO3",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": {
      "value": "50",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution B table; Na2CO3 row",
        "exact_source_quote": "Na2CO3                                                           2.50          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 2.5 g in Solution B, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 50 mL stock basis, 2.5 g / (50/1000 L) gives 50 g/L in that stock. The source main aliquot equals that nominal stock volume, so it would supply 2.5 g per batch, not 50 g per final liter."
  },
  {
    "ingredient_or_context": "Solution B: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution B table; Distilled water row",
        "exact_source_quote": "Distilled water                                                 50.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 ml in Solution B, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution C: Na-formate",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "200",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 200,\n                        \"mmol_l\": 2940.86,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution C table; Na-formate row",
        "exact_source_quote": "Na-formate                                                       2.00          g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 2 g in Solution C, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 10 mL stock basis, 2 g / (10/1000 L) gives 200 g/L in that stock. The source main aliquot equals that nominal stock volume, so it would supply 2 g per batch, not 200 g per final liter."
  },
  {
    "ingredient_or_context": "Solution C: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[3].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution C table; Distilled water row",
        "exact_source_quote": "Distilled water                                                 10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Solution C, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution D: Wolin's vitamin solution (10x)",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[4].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution D table; Wolin's vitamin solution (10x) row",
        "exact_source_quote": "Wolin's vitamin solution (10x)                                   1.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1 ml in Solution D, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution E: Na2S2O3 x 5 H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "200",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[5].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 200,\n                        \"mmol_l\": 805.847,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution E table; Na2S2O3 x 5 H2O row",
        "exact_source_quote": "Na2S2O3 x 5 H2O                                                 2.00         g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 2 g in Solution E, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 10 mL stock basis, 2 g / (10/1000 L) gives 200 g/L in that stock. The source main aliquot equals that nominal stock volume, so it would supply 2 g per batch, not 200 g per final liter."
  },
  {
    "ingredient_or_context": "Solution E: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[5].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution E table; Distilled water row",
        "exact_source_quote": "Distilled water                                                10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Solution E, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution F: Na2S x 9 H2O",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "30",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[6].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"condition\": \"\",\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution F table; Na2S x 9 H2O row",
        "exact_source_quote": "Na2S x 9 H2O                                                    0.30         g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.3 g in Solution F, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 10 mL stock basis, 0.3 g / (10/1000 L) gives 30 g/L in that stock. The source main aliquot equals that nominal stock volume, so it would supply 0.3 g per batch, not 30 g per final liter."
  },
  {
    "ingredient_or_context": "Solution F: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[6].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Solution F table; Distilled water row",
        "exact_source_quote": "Distilled water                                                10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Solution F, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: HCl",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; HCl (25%) row",
        "exact_source_quote": "HCl (25%)                                                      10.00        ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 10 ml in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: FeCl2 x 4 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; FeCl2 x 4 H2O row",
        "exact_source_quote": "FeCl2 x 4 H2O                                                   1.50         g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1.5 g in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: ZnCl2",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.07",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; ZnCl2 row",
        "exact_source_quote": "ZnCl2                                                          70.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 70 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: MnCl2 x 4 H2O",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; MnCl2 x 4 H2O row",
        "exact_source_quote": "MnCl2 x 4 H2O                                                100.00        mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 100 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: H3BO3",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.006",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; H3BO3 row",
        "exact_source_quote": "H3BO3                                                           6.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 6 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: CoCl2 x 6 H2O",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": {
      "value": "0.19",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; CoCl2 x 6 H2O row",
        "exact_source_quote": "CoCl2 x 6 H2O                                                190.00        mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 190 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: CuCl2 x 2 H2O",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": {
      "value": "0.002",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; CuCl2 x 2 H2O row",
        "exact_source_quote": "CuCl2 x 2 H2O                                                   2.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 2 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: NiCl2 x 6 H2O",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": {
      "value": "0.024",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; NiCl2 x 6 H2O row",
        "exact_source_quote": "NiCl2 x 6 H2O                                                  24.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 24 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: Na2MoO4 x 2 H2O",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": {
      "value": "0.036",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; Na2MoO4 x 2 H2O row",
        "exact_source_quote": "Na2MoO4 x 2 H2O                                                36.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 36 mg in Trace element solution SL-10, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified 25% basis/density blocks an independent mass conversion; retain its 10 mL stock dose."
  },
  {
    "ingredient_or_context": "Trace element solution SL-10: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[7].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Trace element solution SL-10 table; Distilled water row",
        "exact_source_quote": "Distilled water                                              990.00         ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 990 ml in Trace element solution SL-10, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution: NaOH",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[8].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Selenite-tungstate solution table; NaOH row",
        "exact_source_quote": "NaOH                                                            0.50         g",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 0.5 g in Selenite-tungstate solution, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL selenite-tungstate stock basis, its 1 mL dose into A would contribute source stock mass × 1/1000. The listed 1000 mL water is not independently measured final stock volume."
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution: Na2SeO3 x 5 H2O",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": {
      "value": "0.003",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[8].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Selenite-tungstate solution table; Na2SeO3 x 5 H2O row",
        "exact_source_quote": "Na2SeO3 x 5 H2O                                                 3.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 3 mg in Selenite-tungstate solution, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL selenite-tungstate stock basis, its 1 mL dose into A would contribute source stock mass × 1/1000. The listed 1000 mL water is not independently measured final stock volume."
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution: Na2WO4 x 2 H2O",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": {
      "value": "0.004",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[8].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Selenite-tungstate solution table; Na2WO4 x 2 H2O row",
        "exact_source_quote": "Na2WO4 x 2 H2O                                                  4.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 4 mg in Selenite-tungstate solution, with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL selenite-tungstate stock basis, its 1 mL dose into A would contribute source stock mass × 1/1000. The listed 1000 mL water is not independently measured final stock volume."
  },
  {
    "ingredient_or_context": "Selenite-tungstate solution: Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[8].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Selenite-tungstate solution table; Distilled water row",
        "exact_source_quote": "Distilled water                                             1000.00         ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1000 ml in Selenite-tungstate solution, with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Biotin",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Biotin row",
        "exact_source_quote": "Biotin                                                         20.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 20 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Folic acid",
    "field_path": "ingredients[24].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Folic acid row",
        "exact_source_quote": "Folic acid                                                     20.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 20 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Pyridoxine hydrochloride",
    "field_path": "ingredients[25].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Pyridoxine hydrochloride row",
        "exact_source_quote": "Pyridoxine hydrochloride                                     100.00        mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 100 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Thiamine HCl",
    "field_path": "ingredients[26].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Thiamine HCl row",
        "exact_source_quote": "Thiamine HCl                                                   50.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Riboflavin",
    "field_path": "ingredients[27].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Riboflavin row",
        "exact_source_quote": "Riboflavin                                                     50.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Nicotinic acid",
    "field_path": "ingredients[28].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Nicotinic acid row",
        "exact_source_quote": "Nicotinic acid                                                 50.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Calcium D-(+)-pantothenate",
    "field_path": "ingredients[29].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Calcium D-(+)-pantothenate row",
        "exact_source_quote": "Calcium D-(+)-pantothenate                                     50.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Vitamin B12",
    "field_path": "ingredients[30].concentration",
    "decision": "correct",
    "local": {
      "value": "0.001",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Vitamin B12 row",
        "exact_source_quote": "Vitamin B12                                                     1.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): p-Aminobenzoic acid",
    "field_path": "ingredients[31].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; p-Aminobenzoic acid row",
        "exact_source_quote": "p-Aminobenzoic acid                                            50.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): (DL)-alpha-Lipoic acid",
    "field_path": "ingredients[32].concentration",
    "decision": "correct",
    "local": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; (DL)-alpha-Lipoic acid row",
        "exact_source_quote": "(DL)-alpha-Lipoic acid                                         50.00       mg",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 50 mg in Wolin's vitamin solution (10x), with its source identity and stage. The existing direct g/L is a stock-level value and cannot stand for the final medium; attach source evidence after restoring the hierarchy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting Solution D would contribute source milligrams × 1/1000 milligrams per main batch. The 10x label describes this exact printed formulation; do not apply an additional tenfold multiplier or count D and its stock twice."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x): Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[9].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF pages 1–2; Wolin's vitamin solution (10x) table; Distilled water row",
        "exact_source_quote": "Distilled water                                             1000.00         ml",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain 1000 ml in Wolin's vitamin solution (10x), with its source identity and stage. This source water/stock addition is absent as a structured dose. Preserve the batch input without inventing a final-volume basis.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A 100% CO2, 30–45 minutes",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "Sparge solution A with 100% CO2 gas for 30 – 45 min",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "The exact gas fraction and duration survive in local prose without attached claim evidence; stock identity still needs restoration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution B 80% N2/20% CO2",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Preserve the separate B atmosphere and sterilization, not an inferred uniform procedure.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Solutions C/F 100% N2",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "C and F are autoclaved under 100% N2 gas.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "The existing text supports this specific pair and gas fraction; no autoclave cycle is supplied.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Solutions D/E 100% N2 and filtration",
    "field_path": "preparation_steps[0].description",
    "decision": "evidence_only",
    "local": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "Solutions D and E are prepared under 100% N2\ngas and sterilized by filtration.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Filtration is explicitly present in the existing text. Preserve it while structuring the missing stock hierarchy; do not report it as absent.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Completed medium pH 6.8",
    "field_path": "ph_value",
    "decision": "evidence_only",
    "local": 6.8,
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "complete medium to 6.8, if necessary.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "The numeric pH is supported; retain the source’s if-necessary adjustment qualification and attach evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 6.8,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.8,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "SL-10 final makeup 1000 mL",
    "field_path": "preparation_steps[1].description",
    "decision": "correct",
    "local": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 2 SL-10 preparation",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "Retain the endpoint but restore SL-10 stock scope rather than main-medium placement.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Unspecified autoclave cycle",
    "field_path": "preparation_steps[0].description",
    "decision": "not_quantified",
    "local": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "No temperature or duration is given for autoclaving; do not insert a generic cycle.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "Unquantified pH adjustment",
    "field_path": "preparation_steps[0].description",
    "decision": "not_quantified",
    "local": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
    "source_snippets": [
      {
        "source_key": "dsmz503c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf",
        "source_locator": "PDF page 1 preparation",
        "exact_source_quote": "Adjust pH of\ncomplete medium to 6.8, if necessary.",
        "snapshot_sha256": "5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3",
        "parsed_text_sha256": "5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca"
      }
    ],
    "rationale": "The endpoint is specified but adjustment reagent identity, strength and dose are not. Do not invent a titrant amount.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary.",
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "Main nominal total from six source aliquots",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": [
      {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
      },
      {
        "step_number": 2,
        "action": "DISSOLVE",
        "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1063,\n                        \"amount\": 922,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1067,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1068,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1065,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"solution\": \"Solution E\",\n                        \"solution_id\": 1069,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution F\",\n                        \"solution_id\": 1070,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1003",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      }
    ],
    "rationale": "The six listed aliquots sum to the provider’s declared 1003 mL. This is a nominal source sum, not a measurement of the completed medium after pH adjustment.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration. To complete the medium appropriate amounts of solutions B to F are added to the sterile solution A in the sequence as indicated. Adjust pH of complete medium to 6.8, if necessary."
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
    "arithmetic": "922 + 50 + 10 + 1 + 10 + 10 = 1003 mL. No unconditional final g/L normalization is proposed."
  },
  {
    "ingredient_or_context": "Solution A declared versus listed liquid volume",
    "field_path": "solutions",
    "decision": "conflict",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000542299,\n                        \"mmol_l\": 0.00215909,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 920,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      },
      {
        "source_key": "mediadive503capi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/503c",
        "source_locator": "$.data.solutions[1].volume",
        "exact_source_quote": "\"volume\": 922",
        "snapshot_sha256": "8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f"
      }
    ],
    "rationale": "The provider declares 922 mL, whereas water and three liquid additions sum 922.5 mL. The primary does not specify a final A makeup. Preserve the discrepancy.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "920 + 1 + 1 + 0.5 = 922.5 mL versus 922 mL declared; no measured denominator selected."
  }
]

## Findings

### f1: Separate stock strengths replace the final medium formulation

blocker / open / confirmed; issue key: ammonifex-thiophilus-stock-flattening.

All 33 direct concentrations are drawn from A–F or nested trace/vitamin stocks, while the six main aliquots and nested doses are absent as local stock objects. For example, 2 g formate in 10 mL stock becomes 200 g/L directly, and 2.5 g carbonate in 50 mL becomes 50 g/L. This changes formulation identity. The source’s 922 versus 922.5 mL A discrepancy and nominal final sum must remain explicit.

### f2: Two supplied forms are narrowed to different chemical entities

major / open / confirmed; issue key: ammonifex-thiophilus-salt-hydrate-grounding.

The source specifies sodium resazurin and nickel chloride hexahydrate. Local primary CHEBI:8806 is neutral resazurin without sodium, and CHEBI:34887 is anhydrous nickel dichloride in primary and secondary slots. Resazurin has no asserted current secondary slot, so no nonexistent link is included in this finding.

### f3: High-metal classification lacks a valid source-aware calculation

major / open / confirmed; issue key: ammonifex-thiophilus-high-metal-unsupported.

The record’s high_metal:true has no attached quantitative justification. The schema’s millimolar percentile meaning is not established by the inspected analyzer’s approximate/default mass-unit conversion, and this record supplies flattened stock strengths rather than final medium concentrations. This review does not infer that the Boolean must be false; its present scientific support is insufficient.

## Recommended Actions And Acceptance Checks

### a1

Restore A–F and their nested SL-10, selenite-tungstate and vitamin doses in the maintained owner, preserving original source amounts/units and named preparation stages. Retain the existing filtration instructions and relocate SL-10 makeup. Reconcile volume declarations before proposing final concentrations; regenerate only after owner verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve supported source-form identities without inventing replacement CURIEs or changing the source stock masses. Reconcile each actual asserted slot separately; preserve the correctly scoped D-pantothenate and unspecified DL-lipoic metadata.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Reassess the annotation after correcting stock dilution and establishing source-specific units/forms. If retained, document a dimensionally valid total and the applicable percentile population; otherwise explicitly withdraw unsupported classification through separate curation. Do not rerun a bulk label writer as a substitute for this review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch026/253/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/253/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml:1:id: CultureMech:001633<br>./data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml:1:id: CultureMech:001633<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/253/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 44 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/253/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf; DSMZ 503c PDF pages 1–2: A–F additions, all nine component-stock tables and complete preparation | supports | Complete exact primary text and both page images read. All source quantities retain their named solution stage; the main listed aliquots total 1003 mL, without establishing a measured final volume. |
| provider | https://mediadive.dsmz.de/rest/medium/503c; $.data.medium; $.data.solutions[0:10].recipe, volume and steps | supports | Complete medium 503c payload read. Provider g_l values describe individual solution objects; main volume is declared 1003 mL, while Solution A declares 922 mL against 922.5 mL listed liquid additions. |
| solution1063 | https://mediadive.dsmz.de/rest/solution/1063; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution1067 | https://mediadive.dsmz.de/rest/solution/1067; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution1068 | https://mediadive.dsmz.de/rest/solution/1068; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution1065 | https://mediadive.dsmz.de/rest/solution/1065; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution1069 | https://mediadive.dsmz.de/rest/solution/1069; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution1070 | https://mediadive.dsmz.de/rest/solution/1070; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution595 | https://mediadive.dsmz.de/rest/solution/595; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution777 | https://mediadive.dsmz.de/rest/solution/777; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; $.data: exact stock identity, declared volume, complete recipe and preparation | supports | Separate stock endpoint agrees in every non-null recipe field with its exact medium-503c object. Extra null JSON fields do not change the composition. These stock records are not independent evidence of a receiving-medium final concentration. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62965 resolves to sodium formate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62965": [{"label": "Na-formate", "match_type": "preferred_term", "identifier": "CHEBI:62965", "preferred_term": "Na-formate", "ontology_id": "CHEBI:62965", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | scripts/analyze_metal_concentrations.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Metal-analysis conversion, name matching, percentile classification, label writing and high_metal schema definition read statically; no analysis or mutation executed. |
| writer-1 | scripts/add_metal_ree_labels.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Metal-analysis conversion, name matching, percentile classification, label writing and high_metal schema definition read statically; no analysis or mutation executed. |
| writer-2 | src/culturemech/schema/culturemech.yaml; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Metal-analysis conversion, name matching, percentile classification, label writing and high_metal schema definition read statically; no analysis or mutation executed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch026/253/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch026/253/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- All amounts are source batch quantities or provider-declared stock concentrations. No measured final stock or completed-medium volume, HCl percent basis/density or pH titrant amount is inferred.
- The source’s 10x vitamin label is not applied as an extra multiplier. Independent stock endpoints support their own definitions, not unqualified final-medium quantities.
- The metal-analysis code was read statically. No corpus-wide analysis or historical label-generation replay was performed, and no numerical replacement threshold or Boolean is asserted.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150057Z-culturemech-001633-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: ammonifex_thiophilus_medium (CultureMech:001633)'
started_at: '2026-10-21T14:47:43Z'
finished_at: '2026-10-21T15:00:57Z'
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
summary: DSMZ 503c is identifiable and its preparation prose survives, but 33 stock-strength
  values are flattened into direct medium concentrations and the A–F hierarchy is
  absent. Reconstruct the stock doses, correct sodium-resazurin/nickel forms, and
  reassess the unsupported high-metal annotation without inventing a measured final
  volume.
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
  - path: data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
    sha256: 617f2dea3a44f0d9943a8f0d09fac3eb10cf59b819a218b53f085bbf9aa7c2e7
    role: target
  - path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
    sha256: 1590471b41ad162bc8b559a03e22e7d2c9ee20f81429d4cbce2fdf3c6bead84a
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
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
  selection: Task review 253; batch 026 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-five task batches
    contain 250 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 253 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001633
targets:
- target_id: CultureMech:001633
  path: data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  label: ammonifex_thiophilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/253/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/253/strict.tsv"
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001633
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
  - CultureMech:001633
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:40.627691Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/253/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:42.078816Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/253/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:43.713871Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:44.828134Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:00:55Z'
  support: supports
  summary: './data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml:1:id: CultureMech:001633

    ./data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml:1:id: CultureMech:001633

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/253/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:00:55Z'
  support: supports
  summary: 44 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 7bbb388e034be7ce315eb1e91873e9ec694414c821ca7514d353e076ae641ef6
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/253/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 461fb30c13c555c745f1736a598eacc4fced1ea3f821518ed8f169c67170c8f2
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf
  locator: 'DSMZ 503c PDF pages 1–2: A–F additions, all nine component-stock tables
    and complete preparation'
  accessed_at: '2026-10-21T14:16:59.728449Z'
  support: supports
  summary: Complete exact primary text and both page images read. All source quantities
    retain their named solution stage; the main listed aliquots total 1003 mL, without
    establishing a measured final volume.
  snapshot_sha256: 5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/503c
  locator: $.data.medium; $.data.solutions[0:10].recipe, volume and steps
  accessed_at: '2026-10-21T14:16:58.497092Z'
  support: supports
  summary: Complete medium 503c payload read. Provider g_l values describe individual
    solution objects; main volume is declared 1003 mL, while Solution A declares 922
    mL against 922.5 mL listed liquid additions.
  snapshot_sha256: 8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f
- evidence_id: solution1063
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1063
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T14:18:59.886394Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: e8cec452bfb6837575aa9e6b0e179187ab9397c9858bad871080b5d4aaf636c3
- evidence_id: solution1067
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1067
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T14:19:00.513649Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: 6a3c677e45667947a80751b28aee8712af917b98b7bfbcbf7c0ea5ec01971e90
- evidence_id: solution1068
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1068
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T14:19:00.513704Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: 1a60668207a62d1b1cf91027d5a36e9219f95be0b0998cba1fb6eed58450d9d4
- evidence_id: solution1065
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1065
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T14:18:59.886474Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: c2fc5f53b68c0f4ae237fb5bf77584d8f992755a11e8b8948683e1f6b0157f8f
- evidence_id: solution1069
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1069
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T14:19:00.712076Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: f70de4c7bad0e2f0c584ba230189bfe27495e7df80d3abb2168836b2fb14524a
- evidence_id: solution1070
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1070
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T14:19:01.072427Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: 19962d7849361f29a3219f535c40218cb7967add5d6b567db8efb36c2e0a2334
- evidence_id: solution595
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T11:03:05.357684Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: solution777
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/777
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T13:20:07.510517Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: 3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: '$.data: exact stock identity, declared volume, complete recipe and preparation'
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Separate stock endpoint agrees in every non-null recipe field with its
    exact medium-503c object. Extra null JSON fields do not change the composition.
    These stock records are not independent evidence of a receiving-medium final concentration.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
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
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
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
- evidence_id: chebi29377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:31:16.500548Z'
  support: supports
  summary: CHEBI:29377 resolves to sodium carbonate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
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
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
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
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
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
- evidence_id: chebi62965
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.570542Z'
  support: supports
  summary: CHEBI:62965 resolves to sodium formate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f36b7c1107922c948bf6387ce77e0468c3fcdf76ce80969b5411b600e051910d
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
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
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
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
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
  accessed_at: '2026-10-21T15:00:55Z'
  support: supports
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
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type":
    "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id":
    "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150":
    [{"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label":
    "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62965": [{"label":
    "Na-formate", "match_type": "preferred_term", "identifier": "CHEBI:62965", "preferred_term":
    "Na-formate", "ontology_id": "CHEBI:62965", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label":
    "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
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
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMMONIFEX_THIOPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Metal-analysis conversion, name matching, percentile classification, label
    writing and high_metal schema definition read statically; no analysis or mutation
    executed.
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: writer-1
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Metal-analysis conversion, name matching, percentile classification, label
    writing and high_metal schema definition read statically; no analysis or mutation
    executed.
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Metal-analysis conversion, name matching, percentile classification, label
    writing and high_metal schema definition read statically; no analysis or mutation
    executed.
  snapshot_sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/253/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 280cd1b46d8def3c05884ac0b5f0beffbd6211d49bb91e814f4a31221dd88d5c
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/253/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T15:00:55Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 6c103d579c0fa6c5fc557c1caa3e3b254974d6b9d9db5fc31015ac5934f4ae1f
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '33 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 33/33
    primary and 31/33 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32145
  - chebi32150
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi62965
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
  details: 'Instance coverage on a 0–100 percent scale, denominator 33: primary 100.00%;
    secondary 93.94%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact medium and maintained owner
  outcome: supported
  summary: CultureMech:001633, DSMZ/MediaDive 503c and the sole maintained owner agree
    in identity. The target retains the owner’s 33 direct ingredients, two preparation
    steps and high_metal flag; the extra merge event does not repair their scientific
    representation. No organism, strain-specific growth, DOI or PMID is asserted by
    this record; the name and generic cultivation application do not supply new growth
    evidence.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - id-search
- assessment_id: source-stages
  area: consistency
  topic: A–F hierarchy and conditional arithmetic
  outcome: concern
  summary: The source combines A 922 mL, B 50 mL, C 10 mL, D 1 mL, E 10 mL and F 10
    mL. B/C/E/F contain respectively 2.5 g carbonate, 2 g formate, 2 g thiosulfate
    pentahydrate and 0.3 g sulfide nonahydrate; their local 50/200/200/30 g/L values
    are stock strengths. SL-10 and selenite-tungstate are dosed within A; vitamins
    are dosed through D. Solution A lists 920 + 1 + 1 + 0.5 = 922.5 mL liquid additions
    but declares 922 mL. All calculations therefore preserve nominal provider bases
    and source aliquots rather than claim measured final concentrations.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
- assessment_id: preparation
  area: completeness
  topic: Preserved instructions with missing stock structure
  outcome: concern
  summary: The first local step preserves the complete source gas/sterilization sequence,
    including filtration of D/E despite its broad AUTOCLAVE action. A–F are not represented
    as identifiable local stock objects, and SL-10’s 1000 mL makeup instruction is
    incorrectly attached to the main sequence. Restore stage identity and structured
    actions while retaining the already-present filtration, gas fractions, sequence
    and conditional pH endpoint. The source supplies no autoclave temperature/duration
    or quantified pH-adjustment reagent.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
- assessment_id: forms
  area: grounding
  topic: Source salts, hydrates and stereochemistry
  outcome: concern
  summary: Sodium resazurin is grounded to neutral CHEBI:8806 (C12H7NO4), without
    a secondary slot; nickel hexahydrate uses anhydrous CHEBI:34887 in both slots.
    These supplied forms require reconciliation. Calcium D-(+)-pantothenate is compatible
    with the captured D-specific structure/synonyms of CHEBI:31345; generic stereounspecified
    CHEBI:16494 does not falsely assert a single DL-lipoic enantiomer. No extra hydrate
    or stereoisomer is inferred for source names that do not specify one. HCl 25%
    lacks a stated percent basis/density, so the provider’s 2.5 g/L is not independently
    confirmed as a mass conversion.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi8806
  - chebi34887
  - chebi31345
  - chebi16494
- assessment_id: classification
  area: scope
  topic: Defined liquid formulation and high-metal flag
  outcome: concern
  summary: 'DEFINED/DEFINED and LIQUID agree with the named chemical recipe and noncomplex
    provider metadata. The high_metal:true assertion is not established: the schema
    describes a millimolar percentile threshold, but the inspected analyzer treats
    g/L as a numeric proxy without molecular-weight conversion and defaults native
    G_PER_L units to factor one, while consuming only direct ingredients. The flattened
    stock strengths make this record particularly unsuitable for such a classification.
    No corrected total, percentile or replacement Boolean is inferred without a separately
    authorized source-aware calculation.'
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - primary
  - provider
  - writer-0
  - writer-1
  - writer-2
- assessment_id: writers
  area: provenance
  topic: Current import and merge behavior
  outcome: concern
  summary: Current MediaDive composition parsing handles only the primary solution
    and separately preserves stock additions, while preparation parsing still aggregates
    solution-specific steps. Current formulation merging requires compatible formulation
    content. Reconcile the maintained owner and its nested stock definitions before
    regenerating; these current code observations do not reconstruct the historical
    import run.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - owner-0
  - writer-context-0
  - writer-context-1
  - writer-context-2
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 60 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001633
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main sol. 503c: Solution A\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503capi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"solution\\\": \\\"Solution A\\\",\\n                        \\\"solution_id\\\
    \": 1063,\\n                        \\\"amount\\\": 922,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Main sol. 503c table; Solution A row\"\
    ,\n        \"exact_source_quote\": \"Solution A                              \
    \                       922.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 922 ml in Main sol. 503c, with\
    \ its source identity and stage. This source water/stock addition is absent as\
    \ a structured dose. Preserve the batch input without inventing a final-volume\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null,\n        \"decision\": \"add\"\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 503c: Solution B\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"solution\\\
    \": \\\"Solution B\\\",\\n                        \\\"solution_id\\\": 1067,\\\
    n                        \\\"amount\\\": 50,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Main sol. 503c table; Solution B row\"\
    ,\n        \"exact_source_quote\": \"Solution B                              \
    \                        50.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 ml in Main sol. 503c, with its\
    \ source identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 503c: Solution C\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 3,\\n                        \\\"solution\\\
    \": \\\"Solution C\\\",\\n                        \\\"solution_id\\\": 1068,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Main sol. 503c table; Solution C row\"\
    ,\n        \"exact_source_quote\": \"Solution C                              \
    \                        10.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Main sol. 503c, with its\
    \ source identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 503c: Solution D\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 4,\\n                        \\\"solution\\\
    \": \\\"Solution D\\\",\\n                        \\\"solution_id\\\": 1065,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Main sol. 503c table; Solution D row\"\
    ,\n        \"exact_source_quote\": \"Solution D                              \
    \                         1.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1 ml in Main sol. 503c, with its\
    \ source identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 503c: Solution E\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 5,\\n                        \\\"solution\\\
    \": \\\"Solution E\\\",\\n                        \\\"solution_id\\\": 1069,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Main sol. 503c table; Solution E row\"\
    ,\n        \"exact_source_quote\": \"Solution E                              \
    \                        10.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Main sol. 503c, with its\
    \ source identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 503c: Solution F\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 6,\\n                        \\\"solution\\\
    \": \\\"Solution F\\\",\\n                        \\\"solution_id\\\": 1070,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Main sol. 503c table; Solution F row\"\
    ,\n        \"exact_source_quote\": \"Solution F                              \
    \                        10.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Main sol. 503c, with its\
    \ source identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A: KH2PO4\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.21692\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"KH2PO4\\\",\\n                \
    \        \\\"compound_id\\\": 11,\\n                        \\\"amount\\\": 0.2,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.21692,\\n                        \\\"mmol_l\\\": 1.594,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; KH2PO4 row\",\n \
    \       \"exact_source_quote\": \"KH2PO4                                     \
    \                      0.20          g\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.2 g in Solution A, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.21692\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.21692\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: NH4Cl\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": {\n      \"value\": \"0.27115\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"NH4Cl\\\",\\n                 \
    \       \\\"compound_id\\\": 42,\\n                        \\\"amount\\\": 0.25,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.27115,\\n                        \\\"mmol_l\\\": 5.06917,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; NH4Cl row\",\n  \
    \      \"exact_source_quote\": \"NH4Cl                                       \
    \                     0.25          g\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.25 g in Solution A, with its\
    \ source identity and stage. The existing direct g/L is a stock-level value and\
    \ cannot stand for the final medium; attach source evidence after restoring the\
    \ hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n \
    \   \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.27115\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.27115\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: NaCl\",\n\
    \    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"1.0846\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503capi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n \
    \       \"source_locator\": \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.0846,\\n\
    \                        \\\"mmol_l\\\": 18.5592,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF pages 1–2; Solution A table; NaCl row\",\n\
    \        \"exact_source_quote\": \"NaCl                                      \
    \                       1.00          g\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1 g in Solution A, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.0846\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0846\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: MgCl2 x\
    \ 6 H2O\",\n    \"field_path\": \"ingredients[3].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.433839\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 79,\\n                        \\\"amount\\\
    \": 0.4,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.433839,\\n                        \\\"mmol_l\\\": 2.13396,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; MgCl2 x 6 H2O row\"\
    ,\n        \"exact_source_quote\": \"MgCl2 x 6 H2O                           \
    \                         0.40          g\",\n        \"snapshot_sha256\": \"\
    5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n        \"\
    parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.4 g in Solution A, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.433839\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.433839\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: KCl\",\n\
    \    \"field_path\": \"ingredients[4].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"0.542299\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503capi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n \
    \       \"source_locator\": \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.542299,\\\
    n                        \\\"mmol_l\\\": 7.2743,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; KCl row\",\n    \
    \    \"exact_source_quote\": \"KCl                                           \
    \                   0.50          g\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.5 g in Solution A, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.542299\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.542299\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: CaCl2 x\
    \ 2 H2O\",\n    \"field_path\": \"ingredients[5].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.16269\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 7,\\n                        \\\"amount\\\
    \": 0.15,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.16269,\\n                        \\\"mmol_l\\\": 1.10662,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; CaCl2 x 2 H2O row\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O                           \
    \                         0.15          g\",\n        \"snapshot_sha256\": \"\
    5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n        \"\
    parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.15 g in Solution A, with its\
    \ source identity and stage. The existing direct g/L is a stock-level value and\
    \ cannot stand for the final medium; attach source evidence after restoring the\
    \ hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n \
    \   \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.16269\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16269\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: Trace element\
    \ solution SL-10\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"solution\\\": \\\"Trace element solution SL-10\\\"\
    ,\\n                        \\\"solution_id\\\": 595,\\n                     \
    \   \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; Trace element solution\
    \ SL-10 row\",\n        \"exact_source_quote\": \"Trace element solution SL-10\
    \                                     1.00        ml\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1 ml in Solution A, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A: Selenite-tungstate solution\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; Selenite-tungstate\
    \ solution row\",\n        \"exact_source_quote\": \"Selenite-tungstate solution\
    \                                      1.00        ml\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1 ml in Solution A, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A: Sodium resazurin\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.000542299\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"Sodium resazurin\\\",\\n      \
    \                  \\\"compound_id\\\": 1852,\\n                        \\\"attribute\\\
    \": \\\"0.1% w/v\\\",\\n                        \\\"amount\\\": 0.5,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\
    \": 0.000542299,\\n                        \\\"mmol_l\\\": 0.00215909,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; Sodium resazurin\
    \ (0.1% w/v) row\",\n        \"exact_source_quote\": \"Sodium resazurin (0.1%\
    \ w/v)                                      0.50        ml\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.5 ml in Solution A, with its\
    \ source identity and stage. The existing direct g/L is a stock-level value and\
    \ cannot stand for the final medium; attach source evidence after restoring the\
    \ hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n \
    \   \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.000542299\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000542299\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"The provider divides Solution A source grams by its nominal 0.922 L basis;\
    \ main use is 922 mL of A. Its listed liquids instead total 922.5 mL. Preserve\
    \ printed rounding and do not silently choose a measured stock or final denominator.\
    \ For resazurin only: 0.5 mL × 0.1 g/100 mL = 0.0005 g sodium resazurin per source\
    \ A batch.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A: Distilled\
    \ water\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\"\
    ,\n    \"local\": [\n      {\n        \"step_number\": 1,\n        \"action\"\
    : \"AUTOCLAVE\",\n        \"description\": \"Sparge solution A with 100% CO2 gas\
    \ for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved\
    \ separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved\
    \ under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\"\
    : 2,\n        \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 10,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 920,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution A table; Distilled water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water                         \
    \                       920.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 920 ml in Solution A, with its\
    \ source identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": [\n          {\n            \"step_number\": 1,\n     \
    \       \"action\": \"AUTOCLAVE\",\n            \"description\": \"Sparge solution\
    \ A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same\
    \ gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\
    \ Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared\
    \ under 100% N2 gas and sterilized by filtration. To complete the medium appropriate\
    \ amounts of solutions B to F are added to the sterile solution A in the sequence\
    \ as indicated. Adjust pH of complete medium to 6.8, if necessary.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"DISSOLVE\",\n            \"description\": \"First dissolve FeCl2 in the HCl,\
    \ then dilute in water, add and dissolve the other salts. Finally make up to 1000.00\
    \ ml.\"\n          }\n        ],\n        \"decision\": \"add\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution B: Na2CO3\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"50\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Na2CO3\\\",\\n                \
    \        \\\"compound_id\\\": 32,\\n                        \\\"amount\\\": 2.5,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 50,\\n                        \\\"mmol_l\\\": 471.752,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution B table; Na2CO3 row\",\n \
    \       \"exact_source_quote\": \"Na2CO3                                     \
    \                      2.50          g\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 2.5 g in Solution B, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"50\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider’s nominal 50 mL stock basis, 2.5 g / (50/1000 L) gives 50 g/L in\
    \ that stock. The source main aliquot equals that nominal stock volume, so it\
    \ would supply 2.5 g per batch, not 50 g per final liter.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Solution B: Distilled water\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"decision\": \"add\",\n    \"local\": [\n     \
    \ {\n        \"step_number\": 1,\n        \"action\": \"AUTOCLAVE\",\n       \
    \ \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make\
    \ it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. Solution B is autoclaved separately under 80%\
    \ N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2\
    \ gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\": 2,\n  \
    \      \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve FeCl2\
    \ in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 50,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution B table; Distilled water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water                         \
    \                        50.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 ml in Solution B, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": [\n          {\n            \"step_number\": 1,\n     \
    \       \"action\": \"AUTOCLAVE\",\n            \"description\": \"Sparge solution\
    \ A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same\
    \ gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\
    \ Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared\
    \ under 100% N2 gas and sterilized by filtration. To complete the medium appropriate\
    \ amounts of solutions B to F are added to the sterile solution A in the sequence\
    \ as indicated. Adjust pH of complete medium to 6.8, if necessary.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"DISSOLVE\",\n            \"description\": \"First dissolve FeCl2 in the HCl,\
    \ then dilute in water, add and dissolve the other salts. Finally make up to 1000.00\
    \ ml.\"\n          }\n        ],\n        \"decision\": \"add\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution C: Na-formate\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"200\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[3].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Na-formate\\\",\\n            \
    \            \\\"compound_id\\\": 144,\\n                        \\\"amount\\\"\
    : 2,\\n                        \\\"unit\\\": \\\"g\\\",\\n                   \
    \     \\\"g_l\\\": 200,\\n                        \\\"mmol_l\\\": 2940.86,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution C table; Na-formate row\"\
    ,\n        \"exact_source_quote\": \"Na-formate                              \
    \                         2.00          g\",\n        \"snapshot_sha256\": \"\
    5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n        \"\
    parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 2 g in Solution C, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"200\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider’s nominal 10 mL stock basis, 2 g / (10/1000 L) gives 200 g/L in\
    \ that stock. The source main aliquot equals that nominal stock volume, so it\
    \ would supply 2 g per batch, not 200 g per final liter.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Solution C: Distilled water\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"decision\": \"add\",\n    \"local\": [\n     \
    \ {\n        \"step_number\": 1,\n        \"action\": \"AUTOCLAVE\",\n       \
    \ \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make\
    \ it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. Solution B is autoclaved separately under 80%\
    \ N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2\
    \ gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\": 2,\n  \
    \      \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve FeCl2\
    \ in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[3].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution C table; Distilled water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water                         \
    \                        10.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Solution C, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": [\n          {\n            \"step_number\": 1,\n     \
    \       \"action\": \"AUTOCLAVE\",\n            \"description\": \"Sparge solution\
    \ A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same\
    \ gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\
    \ Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared\
    \ under 100% N2 gas and sterilized by filtration. To complete the medium appropriate\
    \ amounts of solutions B to F are added to the sterile solution A in the sequence\
    \ as indicated. Adjust pH of complete medium to 6.8, if necessary.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"DISSOLVE\",\n            \"description\": \"First dissolve FeCl2 in the HCl,\
    \ then dilute in water, add and dissolve the other salts. Finally make up to 1000.00\
    \ ml.\"\n          }\n        ],\n        \"decision\": \"add\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution D: Wolin's vitamin solution (10x)\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF pages 1–2; Solution D table; Wolin's vitamin\
    \ solution (10x) row\",\n        \"exact_source_quote\": \"Wolin's vitamin solution\
    \ (10x)                                   1.00        ml\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1 ml in Solution D, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution E: Na2S2O3 x 5 H2O\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"200\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 65,\\n                        \\\"amount\\\
    \": 2,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 200,\\n                        \\\"mmol_l\\\": 805.847,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution E table; Na2S2O3 x 5 H2O row\"\
    ,\n        \"exact_source_quote\": \"Na2S2O3 x 5 H2O                         \
    \                        2.00         g\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 2 g in Solution E, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"200\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider’s nominal 10 mL stock basis, 2 g / (10/1000 L) gives 200 g/L in\
    \ that stock. The source main aliquot equals that nominal stock volume, so it\
    \ would supply 2 g per batch, not 200 g per final liter.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Solution E: Distilled water\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"decision\": \"add\",\n    \"local\": [\n     \
    \ {\n        \"step_number\": 1,\n        \"action\": \"AUTOCLAVE\",\n       \
    \ \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make\
    \ it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. Solution B is autoclaved separately under 80%\
    \ N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2\
    \ gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\": 2,\n  \
    \      \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve FeCl2\
    \ in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[5].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution E table; Distilled water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water                         \
    \                       10.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Solution E, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": [\n          {\n            \"step_number\": 1,\n     \
    \       \"action\": \"AUTOCLAVE\",\n            \"description\": \"Sparge solution\
    \ A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same\
    \ gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\
    \ Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared\
    \ under 100% N2 gas and sterilized by filtration. To complete the medium appropriate\
    \ amounts of solutions B to F are added to the sterile solution A in the sequence\
    \ as indicated. Adjust pH of complete medium to 6.8, if necessary.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"DISSOLVE\",\n            \"description\": \"First dissolve FeCl2 in the HCl,\
    \ then dilute in water, add and dissolve the other salts. Finally make up to 1000.00\
    \ ml.\"\n          }\n        ],\n        \"decision\": \"add\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution F: Na2S x 9 H2O\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"30\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Na2S x 9 H2O\\\",\\n          \
    \              \\\"compound_id\\\": 54,\\n                        \\\"condition\\\
    \": \\\"\\\",\\n                        \\\"amount\\\": 0.3,\\n              \
    \          \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\\
    n                        \\\"mmol_l\\\": 124.905,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF pages 1–2; Solution F table; Na2S x 9 H2O\
    \ row\",\n        \"exact_source_quote\": \"Na2S x 9 H2O                     \
    \                               0.30         g\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.3 g in Solution F, with its source\
    \ identity and stage. The existing direct g/L is a stock-level value and cannot\
    \ stand for the final medium; attach source evidence after restoring the hierarchy.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"30\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider’s nominal 10 mL stock basis, 0.3 g / (10/1000 L) gives 30 g/L in\
    \ that stock. The source main aliquot equals that nominal stock volume, so it\
    \ would supply 0.3 g per batch, not 30 g per final liter.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Solution F: Distilled water\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"decision\": \"add\",\n    \"local\": [\n     \
    \ {\n        \"step_number\": 1,\n        \"action\": \"AUTOCLAVE\",\n       \
    \ \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make\
    \ it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. Solution B is autoclaved separately under 80%\
    \ N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2\
    \ gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\": 2,\n  \
    \      \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve FeCl2\
    \ in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[6].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Solution F table; Distilled water row\"\
    ,\n        \"exact_source_quote\": \"Distilled water                         \
    \                       10.00        ml\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Solution F, with its source\
    \ identity and stage. This source water/stock addition is absent as a structured\
    \ dose. Preserve the batch input without inventing a final-volume basis.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": [\n          {\n            \"step_number\": 1,\n     \
    \       \"action\": \"AUTOCLAVE\",\n            \"description\": \"Sparge solution\
    \ A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same\
    \ gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\
    \ Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared\
    \ under 100% N2 gas and sterilized by filtration. To complete the medium appropriate\
    \ amounts of solutions B to F are added to the sterile solution A in the sequence\
    \ as indicated. Adjust pH of complete medium to 6.8, if necessary.\"\n       \
    \   },\n          {\n            \"step_number\": 2,\n            \"action\":\
    \ \"DISSOLVE\",\n            \"description\": \"First dissolve FeCl2 in the HCl,\
    \ then dilute in water, add and dissolve the other salts. Finally make up to 1000.00\
    \ ml.\"\n          }\n        ],\n        \"decision\": \"add\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-10: HCl\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"HCl\\\",\\n                   \
    \     \\\"compound_id\\\": 68,\\n                        \\\"attribute\\\": \\\
    \"25%\\\",\\n                        \\\"amount\\\": 10,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 2.5,\\\
    n                        \\\"mmol_l\\\": 68.5683,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ HCl (25%) row\",\n        \"exact_source_quote\": \"HCl (25%)              \
    \                                        10.00        ml\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 10 ml in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[11].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"SL-10\
    \ is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis,\
    \ the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: FeCl2 x 4 H2O\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"FeCl2 x 4 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 260,\\n                        \\\"amount\\\
    \": 1.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 1.5,\\n                        \\\"mmol_l\\\": 7.54482,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ FeCl2 x 4 H2O row\",\n        \"exact_source_quote\": \"FeCl2 x 4 H2O      \
    \                                             1.50         g\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1.5 g in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"SL-10\
    \ is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis,\
    \ the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: ZnCl2\",\n    \"field_path\": \"ingredients[13].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.07\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"ZnCl2\\\",\\n                 \
    \       \\\"compound_id\\\": 64,\\n                        \\\"amount\\\": 70,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.07,\\n                        \\\"mmol_l\\\": 0.513573,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ ZnCl2 row\",\n        \"exact_source_quote\": \"ZnCl2                      \
    \                                    70.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 70 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal\
    \ A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: MnCl2 x 4 H2O\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 36,\\n                        \\\"amount\\\
    \": 100,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.1,\\n                        \\\"mmol_l\\\": 0.505293,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ MnCl2 x 4 H2O row\",\n        \"exact_source_quote\": \"MnCl2 x 4 H2O      \
    \                                          100.00        mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 100 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"SL-10\
    \ is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal A basis,\
    \ the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: H3BO3\",\n    \"field_path\": \"ingredients[15].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.006\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"H3BO3\\\",\\n                 \
    \       \\\"compound_id\\\": 37,\\n                        \\\"amount\\\": 6,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.006,\\n                        \\\"mmol_l\\\": 0.0970246,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ H3BO3 row\",\n        \"exact_source_quote\": \"H3BO3                      \
    \                                     6.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 6 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal\
    \ A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: CoCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.19\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 38,\\n                        \\\"amount\\\
    \": 190,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.19,\\n                        \\\"mmol_l\\\": 1.46335,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ CoCl2 x 6 H2O row\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O      \
    \                                          190.00        mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 190 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal\
    \ A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: CuCl2 x 2 H2O\",\n    \"field_path\": \"ingredients[17].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.002\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 39,\\n                        \\\"amount\\\
    \": 2,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                \
    \        \\\"g_l\\\": 0.002,\\n                        \\\"mmol_l\\\": 0.0117314,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ CuCl2 x 2 H2O row\",\n        \"exact_source_quote\": \"CuCl2 x 2 H2O      \
    \                                             2.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 2 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal\
    \ A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: NiCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[18].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.024\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 40,\\n                        \\\"amount\\\
    \": 24,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.024,\\n                        \\\"mmol_l\\\": 0.185187,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ NiCl2 x 6 H2O row\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O      \
    \                                            24.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 24 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal\
    \ A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: Na2MoO4 x 2 H2O\",\n    \"field_path\": \"ingredients[19].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.036\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[7].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 9,\\n                        \\\"amount\\\
    \": 36,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.036,\\n                        \\\"mmol_l\\\": 0.148791,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ Na2MoO4 x 2 H2O row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O  \
    \                                              36.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 36 mg in Trace element solution\
    \ SL-10, with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"SL-10 is explicitly made up to 1000 mL and dosed 1 mL into A. On the nominal\
    \ A basis, the main 922 mL aliquot would carry stock grams × 1/1000. HCl’s unspecified\
    \ 25% basis/density blocks an independent mass conversion; retain its 10 mL stock\
    \ dose.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace element solution\
    \ SL-10: Distilled water\",\n    \"field_path\": \"preparation_steps\",\n    \"\
    decision\": \"add\",\n    \"local\": [\n      {\n        \"step_number\": 1,\n\
    \        \"action\": \"AUTOCLAVE\",\n        \"description\": \"Sparge solution\
    \ A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same\
    \ gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\
    \ Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\
    \ Solutions C and F are autoclaved under 100% N2 gas. Solutions D and E are prepared\
    \ under 100% N2 gas and sterilized by filtration. To complete the medium appropriate\
    \ amounts of solutions B to F are added to the sterile solution A in the sequence\
    \ as indicated. Adjust pH of complete medium to 6.8, if necessary.\"\n      },\n\
    \      {\n        \"step_number\": 2,\n        \"action\": \"DISSOLVE\",\n   \
    \     \"description\": \"First dissolve FeCl2 in the HCl, then dilute in water,\
    \ add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503capi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n \
    \       \"source_locator\": \"$.data.solutions[7].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 990,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Trace element solution SL-10 table;\
    \ Distilled water row\",\n        \"exact_source_quote\": \"Distilled water  \
    \                                            990.00         ml\",\n        \"\
    snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 990 ml in Trace element solution\
    \ SL-10, with its source identity and stage. This source water/stock addition\
    \ is absent as a structured dose. Preserve the batch input without inventing a\
    \ final-volume basis.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": [\n          {\n\
    \            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\",\n   \
    \         \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min\
    \ to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Selenite-tungstate solution: NaOH\",\n    \"field_path\": \"ingredients[20].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[8].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"NaOH\\\",\\n                  \
    \      \\\"compound_id\\\": 256,\\n                        \\\"amount\\\": 0.5,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 12.5009,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Selenite-tungstate solution table;\
    \ NaOH row\",\n        \"exact_source_quote\": \"NaOH                        \
    \                                    0.50         g\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 0.5 g in Selenite-tungstate solution,\
    \ with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider’s nominal 1000 mL selenite-tungstate stock basis, its 1 mL dose\
    \ into A would contribute source stock mass × 1/1000. The listed 1000 mL water\
    \ is not independently measured final stock volume.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Selenite-tungstate solution: Na2SeO3 x 5 H2O\",\n    \"field_path\": \"ingredients[21].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.003\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[8].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 107,\\n                        \\\"amount\\\
    \": 3,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                \
    \        \\\"g_l\\\": 0.003,\\n                        \\\"mmol_l\\\": 0.0114062,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Selenite-tungstate solution table;\
    \ Na2SeO3 x 5 H2O row\",\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O  \
    \                                               3.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 3 mg in Selenite-tungstate solution,\
    \ with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[21].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider’s nominal 1000 mL selenite-tungstate stock basis, its 1 mL\
    \ dose into A would contribute source stock mass × 1/1000. The listed 1000 mL\
    \ water is not independently measured final stock volume.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Selenite-tungstate solution: Na2WO4 x 2 H2O\",\n  \
    \  \"field_path\": \"ingredients[22].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"0.004\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive503capi\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n \
    \       \"source_locator\": \"$.data.solutions[8].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 249,\\n                        \\\"amount\\\": 4,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.004,\\n                        \\\"mmol_l\\\": 0.0121267,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Selenite-tungstate solution table;\
    \ Na2WO4 x 2 H2O row\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O    \
    \                                              4.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 4 mg in Selenite-tungstate solution,\
    \ with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[22].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider’s nominal 1000 mL selenite-tungstate stock basis, its 1 mL\
    \ dose into A would contribute source stock mass × 1/1000. The listed 1000 mL\
    \ water is not independently measured final stock volume.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Selenite-tungstate solution: Distilled water\",\n \
    \   \"field_path\": \"preparation_steps\",\n    \"decision\": \"add\",\n    \"\
    local\": [\n      {\n        \"step_number\": 1,\n        \"action\": \"AUTOCLAVE\"\
    ,\n        \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45\
    \ min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\": 2,\n  \
    \      \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve FeCl2\
    \ in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[8].recipe[3]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 4,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 1000,\\n                        \\\"\
    unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n       \
    \             }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Selenite-tungstate solution table;\
    \ Distilled water row\",\n        \"exact_source_quote\": \"Distilled water  \
    \                                           1000.00         ml\",\n        \"\
    snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1000 ml in Selenite-tungstate solution,\
    \ with its source identity and stage. This source water/stock addition is absent\
    \ as a structured dose. Preserve the batch input without inventing a final-volume\
    \ basis.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": [\n          {\n            \"step_number\"\
    : 1,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\"\n          },\n          {\n            \"step_number\": 2,\n\
    \            \"action\": \"DISSOLVE\",\n            \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n          }\n        ],\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Biotin\",\n    \"field_path\": \"ingredients[23].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Biotin\\\",\\n                \
    \        \\\"compound_id\\\": 46,\\n                        \\\"amount\\\": 20,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.0818632,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Biotin row\",\n        \"exact_source_quote\": \"Biotin                    \
    \                                     20.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 20 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Folic acid\",\n    \"field_path\": \"ingredients[24].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Folic acid\\\",\\n            \
    \            \\\"compound_id\\\": 138,\\n                        \\\"amount\\\"\
    : 20,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.0453104,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Folic acid row\",\n        \"exact_source_quote\": \"Folic acid            \
    \                                         20.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 20 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[24].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Pyridoxine hydrochloride\",\n    \"field_path\"\
    : \"ingredients[25].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                        \\\"\
    compound_id\\\": 519,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.486287,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Pyridoxine hydrochloride row\",\n        \"exact_source_quote\": \"Pyridoxine\
    \ hydrochloride                                     100.00        mg\",\n    \
    \    \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 100 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"On\
    \ the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Thiamine HCl\",\n    \"field_path\": \"ingredients[26].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"Thiamine HCl\\\",\\n          \
    \              \\\"compound_id\\\": 1207,\\n                        \\\"amount\\\
    \": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.148236,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Thiamine HCl row\",\n        \"exact_source_quote\": \"Thiamine HCl        \
    \                                           50.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[26].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Riboflavin\",\n    \"field_path\": \"ingredients[27].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.05\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Riboflavin\\\",\\n            \
    \            \\\"compound_id\\\": 136,\\n                        \\\"amount\\\"\
    : 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.132837,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Riboflavin row\",\n        \"exact_source_quote\": \"Riboflavin            \
    \                                         50.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[27].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Nicotinic acid\",\n    \"field_path\": \"\
    ingredients[28].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"compound_id\\\
    \": 139,\\n                        \\\"amount\\\": 50,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.406141,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x)\
    \ table; Nicotinic acid row\",\n        \"exact_source_quote\": \"Nicotinic acid\
    \                                                 50.00       mg\",\n        \"\
    snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[28].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Calcium D-(+)-pantothenate\",\n    \"field_path\"\
    : \"ingredients[29].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Calcium D-(+)-pantothenate\\\",\\n                        \\\
    \"compound_id\\\": 1512,\\n                        \\\"amount\\\": 50,\\n    \
    \                    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"\
    g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.209846,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Calcium D-(+)-pantothenate row\",\n        \"exact_source_quote\": \"Calcium\
    \ D-(+)-pantothenate                                     50.00       mg\",\n \
    \       \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[29].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Vitamin B12\",\n    \"field_path\": \"ingredients[30].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.001\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"Vitamin B12\\\",\\n           \
    \             \\\"compound_id\\\": 18,\\n                        \\\"amount\\\"\
    : 1,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                  \
    \      \\\"g_l\\\": 0.001,\\n                        \\\"mmol_l\\\": 0.00073779,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Vitamin B12 row\",\n        \"exact_source_quote\": \"Vitamin B12          \
    \                                           1.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[30].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): p-Aminobenzoic acid\",\n    \"field_path\"\
    : \"ingredients[31].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                        \\\"compound_id\\\
    \": 47,\\n                        \\\"amount\\\": 50,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\n\
    \                        \\\"mmol_l\\\": 0.364591,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x)\
    \ table; p-Aminobenzoic acid row\",\n        \"exact_source_quote\": \"p-Aminobenzoic\
    \ acid                                            50.00       mg\",\n        \"\
    snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[31].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): (DL)-alpha-Lipoic acid\",\n    \"field_path\"\
    : \"ingredients[32].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"(DL)-alpha-Lipoic acid\\\",\\n                        \\\"\
    compound_id\\\": 252,\\n                        \\\"amount\\\": 50,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.05,\\n                        \\\"mmol_l\\\": 0.24233,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ (DL)-alpha-Lipoic acid row\",\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic\
    \ acid                                         50.00       mg\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 50 mg in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. The existing direct g/L is a stock-level\
    \ value and cannot stand for the final medium; attach source evidence after restoring\
    \ the hierarchy.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[32].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"On the provider’s nominal 1000 mL vitamin-stock basis, the 1 mL dose constituting\
    \ Solution D would contribute source milligrams × 1/1000 milligrams per main batch.\
    \ The 10x label describes this exact printed formulation; do not apply an additional\
    \ tenfold multiplier or count D and its stock twice.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x): Distilled water\",\n    \"field_path\": \"\
    preparation_steps\",\n    \"decision\": \"add\",\n    \"local\": [\n      {\n\
    \        \"step_number\": 1,\n        \"action\": \"AUTOCLAVE\",\n        \"description\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\"\n      },\n      {\n        \"step_number\": 2,\n        \"\
    action\": \"DISSOLVE\",\n        \"description\": \"First dissolve FeCl2 in the\
    \ HCl, then dilute in water, add and dissolve the other salts. Finally make up\
    \ to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[9].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\",\n   \
    \     \"source_locator\": \"PDF pages 1–2; Wolin's vitamin solution (10x) table;\
    \ Distilled water row\",\n        \"exact_source_quote\": \"Distilled water  \
    \                                           1000.00         ml\",\n        \"\
    snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain 1000 ml in Wolin's vitamin solution\
    \ (10x), with its source identity and stage. This source water/stock addition\
    \ is absent as a structured dose. Preserve the batch input without inventing a\
    \ final-volume basis.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": [\n          {\n\
    \            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\",\n   \
    \         \"description\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min\
    \ to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A 100% CO2, 30–45 minutes\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": \"Sparge solution A with\
    \ 100% CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved\
    \ separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved\
    \ under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"The exact gas fraction and duration survive\
    \ in local prose without attached claim evidence; stock identity still needs restoration.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to\
    \ make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\",\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Solution B 80% N2/20% CO2\",\n  \
    \  \"field_path\": \"preparation_steps[0].description\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": \"Sparge solution A with 100% CO2 gas for 30\
    \ – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately\
    \ under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under\
    \ 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere.\"\
    ,\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the separate B atmosphere and\
    \ sterilization, not an inferred uniform procedure.\",\n    \"action_taken\":\
    \ \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to\
    \ make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\",\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Solutions C/F 100% N2\",\n    \"\
    field_path\": \"preparation_steps[0].description\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make\
    \ it anoxic, distribute under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave. Solution B is autoclaved separately under 80%\
    \ N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100% N2\
    \ gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"C and F are autoclaved under 100% N2 gas.\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"The existing text supports this specific\
    \ pair and gas fraction; no autoclave cycle is supplied.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to\
    \ make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\",\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Solutions D/E 100% N2 and filtration\"\
    ,\n    \"field_path\": \"preparation_steps[0].description\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": \"Sparge solution A with 100% CO2 gas for\
    \ 30 – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately\
    \ under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under\
    \ 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"Solutions D and E are prepared under 100% N2\\ngas and sterilized by filtration.\"\
    ,\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Filtration is explicitly present in the\
    \ existing text. Preserve it while structuring the missing stock hierarchy; do\
    \ not report it as absent.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Completed medium pH 6.8\",\n    \"\
    field_path\": \"ph_value\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : 6.8,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz503c\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"complete medium to 6.8, if necessary.\",\n        \"snapshot_sha256\": \"\
    5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n        \"\
    parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"The numeric pH is supported; retain the\
    \ source’s if-necessary adjustment qualification and attach evidence.\",\n   \
    \ \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ph_value\"\
    ,\n        \"stored\": 6.8,\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.8,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL-10 final makeup 1000 mL\",\n    \"field_path\": \"preparation_steps[1].description\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": \"First dissolve FeCl2 in the\
    \ HCl, then dilute in water, add and dissolve the other salts. Finally make up\
    \ to 1000.00 ml.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 2 SL-10 preparation\",\n        \"exact_source_quote\"\
    : \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the endpoint but restore SL-10\
    \ stock scope rather than main-medium placement.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"First dissolve FeCl2 in the HCl, then dilute in water,\
    \ add and dissolve the other salts. Finally make up to 1000.00 ml.\",\n      \
    \  \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Unspecified autoclave\
    \ cycle\",\n    \"field_path\": \"preparation_steps[0].description\",\n    \"\
    decision\": \"not_quantified\",\n    \"local\": \"Sparge solution A with 100%\
    \ CO2 gas for 30 – 45 min to make it anoxic, distribute under same gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved\
    \ separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved\
    \ under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.\"\
    ,\n        \"snapshot_sha256\": \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\"\
    ,\n        \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"No temperature or duration is given for\
    \ autoclaving; do not insert a generic cycle.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to\
    \ make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\",\n        \"decision\": \"not_quantified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"not_quantified\"\n      }\n    ]\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Unquantified pH adjustment\",\n \
    \   \"field_path\": \"preparation_steps[0].description\",\n    \"decision\": \"\
    not_quantified\",\n    \"local\": \"Sparge solution A with 100% CO2 gas for 30\
    \ – 45 min to make it anoxic, distribute under same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately\
    \ under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under\
    \ 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz503c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503c.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1 preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH of\\ncomplete medium to 6.8, if necessary.\",\n        \"snapshot_sha256\"\
    : \"5628d25083788581244cfb96689b50180816445298a65f1618d5028832c70ec3\",\n    \
    \    \"parsed_text_sha256\": \"5cc15c26cae9a05c4abb35b5574bc72ad335afd9293aca7689f247b15a5b5eca\"\
    \n      }\n    ],\n    \"rationale\": \"The endpoint is specified but adjustment\
    \ reagent identity, strength and dose are not. Do not invent a titrant amount.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Sparge solution A with 100% CO2 gas for 30 – 45 min to\
    \ make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\",\n        \"decision\": \"not_quantified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Sparge solution A with 100% CO2 gas for 30 – 45 min to make it anoxic, distribute\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas\
    \ atmosphere. Solutions C and F are autoclaved under 100% N2 gas. Solutions D\
    \ and E are prepared under 100% N2 gas and sterilized by filtration. To complete\
    \ the medium appropriate amounts of solutions B to F are added to the sterile\
    \ solution A in the sequence as indicated. Adjust pH of complete medium to 6.8,\
    \ if necessary.\",\n        \"decision\": \"not_quantified\"\n      }\n    ]\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Main nominal total from six source\
    \ aliquots\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\": \"\
    add\",\n    \"local\": [\n      {\n        \"step_number\": 1,\n        \"action\"\
    : \"AUTOCLAVE\",\n        \"description\": \"Sparge solution A with 100% CO2 gas\
    \ for 30 – 45 min to make it anoxic, distribute under same gas atmosphere into\
    \ anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved\
    \ separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved\
    \ under 100% N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized\
    \ by filtration. To complete the medium appropriate amounts of solutions B to\
    \ F are added to the sterile solution A in the sequence as indicated. Adjust pH\
    \ of complete medium to 6.8, if necessary.\"\n      },\n      {\n        \"step_number\"\
    : 2,\n        \"action\": \"DISSOLVE\",\n        \"description\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\"\n      }\n    ],\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"mediadive503capi\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 1,\\n                        \\\"solution\\\
    \": \\\"Solution A\\\",\\n                        \\\"solution_id\\\": 1063,\\\
    n                        \\\"amount\\\": 922,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Solution B\\\",\\n                        \\\"solution_id\\\"\
    : 1067,\\n                        \\\"amount\\\": 50,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    solution\\\": \\\"Solution C\\\",\\n                        \\\"solution_id\\\"\
    : 1068,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    solution\\\": \\\"Solution D\\\",\\n                        \\\"solution_id\\\"\
    : 1065,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n\
    \                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    solution\\\": \\\"Solution E\\\",\\n                        \\\"solution_id\\\"\
    : 1069,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Solution F\\\",\\n                        \\\"solution_id\\\"\
    : 1070,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[0].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1003\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      }\n    ],\n    \"rationale\": \"The six listed aliquots sum to the provider’s\
    \ declared 1003 mL. This is a nominal source sum, not a measurement of the completed\
    \ medium after pH adjustment.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Sparge solution A with 100% CO2 gas for 30 –\
    \ 45 min to make it anoxic, distribute under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Solution B is autoclaved separately under\
    \ 80% N2 and 20% CO2 gas atmosphere. Solutions C and F are autoclaved under 100%\
    \ N2 gas. Solutions D and E are prepared under 100% N2 gas and sterilized by filtration.\
    \ To complete the medium appropriate amounts of solutions B to F are added to\
    \ the sterile solution A in the sequence as indicated. Adjust pH of complete medium\
    \ to 6.8, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          }\n        ],\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"922 + 50 + 10 + 1\
    \ + 10 + 10 = 1003 mL. No unconditional final g/L normalization is proposed.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Solution A declared versus listed\
    \ liquid volume\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"conflict\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive503capi\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"solution\\\": \\\"Trace element solution SL-10\\\"\
    ,\\n                        \\\"solution_id\\\": 595,\\n                     \
    \   \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    solution\\\": \\\"Selenite-tungstate solution\\\",\\n                        \\\
    \"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.000542299,\\n       \
    \                 \\\"mmol_l\\\": 0.00215909,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 920,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      },\n      {\n        \"source_key\": \"mediadive503capi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/503c\",\n        \"source_locator\"\
    : \"$.data.solutions[1].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 922\",\n        \"snapshot_sha256\": \"8aef6f4ffe47bdb22400714a4a4a0bc27eaa57fbc4ccd6d27c9060af9d79ad6f\"\
    \n      }\n    ],\n    \"rationale\": \"The provider declares 922 mL, whereas\
    \ water and three liquid additions sum 922.5 mL. The primary does not specify\
    \ a final A makeup. Preserve the discrepancy.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      }\n    ],\n    \"arithmetic\": \"920 + 1 + 1 + 0.5 = 922.5 mL\
    \ versus 922 mL declared; no measured denominator selected.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: ammonifex-thiophilus-stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Separate stock strengths replace the final medium formulation
  description: All 33 direct concentrations are drawn from A–F or nested trace/vitamin
    stocks, while the six main aliquots and nested doses are absent as local stock
    objects. For example, 2 g formate in 10 mL stock becomes 200 g/L directly, and
    2.5 g carbonate in 50 mL becomes 50 g/L. This changes formulation identity. The
    source’s 922 versus 922.5 mL A discrepancy and nominal final sum must remain explicit.
  target_ids:
  - CultureMech:001633
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
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
  issue_key: ammonifex-thiophilus-salt-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two supplied forms are narrowed to different chemical entities
  description: The source specifies sodium resazurin and nickel chloride hexahydrate.
    Local primary CHEBI:8806 is neutral resazurin without sodium, and CHEBI:34887
    is anhydrous nickel dichloride in primary and secondary slots. Resazurin has no
    asserted current secondary slot, so no nonexistent link is included in this finding.
  target_ids:
  - CultureMech:001633
  field_paths:
  - ingredients[6].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi8806
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
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
  issue_key: ammonifex-thiophilus-high-metal-unsupported
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: High-metal classification lacks a valid source-aware calculation
  description: The record’s high_metal:true has no attached quantitative justification.
    The schema’s millimolar percentile meaning is not established by the inspected
    analyzer’s approximate/default mass-unit conversion, and this record supplies
    flattened stock strengths rather than final medium concentrations. This review
    does not infer that the Boolean must be false; its present scientific support
    is insufficient.
  target_ids:
  - CultureMech:001633
  field_paths:
  - high_metal
  evidence_ids:
  - record
  - owner-0
  - primary
  - writer-0
  - writer-1
  - writer-2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
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
  description: Restore A–F and their nested SL-10, selenite-tungstate and vitamin
    doses in the maintained owner, preserving original source amounts/units and named
    preparation stages. Retain the existing filtration instructions and relocate SL-10
    makeup. Reconcile volume declarations before proposing final concentrations; regenerate
    only after owner verification.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
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
  description: Resolve supported source-form identities without inventing replacement
    CURIEs or changing the source stock masses. Reconcile each actual asserted slot
    separately; preserve the correctly scoped D-pantothenate and unspecified DL-lipoic
    metadata.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
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
  description: Reassess the annotation after correcting stock dilution and establishing
    source-specific units/forms. If retained, document a dimensionally valid total
    and the applicable percentile population; otherwise explicitly withdraw unsupported
    classification through separate curation. Do not rerun a bulk label writer as
    a substitute for this review.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/ammonifex_thiophilus_medium.yaml
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
- All amounts are source batch quantities or provider-declared stock concentrations.
  No measured final stock or completed-medium volume, HCl percent basis/density or
  pH titrant amount is inferred.
- The source’s 10x vitamin label is not applied as an extra multiplier. Independent
  stock endpoints support their own definitions, not unqualified final-medium quantities.
- The metal-analysis code was read statically. No corpus-wide analysis or historical
  label-generation replay was performed, and no numerical replacement threshold or
  Boolean is asserted.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-026
- generated-medium
```
