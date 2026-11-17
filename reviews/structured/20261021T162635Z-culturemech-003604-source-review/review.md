# Source and formulation review: anoxybacillus_amylolyticus_medium (CultureMech:003604)

- Review: 20261021T162635Z-culturemech-003604-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:17:50Z
- Finished UTC: 2026-10-21T16:26:35Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The merged KOMODO/DSMZ 1046 record retains a water mass-concentration error and omits evidence and preparation already present in its maintained contributors. Exact recovered historical API bytes verify the existing owner evidence; current API failures are preserved separately.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 282; batch 029 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-eight task batches contain 280 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 283 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003604 | data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml | generated | anoxybacillus_amylolyticus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003604 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003604 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/282/strict.tsv |
| validate-terms | passed | True | CultureMech:003604 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003604 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003604 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1046api | unavailable | False | CultureMech:003604 | Current exact endpoint attempt mediadive1046api returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| Exact source content access: mediadive1046api_retry | unavailable | False | CultureMech:003604 | Current exact endpoint attempt mediadive1046api_retry returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| Exact source content access: solution2114 | unavailable | False | CultureMech:003604 | Current exact endpoint attempt solution2114 returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| Exact source content access: komodo1046detail | unavailable | False | CultureMech:003604 | Current exact endpoint attempt komodo1046detail returned 403. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003604.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:003604.

2 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 2/3 primary and 2/3 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 3: primary 66.67%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact source and contributor identity

identity: supported. Targets: CultureMech:003604.

The generated CultureMech:003604 target is owned by the explicitly merged KOMODO 1046 and DSMZ 1046 inputs. Its SOURCE_DUPLICATE parent path resolves to CultureMech:000469; the reciprocal contributor link resolves to CultureMech:003604. Exact catalogue/PDF/API correspondence establishes this source relationship beyond ingredient-set matching. Cross-layer reuse of an ID is not an independent-record collision.

### Evidence is supported in maintained owners but missing from the merged target

evidence: concern. Targets: CultureMech:003604.

All nine owner attachments have exact source matches. Both maintained water values are already 1 L with input-volume explanations and evidence. The generated target retains 1000 G_PER_L and has no references or ingredient evidence. The two non-water concentrations agree with the provider-declared basis; their absence of target-level evidence is separate from numerical agreement.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003604.

10 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "label": "Yeast extract",
    "decision": "evidence_only",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "The preserved provider explicitly reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium volume.",
    "local_evidence_status": "No target claim-level evidence; reconcile from the verified maintained inputs."
  },
  {
    "decision_id": "q2",
    "label": "NaCl",
    "decision": "evidence_only",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 102.669,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "The preserved provider explicitly reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium volume.",
    "local_evidence_status": "No target claim-level evidence; reconcile from the verified maintained inputs."
  },
  {
    "decision_id": "q3",
    "label": "Tap water",
    "decision": "correct",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "1000 mL / 1000 mL per L = 1 L source input. It is neither 1000 g/L nor a volume percentage; no water density or measured final volume is inferred.",
    "local_evidence_status": "No target claim-level evidence; reconcile from the verified maintained inputs."
  },
  {
    "decision_id": "q4",
    "label": "Yeast extract",
    "decision": "verified",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "The preserved provider explicitly reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium volume.",
    "local_evidence_status": "Existing claim-specific attachment was checked against the exact historical response hash and literal excerpt; water additionally matches the current primary PDF."
  },
  {
    "decision_id": "q5",
    "label": "NaCl",
    "decision": "verified",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 102.669,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "The preserved provider explicitly reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium volume.",
    "local_evidence_status": "Existing claim-specific attachment was checked against the exact historical response hash and literal excerpt; water additionally matches the current primary PDF."
  },
  {
    "decision_id": "q6",
    "label": "Tap water",
    "decision": "verified",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "1000 mL / 1000 mL per L = 1 L source input. It is neither 1000 g/L nor a volume percentage; no water density or measured final volume is inferred.",
    "local_evidence_status": "Existing claim-specific attachment was checked against the exact historical response hash and literal excerpt; water additionally matches the current primary PDF."
  },
  {
    "decision_id": "q7",
    "label": "Yeast extract",
    "decision": "verified",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "The preserved provider explicitly reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium volume.",
    "local_evidence_status": "Existing claim-specific attachment was checked against the exact historical response hash and literal excerpt; water additionally matches the current primary PDF."
  },
  {
    "decision_id": "q8",
    "label": "NaCl",
    "decision": "verified",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 102.669,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "The preserved provider explicitly reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium volume.",
    "local_evidence_status": "Existing claim-specific attachment was checked against the exact historical response hash and literal excerpt; water additionally matches the current primary PDF."
  },
  {
    "decision_id": "q9",
    "label": "Tap water",
    "decision": "verified",
    "source_stage": "DSMZ 1046 main recipe / original October 7 API capture",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      },
      {
        "source_key": "mediadive1046api_historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1046",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb"
      }
    ],
    "interpretation": "1000 mL / 1000 mL per L = 1 L source input. It is neither 1000 g/L nor a volume percentage; no water density or measured final volume is inferred.",
    "local_evidence_status": "Existing claim-specific attachment was checked against the exact historical response hash and literal excerpt; water additionally matches the current primary PDF."
  },
  {
    "decision_id": "q10",
    "label": "Preparation pH",
    "decision": "evidence_only",
    "source_stage": "Main preparation, not a measured growth optimum",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 5.6
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml",
        "field_path": "ph_value",
        "stored": 5.6
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml",
        "field_path": "ph_value",
        "stored": 5.6
      },
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "adjust pH 5.6",
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz1046",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1046.pdf",
        "source_locator": "Page 1, final instruction",
        "exact_source_quote": "adjust pH 5.6",
        "snapshot_sha256": "1534392d6488ebf9c255814809118f31965cef3d2bfab1e2c7ca534350eef6fb",
        "parsed_text_sha256": "3fced50f8c11f7a01055a0b756f1a16d9d84528b7537aa4c9dfee2a55e41732d"
      }
    ],
    "interpretation": "Retain pH 5.6 and the instruction to adjust to it. Scalar pH is present in all three layers, while the preparation step is present only in the DSMZ owner. Source does not specify titrant, dose, incubation temperature, time or vessel."
  }
]

