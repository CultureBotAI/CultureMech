# Source and formulation review: bacillus_thermoalcalophilus_medium (CultureMech:006100)

- Review: 20261021T215509Z-culturemech-006100-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T21:51:51Z
- Finished UTC: 2026-10-21T21:55:09Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 610 and the exact KOMODO accession support the medium identity and eight provider-normalized ingredient amounts. Both maintained owners have authenticated historical amount evidence that is absent from the generated target. Every layer omits the printed 1000 mL water input; only the DSMZ owner retains the pH preparation text. Source-unqualified supplied forms remain distinct from anhydrous ontology metadata.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 385; batch 039 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-eight task batches contain 380 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 383 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006100 | data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml | generated | bacillus_thermoalcalophilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006100 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006100 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/385/strict.tsv |
| validate-terms | passed | True | CultureMech:006100 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006100 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006100 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive610api | unavailable | False | CultureMech:006100 | The preserved mediadive610api attempt has HTTP status 503. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim. |
| Exact source content access: mediadive610api_retry | unavailable | False | CultureMech:006100 | The preserved mediadive610api_retry attempt has HTTP status 503. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim. |
| Exact source content access: komodo610detail | unavailable | False | CultureMech:006100 | The preserved komodo610detail attempt has HTTP status 403. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006100.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006100.

29 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Na-acetate",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "3",
      "unit": "G_PER_L",
      "original_primary_amount": 3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 1",
        "exact_source_quote": "Na-acetate 3.00 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 36.5703,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q2",
    "name": "Na-acetate",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "3",
      "unit": "G_PER_L",
      "original_primary_amount": 3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 1",
        "exact_source_quote": "Na-acetate 3.00 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 36.5703,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q3",
    "name": "Na-acetate",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "3",
      "unit": "G_PER_L",
      "original_primary_amount": 3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 1",
        "exact_source_quote": "Na-acetate 3.00 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 36.5703,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q4",
    "name": "KCl",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1.8",
      "unit": "G_PER_L",
      "original_primary_amount": 1.8,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 2",
        "exact_source_quote": "KCl 1.80 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 24.1449,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q5",
    "name": "KCl",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1.8",
      "unit": "G_PER_L",
      "original_primary_amount": 1.8,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 2",
        "exact_source_quote": "KCl 1.80 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 24.1449,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q6",
    "name": "KCl",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1.8",
      "unit": "G_PER_L",
      "original_primary_amount": 1.8,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 2",
        "exact_source_quote": "KCl 1.80 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 24.1449,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q7",
    "name": "Na2SO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.4",
      "unit": "G_PER_L",
      "original_primary_amount": 0.4,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 3",
        "exact_source_quote": "Na2SO4 0.40 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 2.81611,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q8",
    "name": "Na2SO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.4",
      "unit": "G_PER_L",
      "original_primary_amount": 0.4,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 3",
        "exact_source_quote": "Na2SO4 0.40 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 2.81611,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q9",
    "name": "Na2SO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.4",
      "unit": "G_PER_L",
      "original_primary_amount": 0.4,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 3",
        "exact_source_quote": "Na2SO4 0.40 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 2.81611,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q10",
    "name": "MgSO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "G_PER_L",
      "original_primary_amount": 0.2,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 4",
        "exact_source_quote": "MgSO4 0.20 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.66154,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q11",
    "name": "MgSO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "G_PER_L",
      "original_primary_amount": 0.2,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 4",
        "exact_source_quote": "MgSO4 0.20 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.66154,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q12",
    "name": "MgSO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "G_PER_L",
      "original_primary_amount": 0.2,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 4",
        "exact_source_quote": "MgSO4 0.20 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.66154,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q13",
    "name": "KH2PO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "G_PER_L",
      "original_primary_amount": 0.3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 5",
        "exact_source_quote": "KH2PO4 0.30 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q14",
    "name": "KH2PO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "G_PER_L",
      "original_primary_amount": 0.3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 5",
        "exact_source_quote": "KH2PO4 0.30 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q15",
    "name": "KH2PO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "G_PER_L",
      "original_primary_amount": 0.3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 5",
        "exact_source_quote": "KH2PO4 0.30 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q16",
    "name": "K2HPO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "G_PER_L",
      "original_primary_amount": 0.3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 6",
        "exact_source_quote": "K2HPO4 0.30 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q17",
    "name": "K2HPO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "G_PER_L",
      "original_primary_amount": 0.3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 6",
        "exact_source_quote": "K2HPO4 0.30 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q18",
    "name": "K2HPO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.3",
      "unit": "G_PER_L",
      "original_primary_amount": 0.3,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 6",
        "exact_source_quote": "K2HPO4 0.30 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q19",
    "name": "FeSO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.01",
      "unit": "G_PER_L",
      "original_primary_amount": 0.01,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 7",
        "exact_source_quote": "FeSO4 0.01 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\": 595,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0658285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q20",
    "name": "FeSO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.01",
      "unit": "G_PER_L",
      "original_primary_amount": 0.01,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 7",
        "exact_source_quote": "FeSO4 0.01 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\": 595,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0658285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q21",
    "name": "FeSO4",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.01",
      "unit": "G_PER_L",
      "original_primary_amount": 0.01,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 7",
        "exact_source_quote": "FeSO4 0.01 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\": 595,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0658285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q22",
    "name": "Yeast extract",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L",
      "original_primary_amount": 10,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 8",
        "exact_source_quote": "Yeast extract 10.00 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This generated field has no attached amount evidence; externally authenticated support warrants evidence-only follow-up, not a verified attached-evidence claim. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q23",
    "name": "Yeast extract",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L",
      "original_primary_amount": 10,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 8",
        "exact_source_quote": "Yeast extract 10.00 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q24",
    "name": "Yeast extract",
    "stage": "DSMZ 610 main recipe, provider-declared normalization",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L",
      "original_primary_amount": 10,
      "original_primary_unit": "g",
      "provider_declared_volume_ml": 1000
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table row 8",
        "exact_source_quote": "Yeast extract 10.00 g",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The stored numeral agrees with the exact historical g_l field. This owner has attached matching amount evidence; verification applies only to this field and layer. Primary batch amounts and provider normalization remain separate; no measured final volume or source hydrate is inferred."
  },
  {
    "decision_id": "q25",
    "name": "Distilled water",
    "stage": "Main recipe solvent input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Na-acetate",
            "term": {
              "id": "CHEBI:32954",
              "label": "sodium acetate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32954",
              "label": "sodium acetate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "1.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "Na2SO4",
            "term": {
              "id": "CHEBI:32149",
              "label": "sodium sulfate"
            },
            "concentration": {
              "value": "0.4",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32149",
              "label": "sodium sulfate"
            }
          },
          {
            "preferred_term": "MgSO4",
            "term": {
              "id": "CHEBI:32599",
              "label": "magnesium sulfate"
            },
            "concentration": {
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32599",
              "label": "magnesium sulfate"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            }
          },
          {
            "preferred_term": "FeSO4",
            "term": {
              "id": "CHEBI:75832",
              "label": "iron(2+) sulfate (anhydrous)"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75832",
              "label": "iron(2+) sulfate (anhydrous)"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Na-acetate",
            "term": {
              "id": "CHEBI:32954",
              "label": "sodium acetate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32954",
              "label": "sodium acetate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 36.5703,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Na-acetate) in MediaDive medium 610; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "1.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 24.1449,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (KCl) in MediaDive medium 610; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.8; check: 1.8 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.8 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Na2SO4",
            "term": {
              "id": "CHEBI:32149",
              "label": "sodium sulfate"
            },
            "concentration": {
              "value": "0.4",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32149",
              "label": "sodium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 2.81611,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (Na2SO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.4; check: 0.4 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.4 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "MgSO4",
            "term": {
              "id": "CHEBI:32599",
              "label": "magnesium sulfate"
            },
            "concentration": {
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32599",
              "label": "magnesium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.66154,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (MgSO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (K2HPO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "FeSO4",
            "term": {
              "id": "CHEBI:75832",
              "label": "iron(2+) sulfate (anhydrous)"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75832",
              "label": "iron(2+) sulfate (anhydrous)"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\": 595,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0658285,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (FeSO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=0.01; check: 0.01 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.01 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[7].concentration (Yeast extract) in MediaDive medium 610; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=10; check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b. KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Na-acetate",
            "term": {
              "id": "CHEBI:32954",
              "label": "sodium acetate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32954",
              "label": "sodium acetate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 36.5703,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (Na-acetate) in MediaDive medium 610; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "1.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.8,\n                        \"mmol_l\": 24.1449,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (KCl) in MediaDive medium 610; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=1.8; check: 1.8 g * 1 g/g / (1000 ml / 1000 ml per L) = 1.8 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "Na2SO4",
            "term": {
              "id": "CHEBI:32149",
              "label": "sodium sulfate"
            },
            "concentration": {
              "value": "0.4",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32149",
              "label": "sodium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 2.81611,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (Na2SO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.4; check: 0.4 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.4 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "MgSO4",
            "term": {
              "id": "CHEBI:32599",
              "label": "magnesium sulfate"
            },
            "concentration": {
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32599",
              "label": "magnesium sulfate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4\",\n                        \"compound_id\": 325,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.66154,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (MgSO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 2.2045,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.7224,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (K2HPO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "FeSO4",
            "term": {
              "id": "CHEBI:75832",
              "label": "iron(2+) sulfate (anhydrous)"
            },
            "concentration": {
              "value": "0.01",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75832",
              "label": "iron(2+) sulfate (anhydrous)"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\": 595,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0658285,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (FeSO4) in MediaDive medium 610; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=0.01; check: 0.01 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.01 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/610",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[7].concentration (Yeast extract) in MediaDive medium 610; locator=$.data.solutions[0].recipe[7]. Provider explicitly reports g_l=10; check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b."
              }
            ]
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 1000,
      "source_unit": "ml",
      "representation": "Preserve as a preparation solvent input; not water mass or proof of final volume"
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Composition table final row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "mediadive610Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/610",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b"
      }
    ],
    "interpretation": "The source water entry is absent from all three layers. Preserve it in an appropriate preparation representation without creating a 1000 G_PER_L assertion or claiming volume additivity."
  },
  {
    "decision_id": "q26",
    "name": "pH",
    "stage": "Main medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 8.2
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.2
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.2
      }
    ],
    "desired": {
      "value": 8.2
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Terminal pH line",
        "exact_source_quote": "pH 8.2",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      }
    ],
    "interpretation": "All stored pH values agree with the primary. The attached ingredient amount evidence does not authenticate this separate field; attach a scoped pH claim."
  },
  {
    "decision_id": "q27",
    "name": "Retained pH preparation text",
    "stage": "DSMZ owner preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 8.2"
      }
    ],
    "desired": {
      "source_text": "pH 8.2"
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Terminal pH line",
        "exact_source_quote": "pH 8.2",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      }
    ],
    "interpretation": "The DSMZ owner already retains the exact pH instruction as MIX prose. Target and KOMODO owner lack preparation_steps; preserve the source scope without inferring a titrant or a mixing protocol."
  },
  {
    "decision_id": "q28",
    "name": "Missing pH preparation context",
    "stage": "Target and KOMODO preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "source_text": "pH 8.2"
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Terminal pH line",
        "exact_source_quote": "pH 8.2",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      }
    ],
    "interpretation": "Top-level pH already exists; this decision preserves the separately missing preparation context, not a new numerical pH."
  },
  {
    "decision_id": "q29",
    "name": "Unquantified conditions",
    "stage": "Preparation and cultivation",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "desired": {
      "measured_final_volume": null,
      "autoclave_temperature_or_duration": null,
      "incubation_temperature_or_duration": null,
      "pH_adjustment_agent_strength_or_dose": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Terminal primary line",
        "exact_source_quote": "pH 8.2",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      },
      {
        "source_key": "dsmz610",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf",
        "source_locator": "Water input",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c",
        "parsed_text_sha256": "fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474"
      }
    ],
    "interpretation": "The provider equipment list names an autoclave, but neither inspected source supplies a numerical cycle or cultivation temperature. Do not fabricate those quantities or a measured final volume."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:006100.

