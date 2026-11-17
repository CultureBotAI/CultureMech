# Source and formulation review: alcanivorax_borkumensis_medium (CultureMech:006526)

- Review: 20261021T122447Z-culturemech-006526-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:11:55Z
- Finished UTC: 2026-10-21T12:24:47Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ/KOMODO 809 formulation is identifiable and all eight source amounts agree with the local nominal provider basis. Both maintained owners retain eight matching quantity excerpts, while the generated target loses them. Phosphate heptahydrate has an anhydrous ontology identity, and the legacy nitrate identifier remains historically unresolved. Source water, preparation context and provenance need bounded curation; the unavailable historical identifier check makes this review partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 197; batch 020 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nineteen task batches contain 190 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 193 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006526 | data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml | generated | alcanivorax_borkumensis_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006526 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006526 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/197/strict.tsv |
| validate-terms | passed | True | CultureMech:006526 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006526 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006526 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo809detail | unavailable | False | CultureMech:006526 | The exact KOMODO detail endpoint returned HTTP 403. The catalog identity row and complete official primary/provider are available. This bounded access failure does not establish historical absence or block the formulation comparison. |
| Historical legacy MIM identifier correspondence | unavailable | True | CultureMech:006526 | MediaIngredientMech:000171 remains unresolved after completed bounded current lookups; no authoritative historical correspondence is captured. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006526.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:006526.

8 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 8/8 primary and 7/8 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%; secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006526.

12 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "NaCl",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "23",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 1",
        "exact_source_quote": "NaCl 23.00 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 23,\n                        \"unit\": \"g\",\n                        \"g_l\": 23,\n                        \"mmol_l\": 393.566,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "23",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "23",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[0].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "23",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[0].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 23 g / (1000 mL / 1000 mL per L) = 23 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "MgSO4 x 7 H2O",
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "5.8",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 2",
        "exact_source_quote": "MgSO4 x 7 H2O 5.80 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 5.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.8,\n                        \"mmol_l\": 23.5317,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5.8",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5.8",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[1].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5.8",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[1].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 5.8 g / (1000 mL / 1000 mL per L) = 5.8 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "MgCl2 x 2 H2O",
    "field_path": "ingredients[2].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "6.16",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 3",
        "exact_source_quote": "MgCl2 x 2 H2O 6.16 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 2 H2O\",\n                        \"compound_id\": 651,\n                        \"amount\": 6.16,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.16,\n                        \"mmol_l\": 46.9366,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.16",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.16",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[2].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "6.16",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[2].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 6.16 g / (1000 mL / 1000 mL per L) = 6.16 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "CaCl2 x 2 H2O",
    "field_path": "ingredients[3].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "1.47",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 4",
        "exact_source_quote": "CaCl2 x 2 H2O 1.47 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1.47,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.47,\n                        \"mmol_l\": 9.99898,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.47",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.47",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[3].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.47",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[3].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 1.47 g / (1000 mL / 1000 mL per L) = 1.47 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "Na2HPO4 x 7 H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "0.89",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 5",
        "exact_source_quote": "Na2HPO4 x 7 H2O 0.89 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2HPO4 x 7 H2O\",\n                        \"compound_id\": 753,\n                        \"amount\": 0.89,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.89,\n                        \"mmol_l\": 6.26942,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.89",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.89",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[4].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.89",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[4].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 0.89 g / (1000 mL / 1000 mL per L) = 0.89 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "NaNO3",
    "field_path": "ingredients[5].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 6",
        "exact_source_quote": "NaNO3 5.00 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaNO3\",\n                        \"compound_id\": 187,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 58.827,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[5].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[5].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 5 g / (1000 mL / 1000 mL per L) = 5 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "FeSO4 x 7 H2O",
    "field_path": "ingredients[6].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 7",
        "exact_source_quote": "FeSO4 x 7 H2O 0.03 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.107908,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[6].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[6].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 0.03 g / (1000 mL / 1000 mL per L) = 0.03 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "Sodium pyruvate",
    "field_path": "ingredients[7].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 8",
        "exact_source_quote": "Sodium pyruvate 10.00 g",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Sodium pyruvate\",\n                        \"compound_id\": 438,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 90.876,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "The target value/unit and nominal main-recipe basis agree but lack attached matching evidence. Both owner layers retain correct values and exact matching claim evidence, so only those layers are verified. This decision validates the source mass convention, not ontology form, molarity or an independently measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[7].evidence[0]"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[7].evidence[0]"
      }
    ],
    "arithmetic": "Provider-declared nominal basis: 10 g / (1000 mL / 1000 mL per L) = 10 g/L. Primary water is a listed batch quantity; the provider basis is not a new measured-volume assertion.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "Main source water",
    "field_path": "source.solution_1643.recipe[8]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, main table row 9",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      },
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "All local layers omit the source water quantity. Preserve 1000 mL distilled water as a batch-preparation quantity, separately from the provider nominal volume; do not replace it with a percentage or claim the primary says bring to a final litre.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "pH 7.0 - 7.5"
          }
        ],
        "decision": "add"
      }
    ],
    "arithmetic": "1000 mL water = 1 L water; this dimensional conversion alone does not establish measured final medium volume.",
    "primary_source_evidence_id": "dsmz809"
  },
  {
    "ingredient_or_context": "Provider nominal main volume",
    "field_path": "source.solution_1643.volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive809api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/809",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6"
      }
    ],
    "rationale": "Retain the provider-declared nominal 1000 mL basis with its source version. It is distinct from the primary water amount and does not establish measured final volume.",
    "action_taken": "Review only; no recipe change."
  },
  {
    "ingredient_or_context": "Main pH range",
    "field_path": "ph_range",
    "decision": "evidence_only",
    "local": {
      "min": 7.0,
      "max": 7.5
    },
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, only preparation statement",
        "exact_source_quote": "pH 7.0 - 7.5",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      }
    ],
    "rationale": "All layers retain the exact source pH range but do not attach matching pH evidence. This is preparation context, not an experimentally established growth optimum.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_range",
        "decision": "evidence_only",
        "stored": {
          "min": 7.0,
          "max": 7.5
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "ph_range",
        "decision": "evidence_only",
        "stored": {
          "min": 7.0,
          "max": 7.5
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "ph_range",
        "decision": "evidence_only",
        "stored": {
          "min": 7.0,
          "max": 7.5
        }
      }
    ]
  },
  {
    "ingredient_or_context": "Preparation pH statement",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz809",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf",
        "source_locator": "DSMZ 809 page 1, only preparation statement",
        "exact_source_quote": "pH 7.0 - 7.5",
        "snapshot_sha256": "de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95",
        "parsed_text_sha256": "b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0"
      }
    ],
    "rationale": "The DSMZ owner preserves the complete source preparation statement without attached pH evidence. Target and KOMODO owner omit that statement even though their ph_range retains the endpoints. Preserve source scope without inventing a reagent, dose, sterilization cycle or oxygen condition.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 7.0 - 7.5",
        "decision": "evidence_only"
      }
    ]
  }
]

