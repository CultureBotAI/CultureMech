# Source and formulation review: alcaligenes_medium (CultureMech:006238)

- Review: 20261021T121916Z-culturemech-006238-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:11:53Z
- Finished UTC: 2026-10-21T12:19:16Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ660 Alcaligenes Medium and both normalized contributors resolve, but stock-strength rows are flattened into the main medium, post-autoclave stock additions are reduced to derived masses, hydrate mappings disagree with the source, and the fully defined classification is too strong for ferric ammonium citrate. Exact source amounts, provider denominators and eight existing dependency evidence objects are kept separate.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 194; batch 020 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nineteen task batches contain 190 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 193 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006238 | data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml | generated | alcaligenes_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006238 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006238 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/194/strict.tsv |
| validate-terms | passed | True | CultureMech:006238 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006238 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006238 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo660 | unavailable | False | CultureMech:006238 | The exact historical KOMODO660 detail page returned403. Current base identity, stable source mapping, DSMZ formulation and provider are independently resolved. Historical full import bytes are optional provenance context; no inaccessible variant is asserted. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006238.

The four documented recipes completed; interpret the scope of each separately.

### Exact source identity and maintained ownership

identity: supported. Targets: CultureMech:006238.

CultureMech:006238 is the generated KOMODO660/DSMZ660 source-duplicate record with exactly two explicit owners. Stable parent/child IDs and paths resolve. Current DSMZ660 PDF and MediaDive660 independently support the exact base formulation; no historical KOMODO full-recipe equivalence is inferred from the unavailable detail page.

### Classification, conditions and organism scope

scope: supported. Targets: CultureMech:006238.

LIQUID fits the absence of an agar addition. Bacterial organization and generic cultivation do not establish a strain-specific growth or oxygen phenotype. DEFINED is qualified separately because ferric ammonium citrate is an indefinite mixture.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006238.

22 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:006238.

19 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 19/19 primary and 19/19 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 19: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006238.