7 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 7/8 primary and 7/8 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 8: primary 87.50%; secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006100.

24 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact DSMZ and KOMODO source identity

identity: supported. Targets: CultureMech:006100.

The exact accession row, primary title and historical raw identify DSMZ 610. Two maintained contributors resolve by exact paths and IDs; their parent/child SOURCE_DUPLICATE links resolve. Shared source accession and composition support this relationship independently of a fingerprint, without asserting all historical source versions equivalent.

### Source formulas and supplied-form specificity

grounding: concern. Targets: CultureMech:006100.

KCl, Na2SO4, KH2PO4 and K2HPO4 identify the corresponding salts. Na-acetate, MgSO4 and FeSO4 are unqualified for supplied hydration; the asserted ontology formulas have no hydration water, with CHEBI:75832 explicitly named anhydrous. That extra supplied-form specificity remains unconfirmed rather than a demonstrated alternate hydrate. CHEBI:131527 has an anhydrous formula and a trihydrate synonym, so the synonym alone is not a basis for replacement or a hydrate conversion. Yeast extract is a complex mixture without an asserted single-chemical identifier.

### Layer-specific historical authentication and generated lag

evidence: concern. Targets: CultureMech:006100.

All sixteen maintained amount claims authenticate to the original raw bytes. Their provenance and direct evidence are missing from the earlier generated target. Verified quantity decisions apply only to each authenticated owner field; target amounts receive evidence-only decisions. The source water input is missing in every layer.

### pH, solvent and source limits

completeness: concern. Targets: CultureMech:006100.

The pH value 8.2 is present in all layers. The DSMZ owner retains pH prose, whereas target and KOMODO owner omit it; every layer omits 1000 mL water. The primary supplies no cycle, titrant or measured final volume.