### Preparation and culture conditions

completeness: concern. Targets: CultureMech:003604.

The primary says to adjust pH to 5.6. That step survives only in the DSMZ maintained contributor; the generated target and KOMODO owner omit preparation_steps. The historical API names Autoclave as equipment but provides no cycle, and the PDF gives no sterilization cycle. No 121 degrees/15 minutes, incubation temperature, gas percentage or titrant can be added from these sources.

### Classification and organism claims

scope: supported. Targets: CultureMech:003604.

Yeast extract makes COMPLEX/UNDEFINED a defensible composition classification; the source is a liquid recipe without a gelling agent. Bacterial filing and a generic cultivation application do not establish a strain-specific growth outcome. The species name in the medium title is not a grounded growth assertion. No target_organisms, ingredient role claims, discussion flag, stock dose or inline variant is asserted; no missing optional field is promoted to a fabricated claim. Pure-water CHEBI identifies water broadly and does not specify tap-water mineral composition.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003604.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained fixes and generated reconciliation

ownership: concern. Targets: CultureMech:003604.

Retain the already-correct water/evidence in both normalized contributors. Complete any missing preparation representation there, then use the owning generator and freshness gates to reconcile the generated record. Do not repeat the water repair or patch the merged YAML directly.

## Findings

### f1: Generated water representation is stale after a verified owner repair

major / open / confirmed; issue key: dsmz1046-generated-water-evidence-stale.

The target states Tap water 1000 G_PER_L. The source states 1000 mL and both maintained contributors already represent 1 L input volume with verified excerpts. The target also omits the associated references and ingredient evidence, including support for unchanged yeast and salt amounts. This is stale generated scientific content, not an unresolved source amount.

### f2: The pH adjustment instruction is missing from the selected output

minor / open / confirmed; issue key: dsmz1046-generated-ph-instruction-missing.

The scalar pH is correct, but preparation_steps is absent from the generated target and KOMODO contributor; the DSMZ contributor and primary retain adjust pH 5.6. This is a bounded protocol completeness gap.

### f3: Legacy timestamp text is malformed or lacks a timezone

minor / open / confirmed; issue key: dsmz1046-history-timestamp-shape.

The KOMODO owner and generated target each retain the malformed January import timestamp ending .fZ and a timezone-naive February resolver timestamp. These are historical metadata limitations; schema success does not repair them.