35 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "Tris",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6.06",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6.06",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6.06",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 6.06,
      "provider_amount": 6.06,
      "provider_unit": "g",
      "provider_g_l": 6.06,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "Tris 6.060 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Tris\",\n                        \"compound_id\": 73,\n                        \"amount\": 6.06,\n                        \"unit\": \"g\",\n                        \"g_l\": 6.06,\n                        \"mmol_l\": 50.0248,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q2",
    "claim": "NaCl",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "4.68",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "4.68",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "4.68",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 4.68,
      "provider_amount": 4.68,
      "provider_unit": "g",
      "provider_g_l": 4.68,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "NaCl 4.680 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 4.68,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.68,\n                        \"mmol_l\": 80.0821,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q3",
    "claim": "KCl",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.49",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.49",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.49",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 1.49,
      "provider_amount": 1.49,
      "provider_unit": "g",
      "provider_g_l": 1.49,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "KCl 1.490 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.49,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.49,\n                        \"mmol_l\": 19.9866,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q4",
    "claim": "NH4Cl",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.07",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.07",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.07",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 1.07,
      "provider_amount": 1.07,
      "provider_unit": "g",
      "provider_g_l": 1.07,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "NH4Cl 1.070 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1.07,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.07,\n                        \"mmol_l\": 20.0037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q5",
    "claim": "Na2SO4",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.43",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.43",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.43",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 0.43,
      "provider_amount": 0.43,
      "provider_unit": "g",
      "provider_g_l": 0.43,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "Na2SO4 0.430 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.43,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.43,\n                        \"mmol_l\": 3.02732,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q6",
    "claim": "MgCl2 x 6 H2O",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 0.2,
      "provider_amount": 0.2,
      "provider_unit": "g",
      "provider_g_l": 0.2,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "MgCl2 x 6 H2O 0.200 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.983753,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q7",
    "claim": "CaCl2 x 2 H2O",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 0.03,
      "provider_amount": 0.03,
      "provider_unit": "g",
      "provider_g_l": 0.03,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.030 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.204061,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q8",
    "claim": "Na2HPO4 x 12 H2O",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.23",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 0.23,
      "provider_amount": 0.23,
      "provider_unit": "g",
      "provider_g_l": 0.23,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "Na2HPO4 x 12 H2O 0.230 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2HPO4 x 12 H2O\",\n                        \"compound_id\": 95,\n                        \"amount\": 0.23,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.23,\n                        \"mmol_l\": 1.62019,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q9",
    "claim": "Fe(NH4)citrate",
    "decision": "evidence_only",
    "stage": "Basal main recipe; provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "primary_mass_g": 0.005,
      "provider_amount": 5,
      "provider_unit": "mg",
      "provider_g_l": 0.005,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal composition exact ingredient row",
        "exact_source_quote": "Fe(III)(NH4)citrate 0.005 g",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Fe(NH4)citrate\",\n                        \"compound_id\": 1203,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The three medium layers store the matching provider-declared value without attached evidence. Preserve primary batch masses and the provider denominator separately; explicit listed liquid inputs total1002 mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding form is assessed independently."
  },
  {
    "decision_id": "q10",
    "claim": "CuSO4 addition and strength",
    "decision": "correct",
    "stage": "Separately filter-sterilized stock added after autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.399025",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.399025",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.399025",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "dose_ml": 2.5,
      "stock_strength": "1.0 M",
      "provider_derived_g_l": 0.399025
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 final preparation sentence",
        "exact_source_quote": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution,",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"CuSO4\",\n                        \"compound_id\": 636,\n                        \"attribute\": \"1 M, sterilized by filtration\",\n                        \"amount\": 2.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.399025,\n                        \"mmol_l\": 2.5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "Restore explicit stock strength, addition volume and timing. Existing provider-derived g/L is not proof of a neat mass addition. CuSO4 source molarity does not identify a weighed hydrate; sodium-succinate40% does not specify w/v or another basis. Do not invent density, form or an independently measured final denominator."
  },
  {
    "decision_id": "q11",
    "claim": "Na-succinate addition and strength",
    "decision": "correct",
    "stage": "Separately filter-sterilized stock added after autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "dose_ml": 10,
      "stock_strength": "40% (basis unspecified)",
      "provider_derived_g_l": 4
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 final preparation sentence",
        "exact_source_quote": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution,",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Sodium succinate\",\n                        \"compound_id\": 730,\n                        \"attribute\": \"40 %, sterilized by filtration\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 24.6837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "Restore explicit stock strength, addition volume and timing. Existing provider-derived g/L is not proof of a neat mass addition. CuSO4 source molarity does not identify a weighed hydrate; sodium-succinate40% does not specify w/v or another basis. Do not invent density, form or an independently measured final denominator."
  },
  {
    "decision_id": "q12",
    "claim": "HCl flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 1,
      "stock_unit": "ml",
      "stock_attribute": "25%",
      "provider_stock_g_l": 0.25,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "HCl (25%) 1.000 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 6.85683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q13",
    "claim": "ZnCl2 flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 70,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.07,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "ZnCl2 70.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q14",
    "claim": "MnCl2 x 4 H2O flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 100,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.1,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "MnCl2 x 4 H2O 100.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q15",
    "claim": "H3BO3 flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 60,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.06,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "H3BO3 60.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 60,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.06,\n                        \"mmol_l\": 0.970246,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q16",
    "claim": "CoCl2 x 6 H2O flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 200,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.2,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "CoCl2 x 6 H2O 200.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q17",
    "claim": "CuCl2 x 2 H2O flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 20,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.02,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "CuCl2 x 2 H2O 20.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q18",
    "claim": "NiCl2 x 6 H2O flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 20,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.02,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "NiCl2 x 6 H2O 20.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q19",
    "claim": "Na2MoO4 x 2 H2O flattened stock row",
    "decision": "correct",
    "stage": "SL-7 stock composition, not a direct main-medium addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "stock_amount": 40,
      "stock_unit": "mg",
      "stock_attribute": null,
      "provider_stock_g_l": 0.04,
      "provider_stock_volume_ml": 1000,
      "main_stock_addition_ml": 1
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 Trace element solution SL-7 subsection exact named row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 40.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 40,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\": 0.165323,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All three medium layers incorrectly use stock-strength g/L as direct main amounts. Preserve the separate stock and its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations. For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived from primary density or percent convention."
  },
  {
    "decision_id": "q20",
    "claim": "SL-7 addition to main recipe",
    "decision": "add",
    "stage": "Main recipe stock dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": {
      "dose": 1.0,
      "unit": "ml",
      "stock": "SL-7"
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 main SL-7 addition row",
        "exact_source_quote": "Trace element solution SL 7 1.000 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Trace element solution SL-7\",\n                        \"solution_id\": 1392,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "All medium layers lack the explicit stock-addition object. The source supports a1 mL dose of the separately specified stock, not the stock component concentrations directly in the receiving medium."
  },
  {
    "decision_id": "q21",
    "claim": "Main water input",
    "decision": "add",
    "stage": "Basal recipe supplied water",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution, both sterilized by filtration."
          }
        ]
      }
    ],
    "source_amount": {
      "value": 988.5,
      "unit": "ml"
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 basal water row",
        "exact_source_quote": "Distilled water 988.500 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 988.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The source water input is absent from all medium layers. The DSMZ owner already has a different post-autoclave preparation sentence; its existing content is preserved in the exact local locator."
  },
  {
    "decision_id": "q22",
    "claim": "Standalone SL-7 HCl",
    "decision": "unsupported",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 1,
      "unit": "ml",
      "attribute": "25%",
      "provider_g_l": 0.25,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "HCl (25%) 1.000 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 6.85683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The HCl0.25 g/L is a provider interpretation without attached evidence and the primary only gives1 mL of25% reagent. Percentage basis and density are unstated; no independent mass conversion or replacement number is justified."
  },
  {
    "decision_id": "q23",
    "claim": "Standalone SL-7 ZnCl2",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 70,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.07,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "ZnCl2 70.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q24",
    "claim": "Standalone SL-7 MnCl2 x 4 H2O",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 100,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.1,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "MnCl2 x 4 H2O 100.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q25",
    "claim": "Standalone SL-7 H3BO3",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.06",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 60,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.06,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "H3BO3 60.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 60,\n                \"unit\": \"mg\",\n                \"g_l\": 0.06,\n                \"mmol_l\": 0.970246,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q26",
    "claim": "Standalone SL-7 CoCl2 x 6 H2O",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 200,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.2,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "CoCl2 x 6 H2O 200.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"mg\",\n                \"g_l\": 0.2,\n                \"mmol_l\": 1.54037,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q27",
    "claim": "Standalone SL-7 CuCl2 x 2 H2O",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 20,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.02,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "CuCl2 x 2 H2O 20.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.117314,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q28",
    "claim": "Standalone SL-7 NiCl2 x 6 H2O",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 20,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.02,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "NiCl2 x 6 H2O 20.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.154322,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q29",
    "claim": "Standalone SL-7 Na2MoO4 x 2 H2O",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "amount": 40,
      "unit": "mg",
      "attribute": null,
      "provider_g_l": 0.04,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 40.000 mg",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 40,\n                \"unit\": \"mg\",\n                \"g_l\": 0.04,\n                \"mmol_l\": 0.165323,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q30",
    "claim": "Standalone SL-7 Distilled water",
    "decision": "verified",
    "stage": "Standalone stock concentration or supplied-water dose; context only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "composition[8].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_amount": {
      "amount": 1000,
      "unit": "ml",
      "attribute": null,
      "provider_g_l": null,
      "provider_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 SL-7 subsection exact named row",
        "exact_source_quote": "Distilled water 1000.000 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "solution1392",
        "source_url": "https://mediadive.dsmz.de/rest/solution/1392",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c"
      }
    ],
    "explanation": "Attached literal evidence and identical historical/current response hash support the existing stock g/L value; for water,1000 mL /1000=1 L is a batch volume, not a final-medium percentage. This does not verify chemical grounding or the receiving-medium value."
  },
  {
    "decision_id": "q31",
    "claim": "Standalone placeholder ingredient",
    "decision": "correct",
    "stage": "Stock dependency representation, not an additional recipe constituent",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": {
      "value": null,
      "basis": "complete named SL-7 composition already exists"
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 stock heading",
        "exact_source_quote": "Trace element solution SL-7:",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 6.85683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "The variable See source for composition placeholder is not an additional source constituent. It should not become a medium ingredient or substitute for the explicit stock composition. Dependency correction is context for a separately authorized owner fix, not a second saved review."
  },
  {
    "decision_id": "q32",
    "claim": "Post-autoclave filtration/timing in target",
    "decision": "add",
    "stage": "Preparation timing of the two later additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": {
      "CuSO4_dose_ml": 2.5,
      "CuSO4_strength_M": 1.0,
      "succinate_dose_ml": 10,
      "succinate_percent": 40,
      "percent_basis": "unspecified"
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 final preparation sentence",
        "exact_source_quote": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution, \nboth sterilized by filtration.",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      }
    ],
    "explanation": "The DSMZ owner already preserves the exact preparation sentence; the KOMODO owner and target omit it. Attach narrow evidence at the existing owner stage and add missing context elsewhere. Do not invent autoclave temperature, time or filtration pore size."
  },
  {
    "decision_id": "q33",
    "claim": "Post-autoclave filtration/timing in KOMODO_660_ALCALIGENES_MEDIUM.yaml",
    "decision": "add",
    "stage": "Preparation timing of the two later additions",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": {
      "CuSO4_dose_ml": 2.5,
      "CuSO4_strength_M": 1.0,
      "succinate_dose_ml": 10,
      "succinate_percent": 40,
      "percent_basis": "unspecified"
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 final preparation sentence",
        "exact_source_quote": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution, \nboth sterilized by filtration.",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      }
    ],
    "explanation": "The DSMZ owner already preserves the exact preparation sentence; the KOMODO owner and target omit it. Attach narrow evidence at the existing owner stage and add missing context elsewhere. Do not invent autoclave temperature, time or filtration pore size."
  },
  {
    "decision_id": "q34",
    "claim": "Post-autoclave filtration/timing in alcaligenes_medium.yaml",
    "decision": "evidence_only",
    "stage": "Preparation timing of the two later additions",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution, both sterilized by filtration."
          }
        ]
      }
    ],
    "source_amount": {
      "CuSO4_dose_ml": 2.5,
      "CuSO4_strength_M": 1.0,
      "succinate_dose_ml": 10,
      "succinate_percent": 40,
      "percent_basis": "unspecified"
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 final preparation sentence",
        "exact_source_quote": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution, \nboth sterilized by filtration.",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      }
    ],
    "explanation": "The DSMZ owner already preserves the exact preparation sentence; the KOMODO owner and target omit it. Attach narrow evidence at the existing owner stage and add missing context elsewhere. Do not invent autoclave temperature, time or filtration pore size."
  },
  {
    "decision_id": "q35",
    "claim": "SL-7 solvent and main-volume accounting",
    "decision": "conflict",
    "stage": "Supplied liquid inputs versus provider-declared main volume",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution, both sterilized by filtration."
          }
        ]
      }
    ],
    "source_amount": {
      "primary_listed_main_liquids_ml": [
        988.5,
        1,
        2.5,
        10
      ],
      "arithmetic_sum_ml": 1002,
      "provider_main_volume_ml": 1000,
      "stock_water_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 main water row",
        "exact_source_quote": "Distilled water 988.500 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 main stock-dose row",
        "exact_source_quote": "Trace element solution SL 7 1.000 ml",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "dsmz660",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf",
        "source_locator": "DSMZ660 page1 final additions",
        "exact_source_quote": "After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution,",
        "snapshot_sha256": "9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e",
        "parsed_text_sha256": "4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a"
      },
      {
        "source_key": "mediadive660api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/660",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a"
      }
    ],
    "explanation": "988.5+1+2.5+10=1002 mL of listed inputs differs from the provider main volume1000 mL. Preserve both source statements; do not infer measured final volume, change water to force a total, or silently divide all quantities by1.002 L."
  }
]

### Stock boundary, percentage and volume conflicts

quantity: concern. Targets: CultureMech:006238.

Every medium concentration and dependency stock amount is scoped. Eight existing dependency evidence objects are verified only for their own stock/water claims. Source1 mL SL-7 dose, post-autoclave additions and1002 mL listed-liquid sum remain distinct from provider1000 mL. HCl25% and succinate40% lack a specified percentage basis.

### Hydrate correspondence versus source specificity

grounding: concern. Targets: CultureMech:006238.

Source Na2HPO4 dodecahydrate and NiCl2 hexahydrate conflict with the asserted anhydrous structures CHEBI:34683 and34887. Other stated hydrate formulas match their captured structures. Sodium-succinate anhydrous identity is more specific than the primary; its form remains unestablished rather than proven wrong. Generic molecular HCl does not establish25% solution composition. No replacement identifier is guessed.

### Defined classification and source mixtures

scope: concern. Targets: CultureMech:006238.

CHEBI:31604 explicitly describes ferric ammonium citrate as a mixture of indefinite composition. Provider complex_medium=no is a catalog classification, not proof that every ingredient has a unique chemical composition. The local DEFINED medium/composition claims need qualification.

## Findings

### f1: Stock strengths are represented as direct main-medium concentrations