### Classification and biological claims

scope: supported. Targets: CultureMech:006100.

The substantial yeast extract supports a complex, undefined liquid formulation. No organism-specific growth, current taxonomic name or temperature is asserted from the medium title. Catalog Aerobic metadata is provenance context and does not establish oxygen physiology.

## Findings

### f1: Solvent and preparation context are incompletely represented

major / open / confirmed; issue key: culturemech.006100.missing-water-and-preparation-context.

All layers omit the printed 1000 mL water input. The target and KOMODO owner lack the pH preparation prose retained in the DSMZ owner, although all already store pH 8.2.

### f2: Generated target lacks authenticated owner evidence

major / open / confirmed; issue key: culturemech.006100.stale-generated-amount-evidence.

The target has no attached ingredient evidence or source references, while both maintained owners have eight authenticated historical amount claims each. This is an observed layer difference, not proof that the current guarded merger discards evidence.

### f3: Supplied hydration is not established for the asserted forms

major / open / confirmed; issue key: culturemech.006100.unqualified-supplied-form-specificity.

The source names Na-acetate, MgSO4 and FeSO4 without hydration qualifiers, while the asserted structures are anhydrous, explicitly so for FeSO4. CHEBI:131527 also has a formula/synonym tension. No particular alternative hydrate or replacement ID is proven.

### f4: KOMODO import history has malformed and timezone-naive timestamps

minor / open / confirmed; issue key: culturemech.006100.malformed-import-timestamps.

The target and KOMODO owner retain one .fZ import timestamp and one timezone-naive resolver timestamp each. DSMZ owner timestamps are parseable.

## Recommended Actions And Acceptance Checks

### a1

Retain the solvent input as preparation context, preserve existing pH, and carry source-scoped preparation/evidence through separately authorized owner review and guarded regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve all sixteen owner claims, review exact formulation compatibility and regenerate only through the current supported path; confirm each intended amount claim survives at its correct field.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Obtain exact supplied-form evidence or qualify unsupported specificity; preserve original source wording and mass amounts without guessing hydrate conversions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve original history and append a supported provenance clarification when independently established; do not fabricate exact times.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch039/385/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/385/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml:1:id: CultureMech:006100<br>./data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml:1:id: CultureMech:006100<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch039/source-preflight-bound/385/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 13 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf; Complete DSMZ 610 composition table and pH line | supports | Eight gram amounts and 1000 mL distilled water are printed as recipe inputs; pH is 8.2. The water input is not an independently measured final volume. |
| provider | https://mediadive.dsmz.de/rest/medium/610; Historical $.data.medium and $.data.solutions[0], including recipe/volume/steps/equipment | supports | Exact historical raw response recovered with its original October 7 access time and hash. Provider volume is 1000 mL; g_l values are provider declarations, not measurements. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 610 row; identity and DSMZ source link only | supports | The catalog maps KOMODO 610 to the exact DSMZ 610 PDF. It supplies no ingredient quantities and proves no organism-specific physiology or historical variant equivalence. |
| mediadive610api-attempt | https://mediadive.dsmz.de/rest/medium/610; Preserved exact public retrieval result | context_only | The preserved mediadive610api attempt has HTTP status 503. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim. |
| mediadive610api_retry-attempt | https://mediadive.dsmz.de/rest/medium/610; Preserved exact public retrieval result | context_only | The preserved mediadive610api_retry attempt has HTTP status 503. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim. |
| komodo610detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=610; Preserved exact public retrieval result | context_only | The preserved komodo610detail attempt has HTTP status 403. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch039/385/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32149 resolves to sodium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32954 resolves to sodium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75832 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75832 resolves to iron(2+) sulfate (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75832": [{"label": "FeSO4", "match_type": "preferred_term", "identifier": "CHEBI:75832", "preferred_term": "FeSO4", "ontology_id": "CHEBI:75832", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml; data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:08.733548"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:08.733548"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml", "events": 7, "timestamp_issues": []}] |
| history-inventory | /private/tmp/culturemech-review-work-batch039/385/history-inventory.json; All sixteen owner ingredient claims, catalog identity claim and two scoped historical reports | context_only | Sixteen amount snippets match the recovered raw hash and exact source substrings. The KOMODO identity snippet matches catalog raw separately. No corresponding amount evidence is attached to the generated target. Reports and history are retained as provenance, not substituted for raw authentication. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer excludes solvent rows from ingredient edges and can consume provider g_l values. Current guarded merger requires encoded formulation compatibility and unions scoped evidence. These current mechanisms do not establish the historical cause of the observed stale target or guarantee compatible merging after future changes. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer excludes solvent rows from ingredient edges and can consume provider g_l values. Current guarded merger requires encoded formulation compatibility and unions scoped evidence. These current mechanisms do not establish the historical cause of the observed stale target or guarantee compatible merging after future changes. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer excludes solvent rows from ingredient edges and can consume provider g_l values. Current guarded merger requires encoded formulation compatibility and unions scoped evidence. These current mechanisms do not establish the historical cause of the observed stale target or guarantee compatible merging after future changes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved mediadive610api attempt has HTTP status 503. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim.
- The preserved mediadive610api_retry attempt has HTTP status 503. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim.
- The preserved komodo610detail attempt has HTTP status 403. Current exact primary and authenticated historical quantity raw are available; this optional access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence claim.
- Current source access failures remain preserved. Exact current primary and recovered historical raw resolve the material amount claims; unavailable optional KOMODO detail does not independently force partial completion.
- The source does not establish supplied hydrates, numerical sterilization or incubation conditions, measured final volume, or species/strain growth. These are explicit limits, not guessed corrections.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T215509Z-culturemech-006100-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_thermoalcalophilus_medium (CultureMech:006100)'
started_at: '2026-10-21T21:51:51Z'
finished_at: '2026-10-21T21:55:09Z'
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
summary: DSMZ 610 and the exact KOMODO accession support the medium identity and eight
  provider-normalized ingredient amounts. Both maintained owners have authenticated
  historical amount evidence that is absent from the generated target. Every layer
  omits the printed 1000 mL water input; only the DSMZ owner retains the pH preparation
  text. Source-unqualified supplied forms remain distinct from anhydrous ontology
  metadata.
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
  - path: data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
    sha256: 0eabe6f4e89f5583ab3d525077fcf21c968259d752ce9634ef3c4a03f588c01b
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    sha256: 5863bef59a82c062c2c6307bbeb014f892995001528bac1f221ae749423ba88e
    role: context
  - path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
    sha256: d86d218091fe401560706ea5509816b1a372969a0e3b52b2d9f049243e15ab6f
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml.md
    sha256: c7c5d71ae3e33040cfb0dd0e4a9af0a2b488ed8e6d501dda32db721370e97f95
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/bacillus_thermoalcalophilus_medium.yaml.md
    sha256: 7c99a1a13d8f6730f9e04dce276d3af65b8e4ab4f59b281ae309bae07e88e6a7
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
  selection: Task review 385; batch 039 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-eight task batches
    contain 380 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 383 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006100