### Exact accession and reciprocal maintained owners

identity: supported. Targets: CultureMech:006526.

The exact primary, provider and catalog mapping identify DSMZ 809. Both maintained owners share the eight source ingredient names, concentrations and term objects; reciprocal SOURCE_DUPLICATE paths and IDs resolve correctly. The generated record names both actual contributors. Matching formulation signatures do not imply equal evidence, references, preparation or curation history.

### All source quantities on their declared basis

consistency: supported. Targets: CultureMech:006526.

All eight mass values match the primary table and provider nominal 1000 mL main-recipe basis: 23, 5.8, 6.16, 1.47, 0.89, 5, 0.03 and 10 g. The source also lists 1000 mL water and pH 7.0–7.5. There are no asserted stocks, stock doses or recipe variants to invent. Sixteen owner quantity decisions are verified because matching evidence is already attached there; all eight target concentration decisions are evidence_only.

### Explicit hydrate identity versus nominal mass support

grounding: concern. Targets: CultureMech:006526.

Primary and API both explicitly say MgCl2 x 2 H2O; CHEBI:131394 is the matching dihydrate and must not be silently changed to a customary hexahydrate. In contrast, source Na2HPO4 x 7 H2O is mapped in every layer to CHEBI:34683, whose formula HO4P.2Na, structure and mass 141.958 omit seven waters. Other asserted salt forms and sodium pyruvate agree with their captured metadata. The provider phosphate mmol_l is not used to validate the supplied hydrate, and verified source mass evidence does not validate secondary ontology mapping.

### Current linkage coverage and unresolved legacy nitrate key

grounding: concern. Targets: CultureMech:006526.

Each layer has eight primary CHEBI links and seven current secondary CHEBI links: 8/8 (100%) primary and 7/8 (87.5%) current secondary coverage. The eighth secondary assertion is legacy MediaIngredientMech:000171 for nitrate. Completed exact current index/catalog/tree searches do not resolve that historical key. Current CHEBI:63005 correctly identifies sodium nitrate; the unresolved legacy identity is a separate assertion, not proof that sodium nitrate or its source amount is wrong.

### Water and pH scope, with source limits

completeness: concern. Targets: CultureMech:006526.

The complete primary supplies only the listed water quantity and pH range, not a sterilization temperature/duration, pressure, gas mixture, incubation temperature or growth experiment. The DSMZ owner preserves the pH statement; target/KOMODO owner keep ph_range but omit the explicit step, and all layers omit water. These are bounded source omissions; an unspecified standard protocol must not be substituted.

### Defined liquid formulation and bounded biological claims

scope: supported. Targets: CultureMech:006526.

DEFINED/DEFINED and LIQUID are consistent with the named salts and sodium pyruvate. No target organism, taxon/strain identifier, assembly, DOI/PMID, paper-derived variant or explicit experimental growth result is asserted. The species name in the title and generic cultivation application do not independently demonstrate growth. Aerobic: No is attributable to KOMODO Is Aerobic=false; the primary itself makes no oxygen-condition claim.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006526.

24 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained evidence and source-transform correspondence

provenance: concern. Targets: CultureMech:006526.

Current import/resolver/merge excerpts are identical to the fully read 195 context and rechecked against fresh input hashes. They describe current behavior, not a replay of the older imports. Both owners have later October claim-evidence curation, while the generated target retains August merge events and lacks those attachments and references. Preserve the sixteen owner amount snippets and one separate catalog identity snippet, their limits and historical timestamps during authorized regeneration; do not infer a new recipe identity or erase owner-specific preparation.

## Findings

### f1: Phosphate heptahydrate is grounded to an anhydrous term