blocker / open / confirmed; issue key: DSM660-flattened-stocks.

Eight SL-7 stock rows appear directly in all three medium ingredient lists. The explicit1 mL stock dose is missing, and later CuSO4/succinate stocks are reduced to provider-derived masses. This changes preparation-stage meaning and the represented formulation.

### f2: Two explicit source hydrates map to anhydrous structures

major / open / confirmed; issue key: DSM660-hydrate-grounding.

Na2HPO4 x12H2O is mapped to disodium hydrogenphosphate CHEBI:34683 and NiCl2 x6H2O to nickel dichloride CHEBI:34887. Captured structures omit the stated waters of hydration. Label validity and stock amount evidence do not verify source form.

### f3: Preparation and narrow evidence are incomplete or lost across layers

major / open / confirmed; issue key: DSM660-preparation-evidence.

Main water and stock addition context are missing; the DSMZ owner alone retains the later filtration/timing sentence. No medium ingredient has attached amount evidence. Existing standalone stock evidence does not support flattened medium values.

### f4: Fully defined classification overstates mixture composition

major / open / confirmed; issue key: DSM660-defined-mixture.

The recipe contains ferric ammonium citrate, whose asserted term explicitly denotes an indefinite mixture. The two local DEFINED fields and provider binary classification do not establish a unique chemical formulation.

### f5: Historical timestamp formatting is inconsistent

minor / open / confirmed; issue key: DSM660-history-timestamps.

The KOMODO-derived target/owner retain a malformed fractional timestamp and a timezone-naive enrichment timestamp. These are historical metadata defects, separate from source formulation correctness.

## Recommended Actions And Acceptance Checks

### a1

