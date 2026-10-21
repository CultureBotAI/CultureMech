# Source and formulation review: aciduliprofundum_medium (CultureMech:003735)

- Review: 20261021T114752Z-culturemech-003735-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:43:20Z
- Finished UTC: 2026-10-21T11:47:52Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ/KOMODO 1083 identity is recoverable, but historical salt sums and partial stock nesting leave the formulation scientifically incorrect. The generated target also loses preparation and nesting, all three stored bacterial relationship paths are broken, and the historical numeric MIM link remains unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 182; batch 019 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eighteen task batches contain 180 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 182 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003735 | data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml | generated | aciduliprofundum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003735 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003735 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/182/strict.tsv |
| validate-terms | passed | True | CultureMech:003735 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003735 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003735 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Historical MIM000198 correspondence | unavailable | True | CultureMech:003735 | The exact historical mapping for asserted MIM000198 could not be verified from the complete pinned public catalog/tree or ignored-inclusive local references. Current sodium-selenate CHEBI metadata does not establish a deprecated numeric link. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003735.

The four documented recipes completed; interpret the scope of each separately.

### Exact accession and all maintained contributors

identity: concern. Targets: CultureMech:003735.

KOMODO 1083 explicitly links DSMZ 1083; the exact main and stock endpoints resolve. Both distinct stable normalized owner IDs are present under archaea. Source identity does not certify the historical summed quantities, nesting, or paths. The catalog aerobic=true conflicts with the primary anoxic preparation; it is attributed metadata, not independent oxygen-growth evidence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003735.