major / open / confirmed; issue key: culturemech.006526.phosphate-hydrate.

Every layer explicitly names Na2HPO4 x 7 H2O but assigns CHEBI:34683 to both primary and current secondary terms. Its formula and structure omit the seven waters, so exact-label checks and correctly sourced 0.89 g nominal mass evidence do not validate this supplied-form identity.

### f2: Legacy nitrate linkage lacks an available historical identity correspondence

major / open / confirmed; issue key: culturemech.006526.legacy-nitrate.

MediaIngredientMech:000171 remains asserted in all layers but is absent from the checked current exact-key index and captured pinned catalog/tree. Repeated local use does not authenticate the historical numeric identity. The required historical check remains unavailable; current sodium nitrate CHEBI:63005 is separately supported.

### f3: Generated output omits maintained claim evidence and references

minor / open / confirmed; issue key: culturemech.006526.generated-evidence-loss.

Both owners retain eight exact matching quantity snippets; the KOMODO owner additionally retains a bounded identity snippet and catalog reference. The generated target lacks these later attachments and references, despite naming both contributors. This is traceability loss, not evidence that the supported numeric values are wrong.

### f4: Source water and preparation context are incomplete, with inherited timestamp defects

minor / open / confirmed; issue key: culturemech.006526.source-context-history.

All layers omit 1000 mL distilled water. Only the DSMZ owner retains the explicit pH preparation statement, although all ph_range values agree. Target/KOMODO owner each contain a malformed import timestamp and timezone-naive resolver timestamp; four inherited instances require clarification rather than silent replacement.

## Recommended Actions And Acceptance Checks

### a1