Restore the separate SL-7 recipe and1 mL addition plus the two later stock doses/strengths. Preserve all source-specific basis limits and separately verified stock evidence; never treat stock g/L as main-medium g/L.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify exact supplied hydrates and repair primary/secondary correspondence in maintained inputs with evidence. Keep source-unspecified succinate form unresolved; do not guess replacements.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach exact main and stock evidence separately, preserve the correct DSMZ preparation sentence, and carry it through authorized regeneration without inventing unspecified sterilization parameters.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Qualify medium/composition classification for the indefinite ingredient and preserve the named source mixture; do not decompose it into invented exact salts.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve append-only history and add an explicit provenance clarification through an authorized maintenance path; do not silently fabricate missing timezones or rewrite old events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/alcaligenes_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch020/194/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/194/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml:1:id: CultureMech:006238<br>./data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml:1:id: CultureMech:006238<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/194/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 25 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| fresh-context | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/194/source-context-current.json; Fresh input hashes and explicit old/new schema/project.justfile transition | context_only | Current repository inputs come from the fresh native inspection and reviewed context transition. Original evidence-context remains a provisional historical snapshot; public source bytes and actual access times are unchanged. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf; Exact collection accession and complete formulation/preparation source | supports | CultureMech:006238 is the generated KOMODO660/DSMZ660 source-duplicate record with exactly two explicit owners. Stable parent/child IDs and paths resolve. Current DSMZ660 PDF and MediaDive660 independently support the exact base formulation; no historical KOMODO full-recipe equivalence is inferred from the unavailable detail page. |
| provider | https://mediadive.dsmz.de/rest/medium/660; Complete exact provider response; identity, original units and recipe/stock boundaries | supports | CultureMech:006238 is the generated KOMODO660/DSMZ660 source-duplicate record with exactly two explicit owners. Stable parent/child IDs and paths resolve. Current DSMZ660 PDF and MediaDive660 independently support the exact base formulation; no historical KOMODO full-recipe equivalence is inferred from the unavailable detail page. |
| history-metadata | data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml; data/normalized_yaml/bacterial/alcaligenes_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:07.244701"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:07.244701"}]}, {"input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml", "events": 6, "timestamp_issues": []}] |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi23414 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23414; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:23414 resolves to copper(II) sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31604 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31604 resolves to ferric ammonium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32149 resolves to sodium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63675 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63675 resolves to sodium succinate (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:9754 resolves to tris. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:23414": [{"label": "CuSO4", "match_type": "preferred_term", "identifier": "CHEBI:23414", "preferred_term": "CuSO4", "ontology_id": "CHEBI:23414", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31604": [{"label": "Ferric ammonium citrate", "match_type": "preferred_term", "identifier": "CHEBI:31604", "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label": "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term": "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63675": [{"label": "Sodium succinate", "match_type": "preferred_term", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754": [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| stock-record | data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml; Complete referenced standalone SL-7 context, including all nine composition rows, evidence, history and placeholder ingredient | context_only | Dependency context only; not a second reviewed target. Eight existing amount excerpts are tested at their stock or water-addition scope and are never inherited by the medium. |
| stock-source | https://mediadive.dsmz.de/rest/solution/1392; $.data identity, volume, all nine recipe objects and equipment | supports | Exact standalone solution1392 resolves to SL-7. Its scientific recipe fields agree with the embedded stock in MediaDive660; distinct raw payload hashes and actual access dates remain preserved. |
| stock-water-term | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS water metadata | supports | Dependency water CHEBI:15377 resolves to the asserted label; it does not turn a water input into a measured final volume. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch020/194/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| komodo-row | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact660 row and full table header | supports | {"header": ["ID", "Name", "PH Info", "Is Complex", "Is Aerobic", "Is SubMedium", "Instructions"], "row": ["660", "ALCALIGENES MEDIUM", "null", "false", "false", "false", "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf"]} Catalog oxygen flags are metadata, not experimental physiology. |
| komodo660-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=660; Preserved exact public retrieval result | context_only | The exact historical KOMODO660 detail page returned403. Current base identity, stable source mapping, DSMZ formulation and provider are independently resolved. Historical full import bytes are optional provenance context; no inaccessible variant is asserted. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main recipe rows and stock additions; resolver/source-copy context and exact stock-evidence writer are read without execution. Current formulation guard rejects incompatible preparation/evidence inputs; old copied signatures are not proof of lossless source equivalence. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main recipe rows and stock additions; resolver/source-copy context and exact stock-evidence writer are read without execution. Current formulation guard rejects incompatible preparation/evidence inputs; old copied signatures are not proof of lossless source equivalence. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main recipe rows and stock additions; resolver/source-copy context and exact stock-evidence writer are read without execution. Current formulation guard rejects incompatible preparation/evidence inputs; old copied signatures are not proof of lossless source equivalence. |
| writer-3 | scripts/repair_mediadive_stock_concentration_evidence.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer separates main recipe rows and stock additions; resolver/source-copy context and exact stock-evidence writer are read without execution. Current formulation guard rejects incompatible preparation/evidence inputs; old copied signatures are not proof of lossless source equivalence. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No organism, strain, optimum, safety or growth-performance claim is inferred from the medium name or generic Microbial cultivation application. No unasserted chemical form or replacement identifier is guessed.
- The exact historical KOMODO660 detail page returned403. Current base identity, stable source mapping, DSMZ formulation and provider are independently resolved. Historical full import bytes are optional provenance context; no inaccessible variant is asserted.
- The current primary does not resolve percent bases or measured final volume. Optional historical KOMODO403 is retained without blocking the independently resolved base formulation. The standalone stock is dependency context only; no second record is formally assessed or saved.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121916Z-culturemech-006238-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alcaligenes_medium (CultureMech:006238)'
started_at: '2026-10-21T12:11:53Z'
finished_at: '2026-10-21T12:19:16Z'
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
summary: DSMZ660 Alcaligenes Medium and both normalized contributors resolve, but
  stock-strength rows are flattened into the main medium, post-autoclave stock additions
  are reduced to derived masses, hydrate mappings disagree with the source, and the
  fully defined classification is too strong for ferric ammonium citrate. Exact source
  amounts, provider denominators and eight existing dependency evidence objects are
  kept separate.
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
  - path: data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
    sha256: b411c6e30ead8f2582994d7e7caccf7bf3751338d8a559a43f34374050002eb5
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    sha256: 018202410b03c111ef474def8ebbc8265af438890698bc0e71b421ab2031d596
    role: context
  - path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
    sha256: e4489a6e6374f1a9cd9948620100282da08f2c7be0b055b05d4334080da1f716
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml
    sha256: 3c71920e6d06d1cd4037282b875de570c23d811f52151727f2708a47604687fc
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
  selection: Task review 194; batch 020 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nineteen task batches
    contain 190 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 193 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006238
targets:
- target_id: CultureMech:006238
  path: data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  label: alcaligenes_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch020/194/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/194/strict.tsv"
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006238
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
  - CultureMech:006238
- check_id: komodo660-source-access
  name: 'Exact source content access: komodo660'
  required: false
  status: unavailable
  summary: The exact historical KOMODO660 detail page returned403. Current base identity,
    stable source mapping, DSMZ formulation and provider are independently resolved.
    Historical full import bytes are optional provenance context; no inaccessible
    variant is asserted.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - komodo660-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:46.732455Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch020/194/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:48.209090Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/194/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:49.696350Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:50.720534Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:19:14Z'
  support: supports
  summary: './data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml:1:id: CultureMech:006238

    ./data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml:1:id: CultureMech:006238

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/194/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:19:14Z'
  support: supports
  summary: 25 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 388e689176fe33000a7fa8b934b3c24ca4e726fa7ec5c842e066a01e95162f1e
- evidence_id: fresh-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/194/source-context-current.json
  locator: Fresh input hashes and explicit old/new schema/project.justfile transition
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Current repository inputs come from the fresh native inspection and reviewed
    context transition. Original evidence-context remains a provisional historical
    snapshot; public source bytes and actual access times are unchanged.
  snapshot_sha256: f3db44ca27f8cfbba42883c710478517640639ff98e8b4cc423474afd0a87462
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf
  locator: Exact collection accession and complete formulation/preparation source
  accessed_at: '2026-10-21T11:55:11.397805Z'
  support: supports
  summary: CultureMech:006238 is the generated KOMODO660/DSMZ660 source-duplicate
    record with exactly two explicit owners. Stable parent/child IDs and paths resolve.
    Current DSMZ660 PDF and MediaDive660 independently support the exact base formulation;
    no historical KOMODO full-recipe equivalence is inferred from the unavailable
    detail page.
  snapshot_sha256: 9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/660
  locator: Complete exact provider response; identity, original units and recipe/stock
    boundaries
  accessed_at: '2026-10-21T11:55:10.842401Z'
  support: supports
  summary: CultureMech:006238 is the generated KOMODO660/DSMZ660 source-duplicate
    record with exactly two explicit owners. Stable parent/child IDs and paths resolve.
    Current DSMZ660 PDF and MediaDive660 independently support the exact base formulation;
    no historical KOMODO full-recipe equivalence is inferred from the unavailable
    detail page.
  snapshot_sha256: 315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml;
    data/normalized_yaml/bacterial/alcaligenes_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:07.244701"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:07.244701"}]}, {"input": "data/normalized_yaml/bacterial/alcaligenes_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
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
- evidence_id: chebi23414
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23414
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:55:12.180406Z'
  support: supports
  summary: CHEBI:23414 resolves to copper(II) sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 7f9d81f59ca2cbe7614d7e0dd3f85cb578000bf273b1b93968e74054e475fee1
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
- evidence_id: chebi31604
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31604
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:44.987529Z'
  support: supports
  summary: CHEBI:31604 resolves to ferric ammonium citrate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 31acf125b469ffd64e2de503550d29336a7a0f99c8a3ea24b80b53bdb715e7f8
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
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
- evidence_id: chebi63675
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:41.075057Z'
  support: supports
  summary: CHEBI:63675 resolves to sodium succinate (anhydrous). Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 4c54df9f2d63f54dea26d64e4ec9fedeb486c2c2abe44b70c5c621512f1fdd3c
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
- evidence_id: chebi9754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:13.713319Z'
  support: supports
  summary: CHEBI:9754 resolves to tris. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:19:14Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17883":
    [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883",
    "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:23414": [{"label": "CuSO4", "match_type": "preferred_term",
    "identifier": "CHEBI:23414", "preferred_term": "CuSO4", "ontology_id": "CHEBI:23414",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label":
    "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31604": [{"label":
    "Ferric ammonium citrate", "match_type": "preferred_term", "identifier": "CHEBI:31604",
    "preferred_term": "Ferric ammonium citrate", "ontology_id": "CHEBI:31604", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type":
    "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id":
    "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588":
    [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588",
    "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34683": [{"label":
    "Na2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:34683", "preferred_term":
    "Na2HPO4", "ontology_id": "CHEBI:34683", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label":
    "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term":
    "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type":
    "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride
    hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63675": [{"label": "Sodium succinate", "match_type": "preferred_term",
    "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id":
    "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213":
    [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term":
    "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity":
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
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754":
    [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754",
    "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: stock-record
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml
  locator: Complete referenced standalone SL-7 context, including all nine composition
    rows, evidence, history and placeholder ingredient
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Dependency context only; not a second reviewed target. Eight existing amount
    excerpts are tested at their stock or water-addition scope and are never inherited
    by the medium.
  snapshot_sha256: 3c71920e6d06d1cd4037282b875de570c23d811f52151727f2708a47604687fc
- evidence_id: stock-source
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1392
  locator: $.data identity, volume, all nine recipe objects and equipment
  accessed_at: '2026-10-21T11:55:47.046380Z'
  support: supports
  summary: Exact standalone solution1392 resolves to SL-7. Its scientific recipe fields
    agree with the embedded stock in MediaDive660; distinct raw payload hashes and
    actual access dates remain preserved.
  snapshot_sha256: edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c
- evidence_id: stock-water-term
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS water metadata
  accessed_at: '2026-10-21T08:17:26.097802Z'
  support: supports
  summary: Dependency water CHEBI:15377 resolves to the asserted label; it does not
    turn a water input into a measured final volume.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/194/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 4f258536fe3976a518613d198197e037ea8ebcf9472f4f1f1a8c6e734d1af3ed
- evidence_id: komodo-row
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact660 row and full table header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: '{"header": ["ID", "Name", "PH Info", "Is Complex", "Is Aerobic", "Is SubMedium",
    "Instructions"], "row": ["660", "ALCALIGENES MEDIUM", "null", "false", "false",
    "false", "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf"]} Catalog
    oxygen flags are metadata, not experimental physiology.'
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo660-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=660
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:55:10.651056Z'
  support: context_only
  summary: The exact historical KOMODO660 detail page returned403. Current base identity,
    stable source mapping, DSMZ formulation and provider are independently resolved.
    Historical full import bytes are optional provenance context; no inaccessible
    variant is asserted.
  snapshot_sha256: 8276270cfd0fd71ec33782a0a632d4169086985f0c5ba1d1349879481652dbd5
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Current importer separates main recipe rows and stock additions; resolver/source-copy
    context and exact stock-evidence writer are read without execution. Current formulation
    guard rejects incompatible preparation/evidence inputs; old copied signatures
    are not proof of lossless source equivalence.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Current importer separates main recipe rows and stock additions; resolver/source-copy
    context and exact stock-evidence writer are read without execution. Current formulation
    guard rejects incompatible preparation/evidence inputs; old copied signatures
    are not proof of lossless source equivalence.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Current importer separates main recipe rows and stock additions; resolver/source-copy
    context and exact stock-evidence writer are read without execution. Current formulation
    guard rejects incompatible preparation/evidence inputs; old copied signatures
    are not proof of lossless source equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: scripts/repair_mediadive_stock_concentration_evidence.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:19:14Z'
  support: context_only
  summary: Current importer separates main recipe rows and stock additions; resolver/source-copy
    context and exact stock-evidence writer are read without execution. Current formulation
    guard rejects incompatible preparation/evidence inputs; old copied signatures
    are not proof of lossless source equivalence.
  snapshot_sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source identity and maintained ownership
  outcome: supported
  summary: CultureMech:006238 is the generated KOMODO660/DSMZ660 source-duplicate
    record with exactly two explicit owners. Stable parent/child IDs and paths resolve.
    Current DSMZ660 PDF and MediaDive660 independently support the exact base formulation;
    no historical KOMODO full-recipe equivalence is inferred from the unavailable
    detail page.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - primary
  - provider
  - owner-0
  - owner-1
- assessment_id: scope-classification
  area: scope
  topic: Classification, conditions and organism scope
  outcome: supported
  summary: LIQUID fits the absence of an agar addition. Bacterial organization and
    generic cultivation do not establish a strain-specific growth or oxygen phenotype.
    DEFINED is qualified separately because ferric ammonium citrate is an indefinite
    mixture.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - primary
  - provider
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 22 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '19 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 19/19 primary and 19/19 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi17883
  - chebi23414
  - chebi26710
  - chebi31206
  - chebi31604
  - chebi32149
  - chebi32588
  - chebi33118
  - chebi34683
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi63675
  - chebi75213
  - chebi86158
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi9754
  details: 'Instance coverage on a 0–100 percent scale, denominator 19: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 35 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"Tris\",\n    \"\
    decision\": \"evidence_only\",\n    \"stage\": \"Basal main recipe; provider-declared\
    \ 1000 mL basis\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 6.06,\n\
    \      \"provider_amount\": 6.06,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 6.06,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Tris 6.060 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Tris\\\",\\n                        \\\"compound_id\\\": 73,\\\
    n                        \\\"amount\\\": 6.06,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 6.06,\\n         \
    \               \\\"mmol_l\\\": 50.0248,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The three medium layers store the matching\
    \ provider-declared value without attached evidence. Preserve primary batch masses\
    \ and the provider denominator separately; explicit listed liquid inputs total1002\
    \ mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding\
    \ form is assessed independently.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n\
    \    \"claim\": \"NaCl\",\n    \"decision\": \"evidence_only\",\n    \"stage\"\
    : \"Basal main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.68\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.68\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.68\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 4.68,\n\
    \      \"provider_amount\": 4.68,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 4.68,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"NaCl 4.680 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 4.68,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 4.68,\\n         \
    \               \\\"mmol_l\\\": 80.0821,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The three medium layers store the matching\
    \ provider-declared value without attached evidence. Preserve primary batch masses\
    \ and the provider denominator separately; explicit listed liquid inputs total1002\
    \ mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding\
    \ form is assessed independently.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n\
    \    \"claim\": \"KCl\",\n    \"decision\": \"evidence_only\",\n    \"stage\"\
    : \"Basal main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 1.49,\n\
    \      \"provider_amount\": 1.49,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 1.49,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"KCl 1.490 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 1.49,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.49,\\n         \
    \               \\\"mmol_l\\\": 19.9866,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The three medium layers store the matching\
    \ provider-declared value without attached evidence. Preserve primary batch masses\
    \ and the provider denominator separately; explicit listed liquid inputs total1002\
    \ mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding\
    \ form is assessed independently.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n\
    \    \"claim\": \"NH4Cl\",\n    \"decision\": \"evidence_only\",\n    \"stage\"\
    : \"Basal main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 1.07,\n\
    \      \"provider_amount\": 1.07,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 1.07,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"NH4Cl 1.070 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 1.07,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.07,\\n         \
    \               \\\"mmol_l\\\": 20.0037,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The three medium layers store the matching\
    \ provider-declared value without attached evidence. Preserve primary batch masses\
    \ and the provider denominator separately; explicit listed liquid inputs total1002\
    \ mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding\
    \ form is assessed independently.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n\
    \    \"claim\": \"Na2SO4\",\n    \"decision\": \"evidence_only\",\n    \"stage\"\
    : \"Basal main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.43\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.43\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.43\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 0.43,\n\
    \      \"provider_amount\": 0.43,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 0.43,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Na2SO4 0.430 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na2SO4\\\",\\n                        \\\"compound_id\\\": 110,\\\
    n                        \\\"amount\\\": 0.43,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.43,\\n         \
    \               \\\"mmol_l\\\": 3.02732,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The three medium layers store the matching\
    \ provider-declared value without attached evidence. Preserve primary batch masses\
    \ and the provider denominator separately; explicit listed liquid inputs total1002\
    \ mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding\
    \ form is assessed independently.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n\
    \    \"claim\": \"MgCl2 x 6 H2O\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"stage\": \"Basal main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 0.2,\n \
    \     \"provider_amount\": 0.2,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 0.2,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 basal composition exact ingredient\
    \ row\",\n        \"exact_source_quote\": \"MgCl2 x 6 H2O 0.200 g\",\n       \
    \ \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 0.983753,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"The three medium layers store the matching provider-declared\
    \ value without attached evidence. Preserve primary batch masses and the provider\
    \ denominator separately; explicit listed liquid inputs total1002 mL, so no measured\
    \ final1000 mL or automatic renormalization is inferred. Grounding form is assessed\
    \ independently.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"claim\": \"\
    CaCl2 x 2 H2O\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Basal\
    \ main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 0.03,\n\
    \      \"provider_amount\": 0.03,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 0.03,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.030 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.03,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.03,\\n\
    \                        \\\"mmol_l\\\": 0.204061,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"The three medium layers store the matching provider-declared\
    \ value without attached evidence. Preserve primary batch masses and the provider\
    \ denominator separately; explicit listed liquid inputs total1002 mL, so no measured\
    \ final1000 mL or automatic renormalization is inferred. Grounding form is assessed\
    \ independently.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"claim\": \"\
    Na2HPO4 x 12 H2O\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Basal\
    \ main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.23\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 0.23,\n\
    \      \"provider_amount\": 0.23,\n      \"provider_unit\": \"g\",\n      \"provider_g_l\"\
    : 0.23,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Na2HPO4 x 12 H2O 0.230 g\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2HPO4 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 95,\\n                        \\\"amount\\\": 0.23,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.23,\\\
    n                        \\\"mmol_l\\\": 1.62019,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"The three medium layers store the matching provider-declared\
    \ value without attached evidence. Preserve primary batch masses and the provider\
    \ denominator separately; explicit listed liquid inputs total1002 mL, so no measured\
    \ final1000 mL or automatic renormalization is inferred. Grounding form is assessed\
    \ independently.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"claim\": \"\
    Fe(NH4)citrate\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Basal\
    \ main recipe; provider-declared 1000 mL basis\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": {\n      \"primary_mass_g\": 0.005,\n\
    \      \"provider_amount\": 5,\n      \"provider_unit\": \"mg\",\n      \"provider_g_l\"\
    : 0.005,\n      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 basal composition exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Fe(III)(NH4)citrate 0.005 g\",\n        \"\
    snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Fe(NH4)citrate\\\",\\n                        \\\"compound_id\\\
    \": 1203,\\n                        \\\"amount\\\": 5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The three medium layers store the matching\
    \ provider-declared value without attached evidence. Preserve primary batch masses\
    \ and the provider denominator separately; explicit listed liquid inputs total1002\
    \ mL, so no measured final1000 mL or automatic renormalization is inferred. Grounding\
    \ form is assessed independently.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n\
    \    \"claim\": \"CuSO4 addition and strength\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Separately filter-sterilized stock added after autoclaving\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.399025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.399025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.399025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_amount\": {\n      \"dose_ml\": 2.5,\n\
    \      \"stock_strength\": \"1.0 M\",\n      \"provider_derived_g_l\": 0.399025\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 final preparation sentence\",\n\
    \        \"exact_source_quote\": \"After autoclaving add 2.5 ml 1.0 M CuSO4 and\
    \ 10 ml of a 40% Na-succinate solution,\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"CuSO4\\\",\\n                        \\\"compound_id\\\":\
    \ 636,\\n                        \\\"attribute\\\": \\\"1 M, sterilized by filtration\\\
    \",\\n                        \\\"amount\\\": 2.5,\\n                        \\\
    \"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.399025,\\n  \
    \                      \\\"mmol_l\\\": 2.5,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"Restore explicit stock strength, addition\
    \ volume and timing. Existing provider-derived g/L is not proof of a neat mass\
    \ addition. CuSO4 source molarity does not identify a weighed hydrate; sodium-succinate40%\
    \ does not specify w/v or another basis. Do not invent density, form or an independently\
    \ measured final denominator.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n  \
    \  \"claim\": \"Na-succinate addition and strength\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Separately filter-sterilized stock added after autoclaving\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"dose_ml\": 10,\n      \"stock_strength\"\
    : \"40% (basis unspecified)\",\n      \"provider_derived_g_l\": 4\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 final preparation sentence\",\n\
    \        \"exact_source_quote\": \"After autoclaving add 2.5 ml 1.0 M CuSO4 and\
    \ 10 ml of a 40% Na-succinate solution,\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Sodium succinate\\\",\\n                        \\\"compound_id\\\
    \": 730,\\n                        \\\"attribute\\\": \\\"40 %, sterilized by\
    \ filtration\\\",\\n                        \\\"amount\\\": 10,\\n           \
    \             \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\"\
    : 4,\\n                        \\\"mmol_l\\\": 24.6837,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n     \
    \ }\n    ],\n    \"explanation\": \"Restore explicit stock strength, addition\
    \ volume and timing. Existing provider-derived g/L is not proof of a neat mass\
    \ addition. CuSO4 source molarity does not identify a weighed hydrate; sodium-succinate40%\
    \ does not specify w/v or another basis. Do not invent density, form or an independently\
    \ measured final denominator.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n  \
    \  \"claim\": \"HCl flattened stock row\",\n    \"decision\": \"correct\",\n \
    \   \"stage\": \"SL-7 stock composition, not a direct main-medium addition\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 1,\n \
    \     \"stock_unit\": \"ml\",\n      \"stock_attribute\": \"25%\",\n      \"provider_stock_g_l\"\
    : 0.25,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"HCl (25%) 1.000 ml\",\n\
    \        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"g_l\\\": 0.25,\\n                        \\\"mmol_l\\\
    \": 6.85683,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"All three medium layers incorrectly\
    \ use stock-strength g/L as direct main amounts. Preserve the separate stock and\
    \ its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations.\
    \ For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"claim\": \"ZnCl2 flattened stock row\",\n    \"decision\": \"\
    correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 70,\n\
    \      \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.07,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"ZnCl2 70.000 mg\",\n \
    \       \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"ZnCl2\\\",\\n                        \\\"compound_id\\\": 64,\\\
    n                        \\\"amount\\\": 70,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.07,\\n              \
    \          \\\"mmol_l\\\": 0.513573,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"All three medium layers incorrectly\
    \ use stock-strength g/L as direct main amounts. Preserve the separate stock and\
    \ its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations.\
    \ For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"claim\": \"MnCl2 x 4 H2O flattened stock row\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 100,\n   \
    \   \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.1,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 100.000\
    \ mg\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.505293,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"All three medium layers incorrectly use stock-strength\
    \ g/L as direct main amounts. Preserve the separate stock and its1 mL addition;\
    \ do not inherit standalone evidence onto receiving-medium concentrations. For\
    \ HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"claim\": \"H3BO3 flattened stock row\",\n    \"decision\": \"\
    correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 60,\n\
    \      \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.06,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"H3BO3 60.000 mg\",\n \
    \       \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 60,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.06,\\n              \
    \          \\\"mmol_l\\\": 0.970246,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"All three medium layers incorrectly\
    \ use stock-strength g/L as direct main amounts. Preserve the separate stock and\
    \ its1 mL addition; do not inherit standalone evidence onto receiving-medium concentrations.\
    \ For HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"claim\": \"CoCl2 x 6 H2O flattened stock row\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 200,\n   \
    \   \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.2,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 200.000\
    \ mg\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 200,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.54037,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"All three medium layers incorrectly use stock-strength\
    \ g/L as direct main amounts. Preserve the separate stock and its1 mL addition;\
    \ do not inherit standalone evidence onto receiving-medium concentrations. For\
    \ HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"claim\": \"CuCl2 x 2 H2O flattened stock row\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 20,\n\
    \      \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.02,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"CuCl2 x 2 H2O 20.000 mg\"\
    ,\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.117314,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"All three medium layers incorrectly use stock-strength\
    \ g/L as direct main amounts. Preserve the separate stock and its1 mL addition;\
    \ do not inherit standalone evidence onto receiving-medium concentrations. For\
    \ HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"claim\": \"NiCl2 x 6 H2O flattened stock row\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 20,\n\
    \      \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.02,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 20.000 mg\"\
    ,\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 20,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.154322,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"All three medium layers incorrectly use stock-strength\
    \ g/L as direct main amounts. Preserve the separate stock and its1 mL addition;\
    \ do not inherit standalone evidence onto receiving-medium concentrations. For\
    \ HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"claim\": \"Na2MoO4 x 2 H2O flattened stock row\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"SL-7 stock composition, not a direct main-medium\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"stock_amount\": 40,\n\
    \      \"stock_unit\": \"mg\",\n      \"stock_attribute\": null,\n      \"provider_stock_g_l\"\
    : 0.04,\n      \"provider_stock_volume_ml\": 1000,\n      \"main_stock_addition_ml\"\
    : 1\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 Trace element solution SL-7 subsection\
    \ exact named row\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 40.000\
    \ mg\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 40,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.04,\\n \
    \                       \\\"mmol_l\\\": 0.165323,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"All three medium layers incorrectly use stock-strength\
    \ g/L as direct main amounts. Preserve the separate stock and its1 mL addition;\
    \ do not inherit standalone evidence onto receiving-medium concentrations. For\
    \ HCl,25% basis is unspecified and provider0.25 g/L is not independently derived\
    \ from primary density or percent convention.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"claim\": \"SL-7 addition to main recipe\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"Main recipe stock dose\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"dose\": 1.0,\n      \"unit\": \"ml\"\
    ,\n      \"stock\": \"SL-7\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 main SL-7 addition row\",\n   \
    \     \"exact_source_quote\": \"Trace element solution SL 7 1.000 ml\",\n    \
    \    \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"solution\\\": \\\"Trace element solution SL-7\\\",\\n                      \
    \  \\\"solution_id\\\": 1392,\\n                        \\\"amount\\\": 1,\\n\
    \                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\n      }\n\
    \    ],\n    \"explanation\": \"All medium layers lack the explicit stock-addition\
    \ object. The source supports a1 mL dose of the separately specified stock, not\
    \ the stock component concentrations directly in the receiving medium.\"\n  },\n\
    \  {\n    \"decision_id\": \"q21\",\n    \"claim\": \"Main water input\",\n  \
    \  \"decision\": \"add\",\n    \"stage\": \"Basal recipe supplied water\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"After autoclaving add 2.5 ml 1.0 M CuSO4 and 10\
    \ ml of a 40% Na-succinate solution, both sterilized by filtration.\"\n      \
    \    }\n        ]\n      }\n    ],\n    \"source_amount\": {\n      \"value\"\
    : 988.5,\n      \"unit\": \"ml\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 basal water row\",\n        \"\
    exact_source_quote\": \"Distilled water 988.500 ml\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 988.5,\\n                   \
    \     \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The source water input is absent from\
    \ all medium layers. The DSMZ owner already has a different post-autoclave preparation\
    \ sentence; its existing content is preserved in the exact local locator.\"\n\
    \  },\n  {\n    \"decision_id\": \"q22\",\n    \"claim\": \"Standalone SL-7 HCl\"\
    ,\n    \"decision\": \"unsupported\",\n    \"stage\": \"Standalone stock concentration\
    \ or supplied-water dose; context only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"amount\": 1,\n      \"\
    unit\": \"ml\",\n      \"attribute\": \"25%\",\n      \"provider_g_l\": 0.25,\n\
    \      \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"HCl (25%) 1.000 ml\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"g_l\\\": 0.25,\\n                        \\\"mmol_l\\\
    \": 6.85683,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The HCl0.25 g/L is a provider interpretation\
    \ without attached evidence and the primary only gives1 mL of25% reagent. Percentage\
    \ basis and density are unstated; no independent mass conversion or replacement\
    \ number is justified.\"\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"claim\"\
    : \"Standalone SL-7 ZnCl2\",\n    \"decision\": \"verified\",\n    \"stage\":\
    \ \"Standalone stock concentration or supplied-water dose; context only\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"amount\": 70,\n      \"\
    unit\": \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.07,\n \
    \     \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"ZnCl2 70.000 mg\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[1]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 2,\\n                \\\"compound\\\": \\\"ZnCl2\\\"\
    ,\\n                \\\"compound_id\\\": 64,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 70,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.07,\\n                \\\"mmol_l\\\": 0.513573,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\
    \n      }\n    ],\n    \"explanation\": \"Attached literal evidence and identical\
    \ historical/current response hash support the existing stock g/L value; for water,1000\
    \ mL /1000=1 L is a batch volume, not a final-medium percentage. This does not\
    \ verify chemical grounding or the receiving-medium value.\"\n  },\n  {\n    \"\
    decision_id\": \"q24\",\n    \"claim\": \"Standalone SL-7 MnCl2 x 4 H2O\",\n \
    \   \"decision\": \"verified\",\n    \"stage\": \"Standalone stock concentration\
    \ or supplied-water dose; context only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"amount\": 100,\n      \"unit\"\
    : \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.1,\n      \"\
    provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 100.000 mg\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[2]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 3,\\n                \\\"compound\\\": \\\"MnCl2 x 4\
    \ H2O\\\",\\n                \\\"compound_id\\\": 36,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 100,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\": 0.505293,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\n     \
    \ }\n    ],\n    \"explanation\": \"Attached literal evidence and identical historical/current\
    \ response hash support the existing stock g/L value; for water,1000 mL /1000=1\
    \ L is a batch volume, not a final-medium percentage. This does not verify chemical\
    \ grounding or the receiving-medium value.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q25\",\n    \"claim\": \"Standalone SL-7 H3BO3\",\n    \"decision\": \"verified\"\
    ,\n    \"stage\": \"Standalone stock concentration or supplied-water dose; context\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.06\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"amount\": 60,\n      \"\
    unit\": \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.06,\n \
    \     \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"H3BO3 60.000 mg\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[3]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 4,\\n                \\\"compound\\\": \\\"H3BO3\\\"\
    ,\\n                \\\"compound_id\\\": 37,\\n                \\\"solution\\\"\
    : null,\\n                \\\"solution_id\\\": null,\\n                \\\"condition\\\
    \": null,\\n                \\\"attribute\\\": null,\\n                \\\"amount\\\
    \": 60,\\n                \\\"unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\
    \": 0.06,\\n                \\\"mmol_l\\\": 0.970246,\\n                \\\"optional\\\
    \": 0\\n            }\",\n        \"snapshot_sha256\": \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\
    \n      }\n    ],\n    \"explanation\": \"Attached literal evidence and identical\
    \ historical/current response hash support the existing stock g/L value; for water,1000\
    \ mL /1000=1 L is a batch volume, not a final-medium percentage. This does not\
    \ verify chemical grounding or the receiving-medium value.\"\n  },\n  {\n    \"\
    decision_id\": \"q26\",\n    \"claim\": \"Standalone SL-7 CoCl2 x 6 H2O\",\n \
    \   \"decision\": \"verified\",\n    \"stage\": \"Standalone stock concentration\
    \ or supplied-water dose; context only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"amount\": 200,\n      \"unit\"\
    : \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.2,\n      \"\
    provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 200.000 mg\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[4]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 5,\\n                \\\"compound\\\": \\\"CoCl2 x 6\
    \ H2O\\\",\\n                \\\"compound_id\\\": 38,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 200,\\n                \\\"unit\\\": \\\"mg\\\",\\n    \
    \            \\\"g_l\\\": 0.2,\\n                \\\"mmol_l\\\": 1.54037,\\n \
    \               \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\n     \
    \ }\n    ],\n    \"explanation\": \"Attached literal evidence and identical historical/current\
    \ response hash support the existing stock g/L value; for water,1000 mL /1000=1\
    \ L is a batch volume, not a final-medium percentage. This does not verify chemical\
    \ grounding or the receiving-medium value.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q27\",\n    \"claim\": \"Standalone SL-7 CuCl2 x 2 H2O\",\n    \"decision\"\
    : \"verified\",\n    \"stage\": \"Standalone stock concentration or supplied-water\
    \ dose; context only\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"amount\": 20,\n      \"\
    unit\": \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.02,\n \
    \     \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"CuCl2 x 2 H2O 20.000 mg\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[5]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 6,\\n                \\\"compound\\\": \\\"CuCl2 x 2\
    \ H2O\\\",\\n                \\\"compound_id\\\": 39,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 20,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\": 0.117314,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\n     \
    \ }\n    ],\n    \"explanation\": \"Attached literal evidence and identical historical/current\
    \ response hash support the existing stock g/L value; for water,1000 mL /1000=1\
    \ L is a batch volume, not a final-medium percentage. This does not verify chemical\
    \ grounding or the receiving-medium value.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q28\",\n    \"claim\": \"Standalone SL-7 NiCl2 x 6 H2O\",\n    \"decision\"\
    : \"verified\",\n    \"stage\": \"Standalone stock concentration or supplied-water\
    \ dose; context only\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"amount\": 20,\n      \"\
    unit\": \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.02,\n \
    \     \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 20.000 mg\",\n        \"snapshot_sha256\"\
    : \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\",\n    \
    \    \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[6]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 7,\\n                \\\"compound\\\": \\\"NiCl2 x 6\
    \ H2O\\\",\\n                \\\"compound_id\\\": 40,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 20,\\n                \\\"unit\\\": \\\"mg\\\",\\n     \
    \           \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\": 0.154322,\\n\
    \                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\n     \
    \ }\n    ],\n    \"explanation\": \"Attached literal evidence and identical historical/current\
    \ response hash support the existing stock g/L value; for water,1000 mL /1000=1\
    \ L is a batch volume, not a final-medium percentage. This does not verify chemical\
    \ grounding or the receiving-medium value.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q29\",\n    \"claim\": \"Standalone SL-7 Na2MoO4 x 2 H2O\",\n    \"decision\"\
    : \"verified\",\n    \"stage\": \"Standalone stock concentration or supplied-water\
    \ dose; context only\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"amount\": 40,\n      \"\
    unit\": \"mg\",\n      \"attribute\": null,\n      \"provider_g_l\": 0.04,\n \
    \     \"provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 40.000 mg\",\n        \"\
    snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[7]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 8,\\n                \\\"compound\\\": \\\"Na2MoO4 x\
    \ 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 40,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.04,\\n                \\\"mmol_l\\\": 0.165323,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\n     \
    \ }\n    ],\n    \"explanation\": \"Attached literal evidence and identical historical/current\
    \ response hash support the existing stock g/L value; for water,1000 mL /1000=1\
    \ L is a batch volume, not a final-medium percentage. This does not verify chemical\
    \ grounding or the receiving-medium value.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q30\",\n    \"claim\": \"Standalone SL-7 Distilled water\",\n    \"decision\"\
    : \"verified\",\n    \"stage\": \"Standalone stock concentration or supplied-water\
    \ dose; context only\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_amount\": {\n      \"amount\": 1000,\n      \"unit\"\
    : \"ml\",\n      \"attribute\": null,\n      \"provider_g_l\": null,\n      \"\
    provider_volume_ml\": 1000\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 SL-7 subsection exact named row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.000 ml\",\n        \"\
    snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"solution1392\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/1392\",\n        \"source_locator\"\
    : \"$.data.recipe[8]\",\n        \"exact_source_quote\": \"{\\n              \
    \  \\\"recipe_order\\\": 9,\\n                \\\"compound\\\": \\\"Distilled\
    \ water\\\",\\n                \\\"compound_id\\\": 4,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 1000,\\n                \\\"unit\\\": \\\"ml\\\
    \",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\": null,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"edfc149d72c19998e133669bdbb2ac3f7340909f82c4282ab9818f884102890c\"\n     \
    \ }\n    ],\n    \"explanation\": \"Attached literal evidence and identical historical/current\
    \ response hash support the existing stock g/L value; for water,1000 mL /1000=1\
    \ L is a batch volume, not a final-medium percentage. This does not verify chemical\
    \ grounding or the receiving-medium value.\"\n  },\n  {\n    \"decision_id\":\
    \ \"q31\",\n    \"claim\": \"Standalone placeholder ingredient\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Stock dependency representation, not an additional\
    \ recipe constituent\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_1392_Trace_element_solution_SL-7.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": {\n      \"value\": null,\n\
    \      \"basis\": \"complete named SL-7 composition already exists\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 stock heading\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-7:\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"g_l\\\": 0.25,\\n                        \\\"mmol_l\\\
    \": 6.85683,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"The variable See source for composition\
    \ placeholder is not an additional source constituent. It should not become a\
    \ medium ingredient or substitute for the explicit stock composition. Dependency\
    \ correction is context for a separately authorized owner fix, not a second saved\
    \ review.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"claim\": \"Post-autoclave\
    \ filtration/timing in target\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Preparation timing of the two later additions\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"CuSO4_dose_ml\": 2.5,\n  \
    \    \"CuSO4_strength_M\": 1.0,\n      \"succinate_dose_ml\": 10,\n      \"succinate_percent\"\
    : 40,\n      \"percent_basis\": \"unspecified\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 final preparation sentence\",\n        \"exact_source_quote\"\
    : \"After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution,\
    \ \\nboth sterilized by filtration.\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already preserves the\
    \ exact preparation sentence; the KOMODO owner and target omit it. Attach narrow\
    \ evidence at the existing owner stage and add missing context elsewhere. Do not\
    \ invent autoclave temperature, time or filtration pore size.\"\n  },\n  {\n \
    \   \"decision_id\": \"q33\",\n    \"claim\": \"Post-autoclave filtration/timing\
    \ in KOMODO_660_ALCALIGENES_MEDIUM.yaml\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"Preparation timing of the two later additions\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"CuSO4_dose_ml\": 2.5,\n  \
    \    \"CuSO4_strength_M\": 1.0,\n      \"succinate_dose_ml\": 10,\n      \"succinate_percent\"\
    : 40,\n      \"percent_basis\": \"unspecified\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n        \"\
    source_locator\": \"DSMZ660 page1 final preparation sentence\",\n        \"exact_source_quote\"\
    : \"After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution,\
    \ \\nboth sterilized by filtration.\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already preserves the\
    \ exact preparation sentence; the KOMODO owner and target omit it. Attach narrow\
    \ evidence at the existing owner stage and add missing context elsewhere. Do not\
    \ invent autoclave temperature, time or filtration pore size.\"\n  },\n  {\n \
    \   \"decision_id\": \"q34\",\n    \"claim\": \"Post-autoclave filtration/timing\
    \ in alcaligenes_medium.yaml\",\n    \"decision\": \"evidence_only\",\n    \"\
    stage\": \"Preparation timing of the two later additions\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"After autoclaving add 2.5 ml 1.0 M CuSO4 and 10\
    \ ml of a 40% Na-succinate solution, both sterilized by filtration.\"\n      \
    \    }\n        ]\n      }\n    ],\n    \"source_amount\": {\n      \"CuSO4_dose_ml\"\
    : 2.5,\n      \"CuSO4_strength_M\": 1.0,\n      \"succinate_dose_ml\": 10,\n \
    \     \"succinate_percent\": 40,\n      \"percent_basis\": \"unspecified\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz660\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 final preparation sentence\",\n\
    \        \"exact_source_quote\": \"After autoclaving add 2.5 ml 1.0 M CuSO4 and\
    \ 10 ml of a 40% Na-succinate solution, \\nboth sterilized by filtration.\",\n\
    \        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      }\n    ],\n    \"explanation\": \"The DSMZ owner already preserves the\
    \ exact preparation sentence; the KOMODO owner and target omit it. Attach narrow\
    \ evidence at the existing owner stage and add missing context elsewhere. Do not\
    \ invent autoclave temperature, time or filtration pore size.\"\n  },\n  {\n \
    \   \"decision_id\": \"q35\",\n    \"claim\": \"SL-7 solvent and main-volume accounting\"\
    ,\n    \"decision\": \"conflict\",\n    \"stage\": \"Supplied liquid inputs versus\
    \ provider-declared main volume\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/ALCALIGENES_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alcaligenes_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"After autoclaving add 2.5 ml 1.0 M CuSO4 and 10\
    \ ml of a 40% Na-succinate solution, both sterilized by filtration.\"\n      \
    \    }\n        ]\n      }\n    ],\n    \"source_amount\": {\n      \"primary_listed_main_liquids_ml\"\
    : [\n        988.5,\n        1,\n        2.5,\n        10\n      ],\n      \"\
    arithmetic_sum_ml\": 1002,\n      \"provider_main_volume_ml\": 1000,\n      \"\
    stock_water_ml\": 1000\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz660\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\"\
    ,\n        \"source_locator\": \"DSMZ660 page1 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 988.500 ml\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n    \
    \    \"source_locator\": \"DSMZ660 page1 main stock-dose row\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL 7 1.000 ml\",\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"dsmz660\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium660.pdf\",\n    \
    \    \"source_locator\": \"DSMZ660 page1 final additions\",\n        \"exact_source_quote\"\
    : \"After autoclaving add 2.5 ml 1.0 M CuSO4 and 10 ml of a 40% Na-succinate solution,\"\
    ,\n        \"snapshot_sha256\": \"9c81f29bacb65ede3f9854c05b48eb292cd2a93bc18fcd81a7dd7e4313dbbb2e\"\
    ,\n        \"parsed_text_sha256\": \"4a4d5eb6db9910006bf821ee1da7c498d3ffafb24745e595733f9af11692bb8a\"\
    \n      },\n      {\n        \"source_key\": \"mediadive660api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/660\",\n        \"source_locator\"\
    : \"$.data.solutions[0].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1000\",\n        \"snapshot_sha256\": \"315cb09171e8d877258515247199d46094f91e8127d663cee8a04f6c54f3799a\"\
    \n      }\n    ],\n    \"explanation\": \"988.5+1+2.5+10=1002 mL of listed inputs\
    \ differs from the provider main volume1000 mL. Preserve both source statements;\
    \ do not infer measured final volume, change water to force a total, or silently\
    \ divide all quantities by1.002 L.\"\n  }\n]"
- assessment_id: stocks-denominators
  area: quantity
  topic: Stock boundary, percentage and volume conflicts
  outcome: concern
  summary: Every medium concentration and dependency stock amount is scoped. Eight
    existing dependency evidence objects are verified only for their own stock/water
    claims. Source1 mL SL-7 dose, post-autoclave additions and1002 mL listed-liquid
    sum remain distinct from provider1000 mL. HCl25% and succinate40% lack a specified
    percentage basis.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - primary
  - provider
  - stock-record
  - stock-source
  - quantity-inventory
- assessment_id: chemical-forms
  area: grounding
  topic: Hydrate correspondence versus source specificity
  outcome: concern
  summary: Source Na2HPO4 dodecahydrate and NiCl2 hexahydrate conflict with the asserted
    anhydrous structures CHEBI:34683 and34887. Other stated hydrate formulas match
    their captured structures. Sodium-succinate anhydrous identity is more specific
    than the primary; its form remains unestablished rather than proven wrong. Generic
    molecular HCl does not establish25% solution composition. No replacement identifier
    is guessed.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - primary
  - chebi34683
  - chebi34887
  - chebi63675
  - chebi17883
- assessment_id: mixture-classification
  area: scope
  topic: Defined classification and source mixtures
  outcome: concern
  summary: CHEBI:31604 explicitly describes ferric ammonium citrate as a mixture of
    indefinite composition. Provider complex_medium=no is a catalog classification,
    not proof that every ingredient has a unique chemical composition. The local DEFINED
    medium/composition claims need qualification.
  target_ids:
  - CultureMech:006238
  evidence_ids:
  - record
  - primary
  - provider
  - chebi31604
findings:
- finding_id: f1
  issue_key: DSM660-flattened-stocks
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock strengths are represented as direct main-medium concentrations
  description: Eight SL-7 stock rows appear directly in all three medium ingredient
    lists. The explicit1 mL stock dose is missing, and later CuSO4/succinate stocks
    are reduced to provider-derived masses. This changes preparation-stage meaning
    and the represented formulation.
  target_ids:
  - CultureMech:006238
  field_paths:
  - ingredients[9:19]
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - stock-source
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  issue_key: DSM660-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two explicit source hydrates map to anhydrous structures
  description: Na2HPO4 x12H2O is mapped to disodium hydrogenphosphate CHEBI:34683
    and NiCl2 x6H2O to nickel dichloride CHEBI:34887. Captured structures omit the
    stated waters of hydration. Label validity and stock amount evidence do not verify
    source form.
  target_ids:
  - CultureMech:006238
  field_paths:
  - ingredients[7].term
  - ingredients[17].term
  - ingredients[7].mediaingredientmech_chebi_term
  - ingredients[17].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - chebi34683
  - chebi34887
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  issue_key: DSM660-preparation-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and narrow evidence are incomplete or lost across layers
  description: Main water and stock addition context are missing; the DSMZ owner alone
    retains the later filtration/timing sentence. No medium ingredient has attached
    amount evidence. Existing standalone stock evidence does not support flattened
    medium values.
  target_ids:
  - CultureMech:006238
  field_paths:
  - preparation_steps
  - ingredients[*].evidence
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - stock-record
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  issue_key: DSM660-defined-mixture
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Fully defined classification overstates mixture composition
  description: The recipe contains ferric ammonium citrate, whose asserted term explicitly
    denotes an indefinite mixture. The two local DEFINED fields and provider binary
    classification do not establish a unique chemical formulation.
  target_ids:
  - CultureMech:006238
  field_paths:
  - medium_type
  - composition_type
  - ingredients[8]
  evidence_ids:
  - record
  - primary
  - chebi31604
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  issue_key: DSM660-history-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamp formatting is inconsistent
  description: The KOMODO-derived target/owner retain a malformed fractional timestamp
    and a timezone-naive enrichment timestamp. These are historical metadata defects,
    separate from source formulation correctness.
  target_ids:
  - CultureMech:006238
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - record
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  description: Restore the separate SL-7 recipe and1 mL addition plus the two later
    stock doses/strengths. Preserve all source-specific basis limits and separately
    verified stock evidence; never treat stock g/L as main-medium g/L.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006238
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  description: Verify exact supplied hydrates and repair primary/secondary correspondence
    in maintained inputs with evidence. Keep source-unspecified succinate form unresolved;
    do not guess replacements.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006238
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  description: Attach exact main and stock evidence separately, preserve the correct
    DSMZ preparation sentence, and carry it through authorized regeneration without
    inventing unspecified sterilization parameters.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006238
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  description: Qualify medium/composition classification for the indefinite ingredient
    and preserve the named source mixture; do not decompose it into invented exact
    salts.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006238
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
  description: Preserve append-only history and add an explicit provenance clarification
    through an authorized maintenance path; do not silently fabricate missing timezones
    or rewrite old events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006238
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alcaligenes_medium.yaml
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
- No organism, strain, optimum, safety or growth-performance claim is inferred from
  the medium name or generic Microbial cultivation application. No unasserted chemical
  form or replacement identifier is guessed.
- The exact historical KOMODO660 detail page returned403. Current base identity, stable
  source mapping, DSMZ formulation and provider are independently resolved. Historical
  full import bytes are optional provenance context; no inaccessible variant is asserted.
- The current primary does not resolve percent bases or measured final volume. Optional
  historical KOMODO403 is retained without blocking the independently resolved base
  formulation. The standalone stock is dependency context only; no second record is
  formally assessed or saved.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-020
- generated-medium
```
