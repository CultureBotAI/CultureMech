# Source and formulation review: acidithiobacillus_caldus_medium (CultureMech:000981)

- Review: 20261021T112631Z-culturemech-000981-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T11:17:45Z
- Finished UTC: 2026-10-21T11:26:31Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSMZ 150a source distinguishes its basal recipe from a separately added trace stock, but both local contributors and the generated target flatten stock-strength solutes into receiving-medium concentrations. KOMODO 150.1 catalog metadata points to DSMZ 150 rather than the later local 150a parent; exact variant content is unavailable. Chemical-form and evidence gaps remain, so this source-identity review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 173; batch 018 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding seventeen task batches contain 170 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 172 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000981 | data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml | generated | acidithiobacillus_caldus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000981 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000981 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/173/strict.tsv |
| validate-terms | passed | True | CultureMech:000981 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000981 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000981 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo150_1 | unavailable | True | CultureMech:000981 | Exact KOMODO150.1 detail returned HTTP403. The table resolves the accession, DSM18786 label, pH0.8 and linked DSMZ150 metadata, but does not supply the variant formulation. The local13-row150a composition and later PH_VARIANT repair therefore lack exact source-identity confirmation; no substitution of150 or150a is inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000981.

The four documented recipes completed; interpret the scope of each separately.

### Distinct accessions and maintained relationship topology

identity: concern. Targets: CultureMech:000981.

The target names DSMZ150a and resolves to two exact normalized owners. Their local paths and IDs exist, but the generated target retains the old reverse SOURCE_DUPLICATE parent while the September owner repair establishes reciprocal PH_VARIANT links under150a. KOMODO150.1 still links DSMZ150 in the captured source catalog and owner notes/history. Identical13-row local arrays do not establish equivalent formulations or justify a pH-only relationship.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000981.