105 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[0].concentration",
    "ingredient": "NaCl",
    "stored": {
      "value": "39.97",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 30,
      "main_source_unit": "g",
      "main_provider_g_per_L": 29.97,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 10,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: NaCl",
        "exact_source_quote": "NaCl 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.97,\n                        \"mmol_l\": 512.834,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: NaCl",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 171.116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[1].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "stored": {
      "value": "33.4965",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 3.5,
      "main_source_unit": "g",
      "main_provider_g_per_L": 3.4965,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 30,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 3.50 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.4965,\n                        \"mmol_l\": 14.186,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 121.716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgCl2 x 6 H2O",
    "stored": {
      "value": "2.74725",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "2.74725",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: MgCl2 x 6 H2O",
        "exact_source_quote": "MgCl2 x 6 H2O 2.75 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 2.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.74725,\n                        \"mmol_l\": 13.5131,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[3].concentration",
    "ingredient": "CaCl2 x 2 H2O",
    "stored": {
      "value": "1.37962",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 0.38,
      "main_source_unit": "g",
      "main_provider_g_per_L": 0.37962,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 1,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 0.38 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.38,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.37962,\n                        \"mmol_l\": 2.58219,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 6.80203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[4].concentration",
    "ingredient": "KCl",
    "stored": {
      "value": "0.32967",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.32967",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: KCl",
        "exact_source_quote": "KCl 0.33 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.32967,\n                        \"mmol_l\": 4.42214,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[5].concentration",
    "ingredient": "NaBr",
    "stored": {
      "value": "0.04995",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.04995",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: NaBr",
        "exact_source_quote": "NaBr 0.05 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.04995,\n                        \"mmol_l\": 0.48547,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[6].concentration",
    "ingredient": "(NH4)2SO4",
    "stored": {
      "value": "0.0999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: (NH4)2SO4",
        "exact_source_quote": "(NH4)2SO4 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\": 0.756017,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[7].concentration",
    "ingredient": "KH2PO4",
    "stored": {
      "value": "0.27972",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.27972",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: KH2PO4",
        "exact_source_quote": "KH2PO4 0.28 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.28,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.27972,\n                        \"mmol_l\": 2.05548,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Sodium resazurin",
    "stored": {
      "value": "0.0004995",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0004995",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sodium resazurin",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[9].concentration",
    "ingredient": "Na3-citrate",
    "stored": {
      "value": "2.93706",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "2.93706",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Na3-citrate",
        "exact_source_quote": "Na3-citrate 2.94 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na3-citrate\",\n                        \"compound_id\": 205,\n                        \"amount\": 2.94,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.93706,\n                        \"mmol_l\": 11.3809,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Yeast extract",
    "stored": {
      "value": "0.999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Yeast extract",
        "exact_source_quote": "Yeast extract 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[11].concentration",
    "ingredient": "Tryptone",
    "stored": {
      "value": "0.999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Tryptone",
        "exact_source_quote": "Tryptone (BD Bacto) 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD Bacto\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[12].concentration",
    "ingredient": "Sulfur",
    "stored": {
      "value": "9.99001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "9.99001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sulfur",
        "exact_source_quote": "Sulfur (powdered) 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.99001,\n                        \"mmol_l\": 311.506,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[13].concentration",
    "ingredient": "Na2S x 9 H2O",
    "stored": {
      "value": "0.499501",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.499501",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Na2S x 9 H2O",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499501,\n                        \"mmol_l\": 2.07967,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[14].concentration",
    "ingredient": "MnSO4 x H2O",
    "stored": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "5",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MnSO4 x H2O",
        "exact_source_quote": "MnSO4 x H2O 5.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 29.583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[15].concentration",
    "ingredient": "FeSO4 x 7 H2O",
    "stored": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: FeSO4 x 7 H2O",
        "exact_source_quote": "FeSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 3.59693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[16].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "stored": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "1.8",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl2 x 6 H2O 1.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 13.8633,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[17].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "stored": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "1.8",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 1.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 6.25954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[18].concentration",
    "ingredient": "CuSO4 x 5 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO4 x 5 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[19].concentration",
    "ingredient": "AlK(SO4)2 x 12 H2O",
    "stored": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.18",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: AlK(SO4)2 x 12 H2O",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.18 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.379436,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[20].concentration",
    "ingredient": "H3BO3",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: H3BO3",
        "exact_source_quote": "H3BO3 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.61708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[21].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[22].concentration",
    "ingredient": "(NH4)2Ni(SO4)2 x 6 H2O",
    "stored": {
      "value": "2.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "2.8",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: (NH4)2Ni(SO4)2 x 6 H2O",
        "exact_source_quote": "(NH4)2Ni(SO4)2 x 6 H2O 2.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"(NH4)2Ni(SO4)2 x 6 H2O\",\n                        \"compound_id\": 739,\n                        \"amount\": 2.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.8,\n                        \"mmol_l\": 7.08884,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[23].concentration",
    "ingredient": "Na2WO4 x 2 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2WO4 x 2 H2O",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.303168,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[24].concentration",
    "ingredient": "Na2SeO4",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2SeO4",
        "exact_source_quote": "Na2SeO4 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO4\",\n                        \"compound_id\": 375,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.529241,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "NaCl",
    "stored": {
      "value": "39.97",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 30,
      "main_source_unit": "g",
      "main_provider_g_per_L": 29.97,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 10,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: NaCl",
        "exact_source_quote": "NaCl 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.97,\n                        \"mmol_l\": 512.834,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: NaCl",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 171.116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "stored": {
      "value": "33.4965",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 3.5,
      "main_source_unit": "g",
      "main_provider_g_per_L": 3.4965,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 30,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 3.50 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.4965,\n                        \"mmol_l\": 14.186,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 121.716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgCl2 x 6 H2O",
    "stored": {
      "value": "2.74725",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "2.74725",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: MgCl2 x 6 H2O",
        "exact_source_quote": "MgCl2 x 6 H2O 2.75 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 2.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.74725,\n                        \"mmol_l\": 13.5131,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "CaCl2 x 2 H2O",
    "stored": {
      "value": "1.37962",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 0.38,
      "main_source_unit": "g",
      "main_provider_g_per_L": 0.37962,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 1,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 0.38 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.38,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.37962,\n                        \"mmol_l\": 2.58219,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 6.80203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "KCl",
    "stored": {
      "value": "0.32967",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.32967",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: KCl",
        "exact_source_quote": "KCl 0.33 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.32967,\n                        \"mmol_l\": 4.42214,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "NaBr",
    "stored": {
      "value": "0.04995",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.04995",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: NaBr",
        "exact_source_quote": "NaBr 0.05 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.04995,\n                        \"mmol_l\": 0.48547,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "(NH4)2SO4",
    "stored": {
      "value": "0.0999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: (NH4)2SO4",
        "exact_source_quote": "(NH4)2SO4 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\": 0.756017,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "KH2PO4",
    "stored": {
      "value": "0.27972",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.27972",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: KH2PO4",
        "exact_source_quote": "KH2PO4 0.28 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.28,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.27972,\n                        \"mmol_l\": 2.05548,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Sodium resazurin",
    "stored": {
      "value": "0.0004995",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0004995",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sodium resazurin",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[9].concentration",
    "ingredient": "Na3-citrate",
    "stored": {
      "value": "2.93706",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "2.93706",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Na3-citrate",
        "exact_source_quote": "Na3-citrate 2.94 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na3-citrate\",\n                        \"compound_id\": 205,\n                        \"amount\": 2.94,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.93706,\n                        \"mmol_l\": 11.3809,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Yeast extract",
    "stored": {
      "value": "0.999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Yeast extract",
        "exact_source_quote": "Yeast extract 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[11].concentration",
    "ingredient": "Tryptone",
    "stored": {
      "value": "0.999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Tryptone",
        "exact_source_quote": "Tryptone (BD Bacto) 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD Bacto\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[12].concentration",
    "ingredient": "Sulfur",
    "stored": {
      "value": "9.99001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "9.99001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sulfur",
        "exact_source_quote": "Sulfur (powdered) 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.99001,\n                        \"mmol_l\": 311.506,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[13].concentration",
    "ingredient": "Na2S x 9 H2O",
    "stored": {
      "value": "0.499501",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.499501",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Na2S x 9 H2O",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499501,\n                        \"mmol_l\": 2.07967,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[14].concentration",
    "ingredient": "CuSO4 x 5 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO4 x 5 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[15].concentration",
    "ingredient": "AlK(SO4)2 x 12 H2O",
    "stored": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.18",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: AlK(SO4)2 x 12 H2O",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.18 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.379436,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[16].concentration",
    "ingredient": "H3BO3",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: H3BO3",
        "exact_source_quote": "H3BO3 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.61708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[17].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[18].concentration",
    "ingredient": "(NH4)2Ni(SO4)2 x 6 H2O",
    "stored": {
      "value": "2.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "2.8",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: (NH4)2Ni(SO4)2 x 6 H2O",
        "exact_source_quote": "(NH4)2Ni(SO4)2 x 6 H2O 2.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"(NH4)2Ni(SO4)2 x 6 H2O\",\n                        \"compound_id\": 739,\n                        \"amount\": 2.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.8,\n                        \"mmol_l\": 7.08884,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[19].concentration",
    "ingredient": "Na2WO4 x 2 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2WO4 x 2 H2O",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.303168,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[20].concentration",
    "ingredient": "Na2SeO4",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2SeO4",
        "exact_source_quote": "Na2SeO4 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO4\",\n                        \"compound_id\": 375,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.529241,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions[0].composition[0].concentration",
    "ingredient": "MnSO4 x H2O",
    "stored": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "5",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MnSO4 x H2O",
        "exact_source_quote": "MnSO4 x H2O 5.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 29.583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions[0].composition[1].concentration",
    "ingredient": "FeSO4 x 7 H2O",
    "stored": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: FeSO4 x 7 H2O",
        "exact_source_quote": "FeSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 3.59693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions[0].composition[2].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "stored": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.8",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl2 x 6 H2O 1.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 13.8633,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions[0].composition[3].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "stored": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.8",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 1.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 6.25954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "NaCl",
    "stored": {
      "value": "39.97",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 30,
      "main_source_unit": "g",
      "main_provider_g_per_L": 29.97,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 10,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: NaCl",
        "exact_source_quote": "NaCl 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.97,\n                        \"mmol_l\": 512.834,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: NaCl",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 171.116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "stored": {
      "value": "33.4965",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 3.5,
      "main_source_unit": "g",
      "main_provider_g_per_L": 3.4965,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 30,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 3.50 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.4965,\n                        \"mmol_l\": 14.186,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 121.716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgCl2 x 6 H2O",
    "stored": {
      "value": "2.74725",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "2.74725",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: MgCl2 x 6 H2O",
        "exact_source_quote": "MgCl2 x 6 H2O 2.75 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 2.75,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.74725,\n                        \"mmol_l\": 13.5131,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "CaCl2 x 2 H2O",
    "stored": {
      "value": "1.37962",
      "unit": "G_PER_L"
    },
    "proposed": {
      "main_source_amount": 0.38,
      "main_source_unit": "g",
      "main_provider_g_per_L": 0.37962,
      "main_provider_volume_ml": 1001,
      "separate_stock_g_per_L": 1,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 0.38 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.38,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.37962,\n                        \"mmol_l\": 2.58219,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      },
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 6.80203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stored value combines main-provider g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct main mass and complete stock composition/dose; do not claim the primary water quantity proves a final mixed volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "KCl",
    "stored": {
      "value": "0.32967",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.32967",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: KCl",
        "exact_source_quote": "KCl 0.33 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.32967,\n                        \"mmol_l\": 4.42214,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "NaBr",
    "stored": {
      "value": "0.04995",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.04995",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: NaBr",
        "exact_source_quote": "NaBr 0.05 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.04995,\n                        \"mmol_l\": 0.48547,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "(NH4)2SO4",
    "stored": {
      "value": "0.0999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: (NH4)2SO4",
        "exact_source_quote": "(NH4)2SO4 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0999001,\n                        \"mmol_l\": 0.756017,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "KH2PO4",
    "stored": {
      "value": "0.27972",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.27972",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: KH2PO4",
        "exact_source_quote": "KH2PO4 0.28 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.28,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.27972,\n                        \"mmol_l\": 2.05548,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Sodium resazurin",
    "stored": {
      "value": "0.0004995",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0004995",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sodium resazurin",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[9].concentration",
    "ingredient": "Na3-citrate",
    "stored": {
      "value": "2.93706",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "2.93706",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Na3-citrate",
        "exact_source_quote": "Na3-citrate 2.94 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na3-citrate\",\n                        \"compound_id\": 205,\n                        \"amount\": 2.94,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.93706,\n                        \"mmol_l\": 11.3809,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Yeast extract",
    "stored": {
      "value": "0.999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Yeast extract",
        "exact_source_quote": "Yeast extract 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[11].concentration",
    "ingredient": "Tryptone",
    "stored": {
      "value": "0.999001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.999001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Tryptone",
        "exact_source_quote": "Tryptone (BD Bacto) 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD Bacto\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.999001,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[12].concentration",
    "ingredient": "Sulfur",
    "stored": {
      "value": "9.99001",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "9.99001",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sulfur",
        "exact_source_quote": "Sulfur (powdered) 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.99001,\n                        \"mmol_l\": 311.506,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[13].concentration",
    "ingredient": "Na2S x 9 H2O",
    "stored": {
      "value": "0.499501",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.499501",
      "unit": "G_PER_L",
      "basis": "Provider-declared 1001 ml main solution, not measured final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Na2S x 9 H2O",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499501,\n                        \"mmol_l\": 2.07967,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The existing provider-derived value has no attached evidence. Keep the original source amount/unit and explicit provider basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50 ml dose; this mass equivalence alone is not its full preparation representation."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[14].concentration",
    "ingredient": "CuSO4 x 5 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO4 x 5 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[15].concentration",
    "ingredient": "AlK(SO4)2 x 12 H2O",
    "stored": {
      "value": "0.18",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.18",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: AlK(SO4)2 x 12 H2O",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.18 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.379436,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[16].concentration",
    "ingredient": "H3BO3",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: H3BO3",
        "exact_source_quote": "H3BO3 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 1.61708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[17].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[18].concentration",
    "ingredient": "(NH4)2Ni(SO4)2 x 6 H2O",
    "stored": {
      "value": "2.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "2.8",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: (NH4)2Ni(SO4)2 x 6 H2O",
        "exact_source_quote": "(NH4)2Ni(SO4)2 x 6 H2O 2.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"(NH4)2Ni(SO4)2 x 6 H2O\",\n                        \"compound_id\": 739,\n                        \"amount\": 2.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.8,\n                        \"mmol_l\": 7.08884,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[19].concentration",
    "ingredient": "Na2WO4 x 2 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2WO4 x 2 H2O",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.303168,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[20].concentration",
    "ingredient": "Na2SeO4",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "stock_value": "0.1",
      "stock_unit": "G_PER_L",
      "stock_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Na2SeO4",
        "exact_source_quote": "Na2SeO4 0.10 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO4\",\n                        \"compound_id\": 375,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.529241,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "A stock strength is still in direct ingredients. Move its representation into the complete mineral-elixir stock, preserving dose and scope instead of treating it as a main-medium amount."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "solutions[0].composition[0].concentration",
    "ingredient": "MnSO4 x H2O",
    "stored": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "5",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MnSO4 x H2O",
        "exact_source_quote": "MnSO4 x H2O 5.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 29.583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "solutions[0].composition[1].concentration",
    "ingredient": "FeSO4 x 7 H2O",
    "stored": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: FeSO4 x 7 H2O",
        "exact_source_quote": "FeSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 3.59693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "solutions[0].composition[2].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "stored": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.8",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl2 x 6 H2O 1.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 13.8633,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "solutions[0].composition[3].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "stored": {
      "value": "1.8",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.8",
      "unit": "G_PER_L",
      "basis": "Existing mineral-elixir composition, provider 1000 ml stock volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 1.80 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 6.25954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "This owner already places the unchanged strength under its stock composition, but no attached matching amount evidence exists. It is not verified by the correctly nested position alone."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "solutions",
    "stored": null,
    "ingredient": "Wolfe's mineral elixir addition",
    "proposed": {
      "amount": 1,
      "unit": "ml",
      "basis": "Exact source listed batch; provider main.volume 1001 ml"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Wolfe's mineral elixir",
        "exact_source_quote": "Wolfe's mineral elixir 1.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Wolfe's mineral elixir\",\n                        \"solution_id\": 1605,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The source gives 1 ml per listed batch. Existing owner 1 ML_PER_L and per-litre wording need explicit qualification against provider 1001 ml; the source does not independently measure a final litre. Target omits the addition entirely."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions[0].concentration",
    "stored": {
      "value": "1",
      "unit": "ML_PER_L"
    },
    "ingredient": "Wolfe's mineral elixir addition",
    "proposed": {
      "amount": 1,
      "unit": "ml",
      "basis": "Exact source listed batch; provider main.volume 1001 ml"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Wolfe's mineral elixir",
        "exact_source_quote": "Wolfe's mineral elixir 1.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Wolfe's mineral elixir\",\n                        \"solution_id\": 1605,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The source gives 1 ml per listed batch. Existing owner 1 ML_PER_L and per-litre wording need explicit qualification against provider 1001 ml; the source does not independently measure a final litre. Target omits the addition entirely."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "solutions[0].concentration",
    "stored": {
      "value": "1",
      "unit": "ML_PER_L"
    },
    "ingredient": "Wolfe's mineral elixir addition",
    "proposed": {
      "amount": 1,
      "unit": "ml",
      "basis": "Exact source listed batch; provider main.volume 1001 ml"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Wolfe's mineral elixir",
        "exact_source_quote": "Wolfe's mineral elixir 1.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Wolfe's mineral elixir\",\n                        \"solution_id\": 1605,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The source gives 1 ml per listed batch. Existing owner 1 ML_PER_L and per-litre wording need explicit qualification against provider 1001 ml; the source does not independently measure a final litre. Target omits the addition entirely."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      }
    ],
    "ingredient": "Distinct mineral-elixir MgSO4 x 7 H2O",
    "proposed": {
      "value": 30,
      "unit": "G_PER_L",
      "scope": "Stock composition only"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 30.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 121.716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "These three stock constituents were combined into main-salt numbers rather than retained as separate stock constituents. Restore the stock node while correcting the corresponding historical sum; do not add a second neat main dose."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      }
    ],
    "ingredient": "Distinct mineral-elixir NaCl",
    "proposed": {
      "value": 10,
      "unit": "G_PER_L",
      "scope": "Stock composition only"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: NaCl",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 171.116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "These three stock constituents were combined into main-salt numbers rather than retained as separate stock constituents. Restore the stock node while correcting the corresponding historical sum; do not add a second neat main dose."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      }
    ],
    "ingredient": "Distinct mineral-elixir CaCl2 x 2 H2O",
    "proposed": {
      "value": 1,
      "unit": "G_PER_L",
      "scope": "Stock composition only"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 1.00 g",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 6.80203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "These three stock constituents were combined into main-salt numbers rather than retained as separate stock constituents. Restore the stock node while correcting the corresponding historical sum; do not add a second neat main dose."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of powdered sulfur and autoclave for 60 min at &lt;b&gt;105°C&lt;/b&gt;. Prior to inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of complete medium to 4.5."
          },
          {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts."
          }
        ]
      }
    ],
    "ingredient": "Main solvent volume",
    "proposed": {
      "amount": 1000,
      "unit": "ml",
      "scope": "Distilled water in main recipe"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Distilled water",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[15]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Primary water 1000 ml plus 1 ml elixir and 0.5 ml indicator totals 1001.5 ml listed liquids before sulfide stock/titration. Provider declares 1001 ml; do not resolve that difference by assuming measured final volume or a rounding rule."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "ingredient": "Mineral-elixir solvent volume",
    "proposed": {
      "amount": 1000,
      "unit": "ml",
      "scope": "Stock preparation water"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Distilled water",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Stock water is not a second litre added to the receiving medium."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions[0].preparation_notes",
    "stored": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).",
    "ingredient": "Existing stock 1000 ml preparation context",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Distilled water",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The 1000 ml stock context matches the provider stock volume and listed water. The same note’s per-litre addition wording is separately corrected; this decision supports only the stock-preparation volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "solutions[0].preparation_notes",
    "stored": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).",
    "ingredient": "Existing stock 1000 ml preparation context",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 Wolfe's mineral elixir subsection: Distilled water",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[1].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "The 1000 ml stock context matches the provider stock volume and listed water. The same note’s per-litre addition wording is separately corrected; this decision supports only the stock-preparation volume."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      }
    ],
    "ingredient": "Sodium resazurin stock strength",
    "proposed": {
      "value": 0.1,
      "unit": "%w/v",
      "scope": "Indicator stock strength or its listed-batch addition, separately from provider-derived mass"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sodium resazurin",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Preserve both source inputs. 0.1 g/100 ml * 0.5 ml = 0.0005 g transferred; dividing by provider 1.001 L gives approximately 0.0004995 g/L, without establishing true final mixed volume."
  },
  {
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      }
    ],
    "ingredient": "Sodium resazurin stock dose",
    "proposed": {
      "value": 0.5,
      "unit": "ml",
      "scope": "Indicator stock strength or its listed-batch addition, separately from provider-derived mass"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main recipe: Sodium resazurin",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      },
      {
        "source_key": "mediadive1083api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1083",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0004995,\n                        \"mmol_l\": 0.0019887,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0"
      }
    ],
    "explanation": "Preserve both source inputs. 0.1 g/100 ml * 0.5 ml = 0.0005 g transferred; dividing by provider 1.001 L gives approximately 0.0004995 g/L, without establishing true final mixed volume."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Sparging gas",
    "proposed": "80% nitrogen/20% carbon dioxide mixture",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sparging gas",
        "exact_source_quote": "80% N2 and 20%",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Sparging gas",
    "proposed": "80% nitrogen/20% carbon dioxide mixture",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sparging gas",
        "exact_source_quote": "80% N2 and 20%",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "preparation_steps[0].description",
    "stored": "Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of powdered sulfur and autoclave for 60 min at &lt;b&gt;105°C&lt;/b&gt;. Prior to inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of complete medium to 4.5.",
    "ingredient": "Sparging gas",
    "proposed": "80% nitrogen/20% carbon dioxide mixture",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sparging gas",
        "exact_source_quote": "80% N2 and 20%",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Sparging duration",
    "proposed": "30–45 min",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sparging duration",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Sparging duration",
    "proposed": "30–45 min",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sparging duration",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "preparation_steps[0].description",
    "stored": "Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of powdered sulfur and autoclave for 60 min at &lt;b&gt;105°C&lt;/b&gt;. Prior to inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of complete medium to 4.5.",
    "ingredient": "Sparging duration",
    "proposed": "30–45 min",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sparging duration",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Sterilization temperature and duration",
    "proposed": "105°C for 60 min",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sterilization temperature and duration",
        "exact_source_quote": "autoclave for 60 min at 105°C.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Sterilization temperature and duration",
    "proposed": "105°C for 60 min",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sterilization temperature and duration",
        "exact_source_quote": "autoclave for 60 min at 105°C.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "preparation_steps[0].description",
    "stored": "Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of powdered sulfur and autoclave for 60 min at &lt;b&gt;105°C&lt;/b&gt;. Prior to inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of complete medium to 4.5.",
    "ingredient": "Sterilization temperature and duration",
    "proposed": "105°C for 60 min",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Sterilization temperature and duration",
        "exact_source_quote": "autoclave for 60 min at 105°C.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Later sulfide-stock gas",
    "proposed": "100% nitrogen only for the sulfide-stock stage",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Later sulfide-stock gas",
        "exact_source_quote": "stock solution prepared under 100% N2 gas",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "preparation_steps",
    "stored": null,
    "ingredient": "Later sulfide-stock gas",
    "proposed": "100% nitrogen only for the sulfide-stock stage",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Later sulfide-stock gas",
        "exact_source_quote": "stock solution prepared under 100% N2 gas",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "preparation_steps[0].description",
    "stored": "Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of powdered sulfur and autoclave for 60 min at &lt;b&gt;105°C&lt;/b&gt;. Prior to inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of complete medium to 4.5.",
    "ingredient": "Later sulfide-stock gas",
    "proposed": "100% nitrogen only for the sulfide-stock stage",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 main preparation paragraph; Later sulfide-stock gas",
        "exact_source_quote": "stock solution prepared under 100% N2 gas",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner already retains this exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition."
  },
  {
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 4.5
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "ph_value",
        "stored": 4.5
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "ph_value",
        "stored": 4.5
      }
    ],
    "ingredient": "Target complete-medium pH",
    "proposed": 4.5,
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 final main preparation sentence",
        "exact_source_quote": "adjust pH of complete medium to 4.5.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The scalar value already matches; attach narrow evidence and preserve the end-of-main-preparation scope."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "solutions",
    "stored": null,
    "ingredient": "Mineral-elixir pH",
    "proposed": {
      "pH": 1.0,
      "stage": "Water acidification before dissolving stock salts"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 2 continuation of Wolfe mineral-elixir subsection",
        "exact_source_quote": "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner needs its existing root preparation step scoped to the stock. Other layers need this missing stock instruction added. Preserve complete-medium pH 4.5."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "solutions",
    "stored": [
      {
        "preferred_term": "Wolfe's mineral elixir",
        "composition": [
          {
            "preferred_term": "MnSO4 x H2O",
            "term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            },
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86364",
              "label": "manganese(II) sulfate monohydrate"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "CoCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            },
            "concentration": {
              "value": "1.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "1.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          }
        ],
        "concentration": {
          "value": "1",
          "unit": "ML_PER_L"
        },
        "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
      }
    ],
    "ingredient": "Mineral-elixir pH",
    "proposed": {
      "pH": 1.0,
      "stage": "Water acidification before dissolving stock salts"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 2 continuation of Wolfe mineral-elixir subsection",
        "exact_source_quote": "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner needs its existing root preparation step scoped to the stock. Other layers need this missing stock instruction added. Preserve complete-medium pH 4.5."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "preparation_steps[1].description",
    "stored": "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.",
    "ingredient": "Mineral-elixir pH",
    "proposed": {
      "pH": 1.0,
      "stage": "Water acidification before dissolving stock salts"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 2 continuation of Wolfe mineral-elixir subsection",
        "exact_source_quote": "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The DSMZ owner needs its existing root preparation step scoped to the stock. Other layers need this missing stock instruction added. Preserve complete-medium pH 4.5."
  },
  {
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "Wolfe's mineral elixir",
            "composition": [
              {
                "preferred_term": "MnSO4 x H2O",
                "term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                },
                "concentration": {
                  "value": "5",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:86364",
                  "label": "manganese(II) sulfate monohydrate"
                }
              },
              {
                "preferred_term": "FeSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:75836",
                  "label": "iron(2+) sulfate heptahydrate"
                }
              },
              {
                "preferred_term": "CoCl2 x 6 H2O",
                "term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:53503",
                  "label": "cobalt chloride hexahydrate"
                }
              },
              {
                "preferred_term": "ZnSO4 x 7 H2O",
                "term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                },
                "concentration": {
                  "value": "1.8",
                  "unit": "G_PER_L"
                },
                "mediaingredientmech_chebi_term": {
                  "id": "CHEBI:32312",
                  "label": "zinc sulfate heptahydrate"
                }
              }
            ],
            "concentration": {
              "value": "1",
              "unit": "ML_PER_L"
            },
            "preparation_notes": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150)."
          }
        ]
      }
    ],
    "ingredient": "Stock acid amount and strength",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 2 mineral-elixir stock preparation",
        "exact_source_quote": "First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "Diluted sulfuric acid is specified to reach stock pH 1.0, but no acid amount or strength is provided; no numeric conversion is justified."
  },
  {
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing already the appropriate amount of powdered sulfur and autoclave for 60 min at &lt;b&gt;105°C&lt;/b&gt;. Prior to inoculation add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of complete medium to 4.5."
      }
    ],
    "ingredient": "Separate sulfide stock strength and volume",
    "source_snippets": [
      {
        "source_key": "dsmz1083",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf",
        "source_locator": "Page 1 later main-preparation sulfide addition",
        "exact_source_quote": "add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas",
        "snapshot_sha256": "fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba",
        "parsed_text_sha256": "bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249"
      }
    ],
    "explanation": "The main table supports 0.50 g Na2S·9H2O per listed batch; the separate sulfide stock strength and transfer volume are not supplied. Preserve this unresolved preparation detail without inferring a stock recipe."
  }
]

### Identifier metadata, exact secondary keys and supplied-form scope

grounding: concern. Targets: CultureMech:003735.

23 distinct primary/current-secondary identifiers resolve. 0 label instances differ from current canonical labels; 1 asserted current secondary keys lack an exact pinned index row. Legacy numeric links are assessed separately and are not established by CHEBI correspondence. Target linkage is 23/25 primary and 22/25 secondary ingredient instances; this measures presence, not source validity.

{"label_drift": [], "missing_secondary_keys": ["CHEBI:26833"], "legacy_instances": [{"input": "target", "field_path": "ingredients[24].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml", "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml", "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}], "coverage_scale": "0–100 percent; each ingredient instance counted once", "denominator": 25, "primary_percent": 92.0, "secondary_percent": 88.0}

### Supplied chemical forms and secondary-link limits

grounding: concern. Targets: CultureMech:003735.

Sodium resazurin is mapped to CHEBI:8806, whose formula C12H7NO4 contains no sodium. Sulfur atom is a valid broader elemental term but does not carry the source powder context; no specific allotrope or replacement is inferred. CHEBI:26833 has zero exact rows in the fully available pinned MIM index, a confirmed secondary mapping gap rather than an unavailable check. All stated hydrates otherwise retain matching source forms; unspecified citrate hydration is not guessed.

### Main/stock sequence and generated-layer loss

completeness: concern. Targets: CultureMech:003735.

The target has 25 direct ingredients and no solutions; both current owners have 21 direct ingredients and four nested stock components, still incomplete. Only the DSMZ owner retains the anoxic preparation, temperature/time and sulfide sequence; its stock-pH instruction is misplaced at root. The target omits that preparation. Liquid/complex/undefined annotations are compatible with the documented yeast extract and BD Bacto tryptone; preserve powder/product descriptions without invented supplier identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003735.

30 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: Undiluted stock strengths and historical salt sums corrupt the formulation

blocker / open / confirmed; issue key: CM003735-summed-stock-formulation.

NaCl 39.97, MgSO4·7H2O 33.4965 and CaCl2·2H2O 1.37962 g/L combine main-provider concentrations with full stock strengths. Eleven target stock components remain direct; only four moved under each owner stock, leaving seven direct and three conflated. All 77 local concentration instances and exact stock/source bases are assessed.

### f2: Three stored bacterial relationship paths do not resolve

blocker / open / confirmed; issue key: CM003735-broken-relationship-paths.

Target and KOMODO parent paths and the DSMZ child path point to bacterial files; the same stable IDs resolve to the captured archaea owners. The actual contributors are identifiable, but these exact stored paths remain broken.

### f3: Sodium resazurin is linked to a structure without sodium

major / open / confirmed; issue key: CM003735-resazurin-salt-grounding.

The source explicitly supplies sodium resazurin stock. CHEBI:8806 resolves to neutral-form metadataC12H7NO4 and therefore does not encode the specified sodium salt.

### f4: Preparation, source grades and amount evidence need exact stage scope

major / open / confirmed; issue key: CM003735-stage-evidence-preparation.

Neither target nor KOMODO owner retains preparation; the DSMZ owner has the stock-pH 1.0 step in the root sequence. Existing amounts lack attached evidence, source indicator strength/dose and stock additions need explicit bases, and BD Bacto/powder descriptions are dropped. Catalog aerobic=true must remain attributed alongside the documented anoxic preparation.

### f5: A current secondary key is unmapped and a historical link is unresolved

minor / open / confirmed; issue key: CM003735-mim-key-limits.

CHEBI:26833 is a valid live ontology term with no row in the fully searched pinned secondary index. MIM000198 remains asserted for sodium selenate but its historical correspondence cannot be independently recovered; CHEBI:77775 existence is not proof of that legacy link.

### f6: KOMODO provenance timestamps are malformed or timezone-naive

minor / open / confirmed; issue key: CM003735-history-timestamps.

The target and KOMODO history retain a malformed January timestamp and a February timestamp without timezone; later repair and merge dates remain separate recorded events.

## Recommended Actions And Acceptance Checks

### a1

Restore the complete 14-salt stock and listed 1 ml batch addition, separate historical main/stock sums, retain provider 1001 ml versus source listed-liquid limits, and regenerate only after owner review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct exact maintained relationship paths to the verified same-ID archaea owners and regenerate affected derived references; verify exact Git path spelling.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify an appropriate exact salt identity before changing the maintained primary mapping; do not infer a replacement identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Restore missing preparation and precise stock stages, attach literal quantity evidence, preserve source product/powder scope and explain the catalog/preparation conflict without inferring growth physiology.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve the confirmed current mapping gap and unresolved historical link separately; verify archival correspondence or explicitly qualify the legacy assertion without guessing a replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve history and append any supported later clarification without inventing a historical timezone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/archaea/aciduliprofundum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch019/182/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/182/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml:1:id: CultureMech:003735<br>./data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml:1:id: CultureMech:003735<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/182/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 29 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz1083 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf; Pages 1–2: complete main recipe, preparation and Wolfe mineral elixir subsection | supports | Both main formulation and complete referenced stock are specified in this exact document; medium 792 is named only as the origin of this stock. |
| mediadive1083api | https://mediadive.dsmz.de/rest/medium/1083; $.data.medium and complete $.data.solutions[0:2] | supports | Explicit main 1001 ml versus stock 1000 ml provider bases, source labels/amounts and stage-specific steps. |
| solution1605 | https://mediadive.dsmz.de/rest/solution/1605; $.data complete exact solution 1605 | supports | Independent exact stock endpoint matches the mineral-elixir identity and all 14 salts. |
| komodo | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact ID 1083 row and Is Aerobic column header | supports | 1083 &#124; ACIDULIPROFUNDUM medium &#124; 4.5 &#124; true &#124; true &#124; false &#124; http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf; true is an actual catalog flag, while the primary explicitly prepares anoxic medium. Preserve this source disagreement rather than treating the flag as physiological validation. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch019/182/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:26710 resolves to sodium chloride. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:26833 resolves to sulfur atom. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:32588 resolves to potassium chloride. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:33118 resolves to boric acid. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:53258 resolves to sodium citrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:62946 resolves to ammonium sulfate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:63004 resolves to sodium bromide. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:77775 resolves to sodium selenate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:8806 resolves to Resazurin. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent source revision/hash | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "asserted_secondary_rows": {"CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833": [], "CHEBI:31440": [{"label": "Copper (II) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulphate(5.H2O)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate (1:1) pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) sulfate, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cupric sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO .5H O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 .5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 · 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 ⋅ 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4*5 H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4.5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4·5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4・5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "zinc sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zinc sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc sulfate heptahydrate (1:1:7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zn2SO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 .7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 × 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7 H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4-7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4∙7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4･7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "[KCl]", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaliumchlorid", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaon-Cl 10", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl (Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS: 7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS:7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klor-con", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klotrix", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "muriate of potash", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sylvite", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "[B(OH)3]", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "B(OH)3", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Boric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "boron trihydroxide", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "orthoboric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "trihydroxidoboron", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "citric acid trisodium salt", "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na3-citrate", "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium citrate", "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "Tri-sodium citrate", "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "trisodium 2-hydroxypropane-1,2,3-tricarboxylate", "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:53503": [{"label": "cobalt (II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt chloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "cobalt chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+) dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 4 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 × 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 ∙ 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2 SO4", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2S4", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4(Fisher A 702)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium sulfate (2:1)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium sulphate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diammonium sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diazanium sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "mascagnite", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid ammonium salt (1:2)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid, diammonium salt", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of ammonia", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label": "Bromide salt of sodium", "match_type": "synonym", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bromnatrium", "match_type": "synonym", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium bromide", "match_type": "synonym", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Trisodium tribromide", "match_type": "synonym", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P 0662)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MKP", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Orthophosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium acid phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate monobasic", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sorensen's potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Disodium tetraoxotungstate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na-tungstate x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO2.2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 × 2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4•2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4・2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaWO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)tungsten--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium orthotungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium tetraoxotungstate(VI)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium tungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium tungstate(VI)", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium tungstate(VI) dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium tungsten oxide", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium wolframate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Tungstic acid, disodium salt", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Tungstic acid, sodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Molybdic acid, disodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2 MoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2Mo4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 ⋅ 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4. 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO7 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7O4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)molybdenum--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Molybdate Dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium molybdate(VI) dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium orthomolybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "Fe SO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ferrous sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ferrous sulfate.7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 x 7H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron (II) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron(II) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "disodium sulfide--water (1/9)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S . 9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O (3% w/v)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O(24% w/v)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S ∙ 9 H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S-9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S·9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S⋅9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S・9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium monosulfide.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfide nonahydrate", "match_type": "ontology_label", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfide.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2.6H2O", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2·6H2O", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2•6H2O", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2•6H2O", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2・6H2O", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel sulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel sulfate hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium nickel(2+) sulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel(2+) sulfate--water (2/1/2/6)", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel(2+) sulfate--water (2/1/2/6)", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel(II) sulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Diammonium nickel disulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel ammonium sulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel diammonium disulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS: 10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "CCRIS 3494", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Chlorure de magnesium hydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride anhydrous", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl 2", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2  x 76 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "MgCl2 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2.6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x7H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate hydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "ontology_label", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "manganese(II) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 . 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2 x 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2.12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2·12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2・12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aluminium potassium sulfate--water (1/12)", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Aluminum potassium disulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Aluminum potassium sulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2 . 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2 x 12 H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2·12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2・12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kalinite", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potash alum dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium alum dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "potassium aluminium sulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium aluminum disulfate dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": ["CHEBI:26833"], "legacy_instances": [{"input": "target", "field_path": "ingredients[24].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml", "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml", "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}]} |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Whole pinned public catalog or complete recursive tree; exact legacy000198 lookup | supports | The available current pinned material has no000198 token. It does not supply the historical numeric-ID correspondence; current CHEBI:77775 resolves independently. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Whole pinned public catalog or complete recursive tree; exact legacy000198 lookup | supports | The available current pinned material has no000198 token. It does not supply the historical numeric-ID correspondence; current CHEBI:77775 resolves independently. |
| legacy-local-search | owned checkout; Exact historical key search in data/src/docs | context_only | data/normalized_yaml/fungal/ferrous_iron_yeast_extract_medium.yaml:174:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/modified_picrophilus_medium.yaml:245:    id: MediaIngredientMech:000198<br>data/normalized_yaml/specialized/modified_marine_medium.yaml:118:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/KOMODO_792_PYROLOBUS_FUMARII_MEDIUM.yaml:206:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml:213:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/KOMODO_766_THERMOCOCCUS_CHITINOPHAGUS_MEDIUM.yaml:66:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml:54:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/methanogen_ms_i_medium.yaml:226:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/pyrolobus_medium.yaml:228:    id: MediaIngredientMech:000198<br>data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml:182:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/pyrolobus_fumarii_medium.yaml:215:    id: MediaIngredientMech:000198<br>data/normalized_yaml/specialized/fe_iii_reducer_marine_enrichment_medium.yaml:128:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/aciduliprofundum_medium.yaml:212:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/methanosphaera_medium_i.yaml:55:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/methanosphaera_medium.yaml:54:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/JCM_J355_METHANOSPHAERA_MEDIUM.yaml:57:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/thermofilum_medium.yaml:86:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/archaeoglobus_infectus_medium.yaml:199:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml:242:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/mo_cfxi_medium__58d3ad1b.yaml:182:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/thermococcus_chitinophagus_medium.yaml:65:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/SPIROCHAETA_CELLOBIOSIPHILA_MEDIUM.yaml:176:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/sea_salts_tyg_medium__6486dbac.yaml:213:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/methanosphaera_medium__f110a698.yaml:54:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/syphc_medium.yaml:212:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/VULCANITHERMUS_MEDIUM.yaml:266:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/PLANTOMYCETACEAE_MEDIUM.yaml:150:    id: MediaIngredientMech:000198<br>data/normalized_yaml/archaea/pfennig_thermofilum_medium.yaml:182:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium__2616625b.yaml:84:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/kiritimatiella_tyg_medium.yaml:215:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml:128:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/HALARSENATIBACTER_MEDIUM.yaml:115:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/pyrobaculum_aerophilum_medium__bc93f572.yaml:54:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/MARIDESULFOVIBRIO_MEDIUM.yaml:201:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/Meiothermus_hypogaeus_MEDIUM.yaml:213:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/NAUTILIA_NITRATIREDUCENS_MEDIUM.yaml:248:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/VULCANIBACILLUS_MEDIUM.yaml:210:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMOANAEROBACULUM_AQUATICUM_MEDIUM.yaml:235:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/thermocrinis_albus_medium__8e47ff6d.yaml:135:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/st65_medium__23c51571.yaml:183:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/spirochaeta_cellobiosiphila_medium.yaml:136:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/pyrolobus_fumarii_medium__0aa02c21.yaml:255:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMOVIBRIO_AMMONIFICANS_MEDIUM.yaml:245:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/congregibacter_syphc_medium.yaml:224:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/IGNAVIBACTERIA_MEDIUM.yaml:140:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/vulcanibacillus_medium__2277eb74.yaml:211:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/thermogutta_hypogea_medium.yaml:177:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/mariprofundus_es_medium.yaml:220:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/tanner_mod2_medium__ec1a1c56.yaml:215:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/DESULFUROMUSA_FERRIREDUCENS_MEDIUM.yaml:211:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/ferrous_iron_yeast_extract_medium__a821658e.yaml:174:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/thermincola_medium_co.yaml:246:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/vulcanithermus_medium.yaml:265:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml:128:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMODESULFITIMONAS_MEDIUM.yaml:225:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml:194:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/sypg_medium__0c1821a0.yaml:225:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/methylomonas_medium_surf.yaml:285:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml:182:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml:137:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/acidihalobacter_prosperus_f5_medium__0fa15dd8.yaml:161:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/SMITHELLA_MEDIUM.yaml:233:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml:266:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/freshwater_iron_gel_medium__d012b865.yaml:64:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.yaml:42:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml:253:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/jcm_medium_no_244.yaml:216:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/svx8_medium__0a0a576b.yaml:183:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/methylomonas_medium_wsc.yaml:286:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/MEDIUM_for_SM250.yaml:144:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/METHANOSPHAERA_MEDIUM.yaml:57:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMOFILUM_MEDIUM.yaml:86:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/thermobacter_roseum_medium__60c6c40b.yaml:277:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/geobacter_nbaf_medium__db485dcd.yaml:104:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml:213:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml:199:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/METALLIBACTERIUM_MEDIUM.yaml:197:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium__6a83808e.yaml:128:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMOHALOBACTER_MEDIUM.yaml:273:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMOCOCCUS_CHITINOPHAGUS_MEDIUM.yaml:66:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/methylocystis_medium_nls.yaml:84:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml:118:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/DESULFOGLAEBA_MEDIUM.yaml:251:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/plantomycetaceae_medium.yaml:150:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/seawater_pyruvate_thiosulfate_medium__e78f35f1.yaml:294:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/syphc_medium__da30d435.yaml:289:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/syfac_medium__0aaeb681.yaml:212:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/ms_sulf_medium.yaml:226:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/desulfamplus_medium__51ba8b93.yaml:263:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/MARISPIROCHAETA_MEDIUM.yaml:193:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/gallionella_es_medium.yaml:199:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/thermincola_medium.yaml:247:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/PLANTOMYCETACEAE_MEDIUM_SBP2.yaml:253:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/acidithrix_ferrooydans_medium__b3120235.yaml:245:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/JCM_J729_ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml:242:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml:127:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml:116:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/pyrolobus_medium__bb7c3cdb.yaml:265:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/dissulfurimicrobium_hydrothermale_medium__63c2d6ea.yaml:163:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/modified_picrophilus_medium__2e13d4cd.yaml:282:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/PFENNIG_THERMOFILUM_MEDIUM.yaml:182:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/SELENATE_REDUCER_MEDIUM.yaml:114:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/sypc_medium.yaml:137:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/thermodesulfobacterium_hydrogenophilum_medium__c1daf6d7.yaml:142:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/ytps_medium__a290bac5.yaml:134:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/JCM_J470_VULCANIBACILLUS_MEDIUM.yaml:210:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/MODIFIED_SME_MEDIUM.yaml:130:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml:199:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml:239:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/THERMOSULFIDIBACTER_MEDIUM.yaml:202:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/medium_for_z_1701_z_1702.yaml:106:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/vulcanibacillus_medium.yaml:212:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/thermoanaerobaculum_aquaticum_medium.yaml:235:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/sea_salts_tyg_medium.yaml:176:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/kiritimatiella_tyg_medium.yaml:175:    id: MediaIngredientMech:000198<br>data/merge_yaml/merged/thermogutta_hypogea_medium__b2091adf.yaml:177:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/desulfamplus_medium.yaml:223:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/mo_cfxi_medium.yaml:182:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/halarsenatibacter_medium.yaml:115:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/tanner_mod2_medium.yaml:215:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/maridesulfovibrio_medium.yaml:161:    id: MediaIngredientMech:000198<br>data/normalized_yaml/bacterial/mei |
| relationships | data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; All three explicit relationship paths compared to exact Git tree and same-ID normalized owners | refutes | [{"input": "target", "field_path": "parent_media.path", "stored": "data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml", "same_id_actual_owner": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml"}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml", "field_path": "parent_media.path", "stored": "data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml", "same_id_actual_owner": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml"}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml", "field_path": "variant_children[0].path", "stored": "data/normalized_yaml/bacterial/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml", "same_id_actual_owner": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml"}] |
| history-metadata | data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml; data/normalized_yaml/archaea/aciduliprofundum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:56.076801"}]}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:56.076801"}]}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml", "events": 9, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer preserves main/stock separation, but its preparation parser collects steps from all solutions without headings. Current cleanup explicitly refuses unequal-value summation. Historical record notes preserve old sums; current code is not claimed to reproduce them. The inspected cocktail helper and its recorded four-row repair do not establish that the whole stock was recovered; current merge requires scientific-field compatibility. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer preserves main/stock separation, but its preparation parser collects steps from all solutions without headings. Current cleanup explicitly refuses unequal-value summation. Historical record notes preserve old sums; current code is not claimed to reproduce them. The inspected cocktail helper and its recorded four-row repair do not establish that the whole stock was recovered; current merge requires scientific-field compatibility. |
| writer-2 | scripts/apply_cocktail_nesting.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer preserves main/stock separation, but its preparation parser collects steps from all solutions without headings. Current cleanup explicitly refuses unequal-value summation. Historical record notes preserve old sums; current code is not claimed to reproduce them. The inspected cocktail helper and its recorded four-row repair do not establish that the whole stock was recovered; current merge requires scientific-field compatibility. |
| writer-3 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer preserves main/stock separation, but its preparation parser collects steps from all solutions without headings. Current cleanup explicitly refuses unequal-value summation. Historical record notes preserve old sums; current code is not claimed to reproduce them. The inspected cocktail helper and its recorded four-row repair do not establish that the whole stock was recovered; current merge requires scientific-field compatibility. |
| writer-4 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer preserves main/stock separation, but its preparation parser collects steps from all solutions without headings. Current cleanup explicitly refuses unequal-value summation. Historical record notes preserve old sums; current code is not claimed to reproduce them. The inspected cocktail helper and its recorded four-row repair do not establish that the whole stock was recovered; current merge requires scientific-field compatibility. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required partial scope is the historical MIM000198 identity correspondence. The current CHEBI:26833 index absence is a completed lookup with a confirmed gap. Provider1001ml and primary listed 1001.5 ml liquids are preserved separately; neither establishes a measured final volume. No other medium 792 formulation or physiology is imported.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114752Z-culturemech-003735-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aciduliprofundum_medium (CultureMech:003735)'
started_at: '2026-10-21T11:43:20Z'
finished_at: '2026-10-21T11:47:52Z'
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
summary: The exact DSMZ/KOMODO 1083 identity is recoverable, but historical salt sums
  and partial stock nesting leave the formulation scientifically incorrect. The generated
  target also loses preparation and nesting, all three stored bacterial relationship
  paths are broken, and the historical numeric MIM link remains unresolved.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
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
  - path: data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
    sha256: 4be9b42a6bad75434527869f26763b0d97f095d6ca7c882136b54904f2c9fc83
    role: target
  - path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    sha256: 92906400c230762d1db735dcb43a91812ac12f45fdb579f993159eda25f272c1
    role: context
  - path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
    sha256: 4b16d9e9de3734421260b6c28fc4fe8576fe7196557fb91223cb728bf665a231
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
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/komodo_web_raw_yaml.py
    sha256: a1a37015b4e6bac657e49f375b39a319815cc6b02a02135674a858a8b6eab03a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 182; batch 019 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eighteen task batches
    contain 180 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 182 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003735
targets:
- target_id: CultureMech:003735
  path: data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  label: aciduliprofundum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/182/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/182/strict.tsv"
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003735
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
  - CultureMech:003735
- check_id: historical-mim000198
  name: Historical MIM000198 correspondence
  required: true
  status: unavailable
  summary: The exact historical mapping for asserted MIM000198 could not be verified
    from the complete pinned public catalog/tree or ignored-inclusive local references.
    Current sodium-selenate CHEBI metadata does not establish a deprecated numeric
    link.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-local-search
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:43:45.492704Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/182/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:43:47.214885Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/182/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:43:49.532423Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:43:50.719567Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:47:50Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml:1:id: CultureMech:003735

    ./data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml:1:id:
    CultureMech:003735

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/182/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:47:50Z'
  support: supports
  summary: 29 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 481408e2bac9f95e218fd31672c448f12da99e713764e45b38555510114dd405
- evidence_id: dsmz1083
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf
  locator: 'Pages 1–2: complete main recipe, preparation and Wolfe mineral elixir
    subsection'
  accessed_at: '2026-10-21T11:29:07.402863Z'
  support: supports
  summary: Both main formulation and complete referenced stock are specified in this
    exact document; medium 792 is named only as the origin of this stock.
  snapshot_sha256: fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba
- evidence_id: mediadive1083api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1083
  locator: $.data.medium and complete $.data.solutions[0:2]
  accessed_at: '2026-10-21T11:29:06.756613Z'
  support: supports
  summary: Explicit main 1001 ml versus stock 1000 ml provider bases, source labels/amounts
    and stage-specific steps.
  snapshot_sha256: 3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0
- evidence_id: solution1605
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1605
  locator: $.data complete exact solution 1605
  accessed_at: '2026-10-21T11:29:45.589163Z'
  support: supports
  summary: Independent exact stock endpoint matches the mineral-elixir identity and
    all 14 salts.
  snapshot_sha256: b8d483a199937e4d251ddb37d334b7b3a24c5db2f29b91cd7923594752c5c69d
- evidence_id: komodo
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact ID 1083 row and Is Aerobic column header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: 1083 | ACIDULIPROFUNDUM medium | 4.5 | true | true | false | http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf;
    true is an actual catalog flag, while the primary explicitly prepares anoxic medium.
    Preserve this source disagreement rather than treating the flag as physiological
    validation.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/182/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: c81c0374a51d5e294a6dbdccc5f5b6d49775aba6699d6c9d0b201e27868018b9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi26833
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:04.114839Z'
  support: supports
  summary: CHEBI:26833 resolves to sulfur atom. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Identity/label existence is
    separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: CHEBI:53258 resolves to sodium citrate. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi63004
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T07:16:25.403149Z'
  support: supports
  summary: CHEBI:63004 resolves to sodium bromide. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 2665f3a4301ab51b67b814a8694bc906c1a13c9b301c85a4416891d3f9412c90
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: CHEBI:63939 resolves to sodium tungstate dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: CHEBI:76209 resolves to sodium sulfide nonahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi77775
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:09.354177Z'
  support: supports
  summary: CHEBI:77775 resolves to sodium selenate. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: a1a4ab87bbf08908fef7df53a788a85d9f6eee32350f082895e0563d6344c908
- evidence_id: chebi86149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:08.844455Z'
  support: supports
  summary: CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 930d93c33f6115f19153868ae36f0153b69406fd555708237a7ccccfb010cd97
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent source revision/hash
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "asserted_secondary_rows":
    {"CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type":
    "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro
    sodico", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type":
    "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833":
    [], "CHEBI:31440": [{"label": "Copper (II) sulfate pentahydrate", "match_type":
    "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper
    sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper sulphate(5.H2O)", "match_type": "synonym", "identifier":
    "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate
    (1:1) pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(2+) sulfate pentahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+)
    sulfate--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(II) sulfate pentahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II)
    sulfate, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "cupric sulfate pentahydrate", "match_type":
    "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO
    .5H O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 .5H2O", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4
    x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4 x 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 · 5H2O", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4
    ⋅ 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4*5 H2O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4.5H2O", "match_type": "synonym",
    "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id":
    "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4·5H2O",
    "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4
    x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuSO4・5H2O", "match_type": "synonym", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate
    (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate
    heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate
    heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate
    heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO
    4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO
    4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4
    . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4
    x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1%
    w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma
    230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS:
    10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma
    230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric
    acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "zinc sulfate (1:1)
    heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Zinc sulfate heptahydrate", "match_type": "synonym", "identifier":
    "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc sulfate heptahydrate
    (1:1:7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "zinc(2+) sulfate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+)
    sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Zn2SO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 . 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4
    .7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 × 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4
    ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4*7 H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4-7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4·7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4∙7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ZnSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4・7H2O", "match_type": "synonym",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4･7H2O",
    "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4
    x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "[KCl]", "match_type": "synonym", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Kaliumchlorid", "match_type": "synonym",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaon-Cl 10", "match_type":
    "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl",
    "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "KCl (Fisher P 217)", "match_type": "synonym", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS: 7447-40-7)", "match_type":
    "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS:7447-40-7)",
    "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl",
    "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KCl(Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Klor-con", "match_type": "synonym", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Klotrix", "match_type": "synonym",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium chloride",
    "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl",
    "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "muriate of potash", "match_type": "synonym", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Potassium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sylvite", "match_type":
    "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "[B(OH)3]", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "B(OH)3", "match_type": "synonym", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Boric acid", "match_type": "synonym", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "boron trihydroxide", "match_type":
    "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H
    BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3",
    "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "H3BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)", "match_type": "synonym",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "orthoboric acid",
    "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3",
    "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "trihydroxidoboron", "match_type": "synonym", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:53258": [{"label": "citric acid trisodium salt",
    "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium
    citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na3-citrate", "match_type": "synonym", "identifier": "CHEBI:53258",
    "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium citrate", "match_type": "synonym",
    "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id":
    "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label":
    "Tri-sodium citrate", "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term":
    "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "trisodium 2-hydroxypropane-1,2,3-tricarboxylate",
    "match_type": "synonym", "identifier": "CHEBI:53258", "preferred_term": "Trisodium
    citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Trisodium citrate", "match_type": "preferred_term", "identifier":
    "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:53503": [{"label":
    "cobalt (II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt chloride
    hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "cobalt chloride hexahydrate", "match_type":
    "ontology_label", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O",
    "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "cobalt chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt dichloride
    hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+) dichloride hexahydrate",
    "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt
    chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Cobalt(II) chloride hexahydrate", "match_type":
    "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate",
    "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Cobalt(II) chloride--water (1/7)", "match_type": "synonym", "identifier":
    "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id":
    "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2
    . 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 4 H2O", "match_type":
    "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label":
    "CoCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 6 H2O", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate",
    "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "CoCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 · 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "CoCl2 × 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2 ∙ 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2·6H2O", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "CoCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2・6H2O", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:62946":
    [{"label": "(NH4)2 SO4", "match_type": "synonym", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2S4", "match_type": "synonym",
    "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "(NH4)2SO4(Fisher A 702)", "match_type": "synonym", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Sulfate", "match_type":
    "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id":
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium
    sulfate (2:1)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "ammonium sulphate", "match_type": "synonym", "identifier":
    "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "diammonium sulfate", "match_type":
    "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id":
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diazanium
    sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "mascagnite", "match_type": "synonym", "identifier": "CHEBI:62946",
    "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid ammonium salt (1:2)",
    "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4",
    "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sulfuric acid, diammonium salt", "match_type": "synonym", "identifier":
    "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of ammonia", "match_type":
    "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id":
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004":
    [{"label": "Bromide salt of sodium", "match_type": "synonym", "identifier": "CHEBI:63004",
    "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Bromnatrium", "match_type": "synonym", "identifier":
    "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaBr", "match_type": "preferred_term",
    "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium bromide",
    "match_type": "synonym", "identifier": "CHEBI:63004", "preferred_term": "NaBr",
    "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Trisodium tribromide", "match_type": "synonym", "identifier": "CHEBI:63004",
    "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4
    (0.4 g/l)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P 0662)", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MKP",
    "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4",
    "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Monopotassium dihydrogen phosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium monophosphate", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium
    orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Monopotassium phosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Orthophosphoric acid, monopotassium
    salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Phosphoric acid, monopotassium salt", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid,
    potassium salt (1:1)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium acid phosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen orthophosphate",
    "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4",
    "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Potassium dihydrogen phosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Phosphate", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium
    phosphate monobasic", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sorensen''s potassium phosphate", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label":
    "Disodium tetraoxotungstate", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na-tungstate x 2 H2O", "match_type":
    "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO2
    x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO2.2H2O", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 . 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4 × 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4.2H2O", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4·2H2O",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2WO4•2H2O", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2WO4・2H2O", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaWO4·2H2O",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sodium dioxido(dioxo)tungsten--water (1/2)", "match_type":
    "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    orthotungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium tetraoxotungstate(VI)", "match_type":
    "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    tungstate dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium tungstate(VI)", "match_type": "synonym", "identifier":
    "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium tungstate(VI)
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium tungsten oxide", "match_type": "synonym", "identifier":
    "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium wolframate",
    "match_type": "synonym", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4
    x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Tungstic acid, disodium salt", "match_type": "synonym",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Tungstic
    acid, sodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Molybdic acid, disodium salt, dihydrate", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2
    MoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2Mo4 x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MO4.2H2O", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4
    . 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2
    H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Na2MoO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O",
    "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Na2MoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4 ⋅ 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO4. 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O",
    "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO4⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4・2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO7 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO7O4 x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7・2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoSO4", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4 x 2 H2O", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NaMoO4 x 2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 · 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NaMoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)molybdenum--water
    (1/2)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium Molybdate Dihydrate", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium molybdate(VI)
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "sodium orthomolybdate dihydrate", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836":
    [{"label": "Fe SO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ferrous sulfate heptahydrate", "match_type":
    "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ferrous
    sulfate.7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4 7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4
    x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 x 7H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x 7H2O",
    "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4
    x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "FeSO4 x7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4
    · 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4.7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4·7H2O",
    "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term": "FeSO4
    x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeSO4・7H2O", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron
    (II) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate heptahydrate", "match_type":
    "ontology_label", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O",
    "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "iron(2+) sulfate heptahydrate", "match_type": "ontology_label", "identifier":
    "CHEBI:75836", "preferred_term": "FeSO4 x 7H2O", "ontology_id": "CHEBI:75836",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "iron(2+) sulfate--water
    (1/7)", "match_type": "synonym", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Iron(II) sulfate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "disodium sulfide--water (1/9)", "match_type": "synonym", "identifier":
    "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S . 9H2O", "match_type":
    "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S
    x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S x 9 H2O (3% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S x 9 H2O(24%
    w/v)", "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S x 9H2O", "match_type": "synonym", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2S ∙ 9 H2O", "match_type": "synonym",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S-9H2O",
    "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S
    x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S.9H2O", "match_type": "synonym", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2S·9H2O", "match_type": "synonym",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2S⋅9H2O",
    "match_type": "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S
    x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2S・9H2O", "match_type": "synonym", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium monosulfide.9H2O", "match_type":
    "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium
    sulfide nonahydrate", "match_type": "ontology_label", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfide.9H2O", "match_type":
    "synonym", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86149":
    [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier": "CHEBI:86149",
    "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2
    x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)", "match_type": "synonym",
    "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id":
    "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2
    x 6 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term":
    "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2.6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id":
    "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2·6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2
    x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "(NH4)2Ni(SO4)2•6H2O", "match_type": "synonym", "identifier":
    "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2•6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2
    x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "(NH4)2Ni(SO4)2・6H2O", "match_type": "synonym", "identifier":
    "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel
    sulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term":
    "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "ammonium nickel sulfate hexahydrate", "match_type":
    "ontology_label", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2",
    "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Ammonium nickel(2+) sulfate hexahydrate", "match_type": "synonym",
    "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id":
    "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium
    nickel(2+) sulfate--water (2/1/2/6)", "match_type": "synonym", "identifier": "CHEBI:86149",
    "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ammonium nickel(2+) sulfate--water
    (2/1/2/6)", "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term":
    "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "ammonium nickel(II) sulfate hexahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6
    H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Diammonium nickel disulfate hexahydrate", "match_type": "synonym",
    "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id":
    "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel
    ammonium sulfate hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86149",
    "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Nickel diammonium disulfate hexahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2
    x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x
    2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50
    g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution
    (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2
    · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type":
    "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label":
    "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2
    x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS:
    10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride
    dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water
    (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86345": [{"label":
    "CCRIS 3494", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Chlorure de magnesium hydrate", "match_type":
    "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium
    chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Magnesium chloride anhydrous", "match_type":
    "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium
    chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Magnesium chloride hydrate", "match_type": "synonym", "identifier":
    "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium dichloride
    hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium dichloride hexahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium
    dichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "magnesium dichloride--water (1/2)",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium
    chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium dichloride--water (1/6)", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium
    dichloride--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl 2", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl*6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "Magnesium
    chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl*6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x 6 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2  x
    7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "MgCl2  x 76 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "MgCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 . 6H2O", "match_type": "synonym", "identifier":
    "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl2 x 6 H2O (200 g/l stock solution)", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O (200 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 X 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    X 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgCl2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "REJECTED", "ambiguity": "resolved:owned"}, {"label": "MgCl2 x 7H2O", "match_type":
    "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity": "unresolved:partial_chemistry"},
    {"label": "MgCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2.6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x
    6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgCl2x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x
    6H2O", "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2x7H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x
    6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unresolved:partial_chemistry"}, {"label": "MgCl2 x 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2x
    6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2·6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2
    x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MgCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:86345",
    "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2⋅6H2O", "match_type": "synonym",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2・6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86345", "preferred_term": "MgCl2
    x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate monohydrate", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese
    sulfate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Manganese sulfate hydrate", "match_type": "synonym", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) sulfate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate--water
    (1/1)", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) sulphate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "manganese(II) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate monohydrate", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4
    . H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O",
    "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4
    x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4
    ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O",
    "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4
    x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity":
    "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 . 12H2O", "match_type": "synonym",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2
    12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2
    x 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "AlK(SO4)2.12H2O", "match_type": "synonym",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "AlK(SO4)2·12H2O",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "AlK(SO4)2・12H2O", "match_type": "synonym", "identifier":
    "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aluminium potassium
    sulfate--water (1/12)", "match_type": "synonym", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Aluminum potassium disulfate dodecahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Aluminum potassium sulfate dodecahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O",
    "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KAl(SO4)2 . 12H2O", "match_type": "synonym", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2 x 12 H2O", "match_type":
    "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O",
    "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "KAl(SO4)2·12H2O", "match_type": "synonym", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KAl(SO4)2・12H2O", "match_type": "synonym",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kalinite",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potash alum dodecahydrate", "match_type": "synonym", "identifier":
    "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium alum
    dodecahydrate", "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "potassium aluminium sulfate dodecahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2
    x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium aluminum disulfate dodecahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O",
    "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}]},
    "missing_current_keys": ["CHEBI:26833"], "legacy_instances": [{"input": "target",
    "field_path": "ingredients[24].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198",
    "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198",
    "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198",
    "label": "Na2SeO4"}}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Whole pinned public catalog or complete recursive tree; exact legacy000198
    lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: The available current pinned material has no000198 token. It does not supply
    the historical numeric-ID correspondence; current CHEBI:77775 resolves independently.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Whole pinned public catalog or complete recursive tree; exact legacy000198
    lookup
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: The available current pinned material has no000198 token. It does not supply
    the historical numeric-ID correspondence; current CHEBI:77775 resolves independently.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-local-search
  kind: search
  reference: owned checkout
  locator: Exact historical key search in data/src/docs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: 'data/normalized_yaml/fungal/ferrous_iron_yeast_extract_medium.yaml:174:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/archaea/modified_picrophilus_medium.yaml:245:    id: MediaIngredientMech:000198

    data/normalized_yaml/specialized/modified_marine_medium.yaml:118:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/KOMODO_792_PYROLOBUS_FUMARII_MEDIUM.yaml:206:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml:213:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/archaea/KOMODO_766_THERMOCOCCUS_CHITINOPHAGUS_MEDIUM.yaml:66:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml:54:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/methanogen_ms_i_medium.yaml:226:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/pyrolobus_medium.yaml:228:    id: MediaIngredientMech:000198

    data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml:182:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/archaea/pyrolobus_fumarii_medium.yaml:215:    id: MediaIngredientMech:000198

    data/normalized_yaml/specialized/fe_iii_reducer_marine_enrichment_medium.yaml:128:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/archaea/aciduliprofundum_medium.yaml:212:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/methanosphaera_medium_i.yaml:55:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/methanosphaera_medium.yaml:54:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/JCM_J355_METHANOSPHAERA_MEDIUM.yaml:57:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/thermofilum_medium.yaml:86:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/archaeoglobus_infectus_medium.yaml:199:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml:242:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/mo_cfxi_medium__58d3ad1b.yaml:182:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/thermococcus_chitinophagus_medium.yaml:65:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/SPIROCHAETA_CELLOBIOSIPHILA_MEDIUM.yaml:176:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/sea_salts_tyg_medium__6486dbac.yaml:213:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/methanosphaera_medium__f110a698.yaml:54:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/syphc_medium.yaml:212:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/VULCANITHERMUS_MEDIUM.yaml:266:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/PLANTOMYCETACEAE_MEDIUM.yaml:150:    id: MediaIngredientMech:000198

    data/normalized_yaml/archaea/pfennig_thermofilum_medium.yaml:182:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium__2616625b.yaml:84:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/kiritimatiella_tyg_medium.yaml:215:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml:128:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/HALARSENATIBACTER_MEDIUM.yaml:115:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/pyrobaculum_aerophilum_medium__bc93f572.yaml:54:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/MARIDESULFOVIBRIO_MEDIUM.yaml:201:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/Meiothermus_hypogaeus_MEDIUM.yaml:213:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/NAUTILIA_NITRATIREDUCENS_MEDIUM.yaml:248:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/VULCANIBACILLUS_MEDIUM.yaml:210:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/THERMOANAEROBACULUM_AQUATICUM_MEDIUM.yaml:235:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/thermocrinis_albus_medium__8e47ff6d.yaml:135:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/st65_medium__23c51571.yaml:183:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/spirochaeta_cellobiosiphila_medium.yaml:136:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/pyrolobus_fumarii_medium__0aa02c21.yaml:255:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/THERMOVIBRIO_AMMONIFICANS_MEDIUM.yaml:245:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/congregibacter_syphc_medium.yaml:224:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/IGNAVIBACTERIA_MEDIUM.yaml:140:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/vulcanibacillus_medium__2277eb74.yaml:211:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/thermogutta_hypogea_medium.yaml:177:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/mariprofundus_es_medium.yaml:220:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/tanner_mod2_medium__ec1a1c56.yaml:215:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/DESULFUROMUSA_FERRIREDUCENS_MEDIUM.yaml:211:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/ferrous_iron_yeast_extract_medium__a821658e.yaml:174:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/thermincola_medium_co.yaml:246:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/vulcanithermus_medium.yaml:265:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml:128:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/THERMODESULFITIMONAS_MEDIUM.yaml:225:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml:194:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/sypg_medium__0c1821a0.yaml:225:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/methylomonas_medium_surf.yaml:285:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/anaerobic_alkaline_glucose_medium__bc3ee096.yaml:182:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml:137:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/acidihalobacter_prosperus_f5_medium__0fa15dd8.yaml:161:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/SMITHELLA_MEDIUM.yaml:233:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml:266:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/freshwater_iron_gel_medium__d012b865.yaml:64:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.yaml:42:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml:253:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/jcm_medium_no_244.yaml:216:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/svx8_medium__0a0a576b.yaml:183:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/methylomonas_medium_wsc.yaml:286:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/MEDIUM_for_SM250.yaml:144:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/METHANOSPHAERA_MEDIUM.yaml:57:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/THERMOFILUM_MEDIUM.yaml:86:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/thermobacter_roseum_medium__60c6c40b.yaml:277:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/geobacter_nbaf_medium__db485dcd.yaml:104:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/1_2_SME_MEDIUM_FOR_YA.yaml:213:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/alkaliphilus_crotonatoxidans_medium.yaml:199:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/METALLIBACTERIUM_MEDIUM.yaml:197:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium__6a83808e.yaml:128:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/THERMOHALOBACTER_MEDIUM.yaml:273:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/THERMOCOCCUS_CHITINOPHAGUS_MEDIUM.yaml:66:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/methylocystis_medium_nls.yaml:84:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml:118:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/DESULFOGLAEBA_MEDIUM.yaml:251:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/plantomycetaceae_medium.yaml:150:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/seawater_pyruvate_thiosulfate_medium__e78f35f1.yaml:294:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/syphc_medium__da30d435.yaml:289:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/syfac_medium__0aaeb681.yaml:212:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/ms_sulf_medium.yaml:226:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/desulfamplus_medium__51ba8b93.yaml:263:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/MARISPIROCHAETA_MEDIUM.yaml:193:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/gallionella_es_medium.yaml:199:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/thermincola_medium.yaml:247:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/PLANTOMYCETACEAE_MEDIUM_SBP2.yaml:253:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/acidithrix_ferrooydans_medium__b3120235.yaml:245:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/bacterial/JCM_J729_ACIDITHIOBACILLUS_FERRIVORANS_MEDIUM.yaml:242:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/modified_sme_medium__937d55ea.yaml:127:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml:116:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/pyrolobus_medium__bb7c3cdb.yaml:265:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/dissulfurimicrobium_hydrothermale_medium__63c2d6ea.yaml:163:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/modified_picrophilus_medium__2e13d4cd.yaml:282:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/PFENNIG_THERMOFILUM_MEDIUM.yaml:182:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/SELENATE_REDUCER_MEDIUM.yaml:114:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/sypc_medium.yaml:137:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/thermodesulfobacterium_hydrogenophilum_medium__c1daf6d7.yaml:142:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/ytps_medium__a290bac5.yaml:134:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/JCM_J470_VULCANIBACILLUS_MEDIUM.yaml:210:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/MODIFIED_SME_MEDIUM.yaml:130:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/alkaliphilus_crotonatoxidans_medium__05e4cdb7.yaml:199:    id:
    MediaIngredientMech:000198

    data/merge_yaml/merged/ARCHAEOGLOBUS_INFECTUS_MEDIUM.yaml:239:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/THERMOSULFIDIBACTER_MEDIUM.yaml:202:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/medium_for_z_1701_z_1702.yaml:106:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/vulcanibacillus_medium.yaml:212:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/thermoanaerobaculum_aquaticum_medium.yaml:235:    id:
    MediaIngredientMech:000198

    data/normalized_yaml/bacterial/sea_salts_tyg_medium.yaml:176:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/kiritimatiella_tyg_medium.yaml:175:    id: MediaIngredientMech:000198

    data/merge_yaml/merged/thermogutta_hypogea_medium__b2091adf.yaml:177:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/desulfamplus_medium.yaml:223:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/mo_cfxi_medium.yaml:182:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/halarsenatibacter_medium.yaml:115:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/tanner_mod2_medium.yaml:215:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/maridesulfovibrio_medium.yaml:161:    id: MediaIngredientMech:000198

    data/normalized_yaml/bacterial/mei'
  search_scope: rg --no-ignore --hidden across data, src and docs; recipe assertions
    are not independent historical identity proof.
- evidence_id: relationships
  kind: record_content
  reference: data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml
  locator: All three explicit relationship paths compared to exact Git tree and same-ID
    normalized owners
  accessed_at: '2026-10-21T11:47:50Z'
  support: refutes
  summary: '[{"input": "target", "field_path": "parent_media.path", "stored": "data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml",
    "same_id_actual_owner": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml"},
    {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "parent_media.path", "stored": "data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml",
    "same_id_actual_owner": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml"},
    {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml", "field_path":
    "variant_children[0].path", "stored": "data/normalized_yaml/bacterial/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "same_id_actual_owner": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml"}]'
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDULIPROFUNDUM_MEDIUM.yaml; data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml;
    data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:56.076801"}]}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:56.076801"}]}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "events": 9, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Current importer preserves main/stock separation, but its preparation parser
    collects steps from all solutions without headings. Current cleanup explicitly
    refuses unequal-value summation. Historical record notes preserve old sums; current
    code is not claimed to reproduce them. The inspected cocktail helper and its recorded
    four-row repair do not establish that the whole stock was recovered; current merge
    requires scientific-field compatibility.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Current importer preserves main/stock separation, but its preparation parser
    collects steps from all solutions without headings. Current cleanup explicitly
    refuses unequal-value summation. Historical record notes preserve old sums; current
    code is not claimed to reproduce them. The inspected cocktail helper and its recorded
    four-row repair do not establish that the whole stock was recovered; current merge
    requires scientific-field compatibility.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: scripts/apply_cocktail_nesting.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Current importer preserves main/stock separation, but its preparation parser
    collects steps from all solutions without headings. Current cleanup explicitly
    refuses unequal-value summation. Historical record notes preserve old sums; current
    code is not claimed to reproduce them. The inspected cocktail helper and its recorded
    four-row repair do not establish that the whole stock was recovered; current merge
    requires scientific-field compatibility.
  snapshot_sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Current importer preserves main/stock separation, but its preparation parser
    collects steps from all solutions without headings. Current cleanup explicitly
    refuses unequal-value summation. Historical record notes preserve old sums; current
    code is not claimed to reproduce them. The inspected cocktail helper and its recorded
    four-row repair do not establish that the whole stock was recovered; current merge
    requires scientific-field compatibility.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:47:50Z'
  support: context_only
  summary: Current importer preserves main/stock separation, but its preparation parser
    collects steps from all solutions without headings. Current cleanup explicitly
    refuses unequal-value summation. Historical record notes preserve old sums; current
    code is not claimed to reproduce them. The inspected cocktail helper and its recorded
    four-row repair do not establish that the whole stock was recovered; current merge
    requires scientific-field compatibility.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact accession and all maintained contributors
  outcome: concern
  summary: KOMODO 1083 explicitly links DSMZ 1083; the exact main and stock endpoints
    resolve. Both distinct stable normalized owner IDs are present under archaea.
    Source identity does not certify the historical summed quantities, nesting, or
    paths. The catalog aerobic=true conflicts with the primary anoxic preparation;
    it is attributed metadata, not independent oxygen-growth evidence.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - komodo
  - dsmz1083
  - mediadive1083api
  - id-search
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 105 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"NaCl\",\n    \"stored\": {\n      \"value\": \"39.97\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\": 30,\n  \
    \    \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\": 29.97,\n \
    \     \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\": 10,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: NaCl\",\n        \"exact_source_quote\"\
    : \"NaCl 30.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 30,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 29.97,\\n              \
    \          \\\"mmol_l\\\": 512.834,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n   \
    \     \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: NaCl\",\n\
    \        \"exact_source_quote\": \"NaCl 10.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 171.116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"correct\"\
    ,\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"ingredient\": \"MgSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"33.4965\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n   \
    \   \"main_source_amount\": 3.5,\n      \"main_source_unit\": \"g\",\n      \"\
    main_provider_g_per_L\": 3.4965,\n      \"main_provider_volume_ml\": 1001,\n \
    \     \"separate_stock_g_per_L\": 30,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: MgSO4 x 7 H2O\",\n      \
    \  \"exact_source_quote\": \"MgSO4 x 7 H2O 3.50 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 3.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3.4965,\\\
    n                        \\\"mmol_l\\\": 14.186,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n   \
    \     \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MgSO4 x\
    \ 7 H2O\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 30.00 g\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 30,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\n    \
    \                    \\\"mmol_l\\\": 121.716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"ingredient\": \"MgCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"2.74725\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n   \
    \   \"value\": \"2.74725\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"\
    Provider-declared 1001 ml main solution, not measured final volume\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: MgCl2 x 6 H2O\",\n      \
    \  \"exact_source_quote\": \"MgCl2 x 6 H2O 2.75 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 2.75,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.74725,\\\
    n                        \\\"mmol_l\\\": 13.5131,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\": \"\
    CaCl2 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"1.37962\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\": 0.38,\n\
    \      \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\": 0.37962,\n\
    \      \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\": 1,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: CaCl2 x 2 H2O\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.38 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.38,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.37962,\\\
    n                        \\\"mmol_l\\\": 2.58219,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CaCl2\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 1.00 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 6.80203,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"ingredient\": \"KCl\",\n    \"stored\": {\n      \"value\": \"0.32967\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"0.32967\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared\
    \ 1001 ml main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: KCl\",\n        \"exact_source_quote\"\
    : \"KCl 0.33 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.33,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.32967,\\n      \
    \                  \\\"mmol_l\\\": 4.42214,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\"\
    : \"NaBr\",\n    \"stored\": {\n      \"value\": \"0.04995\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.04995\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: NaBr\",\n        \"exact_source_quote\"\
    : \"NaBr 0.05 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NaBr\\\",\\n                        \\\"compound_id\\\": 353,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.04995,\\n      \
    \                  \\\"mmol_l\\\": 0.48547,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\"\
    : \"(NH4)2SO4\",\n    \"stored\": {\n      \"value\": \"0.0999001\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.0999001\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: (NH4)2SO4\",\n        \"exact_source_quote\"\
    : \"(NH4)2SO4 0.10 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0999001,\\\
    n                        \\\"mmol_l\\\": 0.756017,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"target\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"stored\": {\n      \"value\": \"0.27972\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.27972\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.28 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.28,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.27972,\\n      \
    \                  \\\"mmol_l\\\": 2.05548,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[8].concentration\",\n    \"ingredient\"\
    : \"Sodium resazurin\",\n    \"stored\": {\n      \"value\": \"0.0004995\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"\
    0.0004995\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared\
    \ 1001 ml main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Sodium resazurin\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.0004995,\\n         \
    \               \\\"mmol_l\\\": 0.0019887,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[9].concentration\",\n    \"ingredient\"\
    : \"Na3-citrate\",\n    \"stored\": {\n      \"value\": \"2.93706\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"2.93706\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Na3-citrate\",\n        \"exact_source_quote\"\
    : \"Na3-citrate 2.94 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Na3-citrate\\\",\\n                        \\\"compound_id\\\
    \": 205,\\n                        \\\"amount\\\": 2.94,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.93706,\\\
    n                        \\\"mmol_l\\\": 11.3809,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"target\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"Yeast extract\",\n    \"stored\": {\n      \"value\": \"0.999001\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.999001\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Yeast extract\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.999001,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[11].concentration\",\n    \"\
    ingredient\": \"Tryptone\",\n    \"stored\": {\n      \"value\": \"0.999001\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"0.999001\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared\
    \ 1001 ml main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Tryptone\",\n        \"exact_source_quote\"\
    : \"Tryptone (BD Bacto) 1.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Tryptone\\\",\\n                        \\\"compound_id\\\"\
    : 71,\\n                        \\\"attribute\\\": \\\"BD Bacto\\\",\\n      \
    \                  \\\"amount\\\": 1,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 0.999001,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n     \
    \ }\n    ],\n    \"explanation\": \"The existing provider-derived value has no\
    \ attached evidence. Keep the original source amount/unit and explicit provider\
    \ basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and\
    \ 0.50 ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"target\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"ingredient\"\
    : \"Sulfur\",\n    \"stored\": {\n      \"value\": \"9.99001\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"9.99001\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Sulfur\",\n        \"exact_source_quote\"\
    : \"Sulfur (powdered) 10.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\"\
    : 80,\\n                        \\\"condition\\\": \\\"\\\",\\n              \
    \          \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"\
    amount\\\": 10,\\n                        \\\"unit\\\": \\\"g\\\",\\n        \
    \                \\\"g_l\\\": 9.99001,\\n                        \\\"mmol_l\\\"\
    : 311.506,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[13].concentration\",\n    \"\
    ingredient\": \"Na2S x 9 H2O\",\n    \"stored\": {\n      \"value\": \"0.499501\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"0.499501\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared\
    \ 1001 ml main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Na2S x 9 H2O\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.499501,\\\
    n                        \\\"mmol_l\\\": 2.07967,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[14].concentration\",\n    \"ingredient\": \"\
    MnSO4 x H2O\",\n    \"stored\": {\n      \"value\": \"5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"5\",\n      \"\
    stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MnSO4\
    \ x H2O\",\n        \"exact_source_quote\": \"MnSO4 x H2O 5.00 g\",\n        \"\
    snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 29.583,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[15].concentration\",\n    \"ingredient\": \"\
    FeSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"1\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"1\",\n  \
    \    \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: FeSO4\
    \ x 7 H2O\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 1.00 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"mmol_l\\\": 3.59693,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[16].concentration\",\n    \"ingredient\": \"\
    CoCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"1.8\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"1.8\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CoCl2\
    \ x 6 H2O\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 1.80 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 13.8633,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[17].concentration\",\n    \"ingredient\": \"\
    ZnSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"1.8\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"1.8\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: ZnSO4\
    \ x 7 H2O\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 1.80 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 6.25954,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[18].concentration\",\n    \"ingredient\": \"\
    CuSO4 x 5 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CuSO4\
    \ x 5 H2O\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.10 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.400503,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"ingredients[19].concentration\",\n    \"ingredient\": \"AlK(SO4)2 x 12 H2O\"\
    ,\n    \"stored\": {\n      \"value\": \"0.18\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": {\n      \"stock_value\": \"0.18\",\n      \"stock_unit\"\
    : \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: AlK(SO4)2\
    \ x 12 H2O\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.18 g\",\n\
    \        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.18,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 0.379436,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"ingredients[20].concentration\",\n    \"ingredient\": \"H3BO3\",\n    \"stored\"\
    : {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\"\
    : {\n      \"stock_value\": \"0.1\",\n      \"stock_unit\": \"G_PER_L\",\n   \
    \   \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\":\
    \ 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: H3BO3\"\
    ,\n        \"exact_source_quote\": \"H3BO3 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\":\
    \ 37,\\n                        \\\"amount\\\": 0.1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n   \
    \                     \\\"mmol_l\\\": 1.61708,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[21].concentration\",\n    \"ingredient\": \"\
    Na2MoO4 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2MoO4\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.10 g\",\n  \
    \      \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.413309,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"target\",\n\
    \    \"field_path\": \"ingredients[22].concentration\",\n    \"ingredient\": \"\
    (NH4)2Ni(SO4)2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"2.8\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\":\
    \ \"2.8\",\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: (NH4)2Ni(SO4)2\
    \ x 6 H2O\",\n        \"exact_source_quote\": \"(NH4)2Ni(SO4)2 x 6 H2O 2.80 g\"\
    ,\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"(NH4)2Ni(SO4)2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 739,\\n                        \\\"amount\\\": 2.8,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 2.8,\\n                        \\\"mmol_l\\\": 7.08884,\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n     \
    \ }\n    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"ingredients[23].concentration\",\n    \"ingredient\": \"Na2WO4 x 2 H2O\",\n\
    \    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n      \"stock_unit\"\
    : \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2WO4\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.10 g\",\n   \
    \     \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.303168,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"ingredients[24].concentration\",\n    \"ingredient\": \"Na2SeO4\",\n    \"\
    stored\": {\n      \"value\": \"0.1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"proposed\": {\n      \"stock_value\": \"0.1\",\n      \"stock_unit\": \"\
    G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2SeO4\"\
    ,\n        \"exact_source_quote\": \"Na2SeO4 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2SeO4\\\",\\n                        \\\"compound_id\\\"\
    : 375,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.529241,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"NaCl\",\n    \"stored\": {\n      \"value\": \"39.97\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\": 30,\n  \
    \    \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\": 29.97,\n \
    \     \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\": 10,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: NaCl\",\n        \"exact_source_quote\"\
    : \"NaCl 30.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 30,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 29.97,\\n              \
    \          \\\"mmol_l\\\": 512.834,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n   \
    \     \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: NaCl\",\n\
    \        \"exact_source_quote\": \"NaCl 10.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 171.116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"correct\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"33.4965\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\"\
    : 3.5,\n      \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\": 3.4965,\n\
    \      \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\": 30,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: MgSO4 x 7 H2O\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 3.50 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 3.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3.4965,\\\
    n                        \\\"mmol_l\\\": 14.186,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n   \
    \     \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MgSO4 x\
    \ 7 H2O\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 30.00 g\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 30,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\n    \
    \                    \\\"mmol_l\\\": 121.716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"2.74725\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"2.74725\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: MgCl2 x 6 H2O\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 2.75 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 2.75,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.74725,\\\
    n                        \\\"mmol_l\\\": 13.5131,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"CaCl2 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"1.37962\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\"\
    : 0.38,\n      \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\":\
    \ 0.37962,\n      \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\"\
    : 1,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: CaCl2 x 2 H2O\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.38 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.38,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.37962,\\\
    n                        \\\"mmol_l\\\": 2.58219,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CaCl2\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 1.00 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 6.80203,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"stored\": {\n      \"value\": \"0.32967\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.32967\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KCl\",\n        \"exact_source_quote\"\
    : \"KCl 0.33 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.33,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.32967,\\n      \
    \                  \\\"mmol_l\\\": 4.42214,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\",\n\
    \    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\": \"\
    NaBr\",\n    \"stored\": {\n      \"value\": \"0.04995\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.04995\",\n      \"\
    unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main solution,\
    \ not measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: NaBr\",\n        \"exact_source_quote\"\
    : \"NaBr 0.05 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NaBr\\\",\\n                        \\\"compound_id\\\": 353,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.04995,\\n      \
    \                  \\\"mmol_l\\\": 0.48547,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\",\n\
    \    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\": \"\
    (NH4)2SO4\",\n    \"stored\": {\n      \"value\": \"0.0999001\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.0999001\",\n\
    \      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: (NH4)2SO4\",\n        \"\
    exact_source_quote\": \"(NH4)2SO4 0.10 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0999001,\\\
    n                        \\\"mmol_l\\\": 0.756017,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"stored\": {\n      \"value\": \"0.27972\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.27972\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.28 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.28,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.27972,\\n      \
    \                  \\\"mmol_l\\\": 2.05548,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\",\n\
    \    \"field_path\": \"ingredients[8].concentration\",\n    \"ingredient\": \"\
    Sodium resazurin\",\n    \"stored\": {\n      \"value\": \"0.0004995\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.0004995\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Sodium resazurin\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.0004995,\\n         \
    \               \\\"mmol_l\\\": 0.0019887,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\",\n\
    \    \"field_path\": \"ingredients[9].concentration\",\n    \"ingredient\": \"\
    Na3-citrate\",\n    \"stored\": {\n      \"value\": \"2.93706\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"2.93706\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Na3-citrate\",\n        \"\
    exact_source_quote\": \"Na3-citrate 2.94 g\",\n        \"snapshot_sha256\": \"\
    fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n        \"\
    parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Na3-citrate\\\",\\n                        \\\"compound_id\\\
    \": 205,\\n                        \\\"amount\\\": 2.94,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.93706,\\\
    n                        \\\"mmol_l\\\": 11.3809,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"Yeast extract\",\n    \"stored\": {\n      \"value\": \"0.999001\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.999001\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Yeast extract\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.999001,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\",\n\
    \    \"field_path\": \"ingredients[11].concentration\",\n    \"ingredient\": \"\
    Tryptone\",\n    \"stored\": {\n      \"value\": \"0.999001\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.999001\",\n \
    \     \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Tryptone\",\n        \"exact_source_quote\"\
    : \"Tryptone (BD Bacto) 1.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Tryptone\\\",\\n                        \\\"compound_id\\\"\
    : 71,\\n                        \\\"attribute\\\": \\\"BD Bacto\\\",\\n      \
    \                  \\\"amount\\\": 1,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 0.999001,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n     \
    \ }\n    ],\n    \"explanation\": \"The existing provider-derived value has no\
    \ attached evidence. Keep the original source amount/unit and explicit provider\
    \ basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and\
    \ 0.50 ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"ingredient\"\
    : \"Sulfur\",\n    \"stored\": {\n      \"value\": \"9.99001\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"9.99001\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Sulfur\",\n        \"exact_source_quote\"\
    : \"Sulfur (powdered) 10.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\"\
    : 80,\\n                        \\\"condition\\\": \\\"\\\",\\n              \
    \          \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"\
    amount\\\": 10,\\n                        \\\"unit\\\": \\\"g\\\",\\n        \
    \                \\\"g_l\\\": 9.99001,\\n                        \\\"mmol_l\\\"\
    : 311.506,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\",\n\
    \    \"field_path\": \"ingredients[13].concentration\",\n    \"ingredient\": \"\
    Na2S x 9 H2O\",\n    \"stored\": {\n      \"value\": \"0.499501\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.499501\",\n \
    \     \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Na2S x 9 H2O\",\n       \
    \ \"exact_source_quote\": \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.499501,\\\
    n                        \\\"mmol_l\\\": 2.07967,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[14].concentration\",\n    \"ingredient\"\
    : \"CuSO4 x 5 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CuSO4\
    \ x 5 H2O\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.10 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.400503,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[15].concentration\",\n    \"ingredient\"\
    : \"AlK(SO4)2 x 12 H2O\",\n    \"stored\": {\n      \"value\": \"0.18\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\"\
    : \"0.18\",\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: AlK(SO4)2 x\
    \ 12 H2O\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.18 g\",\n\
    \        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.18,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 0.379436,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[16].concentration\",\n    \"ingredient\"\
    : \"H3BO3\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n    \
    \  \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: H3BO3\"\
    ,\n        \"exact_source_quote\": \"H3BO3 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\":\
    \ 37,\\n                        \\\"amount\\\": 0.1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n   \
    \                     \\\"mmol_l\\\": 1.61708,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[17].concentration\",\n    \"ingredient\"\
    : \"Na2MoO4 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\"\
    ,\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n    \
    \  \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2MoO4 x 2\
    \ H2O\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.10 g\",\n      \
    \  \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.413309,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[18].concentration\",\n    \"ingredient\"\
    : \"(NH4)2Ni(SO4)2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"2.8\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\"\
    : \"2.8\",\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: (NH4)2Ni(SO4)2\
    \ x 6 H2O\",\n        \"exact_source_quote\": \"(NH4)2Ni(SO4)2 x 6 H2O 2.80 g\"\
    ,\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"(NH4)2Ni(SO4)2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 739,\\n                        \\\"amount\\\": 2.8,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 2.8,\\n                        \\\"mmol_l\\\": 7.08884,\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n     \
    \ }\n    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[19].concentration\",\n    \"ingredient\"\
    : \"Na2WO4 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\"\
    ,\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n    \
    \  \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2WO4 x 2 H2O\"\
    ,\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.303168,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[20].concentration\",\n    \"ingredient\"\
    : \"Na2SeO4\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2SeO4\"\
    ,\n        \"exact_source_quote\": \"Na2SeO4 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2SeO4\\\",\\n                        \\\"compound_id\\\"\
    : 375,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.529241,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[0].concentration\",\n    \"\
    ingredient\": \"MnSO4 x H2O\",\n    \"stored\": {\n      \"value\": \"5\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"\
    5\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MnSO4 x H2O\"\
    ,\n        \"exact_source_quote\": \"MnSO4 x H2O 5.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 29.583,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[1].concentration\",\n    \"\
    ingredient\": \"FeSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"1\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"\
    1\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: FeSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 1.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"mmol_l\\\": 3.59693,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[2].concentration\",\n    \"\
    ingredient\": \"CoCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"1.8\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"1.8\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CoCl2 x 6 H2O\"\
    ,\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 1.80 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 13.8633,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[3].concentration\",\n    \"\
    ingredient\": \"ZnSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"1.8\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"1.8\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: ZnSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 1.80 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 6.25954,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"NaCl\",\n    \"stored\": {\n      \"value\": \"39.97\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\": 30,\n  \
    \    \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\": 29.97,\n \
    \     \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\": 10,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: NaCl\",\n        \"exact_source_quote\"\
    : \"NaCl 30.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 30,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 29.97,\\n              \
    \          \\\"mmol_l\\\": 512.834,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n   \
    \     \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: NaCl\",\n\
    \        \"exact_source_quote\": \"NaCl 10.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 171.116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"correct\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"33.4965\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\"\
    : 3.5,\n      \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\": 3.4965,\n\
    \      \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\": 30,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: MgSO4 x 7 H2O\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 3.50 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 3.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3.4965,\\\
    n                        \\\"mmol_l\\\": 14.186,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n   \
    \     \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MgSO4 x\
    \ 7 H2O\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 30.00 g\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 30,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\n    \
    \                    \\\"mmol_l\\\": 121.716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"2.74725\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"2.74725\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: MgCl2 x 6 H2O\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 2.75 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 2.75,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.74725,\\\
    n                        \\\"mmol_l\\\": 13.5131,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"CaCl2 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"1.37962\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"main_source_amount\"\
    : 0.38,\n      \"main_source_unit\": \"g\",\n      \"main_provider_g_per_L\":\
    \ 0.37962,\n      \"main_provider_volume_ml\": 1001,\n      \"separate_stock_g_per_L\"\
    : 1,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: CaCl2 x 2 H2O\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.38 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.38,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.37962,\\\
    n                        \\\"mmol_l\\\": 2.58219,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CaCl2\
    \ x 2 H2O\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 1.00 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 6.80203,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stored value combines main-provider\
    \ g/L and undiluted stock g/L. Those bases cannot be summed. Restore distinct\
    \ main mass and complete stock composition/dose; do not claim the primary water\
    \ quantity proves a final mixed volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"stored\": {\n      \"value\": \"0.32967\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.32967\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KCl\",\n        \"exact_source_quote\"\
    : \"KCl 0.33 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.33,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.32967,\\n      \
    \                  \\\"mmol_l\\\": 4.42214,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"ingredient\": \"NaBr\",\n    \"stored\"\
    : {\n      \"value\": \"0.04995\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"\
    proposed\": {\n      \"value\": \"0.04995\",\n      \"unit\": \"G_PER_L\",\n \
    \     \"basis\": \"Provider-declared 1001 ml main solution, not measured final\
    \ volume\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: NaBr\",\n        \"exact_source_quote\"\
    : \"NaBr 0.05 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NaBr\\\",\\n                        \\\"compound_id\\\": 353,\\\
    n                        \\\"amount\\\": 0.05,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.04995,\\n      \
    \                  \\\"mmol_l\\\": 0.48547,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[6].concentration\",\n    \"ingredient\": \"(NH4)2SO4\",\n    \"\
    stored\": {\n      \"value\": \"0.0999001\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"proposed\": {\n      \"value\": \"0.0999001\",\n      \"unit\": \"\
    G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main solution, not measured\
    \ final volume\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: (NH4)2SO4\",\n        \"\
    exact_source_quote\": \"(NH4)2SO4 0.10 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 0.1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0999001,\\\
    n                        \\\"mmol_l\\\": 0.756017,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"KH2PO4\",\n    \"stored\": {\n      \"value\": \"0.27972\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.27972\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.28 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.28,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.27972,\\n      \
    \                  \\\"mmol_l\\\": 2.05548,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[8].concentration\",\n    \"ingredient\": \"Sodium resazurin\"\
    ,\n    \"stored\": {\n      \"value\": \"0.0004995\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"proposed\": {\n      \"value\": \"0.0004995\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main solution, not\
    \ measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Sodium resazurin\",\n   \
    \     \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.0004995,\\n         \
    \               \\\"mmol_l\\\": 0.0019887,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[9].concentration\",\n    \"ingredient\": \"Na3-citrate\",\n  \
    \  \"stored\": {\n      \"value\": \"2.93706\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": {\n      \"value\": \"2.93706\",\n      \"unit\": \"\
    G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main solution, not measured\
    \ final volume\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Na3-citrate\",\n        \"\
    exact_source_quote\": \"Na3-citrate 2.94 g\",\n        \"snapshot_sha256\": \"\
    fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n        \"\
    parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Na3-citrate\\\",\\n                        \\\"compound_id\\\
    \": 205,\\n                        \\\"amount\\\": 2.94,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.93706,\\\
    n                        \\\"mmol_l\\\": 11.3809,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"Yeast extract\",\n    \"stored\": {\n      \"value\": \"0.999001\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.999001\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml\
    \ main solution, not measured final volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Yeast extract\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.999001,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[11].concentration\",\n    \"ingredient\": \"Tryptone\",\n    \"\
    stored\": {\n      \"value\": \"0.999001\",\n      \"unit\": \"G_PER_L\"\n   \
    \ },\n    \"proposed\": {\n      \"value\": \"0.999001\",\n      \"unit\": \"\
    G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main solution, not measured\
    \ final volume\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Tryptone\",\n        \"exact_source_quote\"\
    : \"Tryptone (BD Bacto) 1.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Tryptone\\\",\\n                        \\\"compound_id\\\"\
    : 71,\\n                        \\\"attribute\\\": \\\"BD Bacto\\\",\\n      \
    \                  \\\"amount\\\": 1,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 0.999001,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n     \
    \ }\n    ],\n    \"explanation\": \"The existing provider-derived value has no\
    \ attached evidence. Keep the original source amount/unit and explicit provider\
    \ basis. For sodium resazurin, preserve separately the source 0.1% w/v stock and\
    \ 0.50 ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"ingredient\"\
    : \"Sulfur\",\n    \"stored\": {\n      \"value\": \"9.99001\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"9.99001\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main\
    \ solution, not measured final volume\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Sulfur\",\n        \"exact_source_quote\"\
    : \"Sulfur (powdered) 10.00 g\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\"\
    : 80,\\n                        \\\"condition\\\": \\\"\\\",\\n              \
    \          \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"\
    amount\\\": 10,\\n                        \\\"unit\\\": \\\"g\\\",\\n        \
    \                \\\"g_l\\\": 9.99001,\\n                        \\\"mmol_l\\\"\
    : 311.506,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The existing provider-derived value\
    \ has no attached evidence. Keep the original source amount/unit and explicit\
    \ provider basis. For sodium resazurin, preserve separately the source 0.1% w/v\
    \ stock and 0.50 ml dose; this mass equivalence alone is not its full preparation\
    \ representation.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[13].concentration\",\n    \"ingredient\": \"Na2S x 9 H2O\",\n\
    \    \"stored\": {\n      \"value\": \"0.499501\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"proposed\": {\n      \"value\": \"0.499501\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"basis\": \"Provider-declared 1001 ml main solution, not\
    \ measured final volume\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Na2S x 9 H2O\",\n       \
    \ \"exact_source_quote\": \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.499501,\\\
    n                        \\\"mmol_l\\\": 2.07967,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing provider-derived value has no attached\
    \ evidence. Keep the original source amount/unit and explicit provider basis.\
    \ For sodium resazurin, preserve separately the source 0.1% w/v stock and 0.50\
    \ ml dose; this mass equivalence alone is not its full preparation representation.\"\
    \n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[14].concentration\",\n    \"ingredient\"\
    : \"CuSO4 x 5 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CuSO4\
    \ x 5 H2O\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.10 g\",\n    \
    \    \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.400503,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[15].concentration\",\n    \"ingredient\"\
    : \"AlK(SO4)2 x 12 H2O\",\n    \"stored\": {\n      \"value\": \"0.18\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\"\
    : \"0.18\",\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: AlK(SO4)2 x\
    \ 12 H2O\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.18 g\",\n\
    \        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.18,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 0.379436,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[16].concentration\",\n    \"ingredient\"\
    : \"H3BO3\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n    \
    \  \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: H3BO3\"\
    ,\n        \"exact_source_quote\": \"H3BO3 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\":\
    \ 37,\\n                        \\\"amount\\\": 0.1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n   \
    \                     \\\"mmol_l\\\": 1.61708,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[17].concentration\",\n    \"ingredient\"\
    : \"Na2MoO4 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\"\
    ,\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n    \
    \  \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2MoO4 x 2\
    \ H2O\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.10 g\",\n      \
    \  \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.413309,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[18].concentration\",\n    \"ingredient\"\
    : \"(NH4)2Ni(SO4)2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"2.8\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\"\
    : \"2.8\",\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n\
    \      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: (NH4)2Ni(SO4)2\
    \ x 6 H2O\",\n        \"exact_source_quote\": \"(NH4)2Ni(SO4)2 x 6 H2O 2.80 g\"\
    ,\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"(NH4)2Ni(SO4)2 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 739,\\n                        \\\"amount\\\": 2.8,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 2.8,\\n                        \\\"mmol_l\\\": 7.08884,\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n     \
    \ }\n    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[19].concentration\",\n    \"ingredient\"\
    : \"Na2WO4 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\"\
    ,\n      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n    \
    \  \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2WO4 x 2 H2O\"\
    ,\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 0.1,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.303168,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\n      }\n\
    \    ],\n    \"explanation\": \"A stock strength is still in direct ingredients.\
    \ Move its representation into the complete mineral-elixir stock, preserving dose\
    \ and scope instead of treating it as a main-medium amount.\"\n  },\n  {\n   \
    \ \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[20].concentration\",\n    \"ingredient\"\
    : \"Na2SeO4\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"stock_value\": \"0.1\",\n\
    \      \"stock_unit\": \"G_PER_L\",\n      \"stock_volume_ml\": 1000,\n      \"\
    stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Na2SeO4\"\
    ,\n        \"exact_source_quote\": \"Na2SeO4 0.10 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2SeO4\\\",\\n                        \\\"compound_id\\\"\
    : 375,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.529241,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"A stock strength is still in direct\
    \ ingredients. Move its representation into the complete mineral-elixir stock,\
    \ preserving dose and scope instead of treating it as a main-medium amount.\"\n\
    \  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[0].concentration\",\n    \"\
    ingredient\": \"MnSO4 x H2O\",\n    \"stored\": {\n      \"value\": \"5\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"\
    5\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MnSO4 x H2O\"\
    ,\n        \"exact_source_quote\": \"MnSO4 x H2O 5.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"mmol_l\\\": 29.583,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[1].concentration\",\n    \"\
    ingredient\": \"FeSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"1\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"\
    1\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: FeSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 1.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"mmol_l\\\": 3.59693,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[2].concentration\",\n    \"\
    ingredient\": \"CoCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"1.8\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"1.8\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CoCl2 x 6 H2O\"\
    ,\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 1.80 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 13.8633,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].composition[3].concentration\",\n    \"\
    ingredient\": \"ZnSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"1.8\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\":\
    \ \"1.8\",\n      \"unit\": \"G_PER_L\",\n      \"basis\": \"Existing mineral-elixir\
    \ composition, provider 1000 ml stock volume\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: ZnSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 1.80 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 6.25954,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"This owner already places the unchanged\
    \ strength under its stock composition, but no attached matching amount evidence\
    \ exists. It is not verified by the correctly nested position alone.\"\n  },\n\
    \  {\n    \"decision\": \"add\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"solutions\",\n    \"stored\": null,\n    \"ingredient\": \"Wolfe's mineral\
    \ elixir addition\",\n    \"proposed\": {\n      \"amount\": 1,\n      \"unit\"\
    : \"ml\",\n      \"basis\": \"Exact source listed batch; provider main.volume\
    \ 1001 ml\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Wolfe's mineral elixir\"\
    ,\n        \"exact_source_quote\": \"Wolfe's mineral elixir 1.00 ml\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Wolfe's mineral elixir\\\",\\n                        \\\"solution_id\\\
    \": 1605,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The source gives 1 ml per listed batch.\
    \ Existing owner 1 ML_PER_L and per-litre wording need explicit qualification\
    \ against provider 1001 ml; the source does not independently measure a final\
    \ litre. Target omits the addition entirely.\"\n  },\n  {\n    \"decision\": \"\
    correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].concentration\",\n    \"stored\": {\n  \
    \    \"value\": \"1\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"ingredient\"\
    : \"Wolfe's mineral elixir addition\",\n    \"proposed\": {\n      \"amount\"\
    : 1,\n      \"unit\": \"ml\",\n      \"basis\": \"Exact source listed batch; provider\
    \ main.volume 1001 ml\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Wolfe's mineral elixir\"\
    ,\n        \"exact_source_quote\": \"Wolfe's mineral elixir 1.00 ml\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Wolfe's mineral elixir\\\",\\n                        \\\"solution_id\\\
    \": 1605,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The source gives 1 ml per listed batch.\
    \ Existing owner 1 ML_PER_L and per-litre wording need explicit qualification\
    \ against provider 1001 ml; the source does not independently measure a final\
    \ litre. Target omits the addition entirely.\"\n  },\n  {\n    \"decision\": \"\
    correct\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].concentration\",\n    \"stored\": {\n  \
    \    \"value\": \"1\",\n      \"unit\": \"ML_PER_L\"\n    },\n    \"ingredient\"\
    : \"Wolfe's mineral elixir addition\",\n    \"proposed\": {\n      \"amount\"\
    : 1,\n      \"unit\": \"ml\",\n      \"basis\": \"Exact source listed batch; provider\
    \ main.volume 1001 ml\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Wolfe's mineral elixir\"\
    ,\n        \"exact_source_quote\": \"Wolfe's mineral elixir 1.00 ml\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Wolfe's mineral elixir\\\",\\n                        \\\"solution_id\\\
    \": 1605,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The source gives 1 ml per listed batch.\
    \ Existing owner 1 ML_PER_L and per-litre wording need explicit qualification\
    \ against provider 1001 ml; the source does not independently measure a final\
    \ litre. Target omits the addition entirely.\"\n  },\n  {\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n   \
    \     \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Distinct mineral-elixir\
    \ MgSO4 x 7 H2O\",\n    \"proposed\": {\n      \"value\": 30,\n      \"unit\"\
    : \"G_PER_L\",\n      \"scope\": \"Stock composition only\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: MgSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 30.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 30,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\n    \
    \                    \\\"mmol_l\\\": 121.716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"These three stock constituents were\
    \ combined into main-salt numbers rather than retained as separate stock constituents.\
    \ Restore the stock node while correcting the corresponding historical sum; do\
    \ not add a second neat main dose.\"\n  },\n  {\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"solutions\",\n        \"stored\": null\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Distinct mineral-elixir\
    \ NaCl\",\n    \"proposed\": {\n      \"value\": 10,\n      \"unit\": \"G_PER_L\"\
    ,\n      \"scope\": \"Stock composition only\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: NaCl\",\n  \
    \      \"exact_source_quote\": \"NaCl 10.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 171.116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"These three stock constituents were\
    \ combined into main-salt numbers rather than retained as separate stock constituents.\
    \ Restore the stock node while correcting the corresponding historical sum; do\
    \ not add a second neat main dose.\"\n  },\n  {\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"solutions\",\n        \"stored\": null\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Distinct mineral-elixir\
    \ CaCl2 x 2 H2O\",\n    \"proposed\": {\n      \"value\": 1,\n      \"unit\":\
    \ \"G_PER_L\",\n      \"scope\": \"Stock composition only\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: CaCl2 x 2 H2O\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 1.00 g\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 6.80203,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"These three stock constituents were\
    \ combined into main-salt numbers rather than retained as separate stock constituents.\
    \ Restore the stock node while correcting the corresponding historical sum; do\
    \ not add a second neat main dose.\"\n  },\n  {\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve ingredients (except sulfur and sulfide)\
    \ and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials containing already the appropriate amount of powdered sulfur\
    \ and autoclave for 60 min at <b>105°C</b>. Prior to inoculation add sulfide from\
    \ a sterile anoxic stock solution prepared under 100% N2 gas and adjust pH of\
    \ complete medium to 4.5.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"ADJUST_PH\",\n            \"description\": \"\
    First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.\"\n\
    \          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Main solvent volume\"\
    ,\n    \"proposed\": {\n      \"amount\": 1000,\n      \"unit\": \"ml\",\n   \
    \   \"scope\": \"Distilled water in main recipe\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main recipe: Distilled water\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[15]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 16,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Primary water 1000 ml plus 1 ml elixir\
    \ and 0.5 ml indicator totals 1001.5 ml listed liquids before sulfide stock/titration.\
    \ Provider declares 1001 ml; do not resolve that difference by assuming measured\
    \ final volume or a rounding rule.\"\n  },\n  {\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"solutions\",\n        \"stored\": null\n      }\n    ],\n    \"\
    ingredient\": \"Mineral-elixir solvent volume\",\n    \"proposed\": {\n      \"\
    amount\": 1000,\n      \"unit\": \"ml\",\n      \"scope\": \"Stock preparation\
    \ water\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n\
    \        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Stock water is not a second litre added\
    \ to the receiving medium.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n\
    \    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].preparation_notes\",\n    \"stored\": \"\
    Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and\
    \ volume from MediaDive (#150).\",\n    \"ingredient\": \"Existing stock 1000\
    \ ml preparation context\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n\
    \        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The 1000 ml stock context matches the\
    \ provider stock volume and listed water. The same note’s per-litre addition wording\
    \ is separately corrected; this decision supports only the stock-preparation volume.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"solutions[0].preparation_notes\",\n    \"stored\": \"\
    Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and\
    \ volume from MediaDive (#150).\",\n    \"ingredient\": \"Existing stock 1000\
    \ ml preparation context\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Wolfe's mineral elixir subsection: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n\
    \        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"The 1000 ml stock context matches the\
    \ provider stock volume and listed water. The same note’s per-litre addition wording\
    \ is separately corrected; this decision supports only the stock-preparation volume.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"target\",\n        \"field_path\": \"solutions\",\n      \
    \  \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Sodium resazurin\
    \ stock strength\",\n    \"proposed\": {\n      \"value\": 0.1,\n      \"unit\"\
    : \"%w/v\",\n      \"scope\": \"Indicator stock strength or its listed-batch addition,\
    \ separately from provider-derived mass\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Sodium resazurin\",\n   \
    \     \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.0004995,\\n         \
    \               \\\"mmol_l\\\": 0.0019887,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve both source inputs. 0.1 g/100\
    \ ml * 0.5 ml = 0.0005 g transferred; dividing by provider 1.001 L gives approximately\
    \ 0.0004995 g/L, without establishing true final mixed volume.\"\n  },\n  {\n\
    \    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"solutions\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Sodium resazurin\
    \ stock dose\",\n    \"proposed\": {\n      \"value\": 0.5,\n      \"unit\": \"\
    ml\",\n      \"scope\": \"Indicator stock strength or its listed-batch addition,\
    \ separately from provider-derived mass\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Sodium resazurin\",\n   \
    \     \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n     \
    \   \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1083api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1083\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.0004995,\\n         \
    \               \\\"mmol_l\\\": 0.0019887,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3d0210944be44bdfbe771bb1e40bdf97680c1a30739a0365668affe9c41304a0\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve both source inputs. 0.1 g/100\
    \ ml * 0.5 ml = 0.0005 g transferred; dividing by provider 1.001 L gives approximately\
    \ 0.0004995 g/L, without establishing true final mixed volume.\"\n  },\n  {\n\
    \    \"decision\": \"add\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\": \"Sparging\
    \ gas\",\n    \"proposed\": \"80% nitrogen/20% carbon dioxide mixture\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sparging gas\"\
    ,\n        \"exact_source_quote\": \"80% N2 and 20%\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Sparging gas\",\n    \"proposed\": \"80% nitrogen/20% carbon dioxide mixture\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sparging gas\"\
    ,\n        \"exact_source_quote\": \"80% N2 and 20%\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0].description\",\n    \"stored\":\
    \ \"Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80%\
    \ N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ already the appropriate amount of powdered sulfur and autoclave for 60 min at\
    \ <b>105°C</b>. Prior to inoculation add sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas and adjust pH of complete medium to 4.5.\",\n   \
    \ \"ingredient\": \"Sparging gas\",\n    \"proposed\": \"80% nitrogen/20% carbon\
    \ dioxide mixture\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sparging gas\"\
    ,\n        \"exact_source_quote\": \"80% N2 and 20%\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"target\",\n  \
    \  \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Sparging duration\",\n    \"proposed\": \"30–45 min\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation paragraph; Sparging duration\"\
    ,\n        \"exact_source_quote\": \"30 - 45 min\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Sparging duration\",\n    \"proposed\": \"30–45 min\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation paragraph; Sparging duration\"\
    ,\n        \"exact_source_quote\": \"30 - 45 min\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0].description\",\n    \"stored\":\
    \ \"Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80%\
    \ N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ already the appropriate amount of powdered sulfur and autoclave for 60 min at\
    \ <b>105°C</b>. Prior to inoculation add sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas and adjust pH of complete medium to 4.5.\",\n   \
    \ \"ingredient\": \"Sparging duration\",\n    \"proposed\": \"30–45 min\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sparging duration\"\
    ,\n        \"exact_source_quote\": \"30 - 45 min\",\n        \"snapshot_sha256\"\
    : \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\",\n    \
    \    \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"target\",\n  \
    \  \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Sterilization temperature and duration\",\n    \"proposed\": \"105°C for 60\
    \ min\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sterilization\
    \ temperature and duration\",\n        \"exact_source_quote\": \"autoclave for\
    \ 60 min at 105°C.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Sterilization temperature and duration\",\n    \"proposed\": \"105°C for 60\
    \ min\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sterilization\
    \ temperature and duration\",\n        \"exact_source_quote\": \"autoclave for\
    \ 60 min at 105°C.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0].description\",\n    \"stored\":\
    \ \"Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80%\
    \ N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ already the appropriate amount of powdered sulfur and autoclave for 60 min at\
    \ <b>105°C</b>. Prior to inoculation add sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas and adjust pH of complete medium to 4.5.\",\n   \
    \ \"ingredient\": \"Sterilization temperature and duration\",\n    \"proposed\"\
    : \"105°C for 60 min\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Sterilization\
    \ temperature and duration\",\n        \"exact_source_quote\": \"autoclave for\
    \ 60 min at 105°C.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"target\",\n  \
    \  \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Later sulfide-stock gas\",\n    \"proposed\": \"100% nitrogen only for the\
    \ sulfide-stock stage\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Later sulfide-stock\
    \ gas\",\n        \"exact_source_quote\": \"stock solution prepared under 100%\
    \ N2 gas\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"Later sulfide-stock gas\",\n    \"proposed\": \"100% nitrogen only for the\
    \ sulfide-stock stage\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Later sulfide-stock\
    \ gas\",\n        \"exact_source_quote\": \"stock solution prepared under 100%\
    \ N2 gas\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0].description\",\n    \"stored\":\
    \ \"Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80%\
    \ N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ already the appropriate amount of powdered sulfur and autoclave for 60 min at\
    \ <b>105°C</b>. Prior to inoculation add sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas and adjust pH of complete medium to 4.5.\",\n   \
    \ \"ingredient\": \"Later sulfide-stock gas\",\n    \"proposed\": \"100% nitrogen\
    \ only for the sulfide-stock stage\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation paragraph; Later sulfide-stock\
    \ gas\",\n        \"exact_source_quote\": \"stock solution prepared under 100%\
    \ N2 gas\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already retains this\
    \ exact stage; target/KOMODO lack preparation. Preserve initial mixed-gas and\
    \ later stock-gas scopes, sulfur-containing vessels and the separate sulfide addition.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"target\",\n        \"field_path\": \"ph_value\"\
    ,\n        \"stored\": 4.5\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 4.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 4.5\n      }\n \
    \   ],\n    \"ingredient\": \"Target complete-medium pH\",\n    \"proposed\":\
    \ 4.5,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final main preparation sentence\",\n \
    \       \"exact_source_quote\": \"adjust pH of complete medium to 4.5.\",\n  \
    \      \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The scalar value already matches; attach\
    \ narrow evidence and preserve the end-of-main-preparation scope.\"\n  },\n  {\n\
    \    \"decision\": \"add\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"solutions\",\n    \"stored\": null,\n    \"ingredient\": \"Mineral-elixir\
    \ pH\",\n    \"proposed\": {\n      \"pH\": 1.0,\n      \"stage\": \"Water acidification\
    \ before dissolving stock salts\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 2 continuation of Wolfe mineral-elixir subsection\"\
    ,\n        \"exact_source_quote\": \"First adjust pH to 1.0 with diluted H2SO4,\
    \ then add and dissolve the salts.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner needs its existing root\
    \ preparation step scoped to the stock. Other layers need this missing stock instruction\
    \ added. Preserve complete-medium pH 4.5.\"\n  },\n  {\n    \"decision\": \"add\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n    \"field_path\": \"solutions\",\n    \"stored\": [\n      {\n        \"\
    preferred_term\": \"Wolfe's mineral elixir\",\n        \"composition\": [\n  \
    \        {\n            \"preferred_term\": \"MnSO4 x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:86364\",\n              \"label\": \"manganese(II)\
    \ sulfate monohydrate\"\n            },\n            \"concentration\": {\n  \
    \            \"value\": \"5\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:86364\",\n              \"label\": \"manganese(II) sulfate monohydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    FeSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\"\
    ,\n              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"1\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"CoCl2 x 6 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt chloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    1.8\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt\
    \ chloride hexahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"ZnSO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate heptahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    1.8\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          }\n        ],\n        \"concentration\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"ML_PER_L\"\n        },\n\
    \        \"preparation_notes\": \"Stock prepared in 1000 ml; added at 1 ml per\
    \ litre of medium. Composition and volume from MediaDive (#150).\"\n      }\n\
    \    ],\n    \"ingredient\": \"Mineral-elixir pH\",\n    \"proposed\": {\n   \
    \   \"pH\": 1.0,\n      \"stage\": \"Water acidification before dissolving stock\
    \ salts\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 2 continuation of Wolfe mineral-elixir subsection\"\
    ,\n        \"exact_source_quote\": \"First adjust pH to 1.0 with diluted H2SO4,\
    \ then add and dissolve the salts.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner needs its existing root\
    \ preparation step scoped to the stock. Other layers need this missing stock instruction\
    \ added. Preserve complete-medium pH 4.5.\"\n  },\n  {\n    \"decision\": \"correct\"\
    ,\n    \"local_input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[1].description\",\n    \"stored\":\
    \ \"First adjust pH to 1.0 with diluted H2SO4, then add and dissolve the salts.\"\
    ,\n    \"ingredient\": \"Mineral-elixir pH\",\n    \"proposed\": {\n      \"pH\"\
    : 1.0,\n      \"stage\": \"Water acidification before dissolving stock salts\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 2 continuation of Wolfe mineral-elixir subsection\"\
    ,\n        \"exact_source_quote\": \"First adjust pH to 1.0 with diluted H2SO4,\
    \ then add and dissolve the salts.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner needs its existing root\
    \ preparation step scoped to the stock. Other layers need this missing stock instruction\
    \ added. Preserve complete-medium pH 4.5.\"\n  },\n  {\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"solutions\",\n        \"stored\": null\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"Wolfe's mineral elixir\",\n            \"composition\"\
    : [\n              {\n                \"preferred_term\": \"MnSO4 x H2O\",\n \
    \               \"term\": {\n                  \"id\": \"CHEBI:86364\",\n    \
    \              \"label\": \"manganese(II) sulfate monohydrate\"\n            \
    \    },\n                \"concentration\": {\n                  \"value\": \"\
    5\",\n                  \"unit\": \"G_PER_L\"\n                },\n          \
    \      \"mediaingredientmech_chebi_term\": {\n                  \"id\": \"CHEBI:86364\"\
    ,\n                  \"label\": \"manganese(II) sulfate monohydrate\"\n      \
    \          }\n              },\n              {\n                \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                },\n                \"concentration\": {\n                 \
    \ \"value\": \"1\",\n                  \"unit\": \"G_PER_L\"\n               \
    \ },\n                \"mediaingredientmech_chebi_term\": {\n                \
    \  \"id\": \"CHEBI:75836\",\n                  \"label\": \"iron(2+) sulfate heptahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"CoCl2 x 6 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\n\
    \                },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:53503\",\n                  \"label\": \"cobalt chloride hexahydrate\"\
    \n                }\n              },\n              {\n                \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n                \"term\": {\n                  \"id\": \"\
    CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\n \
    \               },\n                \"concentration\": {\n                  \"\
    value\": \"1.8\",\n                  \"unit\": \"G_PER_L\"\n                },\n\
    \                \"mediaingredientmech_chebi_term\": {\n                  \"id\"\
    : \"CHEBI:32312\",\n                  \"label\": \"zinc sulfate heptahydrate\"\
    \n                }\n              }\n            ],\n            \"concentration\"\
    : {\n              \"value\": \"1\",\n              \"unit\": \"ML_PER_L\"\n \
    \           },\n            \"preparation_notes\": \"Stock prepared in 1000 ml;\
    \ added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).\"\
    \n          }\n        ]\n      }\n    ],\n    \"ingredient\": \"Stock acid amount\
    \ and strength\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1083\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 2 mineral-elixir stock preparation\",\n\
    \        \"exact_source_quote\": \"First adjust pH to 1.0 with diluted H2SO4,\
    \ then add and dissolve the salts.\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"Diluted sulfuric acid is specified to\
    \ reach stock pH 1.0, but no acid amount or strength is provided; no numeric conversion\
    \ is justified.\"\n  },\n  {\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/aciduliprofundum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except sulfur and sulfide) and sparge medium with 80%\
    \ N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Dispense medium\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials containing\
    \ already the appropriate amount of powdered sulfur and autoclave for 60 min at\
    \ <b>105°C</b>. Prior to inoculation add sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas and adjust pH of complete medium to 4.5.\"\n    \
    \  }\n    ],\n    \"ingredient\": \"Separate sulfide stock strength and volume\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1083\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1083.pdf\"\
    ,\n        \"source_locator\": \"Page 1 later main-preparation sulfide addition\"\
    ,\n        \"exact_source_quote\": \"add sulfide from a sterile anoxic stock solution\
    \ prepared under 100% N2 gas\",\n        \"snapshot_sha256\": \"fa5336b261aa3e5c990086ce968935690d08355f14067f71ac93e6522c2c47ba\"\
    ,\n        \"parsed_text_sha256\": \"bc9036e81357f7ac152f59334524f378a076f38c05bfddc45af8a687c4149249\"\
    \n      }\n    ],\n    \"explanation\": \"The main table supports 0.50 g Na2S·9H2O\
    \ per listed batch; the separate sulfide stock strength and transfer volume are\
    \ not supplied. Preserve this unresolved preparation detail without inferring\
    \ a stock recipe.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Identifier metadata, exact secondary keys and supplied-form scope
  outcome: concern
  summary: 23 distinct primary/current-secondary identifiers resolve. 0 label instances
    differ from current canonical labels; 1 asserted current secondary keys lack an
    exact pinned index row. Legacy numeric links are assessed separately and are not
    established by CHEBI correspondence. Target linkage is 23/25 primary and 22/25
    secondary ingredient instances; this measures presence, not source validity.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - record
  - mim
  - chebi26710
  - chebi26833
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi53258
  - chebi53503
  - chebi62946
  - chebi63004
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi77775
  - chebi86149
  - chebi86158
  - chebi86345
  - chebi86364
  - chebi86465
  - chebi8806
  details: '{"label_drift": [], "missing_secondary_keys": ["CHEBI:26833"], "legacy_instances":
    [{"input": "target", "field_path": "ingredients[24].mediaingredientmech_term",
    "term": {"id": "MediaIngredientMech:000198", "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml",
    "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198",
    "label": "Na2SeO4"}}, {"input": "data/normalized_yaml/archaea/aciduliprofundum_medium.yaml",
    "field_path": "ingredients[20].mediaingredientmech_term", "term": {"id": "MediaIngredientMech:000198",
    "label": "Na2SeO4"}}], "coverage_scale": "0–100 percent; each ingredient instance
    counted once", "denominator": 25, "primary_percent": 92.0, "secondary_percent":
    88.0}'
- assessment_id: forms
  area: grounding
  topic: Supplied chemical forms and secondary-link limits
  outcome: concern
  summary: Sodium resazurin is mapped to CHEBI:8806, whose formula C12H7NO4 contains
    no sodium. Sulfur atom is a valid broader elemental term but does not carry the
    source powder context; no specific allotrope or replacement is inferred. CHEBI:26833
    has zero exact rows in the fully available pinned MIM index, a confirmed secondary
    mapping gap rather than an unavailable check. All stated hydrates otherwise retain
    matching source forms; unspecified citrate hydration is not guessed.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - dsmz1083
  - chebi8806
  - chebi26833
  - chebi53258
  - mim
- assessment_id: preparation
  area: completeness
  topic: Main/stock sequence and generated-layer loss
  outcome: concern
  summary: The target has 25 direct ingredients and no solutions; both current owners
    have 21 direct ingredients and four nested stock components, still incomplete.
    Only the DSMZ owner retains the anoxic preparation, temperature/time and sulfide
    sequence; its stock-pH instruction is misplaced at root. The target omits that
    preparation. Liquid/complex/undefined annotations are compatible with the documented
    yeast extract and BD Bacto tryptone; preserve powder/product descriptions without
    invented supplier identity.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1083
  - quantity-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 30 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003735
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: CM003735-summed-stock-formulation
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Undiluted stock strengths and historical salt sums corrupt the formulation
  description: NaCl 39.97, MgSO4·7H2O 33.4965 and CaCl2·2H2O 1.37962 g/L combine main-provider
    concentrations with full stock strengths. Eleven target stock components remain
    direct; only four moved under each owner stock, leaving seven direct and three
    conflated. All 77 local concentration instances and exact stock/source bases are
    assessed.
  target_ids:
  - CultureMech:003735
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1083
  - mediadive1083api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  issue_key: CM003735-broken-relationship-paths
  category: provenance
  severity: blocker
  status: open
  certainty: confirmed
  title: Three stored bacterial relationship paths do not resolve
  description: Target and KOMODO parent paths and the DSMZ child path point to bacterial
    files; the same stable IDs resolve to the captured archaea owners. The actual
    contributors are identifiable, but these exact stored paths remain broken.
  target_ids:
  - CultureMech:003735
  field_paths:
  - parent_media.path
  - variant_children[*].path
  evidence_ids:
  - relationships
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  issue_key: CM003735-resazurin-salt-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin is linked to a structure without sodium
  description: The source explicitly supplies sodium resazurin stock. CHEBI:8806 resolves
    to neutral-form metadataC12H7NO4 and therefore does not encode the specified sodium
    salt.
  target_ids:
  - CultureMech:003735
  field_paths:
  - ingredients[8].term
  evidence_ids:
  - dsmz1083
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  issue_key: CM003735-stage-evidence-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation, source grades and amount evidence need exact stage scope
  description: Neither target nor KOMODO owner retains preparation; the DSMZ owner
    has the stock-pH 1.0 step in the root sequence. Existing amounts lack attached
    evidence, source indicator strength/dose and stock additions need explicit bases,
    and BD Bacto/powder descriptions are dropped. Catalog aerobic=true must remain
    attributed alongside the documented anoxic preparation.
  target_ids:
  - CultureMech:003735
  field_paths:
  - preparation_steps
  - solutions
  - ingredients[*].evidence
  - notes
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1083
  - komodo
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  issue_key: CM003735-mim-key-limits
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: A current secondary key is unmapped and a historical link is unresolved
  description: CHEBI:26833 is a valid live ontology term with no row in the fully
    searched pinned secondary index. MIM000198 remains asserted for sodium selenate
    but its historical correspondence cannot be independently recovered; CHEBI:77775
    existence is not proof of that legacy link.
  target_ids:
  - CultureMech:003735
  field_paths:
  - ingredients[*].mediaingredientmech_chebi_term
  - ingredients[*].mediaingredientmech_term
  evidence_ids:
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-local-search
  - chebi26833
  - chebi77775
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  issue_key: CM003735-history-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO provenance timestamps are malformed or timezone-naive
  description: The target and KOMODO history retain a malformed January timestamp
    and a February timestamp without timezone; later repair and merge dates remain
    separate recorded events.
  target_ids:
  - CultureMech:003735
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  description: Restore the complete 14-salt stock and listed 1 ml batch addition,
    separate historical main/stock sums, retain provider 1001 ml versus source listed-liquid
    limits, and regenerate only after owner review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003735
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  description: Correct exact maintained relationship paths to the verified same-ID
    archaea owners and regenerate affected derived references; verify exact Git path
    spelling.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003735
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  description: Verify an appropriate exact salt identity before changing the maintained
    primary mapping; do not infer a replacement identifier.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003735
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  description: Restore missing preparation and precise stock stages, attach literal
    quantity evidence, preserve source product/powder scope and explain the catalog/preparation
    conflict without inferring growth physiology.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003735
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  description: Preserve the confirmed current mapping gap and unresolved historical
    link separately; verify archival correspondence or explicitly qualify the legacy
    assertion without guessing a replacement.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003735
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
  description: Preserve history and append any supported later clarification without
    inventing a historical timezone.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:003735
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/aciduliprofundum_medium.yaml
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
- Required partial scope is the historical MIM000198 identity correspondence. The
  current CHEBI:26833 index absence is a completed lookup with a confirmed gap. Provider1001ml
  and primary listed 1001.5 ml liquids are preserved separately; neither establishes
  a measured final volume. No other medium 792 formulation or physiology is imported.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-019
- generated-medium
```