## Recommended Actions And Acceptance Checks

### a1

Preserve the maintained 1 L water input and verified concentration evidence; reconcile via the merge generator after confirming both contributors and retain source-scoped evidence through generation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Confirm water remains an input volume, both unchanged non-water claims retain their attached evidence, and no density/final-volume inference is introduced.

### a2

Preserve the verified pH adjustment step in maintained inputs and its regenerated output, without inventing an autoclave cycle or culture conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve historical events and append a clarification only when independent provenance establishes the missing time information; do not invent a timezone or rewrite old events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch029/282/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/282/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml:1:id: CultureMech:003604<br>./data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml:1:id: CultureMech:003604<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/282/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 10 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1046.pdf; Page 1, complete formulation and pH instruction | supports | Exact primary DSMZ 1046 identifies the formulation and its three batch inputs. The copyright year is not treated as a publication year; individual authors and issue date are not supplied. |
| api-historical | https://mediadive.dsmz.de/rest/medium/1046; $.data.medium and $.data.solutions[0], complete preserved response | supports | Original October 7 response recovered byte-for-byte from the tracked water-repair context. Its hash matches existing owner evidence; volume 1000 is a provider-declared recipe basis, not an independently measured final volume. |
| solution-historical | https://mediadive.dsmz.de/rest/solution/2114; $.data, complete preserved solution 2114 | supports | Historical linked solution 2114 agrees on recipe rows after removing null-only fields, declared volume 1000 and the pH instruction. This is source consistency, not a stock addition to this medium. |
| komodo | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact MediaInfo=1046 row and preceding column header | supports | KOMODO 1046 maps explicitly to the DSMZ 1046 PDF and pH 5.6. The Is Aerobic column is false; this is attributed catalogue metadata, not evidence of organism physiology or an anoxic preparation method. |
| existing-evidence | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/282/evidence-context-original.json; existing_owner_evidence_recheck and historical_response_recovery | supports | All nine existing owner evidence objects were checked against exact successful captures and their asserted hashes: six API objects, two PDF water snippets and one catalogue identity object. Recovery retains original October timestamps; current failed requests are distinct. |
| mediadive1046api-attempt | https://mediadive.dsmz.de/rest/medium/1046; Preserved exact public retrieval result | context_only | Current exact endpoint attempt mediadive1046api returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| mediadive1046api_retry-attempt | https://mediadive.dsmz.de/rest/medium/1046; Preserved exact public retrieval result | context_only | Current exact endpoint attempt mediadive1046api_retry returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| solution2114-attempt | https://mediadive.dsmz.de/rest/solution/2114; Preserved exact public retrieval result | context_only | Current exact endpoint attempt solution2114 returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| komodo1046detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1046; Preserved exact public retrieval result | context_only | Current exact endpoint attempt komodo1046detail returned 403. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch029/282/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| history-metadata | data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml; data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:11.526773"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:11.526773"}]}, {"input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/merge/merge_recipes.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge/formulation and guarded water-repair implementations were read as maintained-input ownership context. The repair preserves input volume and evidence; existing owner bytes show it has already landed. Current code is not a historical replay or proof of which old code path produced the merged target. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge/formulation and guarded water-repair implementations were read as maintained-input ownership context. The repair preserves input volume and evidence; existing owner bytes show it has already landed. Current code is not a historical replay or proof of which old code path produced the merged target. |
| writer-2 | scripts/repair_dsmz803_1046_1065_water.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current merge/formulation and guarded water-repair implementations were read as maintained-input ownership context. The repair preserves input volume and evidence; existing owner bytes show it has already landed. Current code is not a historical replay or proof of which old code path produced the merged target. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current exact endpoint attempt mediadive1046api returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed.
- Current exact endpoint attempt mediadive1046api_retry returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed.
- Current exact endpoint attempt solution2114 returned 503. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed.
- Current exact endpoint attempt komodo1046detail returned 403. It supplies no formulation content. Exact historical API and current primary/catalogue captures cover the reviewed formulation and existing attached evidence; no current successful fetch is claimed.
- Completed denotes the bounded review using current primary/catalogue text and exact historical API captures. It does not claim that the currently failing API endpoints were successfully accessed or that cultivar growth was demonstrated.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162635Z-culturemech-003604-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anoxybacillus_amylolyticus_medium (CultureMech:003604)'
started_at: '2026-10-21T16:17:50Z'
finished_at: '2026-10-21T16:26:35Z'
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
summary: The merged KOMODO/DSMZ 1046 record retains a water mass-concentration error
  and omits evidence and preparation already present in its maintained contributors.
  Exact recovered historical API bytes verify the existing owner evidence; current
  API failures are preserved separately.
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
  - path: data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
    sha256: b0f5e823e5535f8a7e01c5330d843a297bb87041fa719f83f6023cc262cac371
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    sha256: 60fd54e5e85a6635980a8e25e9252ecedb8c71229ca78d63587018e7e3f1c73b
    role: context
  - path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
    sha256: 61c23027dda09a164eb95d88e64807158766fea9d9e208369e04d581a5948ec5
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
  - path: reports/ingredient_concentration_curation/20261008-dsmz803-1046-1065-water/inspected-context.json
    sha256: 8ec4c3dae8b5a3a0ee707c6ee2757ae7bbf4f41984e15f270697afa21eb03d5b
    role: context
  - path: reports/ingredient_concentration_curation/20261008-dsmz803-1046-1065-water/records/1046-komodo.md
    sha256: 0787da1d53dd85fd5db2f1a62a8556551d220e651629f32d8155aab02ab50e6b
    role: context
  - path: reports/ingredient_concentration_curation/20261008-dsmz803-1046-1065-water/records/1046-medium.md
    sha256: 4c6ec3b7d8c0291f6f7348d6e787e9c512797c739d56a16df6064b59ab35a751
    role: context
  - path: reports/ingredient_concentration_curation/20261008-dsmz803-1046-1065-water/records/1046-solution.md
    sha256: 99436ac98d0023367a4d8deb041ad654f21fd7e74e28345ef1b742fd35816f55
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_dsmz803_1046_1065_water.py
    sha256: a65ea58bea9cbc3e195cbddd2d0e96f80479e0df8811831cc87d5f2bc82092c1
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  selection: Task review 282; batch 029 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-eight task batches
    contain 280 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 283 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003604