targets:
- target_id: CultureMech:006100
  path: data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  label: bacillus_thermoalcalophilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/385/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/385/strict.tsv"
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006100
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
  - CultureMech:006100
- check_id: mediadive610api-source-access
  name: 'Exact source content access: mediadive610api'
  required: false
  status: unavailable
  summary: The preserved mediadive610api attempt has HTTP status 503. Current exact
    primary and authenticated historical quantity raw are available; this optional
    access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence
    claim.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - mediadive610api-attempt
- check_id: mediadive610api_retry-source-access
  name: 'Exact source content access: mediadive610api_retry'
  required: false
  status: unavailable
  summary: The preserved mediadive610api_retry attempt has HTTP status 503. Current
    exact primary and authenticated historical quantity raw are available; this optional
    access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence
    claim.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - mediadive610api_retry-attempt
- check_id: komodo610detail-source-access
  name: 'Exact source content access: komodo610detail'
  required: false
  status: unavailable
  summary: The preserved komodo610detail attempt has HTTP status 403. Current exact
    primary and authenticated historical quantity raw are available; this optional
    access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence
    claim.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - komodo610detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:24.473689Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/385/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:25.498912Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/385/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:26.707994Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:27.468736Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T21:55:08Z'
  support: supports
  summary: './data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml:1:id:
    CultureMech:006100

    ./data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml:1:id:
    CultureMech:006100

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/source-preflight-bound/385/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T21:55:08Z'
  support: supports
  summary: 13 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e7cccf8f647a4790d54428f10c1f9c538a80592fdb1b55cb07b2577425874643
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf
  locator: Complete DSMZ 610 composition table and pH line
  accessed_at: '2026-10-21T20:56:16.205884Z'
  support: supports
  summary: Eight gram amounts and 1000 mL distilled water are printed as recipe inputs;
    pH is 8.2. The water input is not an independently measured final volume.
  quote: 610. BACILLUS THERMOALCALOPHILUS MEDIUM
  snapshot_sha256: e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/610
  locator: Historical $.data.medium and $.data.solutions[0], including recipe/volume/steps/equipment
  accessed_at: '2026-10-07T12:16:22.795206Z'
  support: supports
  summary: Exact historical raw response recovered with its original October 7 access
    time and hash. Provider volume is 1000 mL; g_l values are provider declarations,
    not measurements.
  quote: '"volume": 1000'
  snapshot_sha256: b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 610 row; identity and DSMZ source link only
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The catalog maps KOMODO 610 to the exact DSMZ 610 PDF. It supplies no ingredient
    quantities and proves no organism-specific physiology or historical variant equivalence.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=610'\
    \ >610</a></TD>\n\t\t\t\t\t<TD>BACILLUS THERMOALCALOPHILUS medium</TD>\n\t\t\t\
    \t\t<TD> 8.2</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\
    \t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive610api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/610
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:14.878547Z'
  support: context_only
  summary: The preserved mediadive610api attempt has HTTP status 503. Current exact
    primary and authenticated historical quantity raw are available; this optional
    access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence
    claim.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive610api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/610
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:57:45.385801Z'
  support: context_only
  summary: The preserved mediadive610api_retry attempt has HTTP status 503. Current
    exact primary and authenticated historical quantity raw are available; this optional
    access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence
    claim.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo610detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=610
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T20:56:14.547336Z'
  support: context_only
  summary: The preserved komodo610detail attempt has HTTP status 403. Current exact
    primary and authenticated historical quantity raw are available; this optional
    access gap does not authenticate any unseen KOMODO detail or require a new historical-equivalence
    claim.
  snapshot_sha256: dc6a0d7534b93008bed923ae30ada4eb5282821bfbf246a736dd2a877db5b81e
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/385/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 01bf6c7bc28e24d312e9fb27aa10a3907c0e9e1048355ae089f82b22a22c3bb0
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
- evidence_id: chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.640268Z'
  support: supports
  summary: CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: CHEBI:32954 resolves to sodium acetate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
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
- evidence_id: chebi75832
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:01:47.645147Z'
  support: supports
  summary: CHEBI:75832 resolves to iron(2+) sulfate (anhydrous). Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9119cb3893b1a8171f719ef3e8fe6e5775a4fd59575baec8cd6da953801d089
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T21:55:08Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term",
    "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id":
    "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954":
    [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954",
    "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75832":
    [{"label": "FeSO4", "match_type": "preferred_term", "identifier": "CHEBI:75832",
    "preferred_term": "FeSO4", "ontology_id": "CHEBI:75832", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml;
    data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:08.733548"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:08.733548"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/385/history-inventory.json
  locator: All sixteen owner ingredient claims, catalog identity claim and two scoped
    historical reports
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Sixteen amount snippets match the recovered raw hash and exact source substrings.
    The KOMODO identity snippet matches catalog raw separately. No corresponding amount
    evidence is attached to the generated target. Reports and history are retained
    as provenance, not substituted for raw authentication.
  snapshot_sha256: 07bacd83f840d1cb06f11d215c9ffd27229f28c0c6f487131c17f920ba743831
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Current importer excludes solvent rows from ingredient edges and can consume
    provider g_l values. Current guarded merger requires encoded formulation compatibility
    and unions scoped evidence. These current mechanisms do not establish the historical
    cause of the observed stale target or guarantee compatible merging after future
    changes.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Current importer excludes solvent rows from ingredient edges and can consume
    provider g_l values. Current guarded merger requires encoded formulation compatibility
    and unions scoped evidence. These current mechanisms do not establish the historical
    cause of the observed stale target or guarantee compatible merging after future
    changes.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:55:08Z'
  support: context_only
  summary: Current importer excludes solvent rows from ingredient edges and can consume
    provider g_l values. Current guarded merger requires encoded formulation compatibility
    and unions scoped evidence. These current mechanisms do not establish the historical
    cause of the observed stale target or guarantee compatible merging after future
    changes.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 29 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Na-acetate\",\n\
    \    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 1\",\n        \"exact_source_quote\"\
    : \"Na-acetate 3.00 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Na-acetate\\\",\\n                        \\\"compound_id\\\
    \": 23,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 36.5703,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This generated field has no attached amount evidence;\
    \ externally authenticated support warrants evidence-only follow-up, not a verified\
    \ attached-evidence claim. Primary batch amounts and provider normalization remain\
    \ separate; no measured final volume or source hydrate is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"name\": \"Na-acetate\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 1\",\n        \"exact_source_quote\"\
    : \"Na-acetate 3.00 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Na-acetate\\\",\\n                        \\\"compound_id\\\
    \": 23,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 36.5703,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"name\": \"Na-acetate\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 1\",\n        \"exact_source_quote\"\
    : \"Na-acetate 3.00 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Na-acetate\\\",\\n                        \\\"compound_id\\\
    \": 23,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 36.5703,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\": \"KCl\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"1.8\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 1.8,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 2\",\n        \"exact_source_quote\"\
    : \"KCl 1.80 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 24.1449,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This generated field has no attached amount evidence;\
    \ externally authenticated support warrants evidence-only follow-up, not a verified\
    \ attached-evidence claim. Primary batch amounts and provider normalization remain\
    \ separate; no measured final volume or source hydrate is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q5\",\n    \"name\": \"KCl\",\n    \"stage\": \"\
    DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\": \"\
    verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"1.8\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 1.8,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 2\",\n        \"exact_source_quote\"\
    : \"KCl 1.80 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 24.1449,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"name\": \"KCl\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"1.8\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 1.8,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 2\",\n        \"exact_source_quote\"\
    : \"KCl 1.80 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\
    \": 61,\\n                        \\\"amount\\\": 1.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n \
    \                       \\\"mmol_l\\\": 24.1449,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"name\": \"Na2SO4\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.4\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.4,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 3\",\n        \"exact_source_quote\"\
    : \"Na2SO4 0.40 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2SO4\\\",\\n                        \\\"compound_id\\\
    \": 110,\\n                        \\\"amount\\\": 0.4,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n\
    \                        \\\"mmol_l\\\": 2.81611,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The stored numeral agrees with the exact historical\
    \ g_l field. This generated field has no attached amount evidence; externally\
    \ authenticated support warrants evidence-only follow-up, not a verified attached-evidence\
    \ claim. Primary batch amounts and provider normalization remain separate; no\
    \ measured final volume or source hydrate is inferred.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"name\": \"Na2SO4\",\n    \"stage\": \"DSMZ 610 main recipe, provider-declared\
    \ normalization\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.4\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.4,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 3\",\n        \"exact_source_quote\"\
    : \"Na2SO4 0.40 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2SO4\\\",\\n                        \\\"compound_id\\\
    \": 110,\\n                        \\\"amount\\\": 0.4,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n\
    \                        \\\"mmol_l\\\": 2.81611,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The stored numeral agrees with the exact historical\
    \ g_l field. This owner has attached matching amount evidence; verification applies\
    \ only to this field and layer. Primary batch amounts and provider normalization\
    \ remain separate; no measured final volume or source hydrate is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q9\",\n    \"name\": \"Na2SO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.4\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.4,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 3\",\n        \"exact_source_quote\"\
    : \"Na2SO4 0.40 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"Na2SO4\\\",\\n                        \\\"compound_id\\\
    \": 110,\\n                        \\\"amount\\\": 0.4,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n\
    \                        \\\"mmol_l\\\": 2.81611,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The stored numeral agrees with the exact historical\
    \ g_l field. This owner has attached matching amount evidence; verification applies\
    \ only to this field and layer. Primary batch amounts and provider normalization\
    \ remain separate; no measured final volume or source hydrate is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q10\",\n    \"name\": \"MgSO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\
    ,\n      \"original_primary_amount\": 0.2,\n      \"original_primary_unit\": \"\
    g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 4\",\n        \"exact_source_quote\"\
    : \"MgSO4 0.20 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\
    \": 325,\\n                        \\\"amount\\\": 0.2,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.66154,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The stored numeral agrees with the exact historical\
    \ g_l field. This generated field has no attached amount evidence; externally\
    \ authenticated support warrants evidence-only follow-up, not a verified attached-evidence\
    \ claim. Primary batch amounts and provider normalization remain separate; no\
    \ measured final volume or source hydrate is inferred.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"MgSO4\",\n    \"stage\": \"DSMZ 610 main recipe, provider-declared\
    \ normalization\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.2,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 4\",\n        \"exact_source_quote\"\
    : \"MgSO4 0.20 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\
    \": 325,\\n                        \\\"amount\\\": 0.2,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.66154,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The stored numeral agrees with the exact historical\
    \ g_l field. This owner has attached matching amount evidence; verification applies\
    \ only to this field and layer. Primary batch amounts and provider normalization\
    \ remain separate; no measured final volume or source hydrate is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q12\",\n    \"name\": \"MgSO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.2,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 4\",\n        \"exact_source_quote\"\
    : \"MgSO4 0.20 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\
    \": 325,\\n                        \\\"amount\\\": 0.2,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.66154,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n      }\n\
    \    ],\n    \"interpretation\": \"The stored numeral agrees with the exact historical\
    \ g_l field. This owner has attached matching amount evidence; verification applies\
    \ only to this field and layer. Primary batch amounts and provider normalization\
    \ remain separate; no measured final volume or source hydrate is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q13\",\n    \"name\": \"KH2PO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n\
    \    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"unit\": \"G_PER_L\"\
    ,\n      \"original_primary_amount\": 0.3,\n      \"original_primary_unit\": \"\
    g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 5\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.30 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 2.2045,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This generated field has no attached amount evidence;\
    \ externally authenticated support warrants evidence-only follow-up, not a verified\
    \ attached-evidence claim. Primary batch amounts and provider normalization remain\
    \ separate; no measured final volume or source hydrate is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q14\",\n    \"name\": \"KH2PO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 5\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.30 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 2.2045,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"name\": \"KH2PO4\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 5\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.30 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 2.2045,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"name\": \"K2HPO4\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 6\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.30 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 1.7224,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This generated field has no attached amount evidence;\
    \ externally authenticated support warrants evidence-only follow-up, not a verified\
    \ attached-evidence claim. Primary batch amounts and provider normalization remain\
    \ separate; no measured final volume or source hydrate is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q17\",\n    \"name\": \"K2HPO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 6\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.30 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 1.7224,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"name\": \"K2HPO4\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.3\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 0.3,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 6\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.30 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 1.7224,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"FeSO4\"\
    ,\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.01\",\n      \"\
    unit\": \"G_PER_L\",\n      \"original_primary_amount\": 0.01,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 7\",\n        \"exact_source_quote\"\
    : \"FeSO4 0.01 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4\\\",\\n                        \\\"compound_id\\\
    \": 595,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0658285,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the exact\
    \ historical g_l field. This generated field has no attached amount evidence;\
    \ externally authenticated support warrants evidence-only follow-up, not a verified\
    \ attached-evidence claim. Primary batch amounts and provider normalization remain\
    \ separate; no measured final volume or source hydrate is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q20\",\n    \"name\": \"FeSO4\",\n    \"stage\":\
    \ \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.01\",\n      \"\
    unit\": \"G_PER_L\",\n      \"original_primary_amount\": 0.01,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 7\",\n        \"exact_source_quote\"\
    : \"FeSO4 0.01 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4\\\",\\n                        \\\"compound_id\\\
    \": 595,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0658285,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the exact\
    \ historical g_l field. This owner has attached matching amount evidence; verification\
    \ applies only to this field and layer. Primary batch amounts and provider normalization\
    \ remain separate; no measured final volume or source hydrate is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q21\",\n    \"name\": \"FeSO4\",\n    \"stage\"\
    : \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.01\",\n      \"\
    unit\": \"G_PER_L\",\n      \"original_primary_amount\": 0.01,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 7\",\n        \"exact_source_quote\"\
    : \"FeSO4 0.01 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4\\\",\\n                        \\\"compound_id\\\
    \": 595,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0658285,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\n     \
    \ }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the exact\
    \ historical g_l field. This owner has attached matching amount evidence; verification\
    \ applies only to this field and layer. Primary batch amounts and provider normalization\
    \ remain separate; no measured final volume or source hydrate is inferred.\"\n\
    \  },\n  {\n    \"decision_id\": \"q22\",\n    \"name\": \"Yeast extract\",\n\
    \    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 10,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 8\",\n        \"exact_source_quote\"\
    : \"Yeast extract 10.00 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 10,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 10,\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This generated field has no attached amount evidence;\
    \ externally authenticated support warrants evidence-only follow-up, not a verified\
    \ attached-evidence claim. Primary batch amounts and provider normalization remain\
    \ separate; no measured final volume or source hydrate is inferred.\"\n  },\n\
    \  {\n    \"decision_id\": \"q23\",\n    \"name\": \"Yeast extract\",\n    \"\
    stage\": \"DSMZ 610 main recipe, provider-declared normalization\",\n    \"decision\"\
    : \"verified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 10,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 8\",\n        \"exact_source_quote\"\
    : \"Yeast extract 10.00 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 10,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 10,\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"name\": \"Yeast\
    \ extract\",\n    \"stage\": \"DSMZ 610 main recipe, provider-declared normalization\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"original_primary_amount\": 10,\n      \"original_primary_unit\"\
    : \"g\",\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Composition table row 8\",\n        \"exact_source_quote\"\
    : \"Yeast extract 10.00 g\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 10,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 10,\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored numeral agrees with the\
    \ exact historical g_l field. This owner has attached matching amount evidence;\
    \ verification applies only to this field and layer. Primary batch amounts and\
    \ provider normalization remain separate; no measured final volume or source hydrate\
    \ is inferred.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"name\": \"Distilled\
    \ water\",\n    \"stage\": \"Main recipe solvent input\",\n    \"decision\": \"\
    add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Na-acetate\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:32954\",\n              \"label\": \"sodium acetate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32954\",\n              \"label\": \"sodium\
    \ acetate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"KCl\",\n            \"term\": {\n              \"id\": \"CHEBI:32588\",\n\
    \              \"label\": \"potassium chloride\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"1.8\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32588\",\n              \"label\": \"potassium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SO4\",\n            \"term\": {\n              \"id\": \"CHEBI:32149\"\
    ,\n              \"label\": \"sodium sulfate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.4\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32149\",\n              \"label\": \"sodium\
    \ sulfate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4\",\n            \"term\": {\n              \"id\": \"CHEBI:32599\",\n\
    \              \"label\": \"magnesium sulfate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.2\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32599\",\n              \"label\": \"magnesium\
    \ sulfate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.3\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"K2HPO4\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium hydrogen phosphate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            }\n          },\n          {\n           \
    \ \"preferred_term\": \"FeSO4\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:75832\",\n              \"label\": \"iron(2+) sulfate (anhydrous)\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    0.01\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75832\",\n              \"label\": \"iron(2+)\
    \ sulfate (anhydrous)\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"Yeast extract\",\n            \"concentration\": {\n\
    \              \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n     \
    \       }\n          }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Na-acetate\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:32954\",\n              \"label\": \"sodium acetate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32954\",\n              \"label\": \"sodium\
    \ acetate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 1,\\n                        \\\
    \"compound\\\": \\\"Na-acetate\\\",\\n                        \\\"compound_id\\\
    \": 23,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 36.5703,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[0].concentration (Na-acetate) in MediaDive medium 610;\
    \ locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=3; check:\
    \ 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KCl\",\n            \"term\": {\n              \"id\": \"CHEBI:32588\",\n\
    \              \"label\": \"potassium chloride\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"1.8\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32588\",\n              \"label\": \"potassium\
    \ chloride\"\n            },\n            \"evidence\": [\n              {\n \
    \               \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 2,\\n                        \\\
    \"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 1.8,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n                \
    \        \\\"mmol_l\\\": 24.1449,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[1].concentration (KCl) in MediaDive medium 610; locator=$.data.solutions[0].recipe[1].\
    \ Provider explicitly reports g_l=1.8; check: 1.8 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 1.8 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SO4\",\n            \"term\": {\n              \"id\": \"CHEBI:32149\"\
    ,\n              \"label\": \"sodium sulfate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.4\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32149\",\n              \"label\": \"sodium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 3,\\n                        \\\
    \"compound\\\": \\\"Na2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 110,\\n                        \\\"amount\\\": 0.4,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n  \
    \                      \\\"mmol_l\\\": 2.81611,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (Na2SO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.4; check: 0.4 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.4 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4\",\n            \"term\": {\n              \"id\": \"CHEBI:32599\",\n\
    \              \"label\": \"magnesium sulfate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.2\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32599\",\n              \"label\": \"magnesium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 4,\\n                        \\\
    \"compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\":\
    \ 325,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n  \
    \                      \\\"mmol_l\\\": 1.66154,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[3].concentration (MgSO4) in MediaDive medium\
    \ 610; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.2;\
    \ check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the\
    \ provider-declared main-recipe concentration, not an independently measured final\
    \ volume, a stock composition, or a downstream assay dilution. Water alone does\
    \ not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.3\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 2.2045,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports\
    \ g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"K2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:131527\"\
    ,\n              \"label\": \"dipotassium hydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.3\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 1.7224,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[5].concentration (K2HPO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports\
    \ g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"FeSO4\",\n            \"term\": {\n              \"id\": \"CHEBI:75832\",\n\
    \              \"label\": \"iron(2+) sulfate (anhydrous)\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.01\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75832\",\n              \"label\": \"iron(2+)\
    \ sulfate (anhydrous)\"\n            },\n            \"evidence\": [\n       \
    \       {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 7,\\n                      \
    \  \\\"compound\\\": \\\"FeSO4\\\",\\n                        \\\"compound_id\\\
    \": 595,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0658285,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[6].concentration (FeSO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports\
    \ g_l=0.01; check: 0.01 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.01 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"10\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 8,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \         \"explanation\": \"Concentration evidence for ingredients[7].concentration\
    \ (Yeast extract) in MediaDive medium 610; locator=$.data.solutions[0].recipe[7].\
    \ Provider explicitly reports g_l=10; check: 10 g * 1 g/g / (1000 ml / 1000 ml\
    \ per L) = 10 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\
    \ KOMODO accession 610 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Na-acetate\",\n            \"term\": {\n\
    \              \"id\": \"CHEBI:32954\",\n              \"label\": \"sodium acetate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32954\",\n              \"label\": \"sodium\
    \ acetate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 1,\\n                        \\\
    \"compound\\\": \\\"Na-acetate\\\",\\n                        \\\"compound_id\\\
    \": 23,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 36.5703,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[0].concentration (Na-acetate) in MediaDive medium 610;\
    \ locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=3; check:\
    \ 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KCl\",\n            \"term\": {\n              \"id\": \"CHEBI:32588\",\n\
    \              \"label\": \"potassium chloride\"\n            },\n           \
    \ \"concentration\": {\n              \"value\": \"1.8\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32588\",\n              \"label\": \"potassium\
    \ chloride\"\n            },\n            \"evidence\": [\n              {\n \
    \               \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 2,\\n                        \\\
    \"compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 1.8,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.8,\\n                \
    \        \\\"mmol_l\\\": 24.1449,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[1].concentration (KCl) in MediaDive medium 610; locator=$.data.solutions[0].recipe[1].\
    \ Provider explicitly reports g_l=1.8; check: 1.8 g * 1 g/g / (1000 ml / 1000\
    \ ml per L) = 1.8 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na2SO4\",\n            \"term\": {\n              \"id\": \"CHEBI:32149\"\
    ,\n              \"label\": \"sodium sulfate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.4\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32149\",\n              \"label\": \"sodium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 3,\\n                        \\\
    \"compound\\\": \\\"Na2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 110,\\n                        \\\"amount\\\": 0.4,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n  \
    \                      \\\"mmol_l\\\": 2.81611,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (Na2SO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.4; check: 0.4 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.4 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4\",\n            \"term\": {\n              \"id\": \"CHEBI:32599\",\n\
    \              \"label\": \"magnesium sulfate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"0.2\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32599\",\n              \"label\": \"magnesium\
    \ sulfate\"\n            },\n            \"evidence\": [\n              {\n  \
    \              \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\",\n\
    \                \"supports\": \"SUPPORT\",\n                \"snippet\": \"{\\\
    n                        \\\"recipe_order\\\": 4,\\n                        \\\
    \"compound\\\": \\\"MgSO4\\\",\\n                        \\\"compound_id\\\":\
    \ 325,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n  \
    \                      \\\"mmol_l\\\": 1.66154,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[3].concentration (MgSO4) in MediaDive medium\
    \ 610; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.2;\
    \ check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the\
    \ provider-declared main-recipe concentration, not an independently measured final\
    \ volume, a stock composition, or a downstream assay dilution. Water alone does\
    \ not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.3\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 2.2045,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports\
    \ g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"K2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:131527\"\
    ,\n              \"label\": \"dipotassium hydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.3\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.3,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n \
    \                       \\\"mmol_l\\\": 1.7224,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[5].concentration (K2HPO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports\
    \ g_l=0.3; check: 0.3 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.3 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"FeSO4\",\n            \"term\": {\n              \"id\": \"CHEBI:75832\",\n\
    \              \"label\": \"iron(2+) sulfate (anhydrous)\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.01\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75832\",\n              \"label\": \"iron(2+)\
    \ sulfate (anhydrous)\"\n            },\n            \"evidence\": [\n       \
    \       {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 7,\\n                      \
    \  \\\"compound\\\": \\\"FeSO4\\\",\\n                        \\\"compound_id\\\
    \": 595,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0658285,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[6].concentration (FeSO4) in MediaDive\
    \ medium 610; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports\
    \ g_l=0.01; check: 0.01 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.01 g/L. This\
    \ supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T12:16:22.795206+00:00;\
    \ response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"10\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/610\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 8,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \         \"explanation\": \"Concentration evidence for ingredients[7].concentration\
    \ (Yeast extract) in MediaDive medium 610; locator=$.data.solutions[0].recipe[7].\
    \ Provider explicitly reports g_l=10; check: 10 g * 1 g/g / (1000 ml / 1000 ml\
    \ per L) = 10 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T12:16:22.795206+00:00; response SHA256=b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b.\"\
    \n              }\n            ]\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 1000,\n      \"source_unit\": \"ml\"\
    ,\n      \"representation\": \"Preserve as a preparation solvent input; not water\
    \ mass or proof of final volume\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz610\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\"\
    ,\n        \"source_locator\": \"Composition table final row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"mediadive610Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/610\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b1ab73351f22613b26d3aa915047a0d1996486ef4b1b07564b5c85a4c9a4bd3b\"\
    \n      }\n    ],\n    \"interpretation\": \"The source water entry is absent\
    \ from all three layers. Preserve it in an appropriate preparation representation\
    \ without creating a 1000 G_PER_L assertion or claiming volume additivity.\"\n\
    \  },\n  {\n    \"decision_id\": \"q26\",\n    \"name\": \"pH\",\n    \"stage\"\
    : \"Main medium\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.2\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.2\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 8.2\n      }\n \
    \   ],\n    \"desired\": {\n      \"value\": 8.2\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n        \"\
    source_locator\": \"Terminal pH line\",\n        \"exact_source_quote\": \"pH\
    \ 8.2\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      }\n    ],\n    \"interpretation\": \"All stored pH values agree with the\
    \ primary. The attached ingredient amount evidence does not authenticate this\
    \ separate field; attach a scoped pH claim.\"\n  },\n  {\n    \"decision_id\"\
    : \"q27\",\n    \"name\": \"Retained pH preparation text\",\n    \"stage\": \"\
    DSMZ owner preparation\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"pH 8.2\"\n      }\n    ],\n    \"desired\": {\n      \"source_text\": \"pH\
    \ 8.2\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz610\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\"\
    ,\n        \"source_locator\": \"Terminal pH line\",\n        \"exact_source_quote\"\
    : \"pH 8.2\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      }\n    ],\n    \"interpretation\": \"The DSMZ owner already retains the\
    \ exact pH instruction as MIX prose. Target and KOMODO owner lack preparation_steps;\
    \ preserve the source scope without inferring a titrant or a mixing protocol.\"\
    \n  },\n  {\n    \"decision_id\": \"q28\",\n    \"name\": \"Missing pH preparation\
    \ context\",\n    \"stage\": \"Target and KOMODO preparation\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_text\": \"pH 8.2\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz610\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\"\
    ,\n        \"source_locator\": \"Terminal pH line\",\n        \"exact_source_quote\"\
    : \"pH 8.2\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      }\n    ],\n    \"interpretation\": \"Top-level pH already exists; this\
    \ decision preserves the separately missing preparation context, not a new numerical\
    \ pH.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"name\": \"Unquantified\
    \ conditions\",\n    \"stage\": \"Preparation and cultivation\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\",\n        \"\
    field_path\": \"temperature_value\",\n        \"stored\": null\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOALCALOPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"desired\": {\n      \"measured_final_volume\": null,\n   \
    \   \"autoclave_temperature_or_duration\": null,\n      \"incubation_temperature_or_duration\"\
    : null,\n      \"pH_adjustment_agent_strength_or_dose\": null\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz610\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\"\
    ,\n        \"source_locator\": \"Terminal primary line\",\n        \"exact_source_quote\"\
    : \"pH 8.2\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      },\n      {\n        \"source_key\": \"dsmz610\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium610.pdf\",\n    \
    \    \"source_locator\": \"Water input\",\n        \"exact_source_quote\": \"\
    Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"e65f315af4b6d8ff08e4eac88572f74402306de64d1a456050b21ade56a3782c\"\
    ,\n        \"parsed_text_sha256\": \"fa16eb013563a2c370931f84ca038a3743def0cb744cc00e9af30ada4db8f474\"\
    \n      }\n    ],\n    \"interpretation\": \"The provider equipment list names\
    \ an autoclave, but neither inspected source supplies a numerical cycle or cultivation\
    \ temperature. Do not fabricate those quantities or a measured final volume.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '7 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 7/8 primary
    and 7/8 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi32149
  - chebi32588
  - chebi32599
  - chebi32954
  - chebi63036
  - chebi75832
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 87.50%;
    secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 24 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Exact DSMZ and KOMODO source identity
  outcome: supported
  summary: The exact accession row, primary title and historical raw identify DSMZ
    610. Two maintained contributors resolve by exact paths and IDs; their parent/child
    SOURCE_DUPLICATE links resolve. Shared source accession and composition support
    this relationship independently of a fingerprint, without asserting all historical
    source versions equivalent.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - primary
  - provider
  - catalog
  - record
  - owner-0
  - owner-1
- assessment_id: forms
  area: grounding
  topic: Source formulas and supplied-form specificity
  outcome: concern
  summary: KCl, Na2SO4, KH2PO4 and K2HPO4 identify the corresponding salts. Na-acetate,
    MgSO4 and FeSO4 are unqualified for supplied hydration; the asserted ontology
    formulas have no hydration water, with CHEBI:75832 explicitly named anhydrous.
    That extra supplied-form specificity remains unconfirmed rather than a demonstrated
    alternate hydrate. CHEBI:131527 has an anhydrous formula and a trihydrate synonym,
    so the synonym alone is not a basis for replacement or a hydrate conversion. Yeast
    extract is a complex mixture without an asserted single-chemical identifier.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - primary
  - chebi32588
  - chebi32149
  - chebi63036
  - chebi131527
  - chebi32954
  - chebi32599
  - chebi75832
- assessment_id: evidence-placement
  area: evidence
  topic: Layer-specific historical authentication and generated lag
  outcome: concern
  summary: All sixteen maintained amount claims authenticate to the original raw bytes.
    Their provenance and direct evidence are missing from the earlier generated target.
    Verified quantity decisions apply only to each authenticated owner field; target
    amounts receive evidence-only decisions. The source water input is missing in
    every layer.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - provider
  - history-inventory
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: pH, solvent and source limits
  outcome: concern
  summary: The pH value 8.2 is present in all layers. The DSMZ owner retains pH prose,
    whereas target and KOMODO owner omit it; every layer omits 1000 mL water. The
    primary supplies no cycle, titrant or measured final volume.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-1
- assessment_id: growth
  area: scope
  topic: Classification and biological claims
  outcome: supported
  summary: The substantial yeast extract supports a complex, undefined liquid formulation.
    No organism-specific growth, current taxonomic name or temperature is asserted
    from the medium title. Catalog Aerobic metadata is provenance context and does
    not establish oxygen physiology.
  target_ids:
  - CultureMech:006100
  evidence_ids:
  - record
  - primary
  - catalog
findings:
- finding_id: f1
  issue_key: culturemech.006100.missing-water-and-preparation-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Solvent and preparation context are incompletely represented
  description: All layers omit the printed 1000 mL water input. The target and KOMODO
    owner lack the pH preparation prose retained in the DSMZ owner, although all already
    store pH 8.2.
  target_ids:
  - CultureMech:006100
  field_paths:
  - ingredients
  - preparation_steps
  - ph_value
  evidence_ids:
  - primary
  - quantity-inventory
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
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
  issue_key: culturemech.006100.stale-generated-amount-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated target lacks authenticated owner evidence
  description: The target has no attached ingredient evidence or source references,
    while both maintained owners have eight authenticated historical amount claims
    each. This is an observed layer difference, not proof that the current guarded
    merger discards evidence.
  target_ids:
  - CultureMech:006100
  field_paths:
  - ingredients[*].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - provider
  - history-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
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
  issue_key: culturemech.006100.unqualified-supplied-form-specificity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Supplied hydration is not established for the asserted forms
  description: The source names Na-acetate, MgSO4 and FeSO4 without hydration qualifiers,
    while the asserted structures are anhydrous, explicitly so for FeSO4. CHEBI:131527
    also has a formula/synonym tension. No particular alternative hydrate or replacement
    ID is proven.
  target_ids:
  - CultureMech:006100
  field_paths:
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  - ingredients[3].term
  - ingredients[3].mediaingredientmech_chebi_term
  - ingredients[5].term
  - ingredients[5].mediaingredientmech_chebi_term
  - ingredients[6].term
  - ingredients[6].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - chebi32954
  - chebi32599
  - chebi131527
  - chebi75832
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
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
  issue_key: culturemech.006100.malformed-import-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO import history has malformed and timezone-naive timestamps
  description: The target and KOMODO owner retain one .fZ import timestamp and one
    timezone-naive resolver timestamp each. DSMZ owner timestamps are parseable.
  target_ids:
  - CultureMech:006100
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
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
  description: Retain the solvent input as preparation context, preserve existing
    pH, and carry source-scoped preparation/evidence through separately authorized
    owner review and guarded regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006100
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
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
  description: Preserve all sixteen owner claims, review exact formulation compatibility
    and regenerate only through the current supported path; confirm each intended
    amount claim survives at its correct field.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006100
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
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
  description: Obtain exact supplied-form evidence or qualify unsupported specificity;
    preserve original source wording and mass amounts without guessing hydrate conversions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006100
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml
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
  description: Preserve original history and append a supported provenance clarification
    when independently established; do not fabricate exact times.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006100
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml
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
- The preserved mediadive610api attempt has HTTP status 503. Current exact primary
  and authenticated historical quantity raw are available; this optional access gap
  does not authenticate any unseen KOMODO detail or require a new historical-equivalence
  claim.
- The preserved mediadive610api_retry attempt has HTTP status 503. Current exact primary
  and authenticated historical quantity raw are available; this optional access gap
  does not authenticate any unseen KOMODO detail or require a new historical-equivalence
  claim.
- The preserved komodo610detail attempt has HTTP status 403. Current exact primary
  and authenticated historical quantity raw are available; this optional access gap
  does not authenticate any unseen KOMODO detail or require a new historical-equivalence
  claim.
- Current source access failures remain preserved. Exact current primary and recovered
  historical raw resolve the material amount claims; unavailable optional KOMODO detail
  does not independently force partial completion.
- The source does not establish supplied hydrates, numerical sterilization or incubation
  conditions, measured final volume, or species/strain growth. These are explicit
  limits, not guessed corrections.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-039
- generated-medium
```