65 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "input": "target",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "2.9703",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 3,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact (NH4)2SO4 row",
        "exact_source_quote": "(NH4)2SO4 3.00 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\": 22.4784,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "3 g /1.010 L = 2.97029703 g/L, rounded by provider to 2.9703. The declared volume is not an independently measured final volume."
  },
  {
    "input": "target",
    "field_path": "ingredients[1].concentration",
    "ingredient": "K2HPO4 x 3 H2O",
    "existing": {
      "value": "0.49505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact K2HPO4 x 3 H2O row",
        "exact_source_quote": "K2HPO4 x 3 H2O 0.50 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.84224,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505. The declared volume is not an independently measured final volume."
  },
  {
    "input": "target",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.49505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact MgSO4 x 7 H2O row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.00851,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505. The declared volume is not an independently measured final volume."
  },
  {
    "input": "target",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.0990099",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.1,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact KCl row",
        "exact_source_quote": "KCl 0.10 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0990099,\n                        \"mmol_l\": 1.3281,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.1 g /1.010 L = 0.099009901 g/L, rounded by provider to 0.0990099. The declared volume is not an independently measured final volume."
  },
  {
    "input": "target",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.019802",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.02,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact Ca(NO3)2 x 4 H2O row",
        "exact_source_quote": "Ca(NO3)2 x 4 H2O 0.02 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.019802,\n                        \"mmol_l\": 0.0838538,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.02 g /1.010 L = 0.0198019802 g/L, rounded by provider to 0.019802. The declared volume is not an independently measured final volume."
  },
  {
    "input": "target",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Sulfur",
    "existing": {
      "value": "4.9505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact Sulfur row",
        "exact_source_quote": "Sulfur (powdered) 5.00 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9505,\n                        \"mmol_l\": 154.365,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "5 g /1.010 L = 4.95049505 g/L, rounded by provider to 4.9505. The declared volume is not an independently measured final volume."
  },
  {
    "input": "target",
    "field_path": "ingredients[6].concentration",
    "ingredient": "FeCl3 x 6 H2O",
    "existing": {
      "value": "1.1",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 1.1,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact FeCl3 x 6 H2O row",
        "exact_source_quote": "FeCl3 x 6 H2O 1.10 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 1.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\": 4.06961,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 1.1 g/L stock ×0.010 L /1.010 L = 0.0108910891 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "target",
    "field_path": "ingredients[7].concentration",
    "ingredient": "CuSO4 x 5 H2O",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact CuSO4 x 5 H2O row",
        "exact_source_quote": "CuSO4 x 5 H2O 0.05 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.200252,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.05 g/L stock ×0.010 L /1.010 L = 0.000495049505 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "target",
    "field_path": "ingredients[8].concentration",
    "ingredient": "H3BO3",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact H3BO3 row",
        "exact_source_quote": "H3BO3 0.20 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 3.23415,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "target",
    "field_path": "ingredients[9].concentration",
    "ingredient": "MnSO4 x H2O",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact MnSO4 x H2O row",
        "exact_source_quote": "MnSO4 x H2O 0.20 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.18332,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "target",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "existing": {
      "value": "0.08",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.08,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact Na2MoO4 x 2 H2O row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.08 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.08,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.330647,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.08 g/L stock ×0.010 L /1.010 L = 0.000792079208 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "target",
    "field_path": "ingredients[11].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "existing": {
      "value": "0.06",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.06,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact CoCl2 x 6 H2O row",
        "exact_source_quote": "CoCl2 x 6 H2O 0.06 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.462111,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.06 g/L stock ×0.010 L /1.010 L = 0.000594059406 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "target",
    "field_path": "ingredients[12].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "existing": {
      "value": "0.09",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.09,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact ZnSO4 x 7 H2O row",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.09 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.09,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.09,\n                        \"mmol_l\": 0.312977,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.09 g/L stock ×0.010 L /1.010 L = 0.000891089109 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "2.9703",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 3,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact (NH4)2SO4 row",
        "exact_source_quote": "(NH4)2SO4 3.00 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\": 22.4784,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "3 g /1.010 L = 2.97029703 g/L, rounded by provider to 2.9703. The declared volume is not an independently measured final volume."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "K2HPO4 x 3 H2O",
    "existing": {
      "value": "0.49505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact K2HPO4 x 3 H2O row",
        "exact_source_quote": "K2HPO4 x 3 H2O 0.50 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.84224,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505. The declared volume is not an independently measured final volume."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.49505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact MgSO4 x 7 H2O row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.00851,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505. The declared volume is not an independently measured final volume."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.0990099",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.1,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact KCl row",
        "exact_source_quote": "KCl 0.10 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0990099,\n                        \"mmol_l\": 1.3281,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.1 g /1.010 L = 0.099009901 g/L, rounded by provider to 0.0990099. The declared volume is not an independently measured final volume."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.019802",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.02,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact Ca(NO3)2 x 4 H2O row",
        "exact_source_quote": "Ca(NO3)2 x 4 H2O 0.02 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.019802,\n                        \"mmol_l\": 0.0838538,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "0.02 g /1.010 L = 0.0198019802 g/L, rounded by provider to 0.019802. The declared volume is not an independently measured final volume."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Sulfur",
    "existing": {
      "value": "4.9505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact Sulfur row",
        "exact_source_quote": "Sulfur (powdered) 5.00 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9505,\n                        \"mmol_l\": 154.365,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "evidence_only",
    "proposed": "Retain the provider-declared basal value with exact source evidence and an explicit1010 ml calculation basis; assess hydrate/material identity separately.",
    "calculation": "5 g /1.010 L = 4.95049505 g/L, rounded by provider to 4.9505. The declared volume is not an independently measured final volume."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "FeCl3 x 6 H2O",
    "existing": {
      "value": "1.1",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 1.1,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact FeCl3 x 6 H2O row",
        "exact_source_quote": "FeCl3 x 6 H2O 1.10 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 1.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\": 4.06961,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 1.1 g/L stock ×0.010 L /1.010 L = 0.0108910891 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "CuSO4 x 5 H2O",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact CuSO4 x 5 H2O row",
        "exact_source_quote": "CuSO4 x 5 H2O 0.05 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.200252,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.05 g/L stock ×0.010 L /1.010 L = 0.000495049505 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[8].concentration",
    "ingredient": "H3BO3",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact H3BO3 row",
        "exact_source_quote": "H3BO3 0.20 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 3.23415,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[9].concentration",
    "ingredient": "MnSO4 x H2O",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact MnSO4 x H2O row",
        "exact_source_quote": "MnSO4 x H2O 0.20 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.18332,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "existing": {
      "value": "0.08",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.08,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact Na2MoO4 x 2 H2O row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.08 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.08,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.330647,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.08 g/L stock ×0.010 L /1.010 L = 0.000792079208 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[11].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "existing": {
      "value": "0.06",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.06,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact CoCl2 x 6 H2O row",
        "exact_source_quote": "CoCl2 x 6 H2O 0.06 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.462111,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.06 g/L stock ×0.010 L /1.010 L = 0.000594059406 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ingredients[12].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "existing": {
      "value": "0.09",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.09,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact ZnSO4 x 7 H2O row",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.09 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.09,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.09,\n                        \"mmol_l\": 0.312977,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ],
    "decision": "correct",
    "proposed": "Move this value to the exact trace-stock composition and represent its10 ml addition separately; do not retain undiluted stock strength as a root concentration.",
    "calculation": "On the provider-declared bases only: 0.09 g/L stock ×0.010 L /1.010 L = 0.000891089109 g/L. This arithmetic illustrates stage error, not an unqualified measured final concentration."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[0].concentration",
    "ingredient": "(NH4)2SO4",
    "existing": {
      "value": "2.9703",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 3,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact (NH4)2SO4 row",
        "exact_source_quote": "(NH4)2SO4 3.00 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.9703,\n                        \"mmol_l\": 22.4784,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[1].concentration",
    "ingredient": "K2HPO4 x 3 H2O",
    "existing": {
      "value": "0.49505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact K2HPO4 x 3 H2O row",
        "exact_source_quote": "K2HPO4 x 3 H2O 0.50 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.84224,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[2].concentration",
    "ingredient": "MgSO4 x 7 H2O",
    "existing": {
      "value": "0.49505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact MgSO4 x 7 H2O row",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.00851,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[3].concentration",
    "ingredient": "KCl",
    "existing": {
      "value": "0.0990099",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.1,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact KCl row",
        "exact_source_quote": "KCl 0.10 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0990099,\n                        \"mmol_l\": 1.3281,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[4].concentration",
    "ingredient": "Ca(NO3)2 x 4 H2O",
    "existing": {
      "value": "0.019802",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 0.02,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact Ca(NO3)2 x 4 H2O row",
        "exact_source_quote": "Ca(NO3)2 x 4 H2O 0.02 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.019802,\n                        \"mmol_l\": 0.0838538,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[5].concentration",
    "ingredient": "Sulfur",
    "existing": {
      "value": "4.9505",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a main recipe",
    "source_amount": {
      "value": 5,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, main table, exact Sulfur row",
        "exact_source_quote": "Sulfur (powdered) 5.00 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"condition\": \"\",\n                        \"attribute\": \"powdered\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9505,\n                        \"mmol_l\": 154.365,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[6].concentration",
    "ingredient": "FeCl3 x 6 H2O",
    "existing": {
      "value": "1.1",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 1.1,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact FeCl3 x 6 H2O row",
        "exact_source_quote": "FeCl3 x 6 H2O 1.10 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 1.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1,\n                        \"mmol_l\": 4.06961,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[7].concentration",
    "ingredient": "CuSO4 x 5 H2O",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.05,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact CuSO4 x 5 H2O row",
        "exact_source_quote": "CuSO4 x 5 H2O 0.05 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.200252,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[8].concentration",
    "ingredient": "H3BO3",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact H3BO3 row",
        "exact_source_quote": "H3BO3 0.20 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 3.23415,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[9].concentration",
    "ingredient": "MnSO4 x H2O",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.2,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact MnSO4 x H2O row",
        "exact_source_quote": "MnSO4 x H2O 0.20 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.18332,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[10].concentration",
    "ingredient": "Na2MoO4 x 2 H2O",
    "existing": {
      "value": "0.08",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.08,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact Na2MoO4 x 2 H2O row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.08 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.08,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.330647,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[11].concentration",
    "ingredient": "CoCl2 x 6 H2O",
    "existing": {
      "value": "0.06",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.06,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact CoCl2 x 6 H2O row",
        "exact_source_quote": "CoCl2 x 6 H2O 0.06 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.462111,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ingredients[12].concentration",
    "ingredient": "ZnSO4 x 7 H2O",
    "existing": {
      "value": "0.09",
      "unit": "G_PER_L"
    },
    "source_stage": "DSMZ150a trace-stock composition before10 ml addition",
    "source_amount": {
      "value": 0.09,
      "unit": "g"
    },
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1, Trace element solution table, exact ZnSO4 x 7 H2O row",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.09 g",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.09,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.09,\n                        \"mmol_l\": 0.312977,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      },
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row: DSMZ150 link and pH metadata only",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ],
    "decision": "unsupported",
    "proposed": "Resolve the exact KOMODO150.1 formulation before endorsing or changing this copied quantity; neither150a nor150 is silently substituted.",
    "explanation": "The local value equals a150a provider stage value, but the exact catalog links150 and the variant detail is inaccessible. Numeric correspondence is not evidence for this variant. If150a identity is later established, stock-stage flattening must still be corrected."
  },
  {
    "input": "target and DSMZ150a owner only; variant identity unresolved",
    "field_path": "solutions / preparation_steps (missing Trace element solution)",
    "ingredient": "Trace element solution",
    "decision": "add",
    "source_amount": {
      "value": 10,
      "unit": "ml"
    },
    "source_stage": "Main recipe; trace stock is added after autoclaving",
    "proposed": "Preserve original batch/stock amount and exact addition stage; do not infer additional doses for KOMODO150.1.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 main table, exact Trace element solution row",
        "exact_source_quote": "Trace element solution 10.00 ml",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 266,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ]
  },
  {
    "input": "target and DSMZ150a owner only; variant identity unresolved",
    "field_path": "solutions / preparation_steps (missing Main distilled water)",
    "ingredient": "Main distilled water",
    "decision": "add",
    "source_amount": {
      "value": 1000,
      "unit": "ml"
    },
    "source_stage": "Main recipe; trace stock is added after autoclaving",
    "proposed": "Preserve original batch/stock amount and exact addition stage; do not infer additional doses for KOMODO150.1.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 main table, exact Main distilled water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ]
  },
  {
    "input": "target and DSMZ150a owner only; variant identity unresolved",
    "field_path": "solutions / preparation_steps (missing Trace-stock distilled water)",
    "ingredient": "Trace-stock distilled water",
    "decision": "add",
    "source_amount": {
      "value": 1000,
      "unit": "ml"
    },
    "source_stage": "Trace stock before use",
    "proposed": "Preserve original batch/stock amount and exact addition stage; do not infer additional doses for KOMODO150.1.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 Trace element solution table, exact Trace-stock distilled water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      },
      {
        "source_key": "mediadive150aapi",
        "source_url": "https://mediadive.dsmz.de/rest/medium/150a",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "ph_value",
    "existing": 2.5,
    "decision": "evidence_only",
    "source_stage": "DSMZ150a initial adjustment before dispensing/autoclaving",
    "proposed": "Retain the separately supported pH metadata and source scope; do not infer a shared formulation or measured final pH.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 preparation paragraph",
        "exact_source_quote": "Adjust pH with 6 N H2SO4 to 2.5,",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "ph_value",
    "existing": 2.5,
    "decision": "evidence_only",
    "source_stage": "DSMZ150a initial adjustment before dispensing/autoclaving",
    "proposed": "Retain the separately supported pH metadata and source scope; do not infer a shared formulation or measured final pH.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 preparation paragraph",
        "exact_source_quote": "Adjust pH with 6 N H2SO4 to 2.5,",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "field_path": "ph_value",
    "existing": 0.8,
    "decision": "evidence_only",
    "source_stage": "Exact KOMODO150.1 metadata only",
    "proposed": "Retain the separately supported pH metadata and source scope; do not infer a shared formulation or measured final pH.",
    "source_snippets": [
      {
        "source_key": "komodoMediaList",
        "source_url": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
        "source_locator": "Exact150.1 row, pH column",
        "exact_source_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1' &gt;150.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 18786&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 0.8&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;",
        "snapshot_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "preparation_steps[0] (acid strength)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve explicit6 N strength; do not equate normality with molarity.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 initial adjustment",
        "exact_source_quote": "6 N H2SO4",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "preparation_steps[0] (acid dose)",
    "decision": "not_quantified",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "No fixed acid addition volume is supplied; preserve titration context.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 initial adjustment",
        "exact_source_quote": "Adjust pH with 6 N H2SO4 to 2.5,",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "preparation_steps[0] (sulfur heating duration)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve3 hours for sulfur only; do not use it as an autoclave duration.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "heat for 3 hours to 90 - 100°C",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "preparation_steps[0] (sulfur temperature range)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve90–100 C range for sulfur only.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "heat for 3 hours to 90 - 100°C",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "preparation_steps[0] (sulfur repeated days)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve the repetition across three days; do not collapse to a single continuous cycle.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "on each of three successive days.",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "target",
    "field_path": "preparation_steps[0] (sulfur wetting water)",
    "decision": "not_quantified",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Retain the nonnumeric few-drops wording; no exact volume is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "wet with a few drops of\nwater",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "preparation_steps[0] (acid strength)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve explicit6 N strength; do not equate normality with molarity.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 initial adjustment",
        "exact_source_quote": "6 N H2SO4",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "preparation_steps[0] (acid dose)",
    "decision": "not_quantified",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "No fixed acid addition volume is supplied; preserve titration context.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 initial adjustment",
        "exact_source_quote": "Adjust pH with 6 N H2SO4 to 2.5,",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "preparation_steps[0] (sulfur heating duration)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve3 hours for sulfur only; do not use it as an autoclave duration.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "heat for 3 hours to 90 - 100°C",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "preparation_steps[0] (sulfur temperature range)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve90–100 C range for sulfur only.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "heat for 3 hours to 90 - 100°C",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "preparation_steps[0] (sulfur repeated days)",
    "decision": "evidence_only",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Preserve the repetition across three days; do not collapse to a single continuous cycle.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "on each of three successive days.",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "field_path": "preparation_steps[0] (sulfur wetting water)",
    "decision": "not_quantified",
    "source_stage": "DSMZ150a acid/base or sulfur preparation, as explicitly named",
    "proposed": "Retain the nonnumeric few-drops wording; no exact volume is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz150a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf",
        "source_locator": "PDF p.1 sulfur preparation",
        "exact_source_quote": "wet with a few drops of\nwater",
        "snapshot_sha256": "a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973",
        "parsed_text_sha256": "ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0"
      }
    ]
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[0].concentration",
    "existing": {
      "value": "1.1",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.1,\n                \"unit\": \"g\",\n                \"g_l\": 1.1,\n                \"mmol_l\": 4.06961,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[1].concentration",
    "existing": {
      "value": "0.05",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"CuSO4 x 5 H2O\",\n                \"compound_id\": 121,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.05,\n                \"unit\": \"g\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.200252,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[2].concentration",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 3.23415,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[3].concentration",
    "existing": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnSO4 x H2O\",\n                \"compound_id\": 14,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.18332,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[4].concentration",
    "existing": {
      "value": "0.08",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.08,\n                \"unit\": \"g\",\n                \"g_l\": 0.08,\n                \"mmol_l\": 0.330647,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[5].concentration",
    "existing": {
      "value": "0.06",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.06,\n                \"unit\": \"g\",\n                \"g_l\": 0.06,\n                \"mmol_l\": 0.462111,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[6].concentration",
    "existing": {
      "value": "0.09",
      "unit": "G_PER_L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\": 35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.09,\n                \"unit\": \"g\",\n                \"g_l\": 0.09,\n                \"mmol_l\": 0.312977,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  },
  {
    "input": "data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml (dependency context only)",
    "field_path": "composition[7].concentration",
    "existing": {
      "value": "1",
      "unit": "L"
    },
    "decision": "verified",
    "source_stage": "Exact standalone stock266 only; no evidence inheritance into receiving-medium layers",
    "source_snippets": [
      {
        "source_key": "solution266",
        "source_url": "https://mediadive.dsmz.de/rest/solution/266",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef"
      }
    ],
    "explanation": "Existing value, unit, stock basis and attached evidence match. Water1000 ml equals1 L as a source batch addition; other values are source-declared stock g/L. This does not endorse copied values in the target."
  }
]

### Identifier metadata, exact secondary keys and supplied-form scope

grounding: concern. Targets: CultureMech:000981.

13 distinct primary/current-secondary identifiers resolve. 0 label instances differ from current canonical labels; 1 asserted current secondary keys lack an exact pinned index row. Legacy numeric links are assessed separately and are not established by CHEBI correspondence. Target linkage is 13/13 primary and 13/13 secondary ingredient instances; this measures presence, not source validity.

{"label_drift": [], "missing_secondary_keys": ["CHEBI:26833"], "legacy_instances": [], "coverage_scale": "0–100 percent; each ingredient instance counted once", "denominator": 13, "primary_percent": 100.0, "secondary_percent": 100.0}

### Source trihydrate, elemental sulfur and other supplied forms

grounding: concern. Targets: CultureMech:000981.

The primary and provider explicitly supply K2HPO4 trihydrate. CHEBI131527 has an anhydrous formula/structure; its related trihydrate synonym does not encode three waters. Sulfur powder is a bulk elemental material, while CHEBI26833 is broader atom-level grounding that does not capture the supplied powder context. This scope difference does not establish a wrong chemical identifier or a particular allotrope. Other named salts retain the source hydrates, including MnSO4 monohydrate rather than an unspecified hydrate. The exact stock compound IDs match the eight captured provider objects.

### Source preparation retained versus missing variant content

completeness: concern. Targets: CultureMech:000981.

Target and DSMZ150a owner retain the source acid adjustment, separate filter-sterilized trace addition and sulfur heating/aseptic layering, but omit the quantified stock addition and water organization. No basal autoclave temperature/duration is supplied. The KOMODO owner lacks preparation; source identity must be resolved before copying150a preparation into it.

### Physical state, defined composition and source metadata

scope: concern. Targets: CultureMech:000981.

DEFINED and LIQUID are consistent with the150a source’s specified salts, trace stock and sulfur suspension without an undefined organic extract or gelling agent. This categorical fit applies only to the150a base and does not repair wrong material forms or concentrations. The exact150.1 catalog also says Is Complex=true; the child’s DEFINED assertion therefore needs source-identity reconciliation rather than automatic inheritance from150a. The exact catalog records Is Aerobic=false for150.1; preserve it as catalog metadata, not independent physiological evidence. DSM18786 is a source label, not an inferred taxonomy or demonstration of growth on the locally copied150a formula.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:000981.

23 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

## Findings

### f1: Seven trace-stock concentrations are asserted as receiving-medium ingredients

blocker / open / confirmed; issue key: culturemech.000981.stock-strength-flattening.

Root ingredients6–12 equal the separately prepared1000 ml trace-stock strengths, although the main recipe adds only10 ml of that stock. The target and DSMZ150a owner have no explicit stock/dose structure or solvent basis. Six basal values use a different1010 ml provider denominator. The KOMODO copy shares the same flattened array, but its exact formulation identity must be resolved separately.

### f2: Generated source-duplicate and later pH-variant claims do not resolve the source mapping

blocker / open / confirmed; issue key: culturemech.000981.variant-source-identity.

The generated target merges KOMODO150.1 as a SOURCE_DUPLICATE and points backward to its DSM18786 wrapper. Current normalized links instead call it a pH-only variant of150a. However, the exact KOMODO catalog and owner source notes link DSMZ150, whose current primary is a materially different formulation. The inaccessible150.1 detail does not establish which formulation belongs to the variant. Local signature equality and ingredients_curated flags cannot resolve this discrepancy.

### f3: Phosphate hydration is mismatched and sulfur powder context is unrepresented

major / open / confirmed; issue key: culturemech.000981.source-material-grounding.

K2HPO4 x3H2O is mapped to an anhydrous dipotassium hydrogen phosphate structure; the OLS related synonym is not structural hydrate support. Separately, CHEBI26833 provides broad atom-level sulfur grounding while the source specifies powder. The powder context needs preservation, but no wrong sulfur identifier or particular allotrope is established. Valid identifiers and labels alone do not resolve the phosphate hydrate mismatch.

### f4: Supported basal quantities and preparation lack attached claim evidence

minor / open / confirmed; issue key: culturemech.000981.claim-provenance-gap.

The source supports the150a basal values on the declared provider basis and the retained preparation statements, but no corresponding target/owner evidence is attached. Existing stock266 evidence is valid only for its own eight composition rows. The child’s missing variant evidence is a separate required limitation.

### f5: Asserted sulfur secondary key is absent from the pinned MIM index

minor / open / confirmed; issue key: culturemech.000981.secondary-index-gap.

CHEBI26833 resolves as a primary ontology ID, but its exact identifier has no row anywhere in the current pinned MIM label index. This confirmed secondary mapping gap is distinct from the missing source powder context and is not evidence of a nonexistent or chemically wrong CHEBI term.

### f6: KOMODO history contains malformed and timezone-unspecified timestamps

minor / open / confirmed; issue key: culturemech.000981.historical-timestamp-shape.

The child preserves2026-01-27T01:15:02.fZ and a timezone-naive enrichment timestamp. The target and DSMZ owner retain valid timezone-aware history. The true historical fraction/timezone were not recovered.

## Recommended Actions And Acceptance Checks

### a1

Represent stock266 composition and its exact10 ml addition separately in the maintained150a record; retain provider-declared versus source-batch bases and preserve existing standalone stock evidence. Resolve the variant before propagating any correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Keep source-specific records distinct, recover exact variant evidence and reconcile150 versus150a before selecting relationship type or merged membership. Preserve historical events and do not silently substitute the catalog-linked recipe.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Reconcile the explicit phosphate trihydrate with supported structural grounding, and preserve the source sulfur powder context separately. Do not infer a sulfur replacement identifier or allotrope, or use an anhydrous molecular weight for the trihydrate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact150a claim snippets, stock boundaries and calculation bases without treating dependency evidence as inherited. Preserve the original stock evidence and unresolved variant scope.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Resolve the exact secondary mapping independently; preserve valid primary provenance and do not guess a replacement MIM identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve old history and append a bounded clarification when authorized; do not fabricate a corrected historical time or retroactively authenticate the enrichment source.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/for_dsm_18786.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch018/173/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch018/173/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml:1:id: CultureMech:000981<br>./data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml:1:id: CultureMech:000981<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch018/source-preflight-bound/173/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 20 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf; PDF page1, entire main recipe, preparation and trace-element table | supports | Exact DSMZ150a source preserves 1000 ml main water, a 10 ml trace-stock addition, 1000 ml stock water, supplied hydrates and source-specific acid/sulfur preparation. No autoclave temperature/time is supplied. |
| provider | https://mediadive.dsmz.de/rest/medium/150a; $.data.medium and $.data.solutions[0:2], IDs265/266 | supports | Provider separates the main solution (declared1010 ml) from the trace stock (1000 ml). Its basal g_l values and stock g_l values have different stage denominators; neither is a measured final volume. |
| source150 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf; PDF page1 heading, full main table and preparation; identity comparison only | supports | The exact catalog-linked DSMZ150 is ACIDIANUS BRIERLEYI MEDIUM with yeast extract and a different sulfur amount, not the DSMZ150a formulation. This source is used to expose the mapping discrepancy, not to replace150a or assert the unavailable variant recipe. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaInfo150.1 row; complete table header separately read | supports | The exact row supports For DSM18786, pH0.8 and a DSMZ150 URL. Is Aerobic=false supports imported catalog metadata only, not independently verified physiology. |
| komodo150_1-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1; Preserved exact public retrieval result | context_only | Exact KOMODO150.1 detail returned HTTP403. The table resolves the accession, DSM18786 label, pH0.8 and linked DSMZ150 metadata, but does not supply the variant formulation. The local13-row150a composition and later PH_VARIANT repair therefore lack exact source-identity confirmation; no substitution of150 or150a is inferred. |
| stock266 | https://mediadive.dsmz.de/rest/solution/266; $.data, all eight recipe rows and volume1000 | supports | Exact stock266 corresponds to the primary trace table. Its eight existing local evidence snippets match this captured response; they do not validate a receiving-medium root amount. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch018/173/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:26833 resolves to sulfur atom. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:32588 resolves to potassium chloride. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:33118 resolves to boric acid. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:62946 resolves to ammonium sulfate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86159 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86159 resolves to calcium nitrate tetrahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86254 resolves to iron trichloride hexahydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identity/label existence is separate from exact supplied form and source-specific ingredient support. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned index exact identifier lookup; adjacent source revision/hash | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "asserted_secondary_rows": {"CHEBI:131527": [{"label": "Dibasic potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium hydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium hydrogenorthophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium monohydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium orthophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Hydrogen dipotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K 2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO4(Sigma P 3786)", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, dipotassium salt", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dibasic phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium monohydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate (dibasic)", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate dibasic", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833": [], "CHEBI:31440": [{"label": "Copper (II) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper sulphate(5.H2O)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate (1:1) pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(2+) sulfate--water (1/5)", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "copper(II) sulfate, pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cupric sulfate pentahydrate", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO .5H O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 . 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 .5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 x 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 · 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4 ⋅ 5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4*5 H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4.5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4·5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CuSO4・5H2O", "match_type": "synonym", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": ".MgSO4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "bitter salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsom salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "epsomite", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate anhydrous", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Magnesium sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate heptahydrate", "match_type": "ontology_label", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "magnesium sulphate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium sulphate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "magnesium(II) sulfate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO .7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO 4 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2 x 7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO2·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H20", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O (100 mM)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O solution (25%)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7 H2O to 15.0 g).", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7 H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4 ·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO47H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO47H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4x7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·7H2O", "ontology_id": "CHEBI:31795", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MgSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O (Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(CAS: 10034-99-8)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4•7H2O(Sigma 230391)", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid magnesium salt heptahydrate", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of magnesia", "match_type": "synonym", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "zinc sulfate (1:1) heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zinc sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc sulfate heptahydrate (1:1:7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate heptahydrate", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "zinc(2+) sulfate--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Zn2SO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 . 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 .7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 x 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 · 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 × 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4 ⋅ 7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7 H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4*7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4-7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4.7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4·7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4∙7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4⋅7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4・7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ZnSO4･7H2O", "match_type": "synonym", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "[KCl]", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaliumchlorid", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kaon-Cl 10", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl (Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS: 7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(CAS:7447-40-7)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KCl(Fisher P 217)", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klor-con", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Klotrix", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Monopotassium chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "muriate of potash", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium Chloride", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sylvite", "match_type": "synonym", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "[B(OH)3]", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "B(OH)3", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Boric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "boron trihydroxide", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "H3BO3(Baker 0084)", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "orthoboric acid", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "trihydroxidoboron", "match_type": "synonym", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "cobalt (II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt chloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "cobalt chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cobalt(2+) dichloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Cobalt(II) chloride--water (1/7)", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 4 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "resolved:owned"}, {"label": "CoCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 x 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "CoCl2 x 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 · 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 × 6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2 ∙ 6 H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2·6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2∙6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2⋅6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "CoCl2・6H2O", "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id": "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2 SO4", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2S4", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2SO4(Fisher A 702)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ammonium Sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium sulfate (2:1)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "ammonium sulphate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diammonium sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "diazanium sulfate", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "mascagnite", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid ammonium salt (1:2)", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulfuric acid, diammonium salt", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sulphate of ammonia", "match_type": "synonym", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Disodium molybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Molybdic acid, disodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2 MoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2Mo4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 . 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 x 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4 ⋅ 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4*2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4*2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4-2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4. 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4.H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4xH2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4·2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO4⋅2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO4・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4·2H2O", "ontology_id": "CHEBI:75213", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "Na2MoO7 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7O4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoO7・2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2MoSO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 x 2 H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4 · 2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaMoO4.2H2O", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium dioxido(dioxo)molybdenum--water (1/2)", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Molybdate Dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium molybdate(VI) dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium orthomolybdate dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86159": [{"label": "(1)  Ca(NO3)2", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(1)  Ca(NO3)2.4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2 x 4 H2O (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2 · 4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2.4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2x4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2·4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2•4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2•4H2O(CAS: 13477-34-4)", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2・4H2O", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium dinitrate tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium nitrate tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "calcium nitrate--water (1/4)", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86254": [{"label": "FeCl3 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O (0.1% w/v in 0.2 N HCl)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O (0.5%)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O (w/v=1%)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O NaEDTA", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O solution (2%)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x6H2O", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3*6 H2O", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3.6H2O", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3·6H2O", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ferric chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron (III) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "iron trichloride hexahydrate", "match_type": "ontology_label", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "trichloroiron--water (1/6)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "Manganese (II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate hydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate--water (1/1)", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "ontology_label", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "manganese(II) sulphate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 · H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 ⋅ H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4.H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4·H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4⋅H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4・xH2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}]}, "missing_current_keys": ["CHEBI:26833"], "legacy_instances": []} |
| history-metadata | data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml; data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml; data/normalized_yaml/bacterial/for_dsm_18786.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:02.972737"}]}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main and referenced stocks; resolver strips alphabetic medium suffixes in its index; the later150.1 repair hard-codes the shared13-row signature and150a topology. These inspected mechanisms identify maintenance points but do not prove which historical execution produced a record or establish source equivalence. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main and referenced stocks; resolver strips alphabetic medium suffixes in its index; the later150.1 repair hard-codes the shared13-row signature and150a topology. These inspected mechanisms identify maintenance points but do not prove which historical execution produced a record or establish source equivalence. |
| writer-2 | scripts/repair_komodo_1501_acidithiobacillus_score10.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main and referenced stocks; resolver strips alphabetic medium suffixes in its index; the later150.1 repair hard-codes the shared13-row signature and150a topology. These inspected mechanisms identify maintenance points but do not prove which historical execution produced a record or establish source equivalence. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main and referenced stocks; resolver strips alphabetic medium suffixes in its index; the later150.1 repair hard-codes the shared13-row signature and150a topology. These inspected mechanisms identify maintenance points but do not prove which historical execution produced a record or establish source equivalence. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact KOMODO150.1 detail returned HTTP403. The table resolves the accession, DSM18786 label, pH0.8 and linked DSMZ150 metadata, but does not supply the variant formulation. The local13-row150a composition and later PH_VARIANT repair therefore lack exact source-identity confirmation; no substitution of150 or150a is inferred.
- The complete pinned MIM index was available and inspected: the asserted sulfur secondary key is confirmed absent. This mapping gap is distinct from live CHEBI validity and does not make that completed lookup unavailable. Partial completion is due to the inaccessible exact KOMODO150.1 formulation.
- Stock266 is source context only, not an additional reviewed target. DSMZ150 is identity comparison only. No organism growth, pressure, basal autoclave setting, fixed acid dose or measured final volume was inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112631Z-culturemech-000981-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidithiobacillus_caldus_medium (CultureMech:000981)'
started_at: '2026-10-21T11:17:45Z'
finished_at: '2026-10-21T11:26:31Z'
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
summary: The DSMZ 150a source distinguishes its basal recipe from a separately added
  trace stock, but both local contributors and the generated target flatten stock-strength
  solutes into receiving-medium concentrations. KOMODO 150.1 catalog metadata points
  to DSMZ 150 rather than the later local 150a parent; exact variant content is unavailable.
  Chemical-form and evidence gaps remain, so this source-identity review is partial.
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
  - path: data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
    sha256: 38d8afae06f9f7c3e5a577a191361d2862ff4c1b3c10757187d1e09e4985c414
    role: target
  - path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    sha256: 79d8e090e93729381c61908b9e07cdfbeda6cccc4661956e92a02b910ff53ad7
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
    sha256: 75f21e5baf07c0dfb9341106525963f0d8232830824c7a8fde67018108585c9f
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml
    sha256: 6ec46d31b31e4c00385cdbecacab6c92c6da1b733d05370e32539423ca9056a3
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
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
  - path: scripts/repair_komodo_1501_acidithiobacillus_score10.py
    sha256: 2357ab5a67d24df9a17926020752e7ca6a5d4dce130d0440c3381d5aa39d690e
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 173; batch 018 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding seventeen task batches
    contain 170 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 172 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000981
targets:
- target_id: CultureMech:000981
  path: data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  label: acidithiobacillus_caldus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/173/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/173/strict.tsv"
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000981
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
  - CultureMech:000981
- check_id: komodo150_1-source-access
  name: 'Exact source content access: komodo150_1'
  required: true
  status: unavailable
  summary: Exact KOMODO150.1 detail returned HTTP403. The table resolves the accession,
    DSM18786 label, pH0.8 and linked DSMZ150 metadata, but does not supply the variant
    formulation. The local13-row150a composition and later PH_VARIANT repair therefore
    lack exact source-identity confirmation; no substitution of150 or150a is inferred.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - komodo150_1-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_18786.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:41.819689Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch018/173/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:43.796534Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-018/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch018/173/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:47.290463Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T11:18:49.189907Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T11:26:30Z'
  support: supports
  summary: './data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml:1:id: CultureMech:000981

    ./data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml:1:id: CultureMech:000981

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/source-preflight-bound/173/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T11:26:30Z'
  support: supports
  summary: 20 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 0feba3de95d5ada5f21d81caddc66c38f66268302f9940025128e323a6d9cf16
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf
  locator: PDF page1, entire main recipe, preparation and trace-element table
  accessed_at: '2026-10-21T11:02:38.702371Z'
  support: supports
  summary: Exact DSMZ150a source preserves 1000 ml main water, a 10 ml trace-stock
    addition, 1000 ml stock water, supplied hydrates and source-specific acid/sulfur
    preparation. No autoclave temperature/time is supplied.
  snapshot_sha256: a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/150a
  locator: $.data.medium and $.data.solutions[0:2], IDs265/266
  accessed_at: '2026-10-21T11:02:37.422716Z'
  support: supports
  summary: Provider separates the main solution (declared1010 ml) from the trace stock
    (1000 ml). Its basal g_l values and stock g_l values have different stage denominators;
    neither is a measured final volume.
  snapshot_sha256: e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a
- evidence_id: source150
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf
  locator: PDF page1 heading, full main table and preparation; identity comparison
    only
  accessed_at: '2026-10-21T11:02:38.114332Z'
  support: supports
  summary: The exact catalog-linked DSMZ150 is ACIDIANUS BRIERLEYI MEDIUM with yeast
    extract and a different sulfur amount, not the DSMZ150a formulation. This source
    is used to expose the mapping discrepancy, not to replace150a or assert the unavailable
    variant recipe.
  snapshot_sha256: 08e2776547138b3af7be160bf68cb9b31014e21ee3f9d29af3e7deece791a0b1
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaInfo150.1 row; complete table header separately read
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact row supports For DSM18786, pH0.8 and a DSMZ150 URL. Is Aerobic=false
    supports imported catalog metadata only, not independently verified physiology.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\n\t\t\t\t\t<TD> For DSM 18786</TD>\n\t\t\t\t\t<TD> 0.8</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo150_1-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:02:37.422960Z'
  support: context_only
  summary: Exact KOMODO150.1 detail returned HTTP403. The table resolves the accession,
    DSM18786 label, pH0.8 and linked DSMZ150 metadata, but does not supply the variant
    formulation. The local13-row150a composition and later PH_VARIANT repair therefore
    lack exact source-identity confirmation; no substitution of150 or150a is inferred.
  snapshot_sha256: 11f41f088cd87dc6bcb465cb5bdd5351bf6f0a05e63f18c5c50960fa775ea7e3
- evidence_id: stock266
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/266
  locator: $.data, all eight recipe rows and volume1000
  accessed_at: '2026-10-21T11:05:17.429069Z'
  support: supports
  summary: Exact stock266 corresponds to the primary trace table. Its eight existing
    local evidence snippets match this captured response; they do not validate a receiving-medium
    root amount.
  snapshot_sha256: be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch018/173/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 5e9ef3ad8ab51e054d206541041234960f8eed4270e82370784bf32de82246bf
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identity/label
    existence is separate from exact supplied form and source-specific ingredient
    support.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
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
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to sodium molybdate dihydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86159
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T10:35:29.712666Z'
  support: supports
  summary: CHEBI:86159 resolves to calcium nitrate tetrahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: d2b0e9caef5876c00ed00136113d600d34a071b137bdd8c661c734ad5435682f
- evidence_id: chebi86254
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254
  locator: Exact OLS obo_id, label, obsolete flag, formula and supplied-form annotations
  accessed_at: '2026-10-21T08:17:30.289392Z'
  support: supports
  summary: CHEBI:86254 resolves to iron trichloride hexahydrate. Identity/label existence
    is separate from exact supplied form and source-specific ingredient support.
  snapshot_sha256: 89afba545ad02f24a850933df154af25dee37357b583f82de13866b44f18d683
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned index exact identifier lookup; adjacent source revision/hash
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "asserted_secondary_rows":
    {"CHEBI:131527": [{"label": "Dibasic potassium phosphate", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium hydrogen
    phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Dipotassium hydrogenorthophosphate", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium monohydrogen
    phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Dipotassium monophosphate", "match_type": "synonym", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium orthophosphate", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "Dipotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Hydrogen dipotassium phosphate", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "K 2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "K2HPO", "match_type": "synonym", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "K2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO4(Sigma P 3786)", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "KH2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Phosphoric acid, dipotassium salt", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dibasic
    phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium monohydrogen phosphate", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium monophosphate",
    "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4",
    "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Potassium phosphate (dibasic)", "match_type": "synonym", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate dibasic", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833":
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
    "ambiguity": "unique"}], "CHEBI:53503": [{"label": "cobalt (II) chloride hexahydrate",
    "match_type": "synonym", "identifier": "CHEBI:53503", "preferred_term": "Cobalt
    chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Cobalt chloride hexahydrate", "match_type":
    "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride
    hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "cobalt chloride hexahydrate", "match_type": "ontology_label",
    "identifier": "CHEBI:53503", "preferred_term": "CoCl2 x 6 H2O", "ontology_id":
    "CHEBI:53503", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "cobalt chloride hydrate", "match_type": "synonym", "identifier": "CHEBI:53503",
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
    "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213":
    [{"label": "Disodium molybdate dihydrate", "match_type": "synonym", "identifier":
    "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Molybdic acid,
    disodium salt, dihydrate", "match_type": "synonym", "identifier": "CHEBI:75213",
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
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86159":
    [{"label": "(1)  Ca(NO3)2", "match_type": "synonym", "identifier": "CHEBI:86159",
    "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "(1)  Ca(NO3)2.4H2O", "match_type":
    "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O",
    "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Ca(NO3)2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86159",
    "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2 x 4 H2O (0.1% w/v)", "match_type":
    "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O",
    "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Ca(NO3)2 · 4H2O", "match_type": "synonym", "identifier": "CHEBI:86159",
    "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2.4H2O", "match_type": "synonym",
    "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id":
    "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2x4H2O",
    "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2
    x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Ca(NO3)2·4H2O", "match_type": "synonym", "identifier": "CHEBI:86159",
    "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2•4H2O", "match_type": "synonym",
    "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id":
    "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Ca(NO3)2•4H2O(CAS:
    13477-34-4)", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term":
    "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Ca(NO3)2・4H2O", "match_type": "synonym", "identifier":
    "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Calcium dinitrate
    tetrahydrate", "match_type": "synonym", "identifier": "CHEBI:86159", "preferred_term":
    "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Calcium nitrate tetrahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O",
    "ontology_id": "CHEBI:86159", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "calcium nitrate--water (1/4)", "match_type": "synonym", "identifier":
    "CHEBI:86159", "preferred_term": "Ca(NO3)2 x 4 H2O", "ontology_id": "CHEBI:86159",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86254": [{"label":
    "FeCl3 . 6H2O", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term":
    "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeCl3 x 6 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O (0.1%
    w/v in 0.2 N HCl)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term":
    "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeCl3 x 6 H2O (0.5%)", "match_type": "synonym", "identifier":
    "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O (w/v=1%)",
    "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3
    x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeCl3 x 6 H2O NaEDTA", "match_type": "synonym", "identifier":
    "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3 x 6 H2O solution
    (2%)", "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term":
    "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeCl3 x6H2O", "match_type": "synonym", "identifier": "CHEBI:86254",
    "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3*6 H2O", "match_type": "synonym",
    "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id":
    "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "FeCl3.6H2O",
    "match_type": "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3
    x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "FeCl3·6H2O", "match_type": "synonym", "identifier": "CHEBI:86254",
    "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Ferric chloride hexahydrate", "match_type":
    "synonym", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id":
    "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Iron
    (III) chloride hexahydrate", "match_type": "synonym", "identifier": "CHEBI:86254",
    "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "iron trichloride hexahydrate", "match_type":
    "ontology_label", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O",
    "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "trichloroiron--water (1/6)", "match_type": "synonym", "identifier":
    "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label":
    "Manganese (II) sulfate monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Manganese sulfate", "match_type":
    "synonym", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganese
    sulfate hydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Manganese sulfate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(2+) sulfate--water (1/1)", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(2+) sulphate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "manganese(II) sulfate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "manganese(II) sulfate
    monohydrate", "match_type": "ontology_label", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x 1 H2O", "ontology_id": "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity":
    "unique"}, {"label": "manganese(II) sulphate monohydrate", "match_type": "synonym",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Manganous sulfate
    monohydrate", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "MnSO4 . H2O", "match_type": "synonym", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MnSO4 x 1 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x 1 H2O", "ontology_id":
    "CHEBI:86364", "mapping_status": "REJECTED", "ambiguity": "unique"}, {"label":
    "MnSO4 x 1 H2O", "match_type": "synonym", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
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
    "unique"}]}, "missing_current_keys": ["CHEBI:26833"], "legacy_instances": []}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ACIDITHIOBACILLUS_CALDUS_MEDIUM.yaml; data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml;
    data/normalized_yaml/bacterial/for_dsm_18786.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_18786.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:02.972737"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Current importer separates main and referenced stocks; resolver strips
    alphabetic medium suffixes in its index; the later150.1 repair hard-codes the
    shared13-row signature and150a topology. These inspected mechanisms identify maintenance
    points but do not prove which historical execution produced a record or establish
    source equivalence.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Current importer separates main and referenced stocks; resolver strips
    alphabetic medium suffixes in its index; the later150.1 repair hard-codes the
    shared13-row signature and150a topology. These inspected mechanisms identify maintenance
    points but do not prove which historical execution produced a record or establish
    source equivalence.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_komodo_1501_acidithiobacillus_score10.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Current importer separates main and referenced stocks; resolver strips
    alphabetic medium suffixes in its index; the later150.1 repair hard-codes the
    shared13-row signature and150a topology. These inspected mechanisms identify maintenance
    points but do not prove which historical execution produced a record or establish
    source equivalence.
  snapshot_sha256: 2357ab5a67d24df9a17926020752e7ca6a5d4dce130d0440c3381d5aa39d690e
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T11:26:30Z'
  support: context_only
  summary: Current importer separates main and referenced stocks; resolver strips
    alphabetic medium suffixes in its index; the later150.1 repair hard-codes the
    shared13-row signature and150a topology. These inspected mechanisms identify maintenance
    points but do not prove which historical execution produced a record or establish
    source equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Distinct accessions and maintained relationship topology
  outcome: concern
  summary: The target names DSMZ150a and resolves to two exact normalized owners.
    Their local paths and IDs exist, but the generated target retains the old reverse
    SOURCE_DUPLICATE parent while the September owner repair establishes reciprocal
    PH_VARIANT links under150a. KOMODO150.1 still links DSMZ150 in the captured source
    catalog and owner notes/history. Identical13-row local arrays do not establish
    equivalent formulations or justify a pH-only relationship.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - source150
  - catalog
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 65 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"ingredient\": \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"\
    2.9703\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a\
    \ main recipe\",\n    \"source_amount\": {\n      \"value\": 3,\n      \"unit\"\
    : \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact (NH4)2SO4 row\",\n\
    \        \"exact_source_quote\": \"(NH4)2SO4 3.00 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 3,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.9703,\\n     \
    \                   \\\"mmol_l\\\": 22.4784,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"\
    Retain the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"3 g /1.010 L = 2.97029703 g/L, rounded by provider to 2.9703.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"ingredient\": \"K2HPO4 x 3 H2O\",\n    \"existing\": {\n      \"value\"\
    : \"0.49505\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"\
    DSMZ150a main recipe\",\n    \"source_amount\": {\n      \"value\": 0.5,\n   \
    \   \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact K2HPO4 x 3 H2O row\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 x 3 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"K2HPO4 x 3 H2O\\\",\\n                        \\\"compound_id\\\
    \": 244,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.84224,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      }\n\
    \    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"Retain the\
    \ provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"ingredient\": \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\"\
    : \"0.49505\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"\
    DSMZ150a main recipe\",\n    \"source_amount\": {\n      \"value\": 0.5,\n   \
    \   \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact MgSO4 x 7 H2O row\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.00851,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      }\n\
    \    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"Retain the\
    \ provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"ingredient\": \"KCl\",\n    \"existing\": {\n      \"value\": \"0.0990099\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main\
    \ recipe\",\n    \"source_amount\": {\n      \"value\": 0.1,\n      \"unit\":\
    \ \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact KCl row\",\n     \
    \   \"exact_source_quote\": \"KCl 0.10 g\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0990099,\\n          \
    \              \\\"mmol_l\\\": 1.3281,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"\
    Retain the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.1 g /1.010 L = 0.099009901 g/L, rounded by provider to 0.0990099.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"ingredient\": \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\"\
    : \"0.019802\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"\
    DSMZ150a main recipe\",\n    \"source_amount\": {\n      \"value\": 0.02,\n  \
    \    \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact Ca(NO3)2 x 4 H2O row\"\
    ,\n        \"exact_source_quote\": \"Ca(NO3)2 x 4 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 213,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.019802,\\\
    n                        \\\"mmol_l\\\": 0.0838538,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n     \
    \ }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"Retain\
    \ the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.02 g /1.010 L = 0.0198019802 g/L, rounded by provider to 0.019802.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"ingredient\": \"Sulfur\",\n    \"existing\": {\n      \"value\": \"4.9505\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main\
    \ recipe\",\n    \"source_amount\": {\n      \"value\": 5,\n      \"unit\": \"\
    g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact Sulfur row\",\n  \
    \      \"exact_source_quote\": \"Sulfur (powdered) 5.00 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\": 80,\\\
    n                        \\\"condition\\\": \\\"\\\",\\n                     \
    \   \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"amount\\\
    \": 5,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 4.9505,\\n                        \\\"mmol_l\\\": 154.365,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"\
    Retain the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"5 g /1.010 L = 4.95049505 g/L, rounded by provider to 4.9505.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"target\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"ingredient\": \"FeCl3 x 6 H2O\",\n    \"existing\": {\n      \"value\"\
    : \"1.1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a\
    \ trace-stock composition before10 ml addition\",\n    \"source_amount\": {\n\
    \      \"value\": 1.1,\n      \"unit\": \"g\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, Trace element solution table, exact FeCl3 x 6\
    \ H2O row\",\n        \"exact_source_quote\": \"FeCl3 x 6 H2O 1.10 g\",\n    \
    \    \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 82,\\n                        \\\"amount\\\": 1.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.1,\\n \
    \                       \\\"mmol_l\\\": 4.06961,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 1.1 g/L stock ×0.010 L /1.010 L = 0.0108910891\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\"\
    : \"ingredients[7].concentration\",\n    \"ingredient\": \"CuSO4 x 5 H2O\",\n\
    \    \"existing\": {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_stage\": \"DSMZ150a trace-stock composition before10 ml\
    \ addition\",\n    \"source_amount\": {\n      \"value\": 0.05,\n      \"unit\"\
    : \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ CuSO4 x 5 H2O row\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.05 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.05,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.200252,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.05 g/L stock ×0.010 L /1.010 L = 0.000495049505\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\"\
    : \"ingredients[8].concentration\",\n    \"ingredient\": \"H3BO3\",\n    \"existing\"\
    : {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\"\
    : \"DSMZ150a trace-stock composition before10 ml addition\",\n    \"source_amount\"\
    : {\n      \"value\": 0.2,\n      \"unit\": \"g\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1, Trace element solution table, exact H3BO3 row\"\
    ,\n        \"exact_source_quote\": \"H3BO3 0.20 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                \
    \        \\\"mmol_l\\\": 3.23415,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\"\
    : \"ingredients[9].concentration\",\n    \"ingredient\": \"MnSO4 x H2O\",\n  \
    \  \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"source_stage\": \"DSMZ150a trace-stock composition before10 ml addition\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.2,\n      \"unit\": \"g\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ MnSO4 x H2O row\",\n        \"exact_source_quote\": \"MnSO4 x H2O 0.20 g\",\n\
    \        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.18332,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\"\
    : \"ingredients[10].concentration\",\n    \"ingredient\": \"Na2MoO4 x 2 H2O\"\
    ,\n    \"existing\": {\n      \"value\": \"0.08\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition before10 ml\
    \ addition\",\n    \"source_amount\": {\n      \"value\": 0.08,\n      \"unit\"\
    : \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ Na2MoO4 x 2 H2O row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.08\
    \ g\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.08,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.08,\\n\
    \                        \\\"mmol_l\\\": 0.330647,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.08 g/L stock ×0.010 L /1.010 L = 0.000792079208\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\"\
    : \"ingredients[11].concentration\",\n    \"ingredient\": \"CoCl2 x 6 H2O\",\n\
    \    \"existing\": {\n      \"value\": \"0.06\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_stage\": \"DSMZ150a trace-stock composition before10 ml\
    \ addition\",\n    \"source_amount\": {\n      \"value\": 0.06,\n      \"unit\"\
    : \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ CoCl2 x 6 H2O row\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 0.06 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 0.06,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.06,\\\
    n                        \\\"mmol_l\\\": 0.462111,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.06 g/L stock ×0.010 L /1.010 L = 0.000594059406\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\"\
    : \"ingredients[12].concentration\",\n    \"ingredient\": \"ZnSO4 x 7 H2O\",\n\
    \    \"existing\": {\n      \"value\": \"0.09\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_stage\": \"DSMZ150a trace-stock composition before10 ml\
    \ addition\",\n    \"source_amount\": {\n      \"value\": 0.09,\n      \"unit\"\
    : \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ ZnSO4 x 7 H2O row\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.09 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.09,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.09,\\\
    n                        \\\"mmol_l\\\": 0.312977,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.09 g/L stock ×0.010 L /1.010 L = 0.000891089109\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"2.9703\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\",\n\
    \    \"source_amount\": {\n      \"value\": 3,\n      \"unit\": \"g\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact (NH4)2SO4 row\",\n\
    \        \"exact_source_quote\": \"(NH4)2SO4 3.00 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 3,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.9703,\\n     \
    \                   \\\"mmol_l\\\": 22.4784,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"\
    Retain the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"3 g /1.010 L = 2.97029703 g/L, rounded by provider to 2.9703.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"K2HPO4 x 3 H2O\",\n    \"existing\": {\n      \"value\": \"0.49505\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact K2HPO4 x 3 H2O row\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 x 3 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"K2HPO4 x 3 H2O\\\",\\n                        \\\"compound_id\\\
    \": 244,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.84224,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      }\n\
    \    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"Retain the\
    \ provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.49505\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact MgSO4 x 7 H2O row\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.00851,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      }\n\
    \    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"Retain the\
    \ provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.5 g /1.010 L = 0.495049505 g/L, rounded by provider to 0.49505.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.0990099\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\",\n    \"\
    source_amount\": {\n      \"value\": 0.1,\n      \"unit\": \"g\"\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact KCl row\",\n     \
    \   \"exact_source_quote\": \"KCl 0.10 g\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0990099,\\n          \
    \              \\\"mmol_l\\\": 1.3281,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"\
    Retain the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.1 g /1.010 L = 0.099009901 g/L, rounded by provider to 0.0990099.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\": \"0.019802\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.02,\n      \"unit\": \"g\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact Ca(NO3)2 x 4 H2O row\"\
    ,\n        \"exact_source_quote\": \"Ca(NO3)2 x 4 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 213,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.019802,\\\
    n                        \\\"mmol_l\\\": 0.0838538,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n     \
    \ }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"Retain\
    \ the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"0.02 g /1.010 L = 0.0198019802 g/L, rounded by provider to 0.019802.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\":\
    \ \"Sulfur\",\n    \"existing\": {\n      \"value\": \"4.9505\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\",\n    \"\
    source_amount\": {\n      \"value\": 5,\n      \"unit\": \"g\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact Sulfur row\",\n  \
    \      \"exact_source_quote\": \"Sulfur (powdered) 5.00 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\": 80,\\\
    n                        \\\"condition\\\": \\\"\\\",\\n                     \
    \   \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"amount\\\
    \": 5,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 4.9505,\\n                        \\\"mmol_l\\\": 154.365,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"evidence_only\",\n    \"proposed\": \"\
    Retain the provider-declared basal value with exact source evidence and an explicit1010\
    \ ml calculation basis; assess hydrate/material identity separately.\",\n    \"\
    calculation\": \"5 g /1.010 L = 4.95049505 g/L, rounded by provider to 4.9505.\
    \ The declared volume is not an independently measured final volume.\"\n  },\n\
    \  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\":\
    \ \"FeCl3 x 6 H2O\",\n    \"existing\": {\n      \"value\": \"1.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 1.1,\n \
    \     \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ FeCl3 x 6 H2O row\",\n        \"exact_source_quote\": \"FeCl3 x 6 H2O 1.10 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 82,\\n                        \\\"amount\\\": 1.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.1,\\n \
    \                       \\\"mmol_l\\\": 4.06961,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 1.1 g/L stock ×0.010 L /1.010 L = 0.0108910891\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"CuSO4 x 5 H2O\",\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.05,\n\
    \      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ CuSO4 x 5 H2O row\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.05 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.05,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.200252,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.05 g/L stock ×0.010 L /1.010 L = 0.000495049505\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[8].concentration\",\n    \"ingredient\":\
    \ \"H3BO3\",\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.2,\n \
    \     \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ H3BO3 row\",\n        \"exact_source_quote\": \"H3BO3 0.20 g\",\n        \"\
    snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                \
    \        \\\"mmol_l\\\": 3.23415,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[9].concentration\",\n    \"ingredient\":\
    \ \"MnSO4 x H2O\",\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.2,\n \
    \     \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ MnSO4 x H2O row\",\n        \"exact_source_quote\": \"MnSO4 x H2O 0.20 g\",\n\
    \        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.18332,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.2 g/L stock ×0.010 L /1.010 L = 0.00198019802\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"Na2MoO4 x 2 H2O\",\n    \"existing\": {\n      \"value\": \"0.08\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock\
    \ composition before10 ml addition\",\n    \"source_amount\": {\n      \"value\"\
    : 0.08,\n      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ Na2MoO4 x 2 H2O row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.08\
    \ g\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.08,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.08,\\n\
    \                        \\\"mmol_l\\\": 0.330647,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.08 g/L stock ×0.010 L /1.010 L = 0.000792079208\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[11].concentration\",\n    \"ingredient\"\
    : \"CoCl2 x 6 H2O\",\n    \"existing\": {\n      \"value\": \"0.06\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.06,\n\
    \      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ CoCl2 x 6 H2O row\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 0.06 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 0.06,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.06,\\\
    n                        \\\"mmol_l\\\": 0.462111,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.06 g/L stock ×0.010 L /1.010 L = 0.000594059406\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"ingredient\"\
    : \"ZnSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.09\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.09,\n\
    \      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ ZnSO4 x 7 H2O row\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.09 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.09,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.09,\\\
    n                        \\\"mmol_l\\\": 0.312977,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive150aapi\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ],\n    \"decision\": \"correct\",\n    \"proposed\": \"Move this\
    \ value to the exact trace-stock composition and represent its10 ml addition separately;\
    \ do not retain undiluted stock strength as a root concentration.\",\n    \"calculation\"\
    : \"On the provider-declared bases only: 0.09 g/L stock ×0.010 L /1.010 L = 0.000891089109\
    \ g/L. This arithmetic illustrates stage error, not an unqualified measured final\
    \ concentration.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"ingredient\":\
    \ \"(NH4)2SO4\",\n    \"existing\": {\n      \"value\": \"2.9703\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\",\n\
    \    \"source_amount\": {\n      \"value\": 3,\n      \"unit\": \"g\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact (NH4)2SO4 row\",\n\
    \        \"exact_source_quote\": \"(NH4)2SO4 3.00 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 3,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.9703,\\n     \
    \                   \\\"mmol_l\\\": 22.4784,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[1].concentration\",\n    \"ingredient\":\
    \ \"K2HPO4 x 3 H2O\",\n    \"existing\": {\n      \"value\": \"0.49505\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact K2HPO4 x 3 H2O row\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 x 3 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"K2HPO4 x 3 H2O\\\",\\n                        \\\"compound_id\\\
    \": 244,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.84224,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"ingredient\":\
    \ \"MgSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.49505\",\n   \
    \   \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.5,\n      \"unit\": \"g\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact MgSO4 x 7 H2O row\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.00851,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"ingredient\":\
    \ \"KCl\",\n    \"existing\": {\n      \"value\": \"0.0990099\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\",\n    \"\
    source_amount\": {\n      \"value\": 0.1,\n      \"unit\": \"g\"\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact KCl row\",\n     \
    \   \"exact_source_quote\": \"KCl 0.10 g\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0990099,\\n          \
    \              \\\"mmol_l\\\": 1.3281,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"ingredient\":\
    \ \"Ca(NO3)2 x 4 H2O\",\n    \"existing\": {\n      \"value\": \"0.019802\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\"\
    ,\n    \"source_amount\": {\n      \"value\": 0.02,\n      \"unit\": \"g\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact Ca(NO3)2 x 4 H2O row\"\
    ,\n        \"exact_source_quote\": \"Ca(NO3)2 x 4 H2O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Ca(NO3)2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 213,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.019802,\\\
    n                        \\\"mmol_l\\\": 0.0838538,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n     \
    \ },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"ingredient\":\
    \ \"Sulfur\",\n    \"existing\": {\n      \"value\": \"4.9505\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a main recipe\",\n    \"\
    source_amount\": {\n      \"value\": 5,\n      \"unit\": \"g\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, main table, exact Sulfur row\",\n  \
    \      \"exact_source_quote\": \"Sulfur (powdered) 5.00 g\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\": 80,\\\
    n                        \\\"condition\\\": \\\"\\\",\\n                     \
    \   \\\"attribute\\\": \\\"powdered\\\",\\n                        \\\"amount\\\
    \": 5,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 4.9505,\\n                        \\\"mmol_l\\\": 154.365,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"ingredient\":\
    \ \"FeCl3 x 6 H2O\",\n    \"existing\": {\n      \"value\": \"1.1\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 1.1,\n \
    \     \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ FeCl3 x 6 H2O row\",\n        \"exact_source_quote\": \"FeCl3 x 6 H2O 1.10 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 82,\\n                        \\\"amount\\\": 1.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.1,\\n \
    \                       \\\"mmol_l\\\": 4.06961,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[7].concentration\",\n    \"ingredient\":\
    \ \"CuSO4 x 5 H2O\",\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.05,\n\
    \      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ CuSO4 x 5 H2O row\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.05 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.05,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.200252,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[8].concentration\",\n    \"ingredient\":\
    \ \"H3BO3\",\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.2,\n \
    \     \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ H3BO3 row\",\n        \"exact_source_quote\": \"H3BO3 0.20 g\",\n        \"\
    snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                \
    \        \\\"mmol_l\\\": 3.23415,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[9].concentration\",\n    \"ingredient\":\
    \ \"MnSO4 x H2O\",\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.2,\n \
    \     \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ MnSO4 x H2O row\",\n        \"exact_source_quote\": \"MnSO4 x H2O 0.20 g\",\n\
    \        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.18332,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      },\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"\
    source_url\": \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[10].concentration\",\n    \"ingredient\"\
    : \"Na2MoO4 x 2 H2O\",\n    \"existing\": {\n      \"value\": \"0.08\",\n    \
    \  \"unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock\
    \ composition before10 ml addition\",\n    \"source_amount\": {\n      \"value\"\
    : 0.08,\n      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ Na2MoO4 x 2 H2O row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.08\
    \ g\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.08,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.08,\\n\
    \                        \\\"mmol_l\\\": 0.330647,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[11].concentration\",\n    \"ingredient\"\
    : \"CoCl2 x 6 H2O\",\n    \"existing\": {\n      \"value\": \"0.06\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.06,\n\
    \      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ CoCl2 x 6 H2O row\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 0.06 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 0.06,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.06,\\\
    n                        \\\"mmol_l\\\": 0.462111,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ingredients[12].concentration\",\n    \"ingredient\"\
    : \"ZnSO4 x 7 H2O\",\n    \"existing\": {\n      \"value\": \"0.09\",\n      \"\
    unit\": \"G_PER_L\"\n    },\n    \"source_stage\": \"DSMZ150a trace-stock composition\
    \ before10 ml addition\",\n    \"source_amount\": {\n      \"value\": 0.09,\n\
    \      \"unit\": \"g\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1, Trace element solution table, exact\
    \ ZnSO4 x 7 H2O row\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.09 g\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.09,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.09,\\\
    n                        \\\"mmol_l\\\": 0.312977,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\n      },\n\
    \      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row: DSMZ150 link and pH metadata\
    \ only\",\n        \"exact_source_quote\": \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\
    \"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ],\n    \"decision\": \"unsupported\",\n    \"proposed\": \"Resolve\
    \ the exact KOMODO150.1 formulation before endorsing or changing this copied quantity;\
    \ neither150a nor150 is silently substituted.\",\n    \"explanation\": \"The local\
    \ value equals a150a provider stage value, but the exact catalog links150 and\
    \ the variant detail is inaccessible. Numeric correspondence is not evidence for\
    \ this variant. If150a identity is later established, stock-stage flattening must\
    \ still be corrected.\"\n  },\n  {\n    \"input\": \"target and DSMZ150a owner\
    \ only; variant identity unresolved\",\n    \"field_path\": \"solutions / preparation_steps\
    \ (missing Trace element solution)\",\n    \"ingredient\": \"Trace element solution\"\
    ,\n    \"decision\": \"add\",\n    \"source_amount\": {\n      \"value\": 10,\n\
    \      \"unit\": \"ml\"\n    },\n    \"source_stage\": \"Main recipe; trace stock\
    \ is added after autoclaving\",\n    \"proposed\": \"Preserve original batch/stock\
    \ amount and exact addition stage; do not infer additional doses for KOMODO150.1.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 main table, exact Trace element solution\
    \ row\",\n        \"exact_source_quote\": \"Trace element solution 10.00 ml\"\
    ,\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 266,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and DSMZ150a owner only;\
    \ variant identity unresolved\",\n    \"field_path\": \"solutions / preparation_steps\
    \ (missing Main distilled water)\",\n    \"ingredient\": \"Main distilled water\"\
    ,\n    \"decision\": \"add\",\n    \"source_amount\": {\n      \"value\": 1000,\n\
    \      \"unit\": \"ml\"\n    },\n    \"source_stage\": \"Main recipe; trace stock\
    \ is added after autoclaving\",\n    \"proposed\": \"Preserve original batch/stock\
    \ amount and exact addition stage; do not infer additional doses for KOMODO150.1.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 main table, exact Main distilled water\
    \ row\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n  \
    \      \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target and DSMZ150a owner only;\
    \ variant identity unresolved\",\n    \"field_path\": \"solutions / preparation_steps\
    \ (missing Trace-stock distilled water)\",\n    \"ingredient\": \"Trace-stock\
    \ distilled water\",\n    \"decision\": \"add\",\n    \"source_amount\": {\n \
    \     \"value\": 1000,\n      \"unit\": \"ml\"\n    },\n    \"source_stage\":\
    \ \"Trace stock before use\",\n    \"proposed\": \"Preserve original batch/stock\
    \ amount and exact addition stage; do not infer additional doses for KOMODO150.1.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 Trace element solution table, exact Trace-stock\
    \ distilled water row\",\n        \"exact_source_quote\": \"Distilled water 1000.00\
    \ ml\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive150aapi\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/150a\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"e053816d9efe9821ead5250714f7ebc356819af77d60eade3699dd9751e0fd0a\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    ph_value\",\n    \"existing\": 2.5,\n    \"decision\": \"evidence_only\",\n  \
    \  \"source_stage\": \"DSMZ150a initial adjustment before dispensing/autoclaving\"\
    ,\n    \"proposed\": \"Retain the separately supported pH metadata and source\
    \ scope; do not infer a shared formulation or measured final pH.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Adjust pH with 6 N H2SO4 to 2.5,\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"existing\": 2.5,\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"DSMZ150a initial adjustment before\
    \ dispensing/autoclaving\",\n    \"proposed\": \"Retain the separately supported\
    \ pH metadata and source scope; do not infer a shared formulation or measured\
    \ final pH.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 preparation paragraph\",\n        \"\
    exact_source_quote\": \"Adjust pH with 6 N H2SO4 to 2.5,\",\n        \"snapshot_sha256\"\
    : \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\",\n    \
    \    \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/for_dsm_18786.yaml\"\
    ,\n    \"field_path\": \"ph_value\",\n    \"existing\": 0.8,\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Exact KOMODO150.1 metadata only\"\
    ,\n    \"proposed\": \"Retain the separately supported pH metadata and source\
    \ scope; do not infer a shared formulation or measured final pH.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"komodoMediaList\",\n        \"source_url\"\
    : \"https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList\"\
    ,\n        \"source_locator\": \"Exact150.1 row, pH column\",\n        \"exact_source_quote\"\
    : \"<TR>\\n\\t\\t\\t\\t\\t<TD width=\\\"50\\\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=150.1'\
    \ >150.1</a></TD>\\n\\t\\t\\t\\t\\t<TD> For DSM 18786</TD>\\n\\t\\t\\t\\t\\t<TD>\
    \ 0.8</TD>\\n\\t\\t\\t\\t\\t<TD>true</TD>\\n\\t\\t\\t\\t\\t<TD>false</TD>\\n\\\
    t\\t\\t\\t\\t<TD>false</TD>\\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150.pdf</a></TD>\\\
    n\\t\\t\\t\\t</TR>\",\n        \"snapshot_sha256\": \"d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    preparation_steps[0] (acid strength)\",\n    \"decision\": \"evidence_only\",\n\
    \    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation, as explicitly\
    \ named\",\n    \"proposed\": \"Preserve explicit6 N strength; do not equate normality\
    \ with molarity.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 initial adjustment\",\n        \"exact_source_quote\"\
    : \"6 N H2SO4\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    preparation_steps[0] (acid dose)\",\n    \"decision\": \"not_quantified\",\n \
    \   \"source_stage\": \"DSMZ150a acid/base or sulfur preparation, as explicitly\
    \ named\",\n    \"proposed\": \"No fixed acid addition volume is supplied; preserve\
    \ titration context.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 initial adjustment\",\n        \"exact_source_quote\"\
    : \"Adjust pH with 6 N H2SO4 to 2.5,\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    preparation_steps[0] (sulfur heating duration)\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation, as explicitly\
    \ named\",\n    \"proposed\": \"Preserve3 hours for sulfur only; do not use it\
    \ as an autoclave duration.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"heat for 3 hours to 90 - 100°C\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    preparation_steps[0] (sulfur temperature range)\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation, as explicitly\
    \ named\",\n    \"proposed\": \"Preserve90–100 C range for sulfur only.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"heat for 3 hours to 90 - 100°C\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    preparation_steps[0] (sulfur repeated days)\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation, as explicitly\
    \ named\",\n    \"proposed\": \"Preserve the repetition across three days; do\
    \ not collapse to a single continuous cycle.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"on each of three successive days.\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"target\",\n    \"field_path\": \"\
    preparation_steps[0] (sulfur wetting water)\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation, as explicitly\
    \ named\",\n    \"proposed\": \"Retain the nonnumeric few-drops wording; no exact\
    \ volume is supplied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"wet with a few drops of\\nwater\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0] (acid strength)\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation,\
    \ as explicitly named\",\n    \"proposed\": \"Preserve explicit6 N strength; do\
    \ not equate normality with molarity.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 initial adjustment\",\n        \"exact_source_quote\"\
    : \"6 N H2SO4\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0] (acid dose)\",\n    \"decision\"\
    : \"not_quantified\",\n    \"source_stage\": \"DSMZ150a acid/base or sulfur preparation,\
    \ as explicitly named\",\n    \"proposed\": \"No fixed acid addition volume is\
    \ supplied; preserve titration context.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 initial adjustment\",\n        \"exact_source_quote\"\
    : \"Adjust pH with 6 N H2SO4 to 2.5,\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0] (sulfur heating duration)\",\n \
    \   \"decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ150a acid/base\
    \ or sulfur preparation, as explicitly named\",\n    \"proposed\": \"Preserve3\
    \ hours for sulfur only; do not use it as an autoclave duration.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"heat for 3 hours to 90 - 100°C\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0] (sulfur temperature range)\",\n\
    \    \"decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ150a acid/base\
    \ or sulfur preparation, as explicitly named\",\n    \"proposed\": \"Preserve90–100\
    \ C range for sulfur only.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz150a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"heat for 3 hours to 90 - 100°C\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0] (sulfur repeated days)\",\n    \"\
    decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ150a acid/base or\
    \ sulfur preparation, as explicitly named\",\n    \"proposed\": \"Preserve the\
    \ repetition across three days; do not collapse to a single continuous cycle.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz150a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\"\
    ,\n        \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"on each of three successive days.\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml\"\
    ,\n    \"field_path\": \"preparation_steps[0] (sulfur wetting water)\",\n    \"\
    decision\": \"not_quantified\",\n    \"source_stage\": \"DSMZ150a acid/base or\
    \ sulfur preparation, as explicitly named\",\n    \"proposed\": \"Retain the nonnumeric\
    \ few-drops wording; no exact volume is supplied.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz150a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium150a.pdf\",\n       \
    \ \"source_locator\": \"PDF p.1 sulfur preparation\",\n        \"exact_source_quote\"\
    : \"wet with a few drops of\\nwater\",\n        \"snapshot_sha256\": \"a356789f713fc46c160c78bf58d303bd62cfd186c6f476dc7e7a6ef7ed81a973\"\
    ,\n        \"parsed_text_sha256\": \"ed6b27ad11140a5d552273d8042c2a329b603f270307e4149e3ef0afbb9f2ae0\"\
    \n      }\n    ]\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[0].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"1.1\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"FeCl3 x 6 H2O\\\",\\n                \\\"compound_id\\\": 82,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1.1,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 1.1,\\n                \\\"mmol_l\\\
    \": 4.06961,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\
    \n      }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and\
    \ attached evidence match. Water1000 ml equals1 L as a source batch addition;\
    \ other values are source-declared stock g/L. This does not endorse copied values\
    \ in the target.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[1].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"0.05\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"CuSO4 x 5 H2O\\\",\\n                \\\"compound_id\\\": 121,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.05,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.200252,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\
    \n      }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and\
    \ attached evidence match. Water1000 ml equals1 L as a source batch addition;\
    \ other values are source-declared stock g/L. This does not endorse copied values\
    \ in the target.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[2].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"H3BO3\\\",\\n                \\\"compound_id\\\": 37,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 0.2,\\n                \\\"unit\\\": \\\"g\\\"\
    ,\\n                \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\": 3.23415,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\n     \
    \ }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and attached\
    \ evidence match. Water1000 ml equals1 L as a source batch addition; other values\
    \ are source-declared stock g/L. This does not endorse copied values in the target.\"\
    \n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[3].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"MnSO4 x H2O\\\",\\n                \\\"compound_id\\\": 14,\\n       \
    \         \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.2,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\
    \": 1.18332,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\
    \n      }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and\
    \ attached evidence match. Water1000 ml equals1 L as a source batch addition;\
    \ other values are source-declared stock g/L. This does not endorse copied values\
    \ in the target.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[4].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"0.08\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"Na2MoO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.08,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.08,\\n                \\\"mmol_l\\\
    \": 0.330647,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\
    \n      }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and\
    \ attached evidence match. Water1000 ml equals1 L as a source batch addition;\
    \ other values are source-declared stock g/L. This does not endorse copied values\
    \ in the target.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[5].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"0.06\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.06,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.06,\\n                \\\"mmol_l\\\
    \": 0.462111,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\
    \n      }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and\
    \ attached evidence match. Water1000 ml equals1 L as a source batch addition;\
    \ other values are source-declared stock g/L. This does not endorse copied values\
    \ in the target.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[6].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"0.09\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone\
    \ stock266 only; no evidence inheritance into receiving-medium layers\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"solution266\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/266\",\n  \
    \      \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"ZnSO4 x 7 H2O\\\",\\n                \\\"compound_id\\\": 35,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.09,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 0.09,\\n                \\\"mmol_l\\\
    \": 0.312977,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\
    \n      }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and\
    \ attached evidence match. Water1000 ml equals1 L as a source batch addition;\
    \ other values are source-declared stock g/L. This does not endorse copied values\
    \ in the target.\"\n  },\n  {\n    \"input\": \"data/normalized_yaml/bacterial/mediadive_266_Trace_element_solution.yaml\
    \ (dependency context only)\",\n    \"field_path\": \"composition[7].concentration\"\
    ,\n    \"existing\": {\n      \"value\": \"1\",\n      \"unit\": \"L\"\n    },\n\
    \    \"decision\": \"verified\",\n    \"source_stage\": \"Exact standalone stock266\
    \ only; no evidence inheritance into receiving-medium layers\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution266\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/266\",\n        \"source_locator\"\
    : \"$.data.recipe[7]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 8,\\n                \\\"compound\\\": \\\"Distilled\
    \ water\\\",\\n                \\\"compound_id\\\": 4,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 1000,\\n                \\\"unit\\\": \\\"ml\\\
    \",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"be617961aa5316e3a8a87c1ea95c870e3d0da06096e692bbd8160d8e3d873cef\"\n     \
    \ }\n    ],\n    \"explanation\": \"Existing value, unit, stock basis and attached\
    \ evidence match. Water1000 ml equals1 L as a source batch addition; other values\
    \ are source-declared stock g/L. This does not endorse copied values in the target.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Identifier metadata, exact secondary keys and supplied-form scope
  outcome: concern
  summary: 13 distinct primary/current-secondary identifiers resolve. 0 label instances
    differ from current canonical labels; 1 asserted current secondary keys lack an
    exact pinned index row. Legacy numeric links are assessed separately and are not
    established by CHEBI correspondence. Target linkage is 13/13 primary and 13/13
    secondary ingredient instances; this measures presence, not source validity.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - record
  - mim
  - chebi131527
  - chebi26833
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi53503
  - chebi62946
  - chebi75213
  - chebi86159
  - chebi86254
  - chebi86364
  details: '{"label_drift": [], "missing_secondary_keys": ["CHEBI:26833"], "legacy_instances":
    [], "coverage_scale": "0–100 percent; each ingredient instance counted once",
    "denominator": 13, "primary_percent": 100.0, "secondary_percent": 100.0}'
- assessment_id: chemical-forms
  area: grounding
  topic: Source trihydrate, elemental sulfur and other supplied forms
  outcome: concern
  summary: The primary and provider explicitly supply K2HPO4 trihydrate. CHEBI131527
    has an anhydrous formula/structure; its related trihydrate synonym does not encode
    three waters. Sulfur powder is a bulk elemental material, while CHEBI26833 is
    broader atom-level grounding that does not capture the supplied powder context.
    This scope difference does not establish a wrong chemical identifier or a particular
    allotrope. Other named salts retain the source hydrates, including MnSO4 monohydrate
    rather than an unspecified hydrate. The exact stock compound IDs match the eight
    captured provider objects.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - primary
  - provider
  - stock266
  - chebi131527
  - chebi26833
  - mim
- assessment_id: preparation
  area: completeness
  topic: Source preparation retained versus missing variant content
  outcome: concern
  summary: Target and DSMZ150a owner retain the source acid adjustment, separate filter-sterilized
    trace addition and sulfur heating/aseptic layering, but omit the quantified stock
    addition and water organization. No basal autoclave temperature/duration is supplied.
    The KOMODO owner lacks preparation; source identity must be resolved before copying150a
    preparation into it.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - record
  - primary
  - catalog
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Physical state, defined composition and source metadata
  outcome: concern
  summary: DEFINED and LIQUID are consistent with the150a source’s specified salts,
    trace stock and sulfur suspension without an undefined organic extract or gelling
    agent. This categorical fit applies only to the150a base and does not repair wrong
    material forms or concentrations. The exact150.1 catalog also says Is Complex=true;
    the child’s DEFINED assertion therefore needs source-identity reconciliation rather
    than automatic inheritance from150a. The exact catalog records Is Aerobic=false
    for150.1; preserve it as catalog metadata, not independent physiological evidence.
    DSM18786 is a source label, not an inferred taxonomy or demonstration of growth
    on the locally copied150a formula.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - record
  - primary
  - catalog
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000981
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
findings:
- finding_id: f1
  issue_key: culturemech.000981.stock-strength-flattening
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Seven trace-stock concentrations are asserted as receiving-medium ingredients
  description: Root ingredients6–12 equal the separately prepared1000 ml trace-stock
    strengths, although the main recipe adds only10 ml of that stock. The target and
    DSMZ150a owner have no explicit stock/dose structure or solvent basis. Six basal
    values use a different1010 ml provider denominator. The KOMODO copy shares the
    same flattened array, but its exact formulation identity must be resolved separately.
  target_ids:
  - CultureMech:000981
  field_paths:
  - ingredients[6:13]
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - primary
  - provider
  - stock266
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  issue_key: culturemech.000981.variant-source-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated source-duplicate and later pH-variant claims do not resolve the
    source mapping
  description: The generated target merges KOMODO150.1 as a SOURCE_DUPLICATE and points
    backward to its DSM18786 wrapper. Current normalized links instead call it a pH-only
    variant of150a. However, the exact KOMODO catalog and owner source notes link
    DSMZ150, whose current primary is a materially different formulation. The inaccessible150.1
    detail does not establish which formulation belongs to the variant. Local signature
    equality and ingredients_curated flags cannot resolve this discrepancy.
  target_ids:
  - CultureMech:000981
  field_paths:
  - parent_media
  - variant_relationship
  - variant_modifications
  - merged_from
  - synonyms
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - source150
  - catalog
  - komodo150_1-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  issue_key: culturemech.000981.source-material-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Phosphate hydration is mismatched and sulfur powder context is unrepresented
  description: K2HPO4 x3H2O is mapped to an anhydrous dipotassium hydrogen phosphate
    structure; the OLS related synonym is not structural hydrate support. Separately,
    CHEBI26833 provides broad atom-level sulfur grounding while the source specifies
    powder. The powder context needs preservation, but no wrong sulfur identifier
    or particular allotrope is established. Valid identifiers and labels alone do
    not resolve the phosphate hydrate mismatch.
  target_ids:
  - CultureMech:000981
  field_paths:
  - ingredients[1].term
  - ingredients[1].mediaingredientmech_chebi_term
  - ingredients[5].term
  - ingredients[5].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - provider
  - chebi131527
  - chebi26833
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  issue_key: culturemech.000981.claim-provenance-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported basal quantities and preparation lack attached claim evidence
  description: The source supports the150a basal values on the declared provider basis
    and the retained preparation statements, but no corresponding target/owner evidence
    is attached. Existing stock266 evidence is valid only for its own eight composition
    rows. The child’s missing variant evidence is a separate required limitation.
  target_ids:
  - CultureMech:000981
  field_paths:
  - ingredients[0:6]
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - provider
  - stock266
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.000981.secondary-index-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Asserted sulfur secondary key is absent from the pinned MIM index
  description: CHEBI26833 resolves as a primary ontology ID, but its exact identifier
    has no row anywhere in the current pinned MIM label index. This confirmed secondary
    mapping gap is distinct from the missing source powder context and is not evidence
    of a nonexistent or chemically wrong CHEBI term.
  target_ids:
  - CultureMech:000981
  field_paths:
  - ingredients[5].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - mim
  - chebi26833
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  issue_key: culturemech.000981.historical-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO history contains malformed and timezone-unspecified timestamps
  description: The child preserves2026-01-27T01:15:02.fZ and a timezone-naive enrichment
    timestamp. The target and DSMZ owner retain valid timezone-aware history. The
    true historical fraction/timezone were not recovered.
  target_ids:
  - CultureMech:000981
  field_paths:
  - curation_history
  evidence_ids:
  - owner-1
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  description: Represent stock266 composition and its exact10 ml addition separately
    in the maintained150a record; retain provider-declared versus source-batch bases
    and preserve existing standalone stock evidence. Resolve the variant before propagating
    any correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000981
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  description: Keep source-specific records distinct, recover exact variant evidence
    and reconcile150 versus150a before selecting relationship type or merged membership.
    Preserve historical events and do not silently substitute the catalog-linked recipe.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000981
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  description: Reconcile the explicit phosphate trihydrate with supported structural
    grounding, and preserve the source sulfur powder context separately. Do not infer
    a sulfur replacement identifier or allotrope, or use an anhydrous molecular weight
    for the trihydrate.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000981
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  description: Attach exact150a claim snippets, stock boundaries and calculation bases
    without treating dependency evidence as inherited. Preserve the original stock
    evidence and unresolved variant scope.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000981
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  description: Resolve the exact secondary mapping independently; preserve valid primary
    provenance and do not guess a replacement MIM identifier.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:000981
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
  description: Preserve old history and append a bounded clarification when authorized;
    do not fabricate a corrected historical time or retroactively authenticate the
    enrichment source.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:000981
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acidithiobacillus_caldus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18786.yaml
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
- Exact KOMODO150.1 detail returned HTTP403. The table resolves the accession, DSM18786
  label, pH0.8 and linked DSMZ150 metadata, but does not supply the variant formulation.
  The local13-row150a composition and later PH_VARIANT repair therefore lack exact
  source-identity confirmation; no substitution of150 or150a is inferred.
- 'The complete pinned MIM index was available and inspected: the asserted sulfur
  secondary key is confirmed absent. This mapping gap is distinct from live CHEBI
  validity and does not make that completed lookup unavailable. Partial completion
  is due to the inaccessible exact KOMODO150.1 formulation.'
- Stock266 is source context only, not an additional reviewed target. DSMZ150 is identity
  comparison only. No organism growth, pressure, basal autoclave setting, fixed acid
  dose or measured final volume was inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-018
- generated-medium
```