targets:
- target_id: CultureMech:003604
  path: data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  label: anoxybacillus_amylolyticus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/282/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/282/strict.tsv"
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003604
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
  - CultureMech:003604
- check_id: mediadive1046api-source-access
  name: 'Exact source content access: mediadive1046api'
  required: false
  status: unavailable
  summary: Current exact endpoint attempt mediadive1046api returned 503. It supplies
    no formulation content. Exact historical API and current primary/catalogue captures
    cover the reviewed formulation and existing attached evidence; no current successful
    fetch is claimed.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - mediadive1046api-attempt
- check_id: mediadive1046api_retry-source-access
  name: 'Exact source content access: mediadive1046api_retry'
  required: false
  status: unavailable
  summary: Current exact endpoint attempt mediadive1046api_retry returned 503. It
    supplies no formulation content. Exact historical API and current primary/catalogue
    captures cover the reviewed formulation and existing attached evidence; no current
    successful fetch is claimed.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - mediadive1046api_retry-attempt
- check_id: solution2114-source-access
  name: 'Exact source content access: solution2114'
  required: false
  status: unavailable
  summary: Current exact endpoint attempt solution2114 returned 503. It supplies no
    formulation content. Exact historical API and current primary/catalogue captures
    cover the reviewed formulation and existing attached evidence; no current successful
    fetch is claimed.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - solution2114-attempt
- check_id: komodo1046detail-source-access
  name: 'Exact source content access: komodo1046detail'
  required: false
  status: unavailable
  summary: Current exact endpoint attempt komodo1046detail returned 403. It supplies
    no formulation content. Exact historical API and current primary/catalogue captures
    cover the reviewed formulation and existing attached evidence; no current successful
    fetch is claimed.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - komodo1046detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:06.886396Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/282/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:08.163496Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/282/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:09.425535Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:10.212950Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:26:34Z'
  support: supports
  summary: './data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml:1:id:
    CultureMech:003604

    ./data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml:1:id:
    CultureMech:003604

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/282/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:26:34Z'
  support: supports
  summary: 10 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: fa2aebe63cc023a317219a08991c35479fec84108a4df210e0956630912f2acf
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1046.pdf
  locator: Page 1, complete formulation and pH instruction
  accessed_at: '2026-10-21T15:56:58.216411Z'
  support: supports
  summary: Exact primary DSMZ 1046 identifies the formulation and its three batch
    inputs. The copyright year is not treated as a publication year; individual authors
    and issue date are not supplied.
  snapshot_sha256: 1534392d6488ebf9c255814809118f31965cef3d2bfab1e2c7ca534350eef6fb