Verify an exact heptahydrate identifier and correct primary/secondary grounding in both maintained owners without changing the supported 0.89 g source amount or using the anhydrous provider molarity as hydrate evidence. Keep a replacement unresolved until independently supported.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the historical legacy identity from an authoritative mapping before retaining, replacing or removing that secondary assertion. Preserve the supported primary sodium nitrate identity and amount; do not infer a numeric-key replacement from name similarity.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the validated owner claim excerpts, their nominal-volume and ontology limits, and separate identity evidence when regeneration is authorized. Retain original source hashes/access metadata and preserve the chronology of later owner curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Represent source water and pH at their proper preparation scope with attached evidence, preserving any existing owner step. Keep catalog oxygen metadata attributed and do not invent a sterilization cycle or measured final volume. Preserve old history and append a dated clarification only when authorized.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch020/197/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/197/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml:1:id: CultureMech:006526<br>./data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml:1:id: CultureMech:006526<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/197/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 14 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| fresh-context-binding | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/197/source-context-current.json; Fresh bound input manifest and explicit old-to-new context transition | context_only | The original preflight evidence context retains its 24a1 provenance. Current native inputs use fresh 033ef569; the two reviewed schema/justfile changes are explicitly bound. Source recipe bytes, captures, timestamps and writer excerpts remain unchanged. |
| dsmz809 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf; Entire official single-page recipe, including all nine table rows and pH; page visually inspected | supports | The source explicitly gives magnesium chloride dihydrate and phosphate heptahydrate. Its entire preparation statement is pH 7.0–7.5; it supplies no sterilization cycle, gas composition, strain-specific growth evidence or measured final volume. |
| mediadive809 | https://mediadive.dsmz.de/rest/medium/809; $.data.medium and complete $.data.solutions[0], recipe, volume and steps | supports | Exact source 809 and main solution 1643 preserve all source masses, water and pH. The provider declares a nominal 1000 mL volume and corresponding g_l values; those are distinguished from measured final volume and from its derived mmol_l values. |
| komodo-list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact row 809 and column headers | supports | KOMODO accession 809 points to the exact DSMZ 809 primary. Its Is Aerobic=false flag is catalog metadata, not a validated oxygen phenotype or instruction to impose an anaerobic culture protocol. |
| komodo809detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=809; Preserved exact public retrieval result | context_only | The exact KOMODO detail endpoint returned HTTP 403. The catalog identity row and complete official primary/provider are available. This bounded access failure does not establish historical absence or block the formulation comparison. |
| chebi131394 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131394; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131394 resolves to magnesium dichloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63005 resolves to sodium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131394": [{"label": "MgCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131394", "preferred_term": "MgCl2 x 2 H2O", "ontology_id": "CHEBI:131394", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| mim-public-catalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned public catalog; exact legacy identifier lookup | supports | The current public catalog was inspected for the exact legacy identity; current chemical labels do not authenticate a historical numeric key. |
| mim-public-tree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete untruncated pinned Git tree; exact numeric filename token | supports | The bounded public tree was checked without inferring deletion or universal absence. |
| legacy-lookup | /private/tmp/culturemech-review-work-batch020/197/legacy-identity-context.json; Exact current packaged-index, pinned public catalog/tree and ignored-inclusive local references | context_only | MediaIngredientMech:000171: 0 current exact-key index rows, 0 catalog matches and 0 tree filename matches. Local repeated assertions are not historical identity authority. |
| attached-evidence-recheck | /private/tmp/culturemech-review-work-batch020/197/attached-evidence-recheck.json; All sixteen ingredient evidence objects and one KOMODO identity object, including complete explanations and references | supports | All sixteen quantity snippets and one identity snippet match their exact captured source bytes and quoted hashes. Quantity support applies only to the two maintained owner layers; the generated target has none. Historical date assertions are retained as provenance. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch020/197/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| writer-context-3 | src/culturemech/enrich/dsmz_resolver.py; _build_dsmz_index lines 43–76; merge_composition lines 112–166; _add_enrichment_metadata lines 195–212 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:06.804145"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:06.804145"}]}, {"input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml", "events": 7, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact KOMODO detail endpoint returned HTTP 403. The catalog identity row and complete official primary/provider are available. This bounded access failure does not establish historical absence or block the formulation comparison.
- Required historical correspondence for MediaIngredientMech:000171 remains unavailable. The completed current lookup does not prove that the old identifier never existed or that the valid current primary CHEBI identity is wrong.
- Source mass agreement and the sixteen verified owner evidence attachments do not validate phosphate hydration grounding, nitrate historical identity, provider-derived molarity, or independently measured final volume.
- Only the exact source recipe and its asserted local fields were assessed; no universal species growth claim, replacement hydrate identifier, or standard preparation protocol was inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122447Z-culturemech-006526-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alcanivorax_borkumensis_medium (CultureMech:006526)'
started_at: '2026-10-21T12:11:55Z'
finished_at: '2026-10-21T12:24:47Z'
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
summary: The exact DSMZ/KOMODO 809 formulation is identifiable and all eight source
  amounts agree with the local nominal provider basis. Both maintained owners retain
  eight matching quantity excerpts, while the generated target loses them. Phosphate
  heptahydrate has an anhydrous ontology identity, and the legacy nitrate identifier
  remains historically unresolved. Source water, preparation context and provenance
  need bounded curation; the unavailable historical identifier check makes this review
  partial.
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
  - path: data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    sha256: 21084c1b9ec2d13460ae7db5dbc86204a2171b527558a6849e4a0d3c739b7936
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    sha256: cebbf99afafedcdfba5d7eb9cb7fb1978e97e7ad592c2d341a33ddf33e6b4323
    role: context
  - path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
    sha256: c58378b738e3ca58cfa055bdc0c6403169b5f0b0d2f7fb787383959b684717d5
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
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
    sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 197; batch 020 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nineteen task batches
    contain 190 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 193 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006526
targets:
- target_id: CultureMech:006526
  path: data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  label: alcanivorax_borkumensis_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch020/197/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/197/strict.tsv"
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006526
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
  - CultureMech:006526
- check_id: komodo809detail-source-access
  name: 'Exact source content access: komodo809detail'
  required: false
  status: unavailable
  summary: The exact KOMODO detail endpoint returned HTTP 403. The catalog identity
    row and complete official primary/provider are available. This bounded access
    failure does not establish historical absence or block the formulation comparison.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - komodo809detail-attempt
- check_id: legacy-historical-identity
  name: Historical legacy MIM identifier correspondence
  required: true
  status: unavailable
  summary: MediaIngredientMech:000171 remains unresolved after completed bounded current
    lookups; no authoritative historical correspondence is captured.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - legacy-lookup
  - mim-public-catalog
  - mim-public-tree
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:05.610883Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch020/197/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:07.064327Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/197/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:08.753212Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:13:09.820922Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:24:43Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml:1:id:
    CultureMech:006526

    ./data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml:1:id: CultureMech:006526

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/197/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:24:43Z'
  support: supports
  summary: 14 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 40a9544b7a3843adba87500891a35e61efc16df82712d0f42170b42691fb42a3
- evidence_id: fresh-context-binding
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/197/source-context-current.json
  locator: Fresh bound input manifest and explicit old-to-new context transition
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: The original preflight evidence context retains its 24a1 provenance. Current
    native inputs use fresh 033ef569; the two reviewed schema/justfile changes are
    explicitly bound. Source recipe bytes, captures, timestamps and writer excerpts
    remain unchanged.
  snapshot_sha256: 545b66f897c2ca2b6d3c75a99ccf8f041a2ef1e7fddeb4c2ed3ce56c4c2d5332
- evidence_id: dsmz809
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf
  locator: Entire official single-page recipe, including all nine table rows and pH;
    page visually inspected
  accessed_at: '2026-10-21T11:58:01.372148Z'
  support: supports
  summary: The source explicitly gives magnesium chloride dihydrate and phosphate
    heptahydrate. Its entire preparation statement is pH 7.0–7.5; it supplies no sterilization
    cycle, gas composition, strain-specific growth evidence or measured final volume.
  snapshot_sha256: de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95
- evidence_id: mediadive809
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/809
  locator: $.data.medium and complete $.data.solutions[0], recipe, volume and steps
  accessed_at: '2026-10-21T11:57:59.803584Z'
  support: supports
  summary: Exact source 809 and main solution 1643 preserve all source masses, water
    and pH. The provider declares a nominal 1000 mL volume and corresponding g_l values;
    those are distinguished from measured final volume and from its derived mmol_l
    values.
  snapshot_sha256: a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6
- evidence_id: komodo-list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact row 809 and column headers
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO accession 809 points to the exact DSMZ 809 primary. Its Is Aerobic=false
    flag is catalog metadata, not a validated oxygen phenotype or instruction to impose
    an anaerobic culture protocol.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo809detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=809
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:57:59.144950Z'
  support: context_only
  summary: The exact KOMODO detail endpoint returned HTTP 403. The catalog identity
    row and complete official primary/provider are available. This bounded access
    failure does not establish historical absence or block the formulation comparison.
  snapshot_sha256: 4c71fbe105974d728e94dd02c1948adb2fd82d5fc8febcab50c9ed39b3c9917e
- evidence_id: chebi131394
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131394
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:58:01.968545Z'
  support: supports
  summary: CHEBI:131394 resolves to magnesium dichloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f36ea2111de28766305d47add3033b580cd7091e3c0a0e7df4ab7299fc2ecaa5
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
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi63005
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T04:02:36.443517Z'
  support: supports
  summary: CHEBI:63005 resolves to sodium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1ec6a815a0e22ba0d12f84ad998bef39b9e6b80cf90c25cd1ab51903bbb54da3
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:24:43Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131394":
    [{"label": "MgCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131394",
    "preferred_term": "MgCl2 x 2 H2O", "ontology_id": "CHEBI:131394", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label":
    "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term":
    "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term",
    "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label":
    "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-public-catalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned public catalog; exact legacy identifier lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: The current public catalog was inspected for the exact legacy identity;
    current chemical labels do not authenticate a historical numeric key.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mim-public-tree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete untruncated pinned Git tree; exact numeric filename token
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: The bounded public tree was checked without inferring deletion or universal
    absence.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-lookup
  kind: search
  reference: /private/tmp/culturemech-review-work-batch020/197/legacy-identity-context.json
  locator: Exact current packaged-index, pinned public catalog/tree and ignored-inclusive
    local references
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: 'MediaIngredientMech:000171: 0 current exact-key index rows, 0 catalog
    matches and 0 tree filename matches. Local repeated assertions are not historical
    identity authority.'
  snapshot_sha256: eff6187e2252f4453530063bab6e99ce156338085f4e2c58224cab1a428fb31f
  search_scope: Whole current pinned label index, whole captured public catalog and
    untruncated tree; fresh local data/normalized_yaml and src/culturemech/data/mediaingredientmech
    searched with rg --no-ignore --hidden. No unbounded historical/remote absence
    claim.
- evidence_id: attached-evidence-recheck
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/197/attached-evidence-recheck.json
  locator: All sixteen ingredient evidence objects and one KOMODO identity object,
    including complete explanations and references
  accessed_at: '2026-10-21T12:24:43Z'
  support: supports
  summary: All sixteen quantity snippets and one identity snippet match their exact
    captured source bytes and quoted hashes. Quantity support applies only to the
    two maintained owner layers; the generated target has none. Historical date assertions
    are retained as provenance.
  snapshot_sha256: 9c734ad6e4db7b4a8bfc142fbe827d378a88d8ec845f739d4faa5e1dc18400be
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/197/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 0f6624ae8b026e01b626b89a01a3fd490245129f1575b19a743eede8a47cf6ab
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-context-3
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: _build_dsmz_index lines 43–76; merge_composition lines 112–166; _add_enrichment_metadata
    lines 195–212
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml;
    data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:24:43Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:06.804145"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:06.804145"}]}, {"input": "data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '8 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 8/8 primary and 7/8 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131394
  - chebi26710
  - chebi31795
  - chebi34683
  - chebi50144
  - chebi63005
  - chebi75836
  - chebi86158
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%;
    secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 12 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"NaCl\",\n    \"field_path\":\
    \ \"ingredients[0].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"23\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz809\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 1\",\n      \
    \  \"exact_source_quote\": \"NaCl 23.00 g\",\n        \"snapshot_sha256\": \"\
    de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n        \"\
    parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 23,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 23,\\n                 \
    \       \\\"mmol_l\\\": 393.566,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\
    \n      }\n    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe\
    \ basis agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"23\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"23\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[0].evidence[0]\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"23\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[0].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"Provider-declared nominal basis: 23 g\
    \ / (1000 mL / 1000 mL per L) = 23 g/L. Primary water is a listed batch quantity;\
    \ the provider basis is not a new measured-volume assertion.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz809\"\n  },\n  {\n    \"ingredient_or_context\": \"MgSO4 x 7 H2O\",\n\
    \    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"value\": \"5.8\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz809\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 2\",\n      \
    \  \"exact_source_quote\": \"MgSO4 x 7 H2O 5.80 g\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 5.8,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5.8,\\n  \
    \                      \\\"mmol_l\\\": 23.5317,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\
    \n      }\n    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe\
    \ basis agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5.8\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[1].evidence[0]\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[1].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"Provider-declared nominal basis: 5.8\
    \ g / (1000 mL / 1000 mL per L) = 5.8 g/L. Primary water is a listed batch quantity;\
    \ the provider basis is not a new measured-volume assertion.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz809\"\n  },\n  {\n    \"ingredient_or_context\": \"MgCl2 x 2 H2O\",\n\
    \    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"value\": \"6.16\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz809\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 3\",\n      \
    \  \"exact_source_quote\": \"MgCl2 x 2 H2O 6.16 g\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 651,\\n                        \\\"amount\\\": 6.16,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 6.16,\\\
    n                        \\\"mmol_l\\\": 46.9366,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\n      }\n\
    \    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe basis\
    \ agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"6.16\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[2].evidence[0]\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[2].evidence[0]\"\n      }\n    ],\n    \"arithmetic\": \"Provider-declared\
    \ nominal basis: 6.16 g / (1000 mL / 1000 mL per L) = 6.16 g/L. Primary water\
    \ is a listed batch quantity; the provider basis is not a new measured-volume\
    \ assertion.\",\n    \"primary_source_evidence_id\": \"dsmz809\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"CaCl2 x 2 H2O\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"\
    1.47\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz809\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 4\",\n      \
    \  \"exact_source_quote\": \"CaCl2 x 2 H2O 1.47 g\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 1.47,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.47,\\n\
    \                        \\\"mmol_l\\\": 9.99898,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\n      }\n\
    \    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe basis\
    \ agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.47\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.47\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[3].evidence[0]\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.47\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[3].evidence[0]\"\n      }\n    ],\n    \"arithmetic\": \"Provider-declared\
    \ nominal basis: 1.47 g / (1000 mL / 1000 mL per L) = 1.47 g/L. Primary water\
    \ is a listed batch quantity; the provider basis is not a new measured-volume\
    \ assertion.\",\n    \"primary_source_evidence_id\": \"dsmz809\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Na2HPO4 x 7 H2O\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"\
    0.89\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"dsmz809\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 5\",\n      \
    \  \"exact_source_quote\": \"Na2HPO4 x 7 H2O 0.89 g\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 753,\\n                        \\\"amount\\\": 0.89,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.89,\\\
    n                        \\\"mmol_l\\\": 6.26942,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\n      }\n\
    \    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe basis\
    \ agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.89\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.89\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[4].evidence[0]\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.89\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[4].evidence[0]\"\n      }\n    ],\n    \"arithmetic\": \"Provider-declared\
    \ nominal basis: 0.89 g / (1000 mL / 1000 mL per L) = 0.89 g/L. Primary water\
    \ is a listed batch quantity; the provider basis is not a new measured-volume\
    \ assertion.\",\n    \"primary_source_evidence_id\": \"dsmz809\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"NaNO3\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"\
    5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz809\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 6\",\n      \
    \  \"exact_source_quote\": \"NaNO3 5.00 g\",\n        \"snapshot_sha256\": \"\
    de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n        \"\
    parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NaNO3\\\",\\n                        \\\"compound_id\\\": 187,\\\
    n                        \\\"amount\\\": 5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n                  \
    \      \\\"mmol_l\\\": 58.827,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\
    \n      }\n    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe\
    \ basis agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[5].evidence[0]\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[5].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"Provider-declared nominal basis: 5 g\
    \ / (1000 mL / 1000 mL per L) = 5 g/L. Primary water is a listed batch quantity;\
    \ the provider basis is not a new measured-volume assertion.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz809\"\n  },\n  {\n    \"ingredient_or_context\": \"FeSO4 x 7 H2O\",\n\
    \    \"field_path\": \"ingredients[6].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"value\": \"0.03\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz809\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 7\",\n      \
    \  \"exact_source_quote\": \"FeSO4 x 7 H2O 0.03 g\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 0.03,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.03,\\\
    n                        \\\"mmol_l\\\": 0.107908,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\n      }\n\
    \    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe basis\
    \ agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[6].evidence[0]\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[6].evidence[0]\"\n      }\n    ],\n    \"arithmetic\": \"Provider-declared\
    \ nominal basis: 0.03 g / (1000 mL / 1000 mL per L) = 0.03 g/L. Primary water\
    \ is a listed batch quantity; the provider basis is not a new measured-volume\
    \ assertion.\",\n    \"primary_source_evidence_id\": \"dsmz809\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Sodium pyruvate\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": {\n      \"value\": \"\
    10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz809\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 8\",\n      \
    \  \"exact_source_quote\": \"Sodium pyruvate 10.00 g\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Sodium pyruvate\\\",\\n                        \\\"compound_id\\\
    \": 438,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n  \
    \                      \\\"mmol_l\\\": 90.876,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\
    \n      }\n    ],\n    \"rationale\": \"The target value/unit and nominal main-recipe\
    \ basis agree but lack attached matching evidence. Both owner layers retain correct\
    \ values and exact matching claim evidence, so only those layers are verified.\
    \ This decision validates the source mass convention, not ontology form, molarity\
    \ or an independently measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[7].evidence[0]\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[7].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"Provider-declared nominal basis: 10 g\
    \ / (1000 mL / 1000 mL per L) = 10 g/L. Primary water is a listed batch quantity;\
    \ the provider basis is not a new measured-volume assertion.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz809\"\n  },\n  {\n    \"ingredient_or_context\": \"Main source water\"\
    ,\n    \"field_path\": \"source.solution_1643.recipe[8]\",\n    \"decision\":\
    \ \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz809\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, main table row 9\",\n      \
    \  \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive809api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/809\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\
    \n      }\n    ],\n    \"rationale\": \"All local layers omit the source water\
    \ quantity. Preserve 1000 mL distilled water as a batch-preparation quantity,\
    \ separately from the provider nominal volume; do not replace it with a percentage\
    \ or claim the primary says bring to a final litre.\",\n    \"action_taken\":\
    \ \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"pH 7.0 - 7.5\"\n          }\n        ],\n    \
    \    \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"1000 mL water\
    \ = 1 L water; this dimensional conversion alone does not establish measured final\
    \ medium volume.\",\n    \"primary_source_evidence_id\": \"dsmz809\"\n  },\n \
    \ {\n    \"ingredient_or_context\": \"Provider nominal main volume\",\n    \"\
    field_path\": \"source.solution_1643.volume\",\n    \"decision\": \"add\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive809api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/809\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"a0d5ae371403f0fce8751c7b5d1efa6de9d6d70122df5f85deff1c8b4dd371d6\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the provider-declared nominal 1000\
    \ mL basis with its source version. It is distinct from the primary water amount\
    \ and does not establish measured final volume.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\"\n  },\n  {\n    \"ingredient_or_context\": \"Main\
    \ pH range\",\n    \"field_path\": \"ph_range\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": {\n      \"min\": 7.0,\n      \"max\": 7.5\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz809\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\",\n        \"\
    source_locator\": \"DSMZ 809 page 1, only preparation statement\",\n        \"\
    exact_source_quote\": \"pH 7.0 - 7.5\",\n        \"snapshot_sha256\": \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\"\
    ,\n        \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      }\n    ],\n    \"rationale\": \"All layers retain the exact source pH\
    \ range but do not attach matching pH evidence. This is preparation context, not\
    \ an experimentally established growth optimum.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ph_range\",\n        \"decision\"\
    : \"evidence_only\",\n        \"stored\": {\n          \"min\": 7.0,\n       \
    \   \"max\": 7.5\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"stored\": {\n          \"min\": 7.0,\n          \"max\": 7.5\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"stored\": {\n          \"min\": 7.0,\n          \"max\": 7.5\n  \
    \      }\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Preparation\
    \ pH statement\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz809\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium809.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 809 page 1, only preparation statement\"\
    ,\n        \"exact_source_quote\": \"pH 7.0 - 7.5\",\n        \"snapshot_sha256\"\
    : \"de2f94b9dba9b0b36f7cdcc10487b477fc3913c3a2731106ea5199294e7fcf95\",\n    \
    \    \"parsed_text_sha256\": \"b3c47852269d357412c3bab81abfae540e8d726846426444e08d5eb6bd1791d0\"\
    \n      }\n    ],\n    \"rationale\": \"The DSMZ owner preserves the complete\
    \ source preparation statement without attached pH evidence. Target and KOMODO\
    \ owner omit that statement even though their ph_range retains the endpoints.\
    \ Preserve source scope without inventing a reagent, dose, sterilization cycle\
    \ or oxygen condition.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"pH 7.0 - 7.5\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n\
    \  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact accession and reciprocal maintained owners
  outcome: supported
  summary: The exact primary, provider and catalog mapping identify DSMZ 809. Both
    maintained owners share the eight source ingredient names, concentrations and
    term objects; reciprocal SOURCE_DUPLICATE paths and IDs resolve correctly. The
    generated record names both actual contributors. Matching formulation signatures
    do not imply equal evidence, references, preparation or curation history.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz809
  - mediadive809
  - komodo-list
  - attached-evidence-recheck
- assessment_id: source-stage-consistency
  area: consistency
  topic: All source quantities on their declared basis
  outcome: supported
  summary: 'All eight mass values match the primary table and provider nominal 1000
    mL main-recipe basis: 23, 5.8, 6.16, 1.47, 0.89, 5, 0.03 and 10 g. The source
    also lists 1000 mL water and pH 7.0–7.5. There are no asserted stocks, stock doses
    or recipe variants to invent. Sixteen owner quantity decisions are verified because
    matching evidence is already attached there; all eight target concentration decisions
    are evidence_only.'
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - dsmz809
  - mediadive809
  - quantity-inventory
  - attached-evidence-recheck
- assessment_id: forms
  area: grounding
  topic: Explicit hydrate identity versus nominal mass support
  outcome: concern
  summary: Primary and API both explicitly say MgCl2 x 2 H2O; CHEBI:131394 is the
    matching dihydrate and must not be silently changed to a customary hexahydrate.
    In contrast, source Na2HPO4 x 7 H2O is mapped in every layer to CHEBI:34683, whose
    formula HO4P.2Na, structure and mass 141.958 omit seven waters. Other asserted
    salt forms and sodium pyruvate agree with their captured metadata. The provider
    phosphate mmol_l is not used to validate the supplied hydrate, and verified source
    mass evidence does not validate secondary ontology mapping.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz809
  - mediadive809
  - chebi131394
  - chebi34683
  - quantity-inventory
- assessment_id: legacy-identity
  area: grounding
  topic: Current linkage coverage and unresolved legacy nitrate key
  outcome: concern
  summary: 'Each layer has eight primary CHEBI links and seven current secondary CHEBI
    links: 8/8 (100%) primary and 7/8 (87.5%) current secondary coverage. The eighth
    secondary assertion is legacy MediaIngredientMech:000171 for nitrate. Completed
    exact current index/catalog/tree searches do not resolve that historical key.
    Current CHEBI:63005 correctly identifies sodium nitrate; the unresolved legacy
    identity is a separate assertion, not proof that sodium nitrate or its source
    amount is wrong.'
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - mim
  - legacy-lookup
  - mim-public-catalog
  - mim-public-tree
  - chebi63005
- assessment_id: preparation
  area: completeness
  topic: Water and pH scope, with source limits
  outcome: concern
  summary: The complete primary supplies only the listed water quantity and pH range,
    not a sterilization temperature/duration, pressure, gas mixture, incubation temperature
    or growth experiment. The DSMZ owner preserves the pH statement; target/KOMODO
    owner keep ph_range but omit the explicit step, and all layers omit water. These
    are bounded source omissions; an unspecified standard protocol must not be substituted.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz809
  - mediadive809
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Defined liquid formulation and bounded biological claims
  outcome: supported
  summary: 'DEFINED/DEFINED and LIQUID are consistent with the named salts and sodium
    pyruvate. No target organism, taxon/strain identifier, assembly, DOI/PMID, paper-derived
    variant or explicit experimental growth result is asserted. The species name in
    the title and generic cultivation application do not independently demonstrate
    growth. Aerobic: No is attributable to KOMODO Is Aerobic=false; the primary itself
    makes no oxygen-condition claim.'
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz809
  - komodo-list
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 24 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: generation
  area: provenance
  topic: Maintained evidence and source-transform correspondence
  outcome: concern
  summary: Current import/resolver/merge excerpts are identical to the fully read
    195 context and rechecked against fresh input hashes. They describe current behavior,
    not a replay of the older imports. Both owners have later October claim-evidence
    curation, while the generated target retains August merge events and lacks those
    attachments and references. Preserve the sixteen owner amount snippets and one
    separate catalog identity snippet, their limits and historical timestamps during
    authorized regeneration; do not infer a new recipe identity or erase owner-specific
    preparation.
  target_ids:
  - CultureMech:006526
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - attached-evidence-recheck
  - history-metadata
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - writer-context-3
findings:
- finding_id: f1
  issue_key: culturemech.006526.phosphate-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Phosphate heptahydrate is grounded to an anhydrous term
  description: Every layer explicitly names Na2HPO4 x 7 H2O but assigns CHEBI:34683
    to both primary and current secondary terms. Its formula and structure omit the
    seven waters, so exact-label checks and correctly sourced 0.89 g nominal mass
    evidence do not validate this supplied-form identity.
  target_ids:
  - CultureMech:006526
  field_paths:
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz809
  - mediadive809
  - chebi34683
  - attached-evidence-recheck
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
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
  issue_key: culturemech.006526.legacy-nitrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Legacy nitrate linkage lacks an available historical identity correspondence
  description: MediaIngredientMech:000171 remains asserted in all layers but is absent
    from the checked current exact-key index and captured pinned catalog/tree. Repeated
    local use does not authenticate the historical numeric identity. The required
    historical check remains unavailable; current sodium nitrate CHEBI:63005 is separately
    supported.
  target_ids:
  - CultureMech:006526
  field_paths:
  - ingredients[5].mediaingredientmech_term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - legacy-lookup
  - mim-public-catalog
  - mim-public-tree
  - chebi63005
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
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
  issue_key: culturemech.006526.generated-evidence-loss
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated output omits maintained claim evidence and references
  description: Both owners retain eight exact matching quantity snippets; the KOMODO
    owner additionally retains a bounded identity snippet and catalog reference. The
    generated target lacks these later attachments and references, despite naming
    both contributors. This is traceability loss, not evidence that the supported
    numeric values are wrong.
  target_ids:
  - CultureMech:006526
  field_paths:
  - ingredients
  - evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - attached-evidence-recheck
  - mediadive809
  - komodo-list
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.006526.source-context-history
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Source water and preparation context are incomplete, with inherited timestamp
    defects
  description: All layers omit 1000 mL distilled water. Only the DSMZ owner retains
    the explicit pH preparation statement, although all ph_range values agree. Target/KOMODO
    owner each contain a malformed import timestamp and timezone-naive resolver timestamp;
    four inherited instances require clarification rather than silent replacement.
  target_ids:
  - CultureMech:006526
  field_paths:
  - preparation_steps
  - ph_range
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz809
  - quantity-inventory
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Verify an exact heptahydrate identifier and correct primary/secondary
    grounding in both maintained owners without changing the supported 0.89 g source
    amount or using the anhydrous provider molarity as hydrate evidence. Keep a replacement
    unresolved until independently supported.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006526
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
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
  description: Resolve the historical legacy identity from an authoritative mapping
    before retaining, replacing or removing that secondary assertion. Preserve the
    supported primary sodium nitrate identity and amount; do not infer a numeric-key
    replacement from name similarity.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006526
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
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
  description: Preserve the validated owner claim excerpts, their nominal-volume and
    ontology limits, and separate identity evidence when regeneration is authorized.
    Retain original source hashes/access metadata and preserve the chronology of later
    owner curation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006526
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
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
  description: Represent source water and pH at their proper preparation scope with
    attached evidence, preserving any existing owner step. Keep catalog oxygen metadata
    attributed and do not invent a sterilization cycle or measured final volume. Preserve
    old history and append a dated clarification only when authorized.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006526
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml
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
- The exact KOMODO detail endpoint returned HTTP 403. The catalog identity row and
  complete official primary/provider are available. This bounded access failure does
  not establish historical absence or block the formulation comparison.
- Required historical correspondence for MediaIngredientMech:000171 remains unavailable.
  The completed current lookup does not prove that the old identifier never existed
  or that the valid current primary CHEBI identity is wrong.
- Source mass agreement and the sixteen verified owner evidence attachments do not
  validate phosphate hydration grounding, nitrate historical identity, provider-derived
  molarity, or independently measured final volume.
- Only the exact source recipe and its asserted local fields were assessed; no universal
  species growth claim, replacement hydrate identifier, or standard preparation protocol
  was inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-020
- generated-medium
```
