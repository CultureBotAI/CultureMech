# Source and formulation review: activated_carbon_medium (CultureMech:001956)

- Review: 20261021T115041Z-culturemech-001956-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:43:22Z
- Finished UTC: 2026-10-21T11:50:41Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 811 identity and preparation resolve, but both local layers flatten eight TS2 stock strengths into the medium and encode 1000 ml water as 1000 g/L. Two explicitly hydrated salts have anhydrous ontology structures, amount evidence is absent, and the fully defined classification overstates the supplied mixture composition.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 184; batch 019 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eighteen task batches contain 180 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 182 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001956 | data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml | generated | activated_carbon_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001956 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001956 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/184/strict.tsv |
| validate-terms | passed | True | CultureMech:001956 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001956 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001956 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001956.

The four documented recipes completed; interpret the scope of each separately.

### Exact single-owner source identity

identity: supported. Targets: CultureMech:001956.

The target and sole normalized owner share CultureMech:001956, identify DSMZ 811 and match the primary title and provider accession. The explicit merge provenance has one contributor; no sibling formulation, strain, or taxonomic growth assertion is substituted.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001956.

42 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[0].concentration",
    "ingredient": "Na2HPO4 x 12 H2O",
    "stored": {
      "value": "9",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "9",
      "unit": "G_PER_L",
      "original_amount": 9,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Na2HPO4 x 12 H2O",
        "exact_source_quote": "Na2HPO4 x 12 H2O 9.0 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\": 95,\n                        \"amount\": 9,\n                        \"unit\": \"g\",\n                        \"g_l\": 9,\n                        \"mmol_l\": 63.3986,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KH2PO4",
    "stored": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.5",
      "unit": "G_PER_L",
      "original_amount": 1.5,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: KH2PO4",
        "exact_source_quote": "KH2PO4 1.5 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[2].concentration",
    "ingredient": "NH4Cl",
    "stored": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.5",
      "unit": "G_PER_L",
      "original_amount": 1.5,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: NH4Cl",
        "exact_source_quote": "NH4Cl 1.5 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 28.0426,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[3].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "stored": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.2",
      "unit": "G_PER_L",
      "original_amount": 0.2,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 0.2 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[4].concentration",
    "ingredient": "CaCl2 x 2 H2O",
    "stored": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.02",
      "unit": "G_PER_L",
      "original_amount": 20,
      "original_unit": "mg",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 20.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.136041,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Fe(NH4)citrate",
    "stored": {
      "value": "0.0012",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0012",
      "unit": "G_PER_L",
      "original_amount": 1.2,
      "original_unit": "mg",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Fe(NH4)citrate",
        "exact_source_quote": "NH4-Fe-III-Citrat 1.2 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Fe(NH4)citrate\",\n                        \"compound_id\": 1203,\n                        \"amount\": 1.2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0012,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Activated carbon",
    "stored": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "5",
      "unit": "G_PER_L",
      "original_amount": 5,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Activated carbon",
        "exact_source_quote": "Activated carbon 5.0 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Activated carbon\",\n                        \"compound_id\": 757,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ingredients[7].concentration",
    "ingredient": "Agar",
    "stored": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "15",
      "unit": "G_PER_L",
      "original_amount": 15,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Agar",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Double distilled water",
    "stored": {
      "value": "1000",
      "unit": "G_PER_L"
    },
    "proposed": {
      "amount": 1000,
      "unit": "ml",
      "scope": "Main-recipe solvent quantity"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Double distilled water",
        "exact_source_quote": "Bidistillated water 1000.0 ml",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Double distilled water\",\n                        \"compound_id\": 1021,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source and provider specify a liquid volume, but the record asserts mass per litre. Preserve the 1000 ml batch solvent quantity and its grade; no source density or independently measured final volume permits a mass conversion."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[9].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 100,
      "original_unit": "mg",
      "stock_g_per_L": 0.1,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 100.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 100 mg in its listed 1000 ml water and provider 1000 ml stock basis: 100 mg * 0.001 g/mg / 1 L = 0.1 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[10].concentration",
    "ingredient": "MnCl2 x 4 H2O",
    "stored": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 30,
      "original_unit": "mg",
      "stock_g_per_L": 0.03,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl2 x 4 H2O 30.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 30,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 30 mg in its listed 1000 ml water and provider 1000 ml stock basis: 30 mg * 0.001 g/mg / 1 L = 0.03 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[11].concentration",
    "ingredient": "H3BO3",
    "stored": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 300,
      "original_unit": "mg",
      "stock_g_per_L": 0.3,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: H3BO3",
        "exact_source_quote": "H3BO3 300.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 300 mg in its listed 1000 ml water and provider 1000 ml stock basis: 300 mg * 0.001 g/mg / 1 L = 0.3 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[12].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "stored": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 200,
      "original_unit": "mg",
      "stock_g_per_L": 0.2,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl2 x 6 H2O 200.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 200 mg in its listed 1000 ml water and provider 1000 ml stock basis: 200 mg * 0.001 g/mg / 1 L = 0.2 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[13].concentration",
    "ingredient": "CuCl2 x 2 H2O",
    "stored": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 10,
      "original_unit": "mg",
      "stock_g_per_L": 0.01,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: CuCl2 x 2 H2O",
        "exact_source_quote": "CuCl2 x 2 H2O 10.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 10 mg in its listed 1000 ml water and provider 1000 ml stock basis: 10 mg * 0.001 g/mg / 1 L = 0.01 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[14].concentration",
    "ingredient": "NiCl2 x 6 H2O",
    "stored": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 20,
      "original_unit": "mg",
      "stock_g_per_L": 0.02,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: NiCl2 x 6 H2O",
        "exact_source_quote": "NiCl2 x 6 H2O 20.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 20 mg in its listed 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[15].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "stored": {
      "value": "0.9",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 900,
      "original_unit": "mg",
      "stock_g_per_L": 0.9,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 900.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 900,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.9,\n                        \"mmol_l\": 3.71978,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 900 mg in its listed 1000 ml water and provider 1000 ml stock basis: 900 mg * 0.001 g/mg / 1 L = 0.9 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "target",
    "field_path": "ingredients[16].concentration",
    "ingredient": "Na2SeO3",
    "stored": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 20,
      "original_unit": "mg",
      "stock_g_per_L": 0.02,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: Na2SeO3",
        "exact_source_quote": "Na2SeO3 20.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\": 699,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.115648,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 20 mg in its listed 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "solutions",
    "stored": null,
    "ingredient": "TS2 addition",
    "proposed": {
      "amount": 1,
      "unit": "ml",
      "scope": "Main source batch addition"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Trace element solution TS2",
        "exact_source_quote": "Trace element solution TS2 1.0 ml",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution TS2\",\n                        \"solution_id\": 1648,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Restore this missing stage-specific source quantity. TS2 stock water is not a second litre of main-medium solvent."
  },
  {
    "decision": "add",
    "local_input": "target",
    "field_path": "solutions",
    "stored": null,
    "ingredient": "TS2 stock water",
    "proposed": {
      "amount": 1000,
      "unit": "ml",
      "scope": "Stock preparation only"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: Distilled water",
        "exact_source_quote": "Distilled water 1000.0 ml",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Restore this missing stage-specific source quantity. TS2 stock water is not a second litre of main-medium solvent."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "ph_value",
    "stored": 7.5,
    "ingredient": "Target pH",
    "proposed": 7.5,
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 final preparation line",
        "exact_source_quote": "pH 7.5",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      }
    ],
    "explanation": "The target pH and existing second preparation step agree with the source. Attach narrow evidence; do not reinterpret the schema target-pH slot as a measured final pH."
  },
  {
    "decision": "evidence_only",
    "local_input": "target",
    "field_path": "preparation_steps[0].description",
    "stored": "Befor autoclaving add trace element solution to the medium. Dissolve first all ingredients then add activated carbon. Finally autoclave.",
    "ingredient": "Existing order of TS2 addition, dissolution, carbon and sterilization",
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "Befor autoclaving add trace element solution to the medium. Dissolve first all ingredients \nthen add activated carbon. Finally autoclave.",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      }
    ],
    "explanation": "Existing preparation retains the source order; attach its exact scope. The source supplies no numeric sterilization duration or temperature, and none is proposed."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "Na2HPO4 x 12 H2O",
    "stored": {
      "value": "9",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "9",
      "unit": "G_PER_L",
      "original_amount": 9,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Na2HPO4 x 12 H2O",
        "exact_source_quote": "Na2HPO4 x 12 H2O 9.0 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\": 95,\n                        \"amount\": 9,\n                        \"unit\": \"g\",\n                        \"g_l\": 9,\n                        \"mmol_l\": 63.3986,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "KH2PO4",
    "stored": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.5",
      "unit": "G_PER_L",
      "original_amount": 1.5,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: KH2PO4",
        "exact_source_quote": "KH2PO4 1.5 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 11.0225,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "NH4Cl",
    "stored": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "1.5",
      "unit": "G_PER_L",
      "original_amount": 1.5,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: NH4Cl",
        "exact_source_quote": "NH4Cl 1.5 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 28.0426,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "stored": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.2",
      "unit": "G_PER_L",
      "original_amount": 0.2,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 0.2 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "CaCl2 x 2 H2O",
    "stored": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.02",
      "unit": "G_PER_L",
      "original_amount": 20,
      "original_unit": "mg",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 20.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.136041,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Fe(NH4)citrate",
    "stored": {
      "value": "0.0012",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "0.0012",
      "unit": "G_PER_L",
      "original_amount": 1.2,
      "original_unit": "mg",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Fe(NH4)citrate",
        "exact_source_quote": "NH4-Fe-III-Citrat 1.2 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Fe(NH4)citrate\",\n                        \"compound_id\": 1203,\n                        \"amount\": 1.2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0012,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "Activated carbon",
    "stored": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "5",
      "unit": "G_PER_L",
      "original_amount": 5,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Activated carbon",
        "exact_source_quote": "Activated carbon 5.0 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Activated carbon\",\n                        \"compound_id\": 757,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "Agar",
    "stored": {
      "value": "15",
      "unit": "G_PER_L"
    },
    "proposed": {
      "value": "15",
      "unit": "G_PER_L",
      "original_amount": 15,
      "original_unit": "g",
      "basis": "Provider-declared 1000 ml main solution"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Agar",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Existing amount and unit match the exact source and provider main basis but have no attached evidence. For milligram inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[8].concentration",
    "ingredient": "Double distilled water",
    "stored": {
      "value": "1000",
      "unit": "G_PER_L"
    },
    "proposed": {
      "amount": 1000,
      "unit": "ml",
      "scope": "Main-recipe solvent quantity"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Double distilled water",
        "exact_source_quote": "Bidistillated water 1000.0 ml",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Double distilled water\",\n                        \"compound_id\": 1021,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source and provider specify a liquid volume, but the record asserts mass per litre. Preserve the 1000 ml batch solvent quantity and its grade; no source density or independently measured final volume permits a mass conversion."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[9].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "stored": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 100,
      "original_unit": "mg",
      "stock_g_per_L": 0.1,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 100.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 100 mg in its listed 1000 ml water and provider 1000 ml stock basis: 100 mg * 0.001 g/mg / 1 L = 0.1 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[10].concentration",
    "ingredient": "MnCl2 x 4 H2O",
    "stored": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 30,
      "original_unit": "mg",
      "stock_g_per_L": 0.03,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl2 x 4 H2O 30.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 30,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 30 mg in its listed 1000 ml water and provider 1000 ml stock basis: 30 mg * 0.001 g/mg / 1 L = 0.03 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[11].concentration",
    "ingredient": "H3BO3",
    "stored": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 300,
      "original_unit": "mg",
      "stock_g_per_L": 0.3,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: H3BO3",
        "exact_source_quote": "H3BO3 300.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 300 mg in its listed 1000 ml water and provider 1000 ml stock basis: 300 mg * 0.001 g/mg / 1 L = 0.3 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[12].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "stored": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 200,
      "original_unit": "mg",
      "stock_g_per_L": 0.2,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl2 x 6 H2O 200.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 200 mg in its listed 1000 ml water and provider 1000 ml stock basis: 200 mg * 0.001 g/mg / 1 L = 0.2 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[13].concentration",
    "ingredient": "CuCl2 x 2 H2O",
    "stored": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 10,
      "original_unit": "mg",
      "stock_g_per_L": 0.01,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: CuCl2 x 2 H2O",
        "exact_source_quote": "CuCl2 x 2 H2O 10.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 10 mg in its listed 1000 ml water and provider 1000 ml stock basis: 10 mg * 0.001 g/mg / 1 L = 0.01 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[14].concentration",
    "ingredient": "NiCl2 x 6 H2O",
    "stored": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 20,
      "original_unit": "mg",
      "stock_g_per_L": 0.02,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: NiCl2 x 6 H2O",
        "exact_source_quote": "NiCl2 x 6 H2O 20.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 20 mg in its listed 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[15].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "stored": {
      "value": "0.9",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 900,
      "original_unit": "mg",
      "stock_g_per_L": 0.9,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 900.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 900,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.9,\n                        \"mmol_l\": 3.71978,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 900 mg in its listed 1000 ml water and provider 1000 ml stock basis: 900 mg * 0.001 g/mg / 1 L = 0.9 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "correct",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ingredients[16].concentration",
    "ingredient": "Na2SeO3",
    "stored": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "proposed": {
      "original_amount": 20,
      "original_unit": "mg",
      "stock_g_per_L": 0.02,
      "stock_provider_volume_ml": 1000,
      "stock_addition_ml_per_source_batch": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: Na2SeO3",
        "exact_source_quote": "Na2SeO3 20.0 mg",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\": 699,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.115648,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "The source stock contains 20 mg in its listed 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02 g/L stock. This existing number is not a neat main-medium dose. Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred grams, without assuming measured final volume."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "solutions",
    "stored": null,
    "ingredient": "TS2 addition",
    "proposed": {
      "amount": 1,
      "unit": "ml",
      "scope": "Main source batch addition"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 main recipe: Trace element solution TS2",
        "exact_source_quote": "Trace element solution TS2 1.0 ml",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution TS2\",\n                        \"solution_id\": 1648,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Restore this missing stage-specific source quantity. TS2 stock water is not a second litre of main-medium solvent."
  },
  {
    "decision": "add",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "solutions",
    "stored": null,
    "ingredient": "TS2 stock water",
    "proposed": {
      "amount": 1000,
      "unit": "ml",
      "scope": "Stock preparation only"
    },
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 Trace element solution TS2 subsection: Distilled water",
        "exact_source_quote": "Distilled water 1000.0 ml",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      },
      {
        "source_key": "mediadive811api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/811",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a"
      }
    ],
    "explanation": "Restore this missing stage-specific source quantity. TS2 stock water is not a second litre of main-medium solvent."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "ph_value",
    "stored": 7.5,
    "ingredient": "Target pH",
    "proposed": 7.5,
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 final preparation line",
        "exact_source_quote": "pH 7.5",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      }
    ],
    "explanation": "The target pH and existing second preparation step agree with the source. Attach narrow evidence; do not reinterpret the schema target-pH slot as a measured final pH."
  },
  {
    "decision": "evidence_only",
    "local_input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "field_path": "preparation_steps[0].description",
    "stored": "Befor autoclaving add trace element solution to the medium. Dissolve first all ingredients then add activated carbon. Finally autoclave.",
    "ingredient": "Existing order of TS2 addition, dissolution, carbon and sterilization",
    "source_snippets": [
      {
        "source_key": "dsmz811",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf",
        "source_locator": "Page 1 preparation paragraph",
        "exact_source_quote": "Befor autoclaving add trace element solution to the medium. Dissolve first all ingredients \nthen add activated carbon. Finally autoclave.",
        "snapshot_sha256": "d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927",
        "parsed_text_sha256": "99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643"
      }
    ],
    "explanation": "Existing preparation retains the source order; attach its exact scope. The source supplies no numeric sterilization duration or temperature, and none is proposed."
  }
]

### Identifier metadata, exact secondary keys and supplied-form scope

grounding: concern. Targets: CultureMech:001956.

16 distinct primary/current-secondary identifiers resolve. 0 label instances differ from current canonical labels; 0 asserted current secondary keys lack an exact pinned index row. Legacy numeric links are assessed separately and are not established by CHEBI correspondence. Target linkage is 16/17 primary and 16/17 secondary ingredient instances; this measures presence, not source validity.

{"label_drift": [], "missing_secondary_keys": [], "legacy_instances": [], "coverage_scale": "0–100 percent; each ingredient instance counted once", "denominator": 17, "primary_percent": 94.11764705882354, "secondary_percent": 94.11764705882354}

### Every asserted primary and secondary chemical form

grounding: concern. Targets: CultureMech:001956.

The explicitly sourced Na2HPO4·12H2O maps to CHEBI:34683 (HO4P.2Na without waters), and NiCl2·6H2O maps to CHEBI:34887 (Cl2Ni without waters). Other explicitly stated hydrates match their source forms. Ferric ammonium citrate resolves as an indefinite mixture, not a molecule with a fixed formula; water identity does not encode double-distillation grade. Activated carbon remains ungrounded rather than receiving an invented pure-carbon or grade identity.

### Solid state versus defined-composition claim

scope: concern. Targets: CultureMech:001956.

SOLID_AGAR is supported by the explicit 15 g agar row. However, composition_type=DEFINED and medium_type=DEFINED assert more than the supplied forms establish: CHEBI agar is a complex polysaccharide mixture, ferric ammonium citrate has indefinite composition, and the source supplies no activated-carbon grade specification. Provider complex_medium=no does not override the local chemical-definition contract. No replacement classification is guessed from missing product details.

### Complete target and owner preparation and evidence

completeness: concern. Targets: CultureMech:001956.

Both layers retain the same correct source order and pH; no missing temperature/time is filled from convention. The full main source and TS2 stock are available, but stock nodes/additions and concentration evidence are absent. General microbial-cultivation application is not strain-specific growth evidence; no organism growth claims are promoted.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001956.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: TS2 stock strengths are presented as direct medium amounts

blocker / open / confirmed; issue key: CM001956-ts2-stock-flattening.

Eight source milligram quantities belong to the 1000 ml TS2 stock, which is added at 1 ml per listed main batch. Both local layers instead place its full g/L strengths in direct ingredients and omit the stock dose.

### f2: A source solvent volume is encoded as mass concentration

major / open / confirmed; issue key: CM001956-water-unit.

The source Bidistillated water 1000.0 ml and provider Double distilled water amount 1000, unit ml became 1000 G_PER_L. No density or final-volume evidence supports that conversion.

### f3: Two explicit hydrates are linked to structures without waters

major / open / confirmed; issue key: CM001956-hydrate-grounding.

Phosphate dodecahydrate and nickel chloride hexahydrate are sourced explicitly, while their primary and secondary IDs encode anhydrous structures. Canonical label passes do not establish correct supplied forms.

### f4: Fully defined classification overstates known mixture composition

major / open / confirmed; issue key: CM001956-defined-mixtures.

The record asserts both defined classifications despite explicit agar and ferric ammonium citrate mixture identities and unspecified activated-carbon grade. The provider flag complex_medium=no does not establish exact component composition under the local enum contract.

### f5: Source-supported amounts and preparation lack attached evidence

major / open / confirmed; issue key: CM001956-amount-evidence.

All 34 local ingredient concentrations lack attached evidence; source-supported main values and current preparation therefore remain evidence_only, while wrong units and stock scopes require correction.

## Recommended Actions And Acceptance Checks

### a1

Restore the complete TS2 stock and exact 1 ml addition in the maintained owner, preserve original milligram and volume bases, and regenerate the target after review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the exact main solvent volume and grade in preparation or an appropriate supported volume field; do not invent water mass or final-volume evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify exact hydrate identifiers before correcting both maintained primary and secondary links; preserve the source-supplied amounts and do not substitute guessed IDs.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reconcile the maintained composition classification with supplied-form evidence and keep its legacy medium_type derivation consistent; record uncertainty instead of inventing a product specification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach exact source snippets and locators to retained or corrected claims in the maintained owner; ensure narrow evidence survives regeneration without implying chemical-form correctness from numerical agreement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/activated_carbon_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch019/184/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch019/184/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml:1:id: CultureMech:001956<br>./data/normalized_yaml/bacterial/activated_carbon_medium.yaml:1:id: CultureMech:001956<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch019/source-preflight-bound/184/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 19 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz811 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf; Page 1 complete main recipe, TS2 subsection and preparation | supports | Exact original masses, milligram units, two separate water volumes and 1 ml TS2 addition. |
| mediadive811api | https://mediadive.dsmz.de/rest/medium/811; $.data.medium and complete $.data.solutions[0:2] | supports | Exact medium identity and provider-declared 1000 ml main/stock bases, with all source quantities and steps. |
| solution1648 | https://mediadive.dsmz.de/rest/solution/1648; $.data complete TS2 stock endpoint | supports | Independent exact stock identity with all eight milligram amounts and its 1000 ml water basis. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch019/184/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:15377 resolves to water. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:2509 resolves to agar. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31206 resolves to ammonium chloride. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31604 resolves to ferric ammonium citrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:33118 resolves to boric acid. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:34887 resolves to nickel dichloride. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi48843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:48843 resolves to disodium selenite. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent source revision/hash | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "asserted_secondary_rows": {"CHEBI:15377": [{"label": "[OH2]", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "acqua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "aqua", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dH2O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydridooxygen", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydrogen oxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distiled water", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water (for liquid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water (for solid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "eau", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H(2)O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H2O", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "HOH", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "hydrogen hydroxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "oxidane", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Wasser", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "WATER", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (BD)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)*", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Molecular Genetics)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar* (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Bacteriological Agar", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "(NH4)Cl", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "[NH4]Cl", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Chloride", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium chloride", "match_type": "ontology_label", "identifier": "CHEBI:31206", "preferred_term": "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammoniumchlorid", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "azanium chloride", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl(CAS: 12125-02-9)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl(Fisher A 649-500)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl2", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31604": [{"label": "Ammonium ferric citrate", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium iron(III) citrate", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "E381", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Fe(NH4)citrate", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ferric ammmonium citrate", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ferric ammonium citrate", "match_type": "preferred_term", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FerriSeltz", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "zinc sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zinc sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc sulfate heptahydrate (1:1:7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zn2SO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 .7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 × 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7 H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4-7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4∙7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4･7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "[B(OH)3]", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "B(OH)3", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Boric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "boron trihydroxide", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "orthoboric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "trihydroxidoboron", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Dibasic sodium phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Disodium hydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Disodium Phosphate", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO anydrous", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2H2PO4", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "[NiCl2]", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel dichloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel(2+) chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel(II) chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel(II) chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NiCl 2", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:48843": [{"label": "disodium selenite", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium selenium trioxide", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2Se2O3", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SeO3", "match_type": "preferred_term", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumselenit", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "selenious acid (H2SeO3) disodium salt", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "selenious acid disodium salt", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "selenious acid, disodium salt", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "selenious acid, sodium salt (1:2)", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium selenite", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "cobalt (II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt chloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "cobalt chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+) dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 4 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 × 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 ∙ 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P 0662)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MKP", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Orthophosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium acid phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen orthophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate monobasic", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sorensen's potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Molybdic acid, disodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2 MoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2Mo4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 ⋅ 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4. 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO7 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7O4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)molybdenum--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Molybdate Dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium molybdate(VI) dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium orthomolybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (50 g/l stock solution)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O (5M)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O solution (7%)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 × 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CaCl2. 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2.2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl22H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CaCl22H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}, {"label": "CaCl2x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2x2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2·2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O (Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(CAS: 10035-04-8)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2•2H2O(Sigma C-3881)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride dihydrate", "match_type": "ontology_label", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term": "CaCl22H2O", "ontology_id": "CHEBI:86158", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "copper (II) chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper dichloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) dichloride --water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Copper(II) chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) chloride--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) chloride.2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Coppertrace", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl 2", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl 2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 .2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2*2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2-2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2.2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2·2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2・2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cupric chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cupric chloride.2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "dichloromanganese--water (1/4)", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese (II) chloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese chloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese dichloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) chloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) chloride--water (1/4)", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) chloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous chloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 . 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 x 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 · 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 × 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 ∙ 4 H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2.4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2·4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2∙4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2⋅4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2・4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2･4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl4 x 4 H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl4・4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys": [], "legacy_instances": []} |
| classification-schema | src/culturemech/schema/culturemech.yaml; MediumTypeEnum.DEFINED and MediumCompositionTypeEnum.DEFINED; known exact composition requirement | context_only | DEFINED denotes chemically defined composition with every component and its exact quantity known. The source provider complex_medium=no is classification metadata, not product-composition evidence. |
| history-metadata | data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml; data/normalized_yaml/bacterial/activated_carbon_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates primary and stock rows and excludes a limited list of water names; its list does not include Double distilled water, and fallback unit normalization does not establish a valid final concentration. Current code is a maintenance context, not proof of the historical transformation. A single-owner merge preserves the supplied fields and does not repair these errors. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates primary and stock rows and excludes a limited list of water names; its list does not include Double distilled water, and fallback unit normalization does not establish a valid final concentration. Current code is a maintenance context, not proof of the historical transformation. A single-owner merge preserves the supplied fields and does not repair these errors. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates primary and stock rows and excludes a limited list of water names; its list does not include Double distilled water, and fallback unit normalization does not establish a valid final concentration. Current code is a maintenance context, not proof of the historical transformation. A single-owner merge preserves the supplied fields and does not repair these errors. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No source-specified carbon grade, exact mixture composition, sterilization temperature/time, density or independently measured final volume is inferred. Source pH is a target value. The two 1000 ml water rows and 1 ml stock addition retain separate stages and are not silently combined into an assumed final litre.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115041Z-culturemech-001956-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: activated_carbon_medium (CultureMech:001956)'
started_at: '2026-10-21T11:43:22Z'
finished_at: '2026-10-21T11:50:41Z'
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
summary: The exact DSMZ 811 identity and preparation resolve, but both local layers
  flatten eight TS2 stock strengths into the medium and encode 1000 ml water as 1000
  g/L. Two explicitly hydrated salts have anhydrous ontology structures, amount evidence
  is absent, and the fully defined classification overstates the supplied mixture
  composition.
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
  - path: data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
    sha256: b572df3e34f0678d422bb71d40497ae7c3311373ff0dc4abf0410c19a5f46b34
    role: target
  - path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
    sha256: 9ce5a2393c67b652d300bec8be5dedd77c67bc7a386e1ff98527c452a5cc609e
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
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 184; batch 019 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eighteen task batches
    contain 180 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 182 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001956
targets:
- target_id: CultureMech:001956
  path: data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  label: activated_carbon_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/184/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/184/strict.tsv"
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001956
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
  - CultureMech:001956
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:02.105276Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch019/184/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:03.879337Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch019/184/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:06.367053Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:44:07.629077Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:50:40Z'
  support: supports
  summary: './data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml:1:id: CultureMech:001956

    ./data/normalized_yaml/bacterial/activated_carbon_medium.yaml:1:id: CultureMech:001956

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/source-preflight-bound/184/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:50:40Z'
  support: supports
  summary: 19 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 37bbe62a985a9ad7473d7e90261527435d80da95a100f3041edb81e5b2664216
- evidence_id: dsmz811
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf
  locator: Page 1 complete main recipe, TS2 subsection and preparation
  accessed_at: '2026-10-21T11:29:08.318015Z'
  support: supports
  summary: Exact original masses, milligram units, two separate water volumes and
    1 ml TS2 addition.
  snapshot_sha256: d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927
- evidence_id: mediadive811api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/811
  locator: $.data.medium and complete $.data.solutions[0:2]
  accessed_at: '2026-10-21T11:29:07.402801Z'
  support: supports
  summary: Exact medium identity and provider-declared 1000 ml main/stock bases, with
    all source quantities and steps.
  snapshot_sha256: 17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a
- evidence_id: solution1648
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1648
  locator: $.data complete TS2 stock endpoint
  accessed_at: '2026-10-21T11:29:45.589592Z'
  support: supports
  summary: Independent exact stock identity with all eight milligram amounts and its
    1000 ml water basis.
  snapshot_sha256: e975a0aaf370a50e3a929c2ffb597c1ca5b9a36c2a710732df763fb919467394
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch019/184/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 9722cf9453273f47774dd98094b0129e145abf60dc6d328bb250880ccca3cbe6
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identity/label existence is separate from
    exact supplied form and source-specific ingredient support.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identity/label existence is separate from
    exact supplied form and source-specific ingredient support.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: CHEBI:31206 resolves to ammonium chloride. Identity/label existence is
    separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31604
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:42:44.987529Z'
  support: supports
  summary: CHEBI:31604 resolves to ferric ammonium citrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 31acf125b469ffd64e2de503550d29336a7a0f99c8a3ea24b80b53bdb715e7f8
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
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: CHEBI:33118 resolves to boric acid. Identity/label existence is separate
    from exact supplied form and source-specific ingredient support.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34683
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:42:46.851695Z'
  support: supports
  summary: CHEBI:34683 resolves to disodium hydrogenphosphate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 288ee6eaa066e7579840122d3411df9987889818425faea2b7203724bbc41fd2
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: CHEBI:34887 resolves to nickel dichloride. Identity/label existence is
    separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi48843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T10:07:16.976958Z'
  support: supports
  summary: CHEBI:48843 resolves to disodium selenite. Identity/label existence is
    separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: f8b54c90292c3ea1c215cbb96e7b9302304ba97f07c586c66f09b6689b9f2d91
- evidence_id: chebi53503
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:04:44.349630Z'
  support: supports
  summary: CHEBI:53503 resolves to cobalt chloride hexahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
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
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: CHEBI:86318 resolves to copper(II) chloride dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent source revision/hash
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "asserted_secondary_rows":
    {"CHEBI:15377": [{"label": "[OH2]", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "acqua", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "agua",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "aqua", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "dH2O", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "dihydridooxygen",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "dihydrogen oxide", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distiled water",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Distilled water", "match_type": "preferred_term", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Distilled water
    (for liquid medium)", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Distilled water (for solid medium)", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "eau",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "H(2)O", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "H2O", "match_type": "synonym", "identifier":
    "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "HOH", "match_type":
    "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "hydrogen
    hydroxide", "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term":
    "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "oxidane", "match_type": "synonym", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Wasser", "match_type": "synonym",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "WATER",
    "match_type": "synonym", "identifier": "CHEBI:15377", "preferred_term": "Distilled
    water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar  (if needed)", "match_type":
    "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar
    (BD)", "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "agar (BD-Difco)", "match_type": "synonym", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Difco)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (if needed)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar (if needed)*", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Agar (Molecular Genetics)", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Agar (Purified)",
    "match_type": "synonym", "identifier": "CHEBI:2509", "preferred_term": "Agar",
    "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Agar* (if needed)", "match_type": "synonym", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Bacteriological Agar", "match_type": "synonym",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "(NH4)Cl", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "[NH4]Cl", "match_type": "synonym", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Ammonium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium chloride",
    "match_type": "ontology_label", "identifier": "CHEBI:31206", "preferred_term":
    "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)",
    "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "Ammonium chloride (nitrogen source)", "ontology_id": "CHEBI:31206", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Ammonium chloride (nitrogen source)",
    "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl",
    "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Ammoniumchlorid", "match_type": "synonym", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "azanium chloride", "match_type": "synonym",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl(CAS:
    12125-02-9)", "match_type": "synonym", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "NH4Cl(Fisher A 649-500)", "match_type": "synonym", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NH4Cl2", "match_type": "synonym",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31604": [{"label":
    "Ammonium ferric citrate", "match_type": "synonym", "identifier": "CHEBI:31604",
    "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "ammonium iron(III) citrate", "match_type":
    "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate",
    "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "E381", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term":
    "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Fe(NH4)citrate", "match_type": "synonym", "identifier":
    "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ferric ammmonium
    citrate", "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term":
    "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Ferric ammonium citrate", "match_type": "preferred_term",
    "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id":
    "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FerriSeltz",
    "match_type": "synonym", "identifier": "CHEBI:31604", "preferred_term": "Ferric
    ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type":
    "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate",
    "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4
    x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate
    anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium
    sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate",
    "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term":
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
    "unique"}], "CHEBI:33118": [{"label": "[B(OH)3]", "match_type": "synonym", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "B(OH)3", "match_type": "synonym",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Boric acid", "match_type":
    "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "boron
    trihydroxide", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "H BO", "match_type": "synonym", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "H3BO", "match_type": "synonym", "identifier":
    "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)",
    "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3",
    "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "orthoboric acid", "match_type": "synonym", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "trihydroxidoboron", "match_type": "synonym",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label":
    "Dibasic sodium phosphate", "match_type": "synonym", "identifier": "CHEBI:34683",
    "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Disodium hydrogen phosphate", "match_type":
    "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id":
    "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium
    hydrogenphosphate", "match_type": "ontology_label", "identifier": "CHEBI:34683",
    "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "disodium hydrogenphosphate", "match_type":
    "ontology_label", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate
    dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Disodium Phosphate", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO", "match_type": "synonym",
    "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na HPO anydrous",
    "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4",
    "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Na2H2PO4", "match_type": "synonym", "identifier": "CHEBI:34683", "preferred_term":
    "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium phosphate dibasic", "match_type":
    "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Sodium phosphate
    dibasic", "ontology_id": "CHEBI:34683", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Sodium phosphate dibasic", "match_type": "synonym", "identifier":
    "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "[NiCl2]", "match_type":
    "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Nickel
    chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "nickel chloride", "match_type": "synonym", "identifier":
    "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "nickel dichloride", "match_type":
    "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "nickel(2+)
    chloride", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Nickel(II) chloride", "match_type": "synonym", "identifier":
    "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "nickel(II) chloride", "match_type":
    "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NiCl
    2", "match_type": "synonym", "identifier": "CHEBI:34887", "preferred_term": "NiCl2",
    "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:48843": [{"label": "disodium selenite", "match_type":
    "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id":
    "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "disodium
    selenium trioxide", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term":
    "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2Se2O3", "match_type": "synonym", "identifier": "CHEBI:48843",
    "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Na2SeO3", "match_type": "preferred_term", "identifier":
    "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Natriumselenit", "match_type": "synonym",
    "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "selenious acid
    (H2SeO3) disodium salt", "match_type": "synonym", "identifier": "CHEBI:48843",
    "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "selenious acid disodium salt", "match_type":
    "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id":
    "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "selenious
    acid, disodium salt", "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term":
    "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "selenious acid, sodium salt (1:2)", "match_type": "synonym",
    "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium selenite",
    "match_type": "synonym", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3",
    "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:53503": [{"label": "cobalt (II) chloride hexahydrate", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate",
    "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier":
    "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id":
    "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt
    chloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "cobalt chloride hydrate", "match_type":
    "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate",
    "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Cobalt dichloride hexahydrate", "match_type": "synonym", "identifier":
    "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id":
    "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+)
    dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride
    hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride--water (1/7)",
    "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt
    chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "CoCl2 . 6H2O", "match_type": "synonym", "identifier":
    "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 2 H2O",
    "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2
    x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "resolved:owned"}, {"label": "CoCl2 x 4 H2O", "match_type": "synonym", "identifier":
    "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503",
    "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2 x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 x 6H2O",
    "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2
    x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 × 6H2O", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "CoCl2 ∙ 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2∙6H2O", "match_type": "synonym",
    "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "CoCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term":
    "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "CoCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:53503",
    "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status":
    "REJECTED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH PO", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4",
    "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "KH2PO4 (0.4 g/l)", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4 (7% w/v)", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2PO4(Sigma P
    0662)", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MKP", "match_type": "synonym", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Monopotassium dihydrogen phosphate", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium
    monophosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Monopotassium orthophosphate", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium phosphate",
    "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4",
    "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Orthophosphoric acid, monopotassium salt", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid,
    monopotassium salt", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Phosphoric acid, potassium salt (1:1)", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium acid
    phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium dihydrogen orthophosphate", "match_type": "synonym",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dihydrogen
    phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium Phosphate", "match_type": "synonym", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate monobasic", "match_type":
    "synonym", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sorensen''s
    potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate dihydrate", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Molybdic
    acid, disodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2 MoO4 x 2 H2O", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2Mo4
    x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 . 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O
    (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4 x 2H2O", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · 2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O",
    "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"},
    {"label": "Na2MoO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 ⋅ 2H2O", "match_type":
    "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.
    2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O", "match_type": "synonym",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O",
    "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4
    x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
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
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl 2 X 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2  x 2 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2
    . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CaCl2 x  2 H2O", "match_type": "synonym", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
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
    "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:86318": [{"label":
    "copper (II) chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "copper dichloride--water (1/2)",
    "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2
    x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(2+) dichloride --water (1/2)", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Copper(II)
    chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "copper(II) chloride--water (1/2)", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II)
    chloride.2H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Coppertrace", "match_type": "synonym", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuCl 2", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl
    2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuCl2 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 .2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2
    x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuCl2 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2 · 2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2*2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2
    x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuCl2-2H2O", "match_type": "synonym", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2.2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2·2H2O",
    "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term": "CuCl2
    x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "CuCl2⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "CuCl2・2H2O", "match_type": "synonym",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cupric
    chloride dihydrate", "match_type": "synonym", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "cupric chloride.2H2O", "match_type": "synonym", "identifier":
    "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label":
    "dichloromanganese--water (1/4)", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Manganese (II) chloride tetrahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2
    x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Manganese chloride tetrahydrate", "match_type": "synonym",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese
    dichloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) chloride tetrahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2
    x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) chloride--water (1/4)", "match_type": "synonym",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II)
    chloride tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Manganous chloride tetrahydrate",
    "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2
    x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnCl2 . 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2
    x 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term":
    "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnCl2 · 4H2O", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2 × 4H2O", "match_type": "synonym",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2
    ∙ 4 H2O", "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term":
    "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnCl2.4H2O", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2·4H2O", "match_type": "synonym",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2∙4H2O",
    "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2
    x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnCl2⋅4H2O", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2・4H2O", "match_type": "synonym",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnCl2･4H2O",
    "match_type": "synonym", "identifier": "CHEBI:86368", "preferred_term": "MnCl2
    x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnCl4 x 4 H2O", "match_type": "synonym", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnCl4・4H2O", "match_type": "synonym",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}, "missing_current_keys":
    [], "legacy_instances": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: classification-schema
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediumTypeEnum.DEFINED and MediumCompositionTypeEnum.DEFINED; known exact
    composition requirement
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: DEFINED denotes chemically defined composition with every component and
    its exact quantity known. The source provider complex_medium=no is classification
    metadata, not product-composition evidence.
  snapshot_sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACTIVATED_CARBON_MEDIUM.yaml; data/normalized_yaml/bacterial/activated_carbon_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/activated_carbon_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: Current importer separates primary and stock rows and excludes a limited
    list of water names; its list does not include Double distilled water, and fallback
    unit normalization does not establish a valid final concentration. Current code
    is a maintenance context, not proof of the historical transformation. A single-owner
    merge preserves the supplied fields and does not repair these errors.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: Current importer separates primary and stock rows and excludes a limited
    list of water names; its list does not include Double distilled water, and fallback
    unit normalization does not establish a valid final concentration. Current code
    is a maintenance context, not proof of the historical transformation. A single-owner
    merge preserves the supplied fields and does not repair these errors.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:50:40Z'
  support: context_only
  summary: Current importer separates primary and stock rows and excludes a limited
    list of water names; its list does not include Double distilled water, and fallback
    unit normalization does not establish a valid final concentration. Current code
    is a maintenance context, not proof of the historical transformation. A single-owner
    merge preserves the supplied fields and does not repair these errors.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact single-owner source identity
  outcome: supported
  summary: The target and sole normalized owner share CultureMech:001956, identify
    DSMZ 811 and match the primary title and provider accession. The explicit merge
    provenance has one contributor; no sibling formulation, strain, or taxonomic growth
    assertion is substituted.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - record
  - owner-0
  - id-search
  - dsmz811
  - mediadive811api
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 42 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"\
    target\",\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\"\
    : \"Na2HPO4 x 12 H2O\",\n    \"stored\": {\n      \"value\": \"9\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"9\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"original_amount\": 9,\n      \"original_unit\"\
    : \"g\",\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Na2HPO4 x 12 H2O\",\n   \
    \     \"exact_source_quote\": \"Na2HPO4 x 12 H2O 9.0 g\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 95,\\n                        \\\"amount\\\": 9,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 9,\\n     \
    \                   \\\"mmol_l\\\": 63.3986,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\"\
    : \"KH2PO4\",\n    \"stored\": {\n      \"value\": \"1.5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"1.5\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_amount\": 1.5,\n      \"original_unit\": \"g\"\
    ,\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH2PO4 1.5 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 11.0225,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\"\
    : \"NH4Cl\",\n    \"stored\": {\n      \"value\": \"1.5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"1.5\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_amount\": 1.5,\n      \"original_unit\": \"g\"\
    ,\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: NH4Cl\",\n        \"exact_source_quote\"\
    : \"NH4Cl 1.5 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 28.0426,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\"\
    : \"MgSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.2\",\n      \"\
    unit\": \"G_PER_L\",\n      \"original_amount\": 0.2,\n      \"original_unit\"\
    : \"g\",\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: MgSO4 x 7 H2O\",\n      \
    \  \"exact_source_quote\": \"MgSO4 x 7 H2O 0.2 g\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n  \
    \                      \\\"mmol_l\\\": 0.811438,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\"\
    : \"CaCl2 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.02\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.02\",\n\
    \      \"unit\": \"G_PER_L\",\n      \"original_amount\": 20,\n      \"original_unit\"\
    : \"mg\",\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: CaCl2 x 2 H2O\",\n      \
    \  \"exact_source_quote\": \"CaCl2 x 2 H2O 20.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n \
    \                       \\\"mmol_l\\\": 0.136041,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"Existing amount and unit match the exact source\
    \ and provider main basis but have no attached evidence. For milligram inputs,\
    \ convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\"\
    : \"Fe(NH4)citrate\",\n    \"stored\": {\n      \"value\": \"0.0012\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"0.0012\"\
    ,\n      \"unit\": \"G_PER_L\",\n      \"original_amount\": 1.2,\n      \"original_unit\"\
    : \"mg\",\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Fe(NH4)citrate\",\n     \
    \   \"exact_source_quote\": \"NH4-Fe-III-Citrat 1.2 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Fe(NH4)citrate\\\",\\n                        \\\"compound_id\\\
    \": 1203,\\n                        \\\"amount\\\": 1.2,\\n                  \
    \      \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0012,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\"\
    : \"Activated carbon\",\n    \"stored\": {\n      \"value\": \"5\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"5\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"original_amount\": 5,\n      \"original_unit\"\
    : \"g\",\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Activated carbon\",\n   \
    \     \"exact_source_quote\": \"Activated carbon 5.0 g\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Activated carbon\\\",\\n                        \\\"compound_id\\\
    \": 757,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\"\
    : \"Agar\",\n    \"stored\": {\n      \"value\": \"15\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"proposed\": {\n      \"value\": \"15\",\n      \"unit\": \"G_PER_L\"\
    ,\n      \"original_amount\": 15,\n      \"original_unit\": \"g\",\n      \"basis\"\
    : \"Provider-declared 1000 ml main solution\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 main recipe: Agar\",\n        \"exact_source_quote\"\
    : \"Agar 15.0 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\"\
    : \"target\",\n    \"field_path\": \"ingredients[8].concentration\",\n    \"ingredient\"\
    : \"Double distilled water\",\n    \"stored\": {\n      \"value\": \"1000\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"amount\": 1000,\n\
    \      \"unit\": \"ml\",\n      \"scope\": \"Main-recipe solvent quantity\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Double distilled water\"\
    ,\n        \"exact_source_quote\": \"Bidistillated water 1000.0 ml\",\n      \
    \  \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Double distilled water\\\",\\n                        \\\"\
    compound_id\\\": 1021,\\n                        \\\"amount\\\": 1000,\\n    \
    \                    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"The source and provider specify a liquid\
    \ volume, but the record asserts mass per litre. Preserve the 1000 ml batch solvent\
    \ quantity and its grade; no source density or independently measured final volume\
    \ permits a mass conversion.\"\n  },\n  {\n    \"decision\": \"correct\",\n  \
    \  \"local_input\": \"target\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"ingredient\": \"ZnSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"0.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"\
    original_amount\": 100,\n      \"original_unit\": \"mg\",\n      \"stock_g_per_L\"\
    : 0.1,\n      \"stock_provider_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Trace element solution TS2 subsection:\
    \ ZnSO4 x 7 H2O\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 100.0 mg\"\
    ,\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.347752,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 100 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 100 mg * 0.001 g/mg / 1 L =\
    \ 0.1 g/L stock. This existing number is not a neat main-medium dose. Preserve\
    \ the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"ingredient\": \"MnCl2 x 4 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"0.03\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"\
    original_amount\": 30,\n      \"original_unit\": \"mg\",\n      \"stock_g_per_L\"\
    : 0.03,\n      \"stock_provider_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Trace element solution TS2 subsection:\
    \ MnCl2 x 4 H2O\",\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 30.0 mg\"\
    ,\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 30,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.03,\\n\
    \                        \\\"mmol_l\\\": 0.151588,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 30 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 30 mg * 0.001 g/mg / 1 L = 0.03\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"ingredient\": \"H3BO3\",\n    \"stored\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\"\
    : 300,\n      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.3,\n    \
    \  \"stock_provider_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Trace element solution TS2 subsection:\
    \ H3BO3\",\n        \"exact_source_quote\": \"H3BO3 300.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 300,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.3,\\n               \
    \         \\\"mmol_l\\\": 4.85123,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock contains 300 mg in\
    \ its listed 1000 ml water and provider 1000 ml stock basis: 300 mg * 0.001 g/mg\
    \ / 1 L = 0.3 g/L stock. This existing number is not a neat main-medium dose.\
    \ Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives\
    \ transferred grams, without assuming measured final volume.\"\n  },\n  {\n  \
    \  \"decision\": \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"ingredients[12].concentration\",\n    \"ingredient\": \"CoCl2 x 6 H2O\",\n\
    \    \"stored\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"proposed\": {\n      \"original_amount\": 200,\n      \"original_unit\"\
    : \"mg\",\n      \"stock_g_per_L\": 0.2,\n      \"stock_provider_volume_ml\":\
    \ 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: CoCl2 x 6 H2O\"\
    ,\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 200.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 200,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.54037,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 200 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 200 mg * 0.001 g/mg / 1 L =\
    \ 0.2 g/L stock. This existing number is not a neat main-medium dose. Preserve\
    \ the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"ingredient\": \"CuCl2 x 2 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"0.01\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"\
    original_amount\": 10,\n      \"original_unit\": \"mg\",\n      \"stock_g_per_L\"\
    : 0.01,\n      \"stock_provider_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Trace element solution TS2 subsection:\
    \ CuCl2 x 2 H2O\",\n        \"exact_source_quote\": \"CuCl2 x 2 H2O 10.0 mg\"\
    ,\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0586569,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n     \
    \ }\n    ],\n    \"explanation\": \"The source stock contains 10 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 10 mg * 0.001 g/mg / 1 L = 0.01\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"ingredient\": \"NiCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"0.02\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"\
    original_amount\": 20,\n      \"original_unit\": \"mg\",\n      \"stock_g_per_L\"\
    : 0.02,\n      \"stock_provider_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Trace element solution TS2 subsection:\
    \ NiCl2 x 6 H2O\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 20.0 mg\"\
    ,\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.154322,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 20 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"ingredient\": \"Na2MoO4 x 2 H2O\",\n    \"stored\": {\n      \"value\"\
    : \"0.9\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"\
    original_amount\": 900,\n      \"original_unit\": \"mg\",\n      \"stock_g_per_L\"\
    : 0.9,\n      \"stock_provider_volume_ml\": 1000,\n      \"stock_addition_ml_per_source_batch\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 Trace element solution TS2 subsection:\
    \ Na2MoO4 x 2 H2O\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 900.0\
    \ mg\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 900,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.9,\\n \
    \                       \\\"mmol_l\\\": 3.71978,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock contains 900 mg in\
    \ its listed 1000 ml water and provider 1000 ml stock basis: 900 mg * 0.001 g/mg\
    \ / 1 L = 0.9 g/L stock. This existing number is not a neat main-medium dose.\
    \ Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives\
    \ transferred grams, without assuming measured final volume.\"\n  },\n  {\n  \
    \  \"decision\": \"correct\",\n    \"local_input\": \"target\",\n    \"field_path\"\
    : \"ingredients[16].concentration\",\n    \"ingredient\": \"Na2SeO3\",\n    \"\
    stored\": {\n      \"value\": \"0.02\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"proposed\": {\n      \"original_amount\": 20,\n      \"original_unit\"\
    : \"mg\",\n      \"stock_g_per_L\": 0.02,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: Na2SeO3\",\n\
    \        \"exact_source_quote\": \"Na2SeO3 20.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2SeO3\\\",\\n                        \\\"compound_id\\\":\
    \ 699,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n \
    \                       \\\"mmol_l\\\": 0.115648,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 20 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"add\",\n    \"local_input\": \"target\",\n    \"field_path\": \"solutions\"\
    ,\n    \"stored\": null,\n    \"ingredient\": \"TS2 addition\",\n    \"proposed\"\
    : {\n      \"amount\": 1,\n      \"unit\": \"ml\",\n      \"scope\": \"Main source\
    \ batch addition\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Trace element solution TS2\"\
    ,\n        \"exact_source_quote\": \"Trace element solution TS2 1.0 ml\",\n  \
    \      \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution TS2\\\",\\n                        \\\
    \"solution_id\\\": 1648,\\n                        \\\"amount\\\": 1,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this missing stage-specific\
    \ source quantity. TS2 stock water is not a second litre of main-medium solvent.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"target\",\n  \
    \  \"field_path\": \"solutions\",\n    \"stored\": null,\n    \"ingredient\":\
    \ \"TS2 stock water\",\n    \"proposed\": {\n      \"amount\": 1000,\n      \"\
    unit\": \"ml\",\n      \"scope\": \"Stock preparation only\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: Distilled water\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.0 ml\",\n        \"\
    snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this missing stage-specific\
    \ source quantity. TS2 stock water is not a second litre of main-medium solvent.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"target\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"stored\": 7.5,\n    \"ingredient\"\
    : \"Target pH\",\n    \"proposed\": 7.5,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final preparation line\",\n        \"\
    exact_source_quote\": \"pH 7.5\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      }\n    ],\n    \"explanation\": \"The target pH and existing second preparation\
    \ step agree with the source. Attach narrow evidence; do not reinterpret the schema\
    \ target-pH slot as a measured final pH.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"target\",\n    \"field_path\": \"preparation_steps[0].description\"\
    ,\n    \"stored\": \"Befor autoclaving add trace element solution to the medium.\
    \ Dissolve first all ingredients then add activated carbon. Finally autoclave.\"\
    ,\n    \"ingredient\": \"Existing order of TS2 addition, dissolution, carbon and\
    \ sterilization\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Befor autoclaving add trace element solution to the medium. Dissolve first\
    \ all ingredients \\nthen add activated carbon. Finally autoclave.\",\n      \
    \  \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      }\n    ],\n    \"explanation\": \"Existing preparation retains the source\
    \ order; attach its exact scope. The source supplies no numeric sterilization\
    \ duration or temperature, and none is proposed.\"\n  },\n  {\n    \"decision\"\
    : \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"Na2HPO4 x 12 H2O\",\n    \"stored\": {\n      \"value\": \"9\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"value\": \"9\",\n  \
    \    \"unit\": \"G_PER_L\",\n      \"original_amount\": 9,\n      \"original_unit\"\
    : \"g\",\n      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Na2HPO4 x 12 H2O\",\n   \
    \     \"exact_source_quote\": \"Na2HPO4 x 12 H2O 9.0 g\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 95,\\n                        \\\"amount\\\": 9,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 9,\\n     \
    \                   \\\"mmol_l\\\": 63.3986,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[1].concentration\",\n    \"ingredient\": \"KH2PO4\",\n    \"stored\"\
    : {\n      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\"\
    : {\n      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\",\n      \"original_amount\"\
    : 1.5,\n      \"original_unit\": \"g\",\n      \"basis\": \"Provider-declared\
    \ 1000 ml main solution\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH2PO4 1.5 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 11.0225,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[2].concentration\",\n    \"ingredient\": \"NH4Cl\",\n    \"stored\"\
    : {\n      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\"\
    : {\n      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\",\n      \"original_amount\"\
    : 1.5,\n      \"original_unit\": \"g\",\n      \"basis\": \"Provider-declared\
    \ 1000 ml main solution\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: NH4Cl\",\n        \"exact_source_quote\"\
    : \"NH4Cl 1.5 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 28.0426,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"ingredient\": \"MgSO4 x 7 H2O\",\n\
    \    \"stored\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"proposed\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\
    ,\n      \"original_amount\": 0.2,\n      \"original_unit\": \"g\",\n      \"\
    basis\": \"Provider-declared 1000 ml main solution\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 main recipe: MgSO4 x 7 H2O\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.2 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n  \
    \                      \\\"mmol_l\\\": 0.811438,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[4].concentration\",\n    \"ingredient\": \"CaCl2 x 2 H2O\",\n\
    \    \"stored\": {\n      \"value\": \"0.02\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": {\n      \"value\": \"0.02\",\n      \"unit\": \"G_PER_L\"\
    ,\n      \"original_amount\": 20,\n      \"original_unit\": \"mg\",\n      \"\
    basis\": \"Provider-declared 1000 ml main solution\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 main recipe: CaCl2 x 2 H2O\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 20.0 mg\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n \
    \                       \\\"mmol_l\\\": 0.136041,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"Existing amount and unit match the exact source\
    \ and provider main basis but have no attached evidence. For milligram inputs,\
    \ convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"ingredient\": \"Fe(NH4)citrate\",\n\
    \    \"stored\": {\n      \"value\": \"0.0012\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": {\n      \"value\": \"0.0012\",\n      \"unit\": \"\
    G_PER_L\",\n      \"original_amount\": 1.2,\n      \"original_unit\": \"mg\",\n\
    \      \"basis\": \"Provider-declared 1000 ml main solution\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Fe(NH4)citrate\",\n     \
    \   \"exact_source_quote\": \"NH4-Fe-III-Citrat 1.2 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Fe(NH4)citrate\\\",\\n                        \\\"compound_id\\\
    \": 1203,\\n                        \\\"amount\\\": 1.2,\\n                  \
    \      \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0012,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[6].concentration\",\n    \"ingredient\": \"Activated carbon\"\
    ,\n    \"stored\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"proposed\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\
    ,\n      \"original_amount\": 5,\n      \"original_unit\": \"g\",\n      \"basis\"\
    : \"Provider-declared 1000 ml main solution\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 main recipe: Activated carbon\",\n        \"exact_source_quote\"\
    : \"Activated carbon 5.0 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Activated carbon\\\",\\n                        \\\"compound_id\\\
    \": 757,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[7].concentration\",\n    \"ingredient\": \"Agar\",\n    \"stored\"\
    : {\n      \"value\": \"15\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"proposed\"\
    : {\n      \"value\": \"15\",\n      \"unit\": \"G_PER_L\",\n      \"original_amount\"\
    : 15,\n      \"original_unit\": \"g\",\n      \"basis\": \"Provider-declared 1000\
    \ ml main solution\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main recipe: Agar\",\n        \"exact_source_quote\"\
    : \"Agar 15.0 g\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Existing amount and unit match the exact\
    \ source and provider main basis but have no attached evidence. For milligram\
    \ inputs, convert with 0.001 g/mg. This quantity judgment does not validate chemical-form\
    \ mappings. Primary 1000 ml water plus 1 ml TS2 is not independently measured\
    \ final volume.\"\n  },\n  {\n    \"decision\": \"correct\",\n    \"local_input\"\
    : \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\",\n    \"field_path\"\
    : \"ingredients[8].concentration\",\n    \"ingredient\": \"Double distilled water\"\
    ,\n    \"stored\": {\n      \"value\": \"1000\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"proposed\": {\n      \"amount\": 1000,\n      \"unit\": \"ml\"\
    ,\n      \"scope\": \"Main-recipe solvent quantity\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 main recipe: Double distilled water\",\n        \"\
    exact_source_quote\": \"Bidistillated water 1000.0 ml\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Double distilled water\\\",\\n                        \\\"\
    compound_id\\\": 1021,\\n                        \\\"amount\\\": 1000,\\n    \
    \                    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"The source and provider specify a liquid\
    \ volume, but the record asserts mass per litre. Preserve the 1000 ml batch solvent\
    \ quantity and its grade; no source density or independently measured final volume\
    \ permits a mass conversion.\"\n  },\n  {\n    \"decision\": \"correct\",\n  \
    \  \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[9].concentration\",\n    \"ingredient\":\
    \ \"ZnSO4 x 7 H2O\",\n    \"stored\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 100,\n\
    \      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.1,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: ZnSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 100.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.347752,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 100 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 100 mg * 0.001 g/mg / 1 L =\
    \ 0.1 g/L stock. This existing number is not a neat main-medium dose. Preserve\
    \ the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"MnCl2 x 4 H2O\",\n    \"stored\": {\n      \"value\": \"0.03\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 30,\n\
    \      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.03,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: MnCl2 x 4 H2O\"\
    ,\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 30.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 30,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.03,\\n\
    \                        \\\"mmol_l\\\": 0.151588,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 30 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 30 mg * 0.001 g/mg / 1 L = 0.03\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[11].concentration\",\n    \"ingredient\"\
    : \"H3BO3\",\n    \"stored\": {\n      \"value\": \"0.3\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 300,\n    \
    \  \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.3,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: H3BO3\",\n \
    \       \"exact_source_quote\": \"H3BO3 300.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 300,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.3,\\n               \
    \         \\\"mmol_l\\\": 4.85123,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock contains 300 mg in\
    \ its listed 1000 ml water and provider 1000 ml stock basis: 300 mg * 0.001 g/mg\
    \ / 1 L = 0.3 g/L stock. This existing number is not a neat main-medium dose.\
    \ Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives\
    \ transferred grams, without assuming measured final volume.\"\n  },\n  {\n  \
    \  \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"ingredient\"\
    : \"CoCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 200,\n\
    \      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.2,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: CoCl2 x 6 H2O\"\
    ,\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 200.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 200,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.54037,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 200 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 200 mg * 0.001 g/mg / 1 L =\
    \ 0.2 g/L stock. This existing number is not a neat main-medium dose. Preserve\
    \ the complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[13].concentration\",\n    \"ingredient\"\
    : \"CuCl2 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.01\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 10,\n\
    \      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.01,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: CuCl2 x 2 H2O\"\
    ,\n        \"exact_source_quote\": \"CuCl2 x 2 H2O 10.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0586569,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n     \
    \ }\n    ],\n    \"explanation\": \"The source stock contains 10 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 10 mg * 0.001 g/mg / 1 L = 0.01\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[14].concentration\",\n    \"ingredient\"\
    : \"NiCl2 x 6 H2O\",\n    \"stored\": {\n      \"value\": \"0.02\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 20,\n\
    \      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.02,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: NiCl2 x 6 H2O\"\
    ,\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 20.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.154322,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 20 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[15].concentration\",\n    \"ingredient\"\
    : \"Na2MoO4 x 2 H2O\",\n    \"stored\": {\n      \"value\": \"0.9\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 900,\n\
    \      \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.9,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: Na2MoO4 x 2\
    \ H2O\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 900.0 mg\",\n    \
    \    \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 900,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.9,\\n \
    \                       \\\"mmol_l\\\": 3.71978,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock contains 900 mg in\
    \ its listed 1000 ml water and provider 1000 ml stock basis: 900 mg * 0.001 g/mg\
    \ / 1 L = 0.9 g/L stock. This existing number is not a neat main-medium dose.\
    \ Preserve the complete stock and its 1 ml addition; stock g/L * 0.001 L gives\
    \ transferred grams, without assuming measured final volume.\"\n  },\n  {\n  \
    \  \"decision\": \"correct\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[16].concentration\",\n    \"ingredient\"\
    : \"Na2SeO3\",\n    \"stored\": {\n      \"value\": \"0.02\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"proposed\": {\n      \"original_amount\": 20,\n \
    \     \"original_unit\": \"mg\",\n      \"stock_g_per_L\": 0.02,\n      \"stock_provider_volume_ml\"\
    : 1000,\n      \"stock_addition_ml_per_source_batch\": 1\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: Na2SeO3\",\n\
    \        \"exact_source_quote\": \"Na2SeO3 20.0 mg\",\n        \"snapshot_sha256\"\
    : \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\",\n    \
    \    \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2SeO3\\\",\\n                        \\\"compound_id\\\":\
    \ 699,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n \
    \                       \\\"mmol_l\\\": 0.115648,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock contains 20 mg in its listed\
    \ 1000 ml water and provider 1000 ml stock basis: 20 mg * 0.001 g/mg / 1 L = 0.02\
    \ g/L stock. This existing number is not a neat main-medium dose. Preserve the\
    \ complete stock and its 1 ml addition; stock g/L * 0.001 L gives transferred\
    \ grams, without assuming measured final volume.\"\n  },\n  {\n    \"decision\"\
    : \"add\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"solutions\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"TS2 addition\",\n    \"proposed\": {\n      \"amount\": 1,\n      \"unit\"\
    : \"ml\",\n      \"scope\": \"Main source batch addition\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 main recipe: Trace element solution TS2\",\n      \
    \  \"exact_source_quote\": \"Trace element solution TS2 1.0 ml\",\n        \"\
    snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace element solution TS2\\\",\\n                        \\\
    \"solution_id\\\": 1648,\\n                        \\\"amount\\\": 1,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this missing stage-specific\
    \ source quantity. TS2 stock water is not a second litre of main-medium solvent.\"\
    \n  },\n  {\n    \"decision\": \"add\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"solutions\",\n    \"stored\": null,\n    \"ingredient\"\
    : \"TS2 stock water\",\n    \"proposed\": {\n      \"amount\": 1000,\n      \"\
    unit\": \"ml\",\n      \"scope\": \"Stock preparation only\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz811\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\",\n        \"\
    source_locator\": \"Page 1 Trace element solution TS2 subsection: Distilled water\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.0 ml\",\n        \"\
    snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      },\n      {\n        \"source_key\": \"mediadive811api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/811\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"17bc00aaac65da4c7bbb9d7169e8340a8445c599b16d9ab92632cb81a24b4e9a\"\
    \n      }\n    ],\n    \"explanation\": \"Restore this missing stage-specific\
    \ source quantity. TS2 stock water is not a second litre of main-medium solvent.\"\
    \n  },\n  {\n    \"decision\": \"evidence_only\",\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"stored\": 7.5,\n    \"ingredient\"\
    : \"Target pH\",\n    \"proposed\": 7.5,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz811\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 final preparation line\",\n        \"\
    exact_source_quote\": \"pH 7.5\",\n        \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      }\n    ],\n    \"explanation\": \"The target pH and existing second preparation\
    \ step agree with the source. Attach narrow evidence; do not reinterpret the schema\
    \ target-pH slot as a measured final pH.\"\n  },\n  {\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_input\": \"data/normalized_yaml/bacterial/activated_carbon_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0].description\",\n    \"stored\":\
    \ \"Befor autoclaving add trace element solution to the medium. Dissolve first\
    \ all ingredients then add activated carbon. Finally autoclave.\",\n    \"ingredient\"\
    : \"Existing order of TS2 addition, dissolution, carbon and sterilization\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz811\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium811.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Befor autoclaving add trace element solution to the medium. Dissolve first\
    \ all ingredients \\nthen add activated carbon. Finally autoclave.\",\n      \
    \  \"snapshot_sha256\": \"d6414174670559e90487dc3e2c755c55554b521ed3a06c5c5746774375671927\"\
    ,\n        \"parsed_text_sha256\": \"99c862298bb32fd328f4050c436fc7acd6a135a8ba5abc961b24a51a72233643\"\
    \n      }\n    ],\n    \"explanation\": \"Existing preparation retains the source\
    \ order; attach its exact scope. The source supplies no numeric sterilization\
    \ duration or temperature, and none is proposed.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Identifier metadata, exact secondary keys and supplied-form scope
  outcome: concern
  summary: 16 distinct primary/current-secondary identifiers resolve. 0 label instances
    differ from current canonical labels; 0 asserted current secondary keys lack an
    exact pinned index row. Legacy numeric links are assessed separately and are not
    established by CHEBI correspondence. Target linkage is 16/17 primary and 16/17
    secondary ingredient instances; this measures presence, not source validity.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi2509
  - chebi31206
  - chebi31604
  - chebi31795
  - chebi32312
  - chebi33118
  - chebi34683
  - chebi34887
  - chebi48843
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi86158
  - chebi86318
  - chebi86368
  details: '{"label_drift": [], "missing_secondary_keys": [], "legacy_instances":
    [], "coverage_scale": "0–100 percent; each ingredient instance counted once",
    "denominator": 17, "primary_percent": 94.11764705882354, "secondary_percent":
    94.11764705882354}'
- assessment_id: forms
  area: grounding
  topic: Every asserted primary and secondary chemical form
  outcome: concern
  summary: The explicitly sourced Na2HPO4·12H2O maps to CHEBI:34683 (HO4P.2Na without
    waters), and NiCl2·6H2O maps to CHEBI:34887 (Cl2Ni without waters). Other explicitly
    stated hydrates match their source forms. Ferric ammonium citrate resolves as
    an indefinite mixture, not a molecule with a fixed formula; water identity does
    not encode double-distillation grade. Activated carbon remains ungrounded rather
    than receiving an invented pure-carbon or grade identity.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - dsmz811
  - mim
  - chebi15377
  - chebi2509
  - chebi31206
  - chebi31604
  - chebi31795
  - chebi32312
  - chebi33118
  - chebi34683
  - chebi34887
  - chebi48843
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi86158
  - chebi86318
  - chebi86368
- assessment_id: classification
  area: scope
  topic: Solid state versus defined-composition claim
  outcome: concern
  summary: 'SOLID_AGAR is supported by the explicit 15 g agar row. However, composition_type=DEFINED
    and medium_type=DEFINED assert more than the supplied forms establish: CHEBI agar
    is a complex polysaccharide mixture, ferric ammonium citrate has indefinite composition,
    and the source supplies no activated-carbon grade specification. Provider complex_medium=no
    does not override the local chemical-definition contract. No replacement classification
    is guessed from missing product details.'
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - record
  - owner-0
  - dsmz811
  - mediadive811api
  - classification-schema
  - chebi2509
  - chebi31604
- assessment_id: preparation
  area: completeness
  topic: Complete target and owner preparation and evidence
  outcome: concern
  summary: Both layers retain the same correct source order and pH; no missing temperature/time
    is filled from convention. The full main source and TS2 stock are available, but
    stock nodes/additions and concentration evidence are absent. General microbial-cultivation
    application is not strain-specific growth evidence; no organism growth claims
    are promoted.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - record
  - owner-0
  - dsmz811
  - quantity-inventory
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001956
  evidence_ids:
  - record
  - history-metadata
  - owner-0
findings:
- finding_id: f1
  issue_key: CM001956-ts2-stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: TS2 stock strengths are presented as direct medium amounts
  description: Eight source milligram quantities belong to the 1000 ml TS2 stock,
    which is added at 1 ml per listed main batch. Both local layers instead place
    its full g/L strengths in direct ingredients and omit the stock dose.
  target_ids:
  - CultureMech:001956
  field_paths:
  - ingredients[9:17].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz811
  - mediadive811api
  - solution1648
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  issue_key: CM001956-water-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: A source solvent volume is encoded as mass concentration
  description: The source Bidistillated water 1000.0 ml and provider Double distilled
    water amount 1000, unit ml became 1000 G_PER_L. No density or final-volume evidence
    supports that conversion.
  target_ids:
  - CultureMech:001956
  field_paths:
  - ingredients[8].concentration
  evidence_ids:
  - record
  - owner-0
  - dsmz811
  - mediadive811api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  issue_key: CM001956-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two explicit hydrates are linked to structures without waters
  description: Phosphate dodecahydrate and nickel chloride hexahydrate are sourced
    explicitly, while their primary and secondary IDs encode anhydrous structures.
    Canonical label passes do not establish correct supplied forms.
  target_ids:
  - CultureMech:001956
  field_paths:
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  - ingredients[14].term
  - ingredients[14].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz811
  - chebi34683
  - chebi34887
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  issue_key: CM001956-defined-mixtures
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Fully defined classification overstates known mixture composition
  description: The record asserts both defined classifications despite explicit agar
    and ferric ammonium citrate mixture identities and unspecified activated-carbon
    grade. The provider flag complex_medium=no does not establish exact component
    composition under the local enum contract.
  target_ids:
  - CultureMech:001956
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - classification-schema
  - chebi2509
  - chebi31604
  - dsmz811
  - mediadive811api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  issue_key: CM001956-amount-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Source-supported amounts and preparation lack attached evidence
  description: All 34 local ingredient concentrations lack attached evidence; source-supported
    main values and current preparation therefore remain evidence_only, while wrong
    units and stock scopes require correction.
  target_ids:
  - CultureMech:001956
  field_paths:
  - ingredients[*].evidence
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  - dsmz811
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  description: Restore the complete TS2 stock and exact 1 ml addition in the maintained
    owner, preserve original milligram and volume bases, and regenerate the target
    after review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  description: Represent the exact main solvent volume and grade in preparation or
    an appropriate supported volume field; do not invent water mass or final-volume
    evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  description: Verify exact hydrate identifiers before correcting both maintained
    primary and secondary links; preserve the source-supplied amounts and do not substitute
    guessed IDs.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  description: Reconcile the maintained composition classification with supplied-form
    evidence and keep its legacy medium_type derivation consistent; record uncertainty
    instead of inventing a product specification.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
  description: Attach exact source snippets and locators to retained or corrected
    claims in the maintained owner; ensure narrow evidence survives regeneration without
    implying chemical-form correctness from numerical agreement.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/activated_carbon_medium.yaml
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
- No source-specified carbon grade, exact mixture composition, sterilization temperature/time,
  density or independently measured final volume is inferred. Source pH is a target
  value. The two 1000 ml water rows and 1 ml stock addition retain separate stages
  and are not silently combined into an assumed final litre.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-019
- generated-medium
```