- evidence_id: api-historical
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1046
  locator: $.data.medium and $.data.solutions[0], complete preserved response
  accessed_at: '2026-10-07T13:16:28.294308Z'
  support: supports
  summary: Original October 7 response recovered byte-for-byte from the tracked water-repair
    context. Its hash matches existing owner evidence; volume 1000 is a provider-declared
    recipe basis, not an independently measured final volume.
  snapshot_sha256: 25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb
- evidence_id: solution-historical
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2114
  locator: $.data, complete preserved solution 2114
  accessed_at: '2026-10-07T09:09:09.259993Z'
  support: supports
  summary: Historical linked solution 2114 agrees on recipe rows after removing null-only
    fields, declared volume 1000 and the pH instruction. This is source consistency,
    not a stock addition to this medium.
  snapshot_sha256: c1ea738fe783d7963260293d5fb71f1c5249007744f90beda491f0af4f3b13e3
- evidence_id: komodo
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact MediaInfo=1046 row and preceding column header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO 1046 maps explicitly to the DSMZ 1046 PDF and pH 5.6. The Is Aerobic
    column is false; this is attributed catalogue metadata, not evidence of organism
    physiology or an anoxic preparation method.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: existing-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/282/evidence-context-original.json
  locator: existing_owner_evidence_recheck and historical_response_recovery
  accessed_at: '2026-10-21T16:26:34Z'
  support: supports
  summary: 'All nine existing owner evidence objects were checked against exact successful
    captures and their asserted hashes: six API objects, two PDF water snippets and
    one catalogue identity object. Recovery retains original October timestamps; current
    failed requests are distinct.'
  snapshot_sha256: 275dcf7a475d176ff0449d2b2c25710e19cf4b3be678c1e2e8ae067626c25dce
- evidence_id: mediadive1046api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1046
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:56:57.033964Z'
  support: context_only
  summary: Current exact endpoint attempt mediadive1046api returned 503. It supplies
    no formulation content. Exact historical API and current primary/catalogue captures
    cover the reviewed formulation and existing attached evidence; no current successful
    fetch is claimed.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1046api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1046
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:09.142095Z'
  support: context_only
  summary: Current exact endpoint attempt mediadive1046api_retry returned 503. It
    supplies no formulation content. Exact historical API and current primary/catalogue
    captures cover the reviewed formulation and existing attached evidence; no current
    successful fetch is claimed.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution2114-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2114
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:09.778665Z'
  support: context_only
  summary: Current exact endpoint attempt solution2114 returned 503. It supplies no
    formulation content. Exact historical API and current primary/catalogue captures
    cover the reviewed formulation and existing attached evidence; no current successful
    fetch is claimed.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo1046detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1046
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:56:57.020792Z'
  support: context_only
  summary: Current exact endpoint attempt komodo1046detail returned 403. It supplies
    no formulation content. Exact historical API and current primary/catalogue captures
    cover the reviewed formulation and existing attached evidence; no current successful
    fetch is claimed.
  snapshot_sha256: d809f9f60e4cfd22649e74c2ffb41c6d80e81f0ae4cfee7ab10b3ce658332248
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T16:26:34Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/282/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: c3a13630f7f1826a053656402b9ff4ce6a005e6e81c1f14d64f6748b879ff250
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml;
    data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:11.526773"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:11.526773"}]}, {"input": "data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Current merge/formulation and guarded water-repair implementations were
    read as maintained-input ownership context. The repair preserves input volume
    and evidence; existing owner bytes show it has already landed. Current code is
    not a historical replay or proof of which old code path produced the merged target.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Current merge/formulation and guarded water-repair implementations were
    read as maintained-input ownership context. The repair preserves input volume
    and evidence; existing owner bytes show it has already landed. Current code is
    not a historical replay or proof of which old code path produced the merged target.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_dsmz803_1046_1065_water.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T16:26:34Z'
  support: context_only
  summary: Current merge/formulation and guarded water-repair implementations were
    read as maintained-input ownership context. The repair preserves input volume
    and evidence; existing owner bytes show it has already landed. Current code is
    not a historical replay or proof of which old code path produced the merged target.
  snapshot_sha256: a65ea58bea9cbc3e195cbddd2d0e96f80479e0df8811831cc87d5f2bc82092c1
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '2 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 2/3 primary
    and 2/3 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi15377
  - chebi26710
  details: 'Instance coverage on a 0–100 percent scale, denominator 3: primary 66.67%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact source and contributor identity
  outcome: supported
  summary: The generated CultureMech:003604 target is owned by the explicitly merged
    KOMODO 1046 and DSMZ 1046 inputs. Its SOURCE_DUPLICATE parent path resolves to
    CultureMech:000469; the reciprocal contributor link resolves to CultureMech:003604.
    Exact catalogue/PDF/API correspondence establishes this source relationship beyond
    ingredient-set matching. Cross-layer reuse of an ID is not an independent-record
    collision.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - dsmz
  - komodo
  - api-historical
- assessment_id: source-evidence
  area: evidence
  topic: Evidence is supported in maintained owners but missing from the merged target
  outcome: concern
  summary: All nine owner attachments have exact source matches. Both maintained water
    values are already 1 L with input-volume explanations and evidence. The generated
    target retains 1000 G_PER_L and has no references or ingredient evidence. The
    two non-water concentrations agree with the provider-declared basis; their absence
    of target-level evidence is separate from numerical agreement.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - existing-evidence
  - api-historical
  - dsmz
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 10 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"label\": \"Yeast extract\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"source_stage\": \"DSMZ 1046 main\
    \ recipe / original October 7 API capture\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"6\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"mediadive1046api_historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1046\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 6,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 6,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"The preserved provider explicitly\
    \ reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that\
    \ declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium\
    \ volume.\",\n    \"local_evidence_status\": \"No target claim-level evidence;\
    \ reconcile from the verified maintained inputs.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"label\": \"NaCl\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"source_stage\": \"DSMZ 1046 main recipe / original October 7 API capture\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1046api_historical\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 6,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 6,\\n     \
    \                   \\\"mmol_l\\\": 102.669,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"The preserved provider explicitly\
    \ reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that\
    \ declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium\
    \ volume.\",\n    \"local_evidence_status\": \"No target claim-level evidence;\
    \ reconcile from the verified maintained inputs.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"label\": \"Tap water\",\n    \"decision\": \"correct\",\n   \
    \ \"source_stage\": \"DSMZ 1046 main recipe / original October 7 API capture\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1046api_historical\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Tap water\\\",\\n                        \\\"compound_id\\\
    \": 322,\\n                        \\\"amount\\\": 1000,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"1000 mL / 1000 mL per L = 1 L source\
    \ input. It is neither 1000 g/L nor a volume percentage; no water density or measured\
    \ final volume is inferred.\",\n    \"local_evidence_status\": \"No target claim-level\
    \ evidence; reconcile from the verified maintained inputs.\"\n  },\n  {\n    \"\
    decision_id\": \"q4\",\n    \"label\": \"Yeast extract\",\n    \"decision\": \"\
    verified\",\n    \"source_stage\": \"DSMZ 1046 main recipe / original October\
    \ 7 API capture\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1046api_historical\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Yeast extract\\\",\\n         \
    \               \\\"compound_id\\\": 16,\\n                        \\\"amount\\\
    \": 6,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 6,\\n                        \\\"optional\\\": 0\\n     \
    \               }\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"The preserved provider explicitly\
    \ reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that\
    \ declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium\
    \ volume.\",\n    \"local_evidence_status\": \"Existing claim-specific attachment\
    \ was checked against the exact historical response hash and literal excerpt;\
    \ water additionally matches the current primary PDF.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"label\": \"NaCl\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"DSMZ 1046 main recipe / original October 7 API capture\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1046api_historical\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"NaCl\\\",\\n                  \
    \      \\\"compound_id\\\": 43,\\n                        \\\"amount\\\": 6,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 6,\\n                        \\\"mmol_l\\\": 102.669,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n    \
    \    \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"The preserved provider explicitly\
    \ reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that\
    \ declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium\
    \ volume.\",\n    \"local_evidence_status\": \"Existing claim-specific attachment\
    \ was checked against the exact historical response hash and literal excerpt;\
    \ water additionally matches the current primary PDF.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"label\": \"Tap water\",\n    \"decision\": \"verified\",\n  \
    \  \"source_stage\": \"DSMZ 1046 main recipe / original October 7 API capture\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1046api_historical\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Tap water\\\",\\n                        \\\"compound_id\\\
    \": 322,\\n                        \\\"amount\\\": 1000,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"1000 mL / 1000 mL per L = 1 L source\
    \ input. It is neither 1000 g/L nor a volume percentage; no water density or measured\
    \ final volume is inferred.\",\n    \"local_evidence_status\": \"Existing claim-specific\
    \ attachment was checked against the exact historical response hash and literal\
    \ excerpt; water additionally matches the current primary PDF.\"\n  },\n  {\n\
    \    \"decision_id\": \"q7\",\n    \"label\": \"Yeast extract\",\n    \"decision\"\
    : \"verified\",\n    \"source_stage\": \"DSMZ 1046 main recipe / original October\
    \ 7 API capture\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1046api_historical\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Yeast extract\\\",\\n         \
    \               \\\"compound_id\\\": 16,\\n                        \\\"amount\\\
    \": 6,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 6,\\n                        \\\"optional\\\": 0\\n     \
    \               }\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"The preserved provider explicitly\
    \ reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that\
    \ declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium\
    \ volume.\",\n    \"local_evidence_status\": \"Existing claim-specific attachment\
    \ was checked against the exact historical response hash and literal excerpt;\
    \ water additionally matches the current primary PDF.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"label\": \"NaCl\",\n    \"decision\": \"verified\",\n    \"source_stage\"\
    : \"DSMZ 1046 main recipe / original October 7 API capture\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1046api_historical\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"NaCl\\\",\\n                  \
    \      \\\"compound_id\\\": 43,\\n                        \\\"amount\\\": 6,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 6,\\n                        \\\"mmol_l\\\": 102.669,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n    \
    \    \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"The preserved provider explicitly\
    \ reports 6 g and g_l=6 with declared recipe volume 1000 mL. Arithmetic on that\
    \ declared basis is 6 g / 1 L = 6 g/L; this is not independently measured final-medium\
    \ volume.\",\n    \"local_evidence_status\": \"Existing claim-specific attachment\
    \ was checked against the exact historical response hash and literal excerpt;\
    \ water additionally matches the current primary PDF.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"label\": \"Tap water\",\n    \"decision\": \"verified\",\n  \
    \  \"source_stage\": \"DSMZ 1046 main recipe / original October 7 API capture\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1046api_historical\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Tap water\\\",\\n                        \\\"compound_id\\\
    \": 322,\\n                        \\\"amount\\\": 1000,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1046api_historical\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1046\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"25268aaa66367ee090f8f496cbee7da20bc0183e587e8b96e53fa88ce1cda6bb\"\
    \n      }\n    ],\n    \"interpretation\": \"1000 mL / 1000 mL per L = 1 L source\
    \ input. It is neither 1000 g/L nor a volume percentage; no water density or measured\
    \ final volume is inferred.\",\n    \"local_evidence_status\": \"Existing claim-specific\
    \ attachment was checked against the exact historical response hash and literal\
    \ excerpt; water additionally matches the current primary PDF.\"\n  },\n  {\n\
    \    \"decision_id\": \"q10\",\n    \"label\": \"Preparation pH\",\n    \"decision\"\
    : \"evidence_only\",\n    \"source_stage\": \"Main preparation, not a measured\
    \ growth optimum\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 5.6\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 5.6\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 5.6\n      },\n\
    \      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"adjust pH 5.6\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1046\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1046.pdf\"\
    ,\n        \"source_locator\": \"Page 1, final instruction\",\n        \"exact_source_quote\"\
    : \"adjust pH 5.6\",\n        \"snapshot_sha256\": \"1534392d6488ebf9c255814809118f31965cef3d2bfab1e2c7ca534350eef6fb\"\
    ,\n        \"parsed_text_sha256\": \"3fced50f8c11f7a01055a0b756f1a16d9d84528b7537aa4c9dfee2a55e41732d\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain pH 5.6 and the instruction\
    \ to adjust to it. Scalar pH is present in all three layers, while the preparation\
    \ step is present only in the DSMZ owner. Source does not specify titrant, dose,\
    \ incubation temperature, time or vessel.\"\n  }\n]"
- assessment_id: preparation
  area: completeness
  topic: Preparation and culture conditions
  outcome: concern
  summary: The primary says to adjust pH to 5.6. That step survives only in the DSMZ
    maintained contributor; the generated target and KOMODO owner omit preparation_steps.
    The historical API names Autoclave as equipment but provides no cycle, and the
    PDF gives no sterilization cycle. No 121 degrees/15 minutes, incubation temperature,
    gas percentage or titrant can be added from these sources.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - api-historical
- assessment_id: classification-growth
  area: scope
  topic: Classification and organism claims
  outcome: supported
  summary: Yeast extract makes COMPLEX/UNDEFINED a defensible composition classification;
    the source is a liquid recipe without a gelling agent. Bacterial filing and a
    generic cultivation application do not establish a strain-specific growth outcome.
    The species name in the medium title is not a grounded growth assertion. No target_organisms,
    ingredient role claims, discussion flag, stock dose or inline variant is asserted;
    no missing optional field is promoted to a fabricated claim. Pure-water CHEBI
    identifies water broadly and does not specify tap-water mineral composition.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - dsmz
  - komodo
  - chebi15377
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: ownership
  area: ownership
  topic: Maintained fixes and generated reconciliation
  outcome: concern
  summary: Retain the already-correct water/evidence in both normalized contributors.
    Complete any missing preparation representation there, then use the owning generator
    and freshness gates to reconcile the generated record. Do not repeat the water
    repair or patch the merged YAML directly.
  target_ids:
  - CultureMech:003604
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: dsmz1046-generated-water-evidence-stale
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated water representation is stale after a verified owner repair
  description: The target states Tap water 1000 G_PER_L. The source states 1000 mL
    and both maintained contributors already represent 1 L input volume with verified
    excerpts. The target also omits the associated references and ingredient evidence,
    including support for unchanged yeast and salt amounts. This is stale generated
    scientific content, not an unresolved source amount.
  target_ids:
  - CultureMech:003604
  field_paths:
  - ingredients[2].concentration
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - api-historical
  - existing-evidence
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: dsmz1046-generated-ph-instruction-missing
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The pH adjustment instruction is missing from the selected output
  description: The scalar pH is correct, but preparation_steps is absent from the
    generated target and KOMODO contributor; the DSMZ contributor and primary retain
    adjust pH 5.6. This is a bounded protocol completeness gap.
  target_ids:
  - CultureMech:003604
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: dsmz1046-history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy timestamp text is malformed or lacks a timezone
  description: The KOMODO owner and generated target each retain the malformed January
    import timestamp ending .fZ and a timezone-naive February resolver timestamp.
    These are historical metadata limitations; schema success does not repair them.
  target_ids:
  - CultureMech:003604
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Preserve the maintained 1 L water input and verified concentration
    evidence; reconcile via the merge generator after confirming both contributors
    and retain source-scoped evidence through generation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003604
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
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
  - Confirm water remains an input volume, both unchanged non-water claims retain
    their attached evidence, and no density/final-volume inference is introduced.
- action_id: a2
  description: Preserve the verified pH adjustment step in maintained inputs and its
    regenerated output, without inventing an autoclave cycle or culture conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003604
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
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
  description: Preserve historical events and append a clarification only when independent
    provenance establishes the missing time information; do not invent a timezone
    or rewrite old events.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003604
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml
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
- Current exact endpoint attempt mediadive1046api returned 503. It supplies no formulation
  content. Exact historical API and current primary/catalogue captures cover the reviewed
  formulation and existing attached evidence; no current successful fetch is claimed.
- Current exact endpoint attempt mediadive1046api_retry returned 503. It supplies
  no formulation content. Exact historical API and current primary/catalogue captures
  cover the reviewed formulation and existing attached evidence; no current successful
  fetch is claimed.
- Current exact endpoint attempt solution2114 returned 503. It supplies no formulation
  content. Exact historical API and current primary/catalogue captures cover the reviewed
  formulation and existing attached evidence; no current successful fetch is claimed.
- Current exact endpoint attempt komodo1046detail returned 403. It supplies no formulation
  content. Exact historical API and current primary/catalogue captures cover the reviewed
  formulation and existing attached evidence; no current successful fetch is claimed.
- Completed denotes the bounded review using current primary/catalogue text and exact
  historical API captures. It does not claim that the currently failing API endpoints
  were successfully accessed or that cultivar growth was demonstrated.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-029
- generated-medium
```
