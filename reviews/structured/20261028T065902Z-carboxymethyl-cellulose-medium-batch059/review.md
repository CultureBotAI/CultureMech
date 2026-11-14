# Carboxymethyl cellulose medium: source preparation, evidence and material identity

- Review: 20261028T065902Z-carboxymethyl-cellulose-medium-batch059
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:47:42.108335Z
- Finished UTC: 2026-10-28T06:59:02.701602Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM1111 amounts and six existing source claims are supported. Three major findings concern missing preparation, generated evidence loss and generic/sodium CMC identity divergence; one minor finding concerns KOMODO provenance. Exact current KOMODO sources remain inaccessible.

## Scope And Provenance

One entire generated record and both maintained contributors:24 local concentration fields, nine source recipe rows, exact chemical IDs, preparation, reciprocal references, history and current writers.

Selection: Batch059 item10 from Python-sorted uncovered paths in successful native lists;513 of6325 corpus paths covered at selection.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003813 | data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml | generated | carboxymethyl_cellulose_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003813 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003813 | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch059/record10/strict.tsv |
| validate-terms | passed | True | CultureMech:003813 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003813 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| check-mim-label-index | passed | True | CultureMech:003813 | MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9<br>Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350<br><br>uv run python scripts/check_mim_label_index.py |
| Manual embedded history and registry assessment | passed | False | CultureMech:003813 | Entire target and both owners read, including malformed historical KOMODO timestamp and later evidence event; exact registry routes checked. Standalone HistoryRecord validator is not an embedded-history checker. |
| Current KOMODO detail and mapping source access | unavailable | True | CultureMech:003813 | Both exact source routes return403. Historical identity context remains explicit and this review is partial. |
| Full-corpus ID, product and merge gates | skipped | False | CultureMech:003813 | No corpus, schema, ID or generator was changed. Full-corpus assign-ids-check,validate-products,verify-merges and audit-merge-freshness were not run; no narrower substitute is claimed. |

## Scientific And Domain Assessments

### DSM1111 provenance and source-duplicate boundary

identity: concern. Targets: CultureMech:003813.

The exact DSM1111 primary and database support the intended medium; stable IDs and reciprocal maintained references resolve. Current KOMODO access and its atmosphere metadata remain unresolved.

Solid agar and complex/undefined composition are supported by agar and Casitone. No organism or growth claim is inferred. The same ingredient set does not prove identical preparation or historical source conditions; current notes, preparation and ancestry differ. iModulonDB is not applicable to this source-defined formulation without a gene, dataset or computational-module assertion.

### Every local concentration and source-only solvent

quantity: supported. Targets: CultureMech:003813.

All eight selected values agree with explicit database g_l; six existing DSM-owner evidence objects authenticate literally against identical fresh bytes. Missing evidence and preparation do not justify changing supported numeric values.

[
  {
    "decision_id": "q01",
    "ingredient": "(NH4)2SO4",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[0].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[0].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[0].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "verified",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[0]",
    "source_snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 7.56773,\n                        \"optional\": 0\n                    }",
    "source_amount": 1,
    "source_unit": "g",
    "provider_g_l": 1,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "1 g / (1000 mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added."
  },
  {
    "decision_id": "q02",
    "ingredient": "MgSO4 x 7 H2O",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[1].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[1].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[1].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "verified",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[1]",
    "source_snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }",
    "source_amount": 1,
    "source_unit": "g",
    "provider_g_l": 1,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "1 g / (1000 mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added."
  },
  {
    "decision_id": "q03",
    "ingredient": "CaCl2 x 2 H2O",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[2].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[2].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[2].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "verified",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[2]",
    "source_snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 6.80203,\n                        \"optional\": 0\n                    }",
    "source_amount": 1,
    "source_unit": "g",
    "provider_g_l": 1,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "1 g / (1000 mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added."
  },
  {
    "decision_id": "q04",
    "ingredient": "FeCl3",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[3].concentration",
        "existing": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 0.2,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[3].concentration",
        "existing": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 0.2,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[3].concentration",
        "existing": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "status": "verified",
        "proposed_value": 0.2,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[3]",
    "source_snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3\",\n                        \"compound_id\": 403,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.23305,\n                        \"optional\": 0\n                    }",
    "source_amount": 0.2,
    "source_unit": "g",
    "provider_g_l": 0.2,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "0.2 g / (1000 mL / 1000 mL per L) = 0.2 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added."
  },
  {
    "decision_id": "q05",
    "ingredient": "K2HPO4",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[4].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[4].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[4].concentration",
        "existing": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 1,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[4]",
    "source_snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"attribute\": \"autoclaved separately\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }",
    "source_amount": 1,
    "source_unit": "g",
    "provider_g_l": 1,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "1 g / (1000 mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added. The phosphate-specific separate-autoclaving instruction is essential context, not a different amount or unspecified stock strength."
  },
  {
    "decision_id": "q06",
    "ingredient": "Casitone",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[5].concentration",
        "existing": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 2,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[5].concentration",
        "existing": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 2,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[5].concentration",
        "existing": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 2,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[5]",
    "source_snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Casitone\",\n                        \"compound_id\": 84,\n                        \"attribute\": \"Difco\",\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }",
    "source_amount": 2,
    "source_unit": "g",
    "provider_g_l": 2,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "2 g / (1000 mL / 1000 mL per L) = 2 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added. Difco identifies the supplied Casitone product; this attribute does not by itself make the explicitly stated amount unknown."
  },
  {
    "decision_id": "q07",
    "ingredient": "Carboxymethyl cellulose",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[6].concentration",
        "existing": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 15,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[6].concentration",
        "existing": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 15,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[6].concentration",
        "existing": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "status": "verified",
        "proposed_value": 15,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[6]",
    "source_snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Carboxymethyl cellulose\",\n                        \"compound_id\": 989,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 62.4454,\n                        \"optional\": 0\n                    }",
    "source_amount": 15,
    "source_unit": "g",
    "provider_g_l": 15,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "15 g / (1000 mL / 1000 mL per L) = 15 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added. The primary table names generic CMC and separately recommends sodium salt of high viscosity. Its15g input is supported; chemical-form/grade reconciliation is a separate finding. No polymer molarity is endorsed."
  },
  {
    "decision_id": "q08",
    "ingredient": "Agar",
    "local_claims": [
      {
        "path": "data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml",
        "field": "ingredients[7].concentration",
        "existing": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 6,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml",
        "field": "ingredients[7].concentration",
        "existing": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "status": "evidence_only",
        "proposed_value": 6,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      },
      {
        "path": "data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml",
        "field": "ingredients[7].concentration",
        "existing": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "status": "verified",
        "proposed_value": 6,
        "proposed_unit": "G_PER_L",
        "action_taken": "none"
      }
    ],
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[7]",
    "source_snippet": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 6,\n                        \"unit\": \"g\",\n                        \"g_l\": 6,\n                        \"mmol_l\": 17.8396,\n                        \"optional\": 0\n                    }",
    "source_amount": 6,
    "source_unit": "g",
    "provider_g_l": 6,
    "provider_volume_ml": 1000,
    "basis": "Explicit database normalization for main solution1111, with primary batch amount independently compared.",
    "calculation": "6 g / (1000 mL / 1000 mL per L) = 6 g/L reproduces the provider declaration; not an inference from water alone.",
    "decision_notes": "Provider-declared main concentration agrees with the local value. Primary gives batch mass and water input, not a measured final-volume statement; no independent final-volume claim is added."
  },
  {
    "decision_id": "q09",
    "ingredient": "Distilled water",
    "local_claims": [],
    "status": "add",
    "reference": "https://mediadive.dsmz.de/rest/medium/1111",
    "locator": "$.data.solutions[0].recipe[8]",
    "source_snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
    "source_amount": 1000,
    "source_unit": "ml",
    "proposed_representation": "Preserve1000ml solvent input in source-scoped preparation/evidence; no water mass, percentage or final-volume concentration asserted.",
    "decision_notes": "Absent from target and both owners. Preserve as preparation solvent rather than assuming water alone defines final volume.",
    "action_taken": "none"
  }
]

### Separate sterilization, source material and solvent context

completeness: concern. Targets: CultureMech:003813.

Both owners omit phosphate separate-autoclaving and explicit preparation water; the generated target also omits the DSM-owner material recommendation. Neither source states pH, incubation, sterilization duration or temperature.

Preserve the Casitone manufacturer qualifier. The CMC sodium-salt/high-viscosity sentence is a recommended material, not an imperative mixing instruction or evidence that every generic CMC formulation requires that exact product. The existing DSM-owner MIX label derives from classifier fallback. No new pH, atmosphere, incubation, vessel, growth or sterilization parameters are supplied.

### Chemical form and MIM publication identity

grounding: concern. Targets: CultureMech:003813.

All seven asserted CHEBI IDs resolve with matching current labels; six of seven existing secondary IDs agree with the maintained MIM resolver. Generic CMC differs from the sodium-salt identity returned for that label.

[{"field": "ingredients[0]", "ingredient": {"preferred_term": "(NH4)2SO4", "term": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:62946", "label": "ammonium sulfate"}}, "decision": {"query_label": "(NH4)2SO4", "identifier": "CHEBI:62946", "ontology_id": "CHEBI:62946", "mim_preferred_term": "(NH4)2SO4", "matched_label": "(NH4)2SO4", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:62946", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[1]", "ingredient": {"preferred_term": "MgSO4 x 7 H2O", "term": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "concentration": {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}}, "decision": {"query_label": "MgSO4 x 7 H2O", "identifier": "CHEBI:31795", "ontology_id": "CHEBI:31795", "mim_preferred_term": "MgSO4 x 7 H2O", "matched_label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:31795", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[2]", "ingredient": {"preferred_term": "CaCl2 x 2 H2O", "term": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "concentration": {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}}, "decision": {"query_label": "CaCl2 x 2 H2O", "identifier": "CHEBI:86158", "ontology_id": "CHEBI:86158", "mim_preferred_term": "CaCl2 x 2 H2O", "matched_label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:86158", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[3]", "ingredient": {"preferred_term": "FeCl3", "term": {"id": "CHEBI:30808", "label": "iron trichloride"}, "concentration": {"value": "0.2", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:30808", "label": "iron trichloride"}}, "decision": {"query_label": "FeCl3", "identifier": "CHEBI:30808", "ontology_id": "CHEBI:30808", "mim_preferred_term": "FeCl3", "matched_label": "FeCl3", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:30808", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[4]", "ingredient": {"preferred_term": "K2HPO4", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}}, "decision": {"query_label": "K2HPO4", "identifier": "CHEBI:131527", "ontology_id": "CHEBI:131527", "mim_preferred_term": "K2HPO4", "matched_label": "K2HPO4", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:131527", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[5]", "ingredient": {"preferred_term": "Casitone", "concentration": {"value": "2", "unit": "G_PER_L"}}, "decision": {"query_label": "Casitone", "identifier": "MICRO:0000606", "ontology_id": "MICRO:0000606", "mim_preferred_term": "Casitone", "matched_label": "Casitone", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": null, "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[6]", "ingredient": {"preferred_term": "Carboxymethyl cellulose", "term": {"id": "CHEBI:85146", "label": "carboxymethylcellulose"}, "concentration": {"value": "15", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:85146", "label": "carboxymethylcellulose"}}, "decision": {"query_label": "Carboxymethyl cellulose", "identifier": "CHEBI:234035", "ontology_id": "CHEBI:234035", "mim_preferred_term": "Carboxymethyl cellulose", "matched_label": "Carboxymethyl cellulose", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:85146", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[7]", "ingredient": {"preferred_term": "Agar", "term": {"id": "CHEBI:2509", "label": "agar"}, "concentration": {"value": "6", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"}}, "decision": {"query_label": "Agar", "identifier": "CHEBI:2509", "ontology_id": "CHEBI:2509", "mim_preferred_term": "Agar", "matched_label": "Agar", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:2509", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}]
The two hydrates are correct. CHEBI:85146 names generic CMC; CHEBI:234035 names its sodium salt. The source recommendation does not certify polymer degree, viscosity number, molar mass or substitution. Do not copy the API polymer mmol_l values or the candidate ontology mass into a conversion. Casitone is an undefined mixture; the MICRO resolver answer is a diagnostic observation, not a newly verified external ontology claim. Full source-grade text has no exact packaged-label answer, which does not imply that the material is absent.

### Current writer behavior, existing evidence and historical reviews

provenance: concern. Targets: CultureMech:003813.

The target lacks six evidence objects already in the DSM owner and preserves only the KOMODO history. Current conservative merger rejects this pair; current importer still drops ingredient attributes.

All six historical reports were read. The two detailed curation reports contain28 API recipe/step objects, all matching current source objects, and their recorded source hash matches fresh bytes. This authenticates content, not historical retrieval time. The September report recommendation to retain a two-record merge is not applicable to current conservative compatibility. Its generated-MIX claim does not describe the current target. The October KOMODO report repeats the phosphate object for every amount and calls all eight conflicts; phosphate preparation and recommended CMC form do not refute unrelated numeric g_l values. The DSM report defers phosphate and Casitone based on attributes; current direct source inspection now supports their numeric values while preserving their attributes. No standalone main-solution record is assessed or copied; the historical solution2232 water allegation is outside the selected record. Current resolver only fills empty KOMODO recipes and skips this populated owner. Stored.fZ and naive timestamp strings remain historical; current formatting code is not proof of exact historical execution.

## Findings

### F1: Source preparation and solvent context are incomplete

major / open / confirmed; issue key: cm003813-source-preparation-attributes.

Phosphate separate-autoclaving is absent from both owners and target;1000ml preparation water and the Casitone manufacturer are also omitted. Preserve the explicit source details without adding unstated final volume, time or temperature.

### F2: Generated record omits maintained source evidence

major / open / confirmed; issue key: cm003813-generated-evidence-preparation-staleness.

Six scoped concentration evidence objects and the material recommendation already exist in the DSM owner but are absent from the target. Current exact-formulation checks reject merging the pair because notes, preparation and ancestry differ. Reconcile maintained provenance and regenerate without forcing the old ingredient-only collapse.

### F3: CMC local and MIM identities diverge

major / open / confirmed; issue key: cm003813-cmc-generic-sodium-identity-divergence.

Local primary and secondary slots use genericCHEBI:85146, while the pinned MIM resolver returns sodium-saltCHEBI:234035 for the same preferred label. The source separately recommends sodium salt of high viscosity. Reconcile intended material scope and current publication identity; matching labels do not make these two identities equivalent, and no automatic primary-term replacement is justified.

### F4: Imported atmosphere and historical timestamps need qualification

minor / open / confirmed; issue key: cm003813-komodo-condition-history-provenance.

The KOMODO-derived Aerobic:No note has no counterpart in the inspected DSM recipe/API and current KOMODO sources are inaccessible. This is unresolved provenance, not proof that the medium is aerobic. Retain the historical malformed.fZ and timezone-free events, documenting their limitations through a future append-only event.

## Recommended Actions And Acceptance Checks

### A1

Preserve phosphate separate sterilization, source solvent input and Difco qualifier in the two maintained records and the MediaDive attribute path; retain the CMC material recommendation in a suitable source-scoped note rather than inferring a MIX instruction.

- Compare all nine exact source rows and the phosphate attribute to the updated maintained fields.
- All eight numeric g_l values stay unchanged unless a separately evidenced variant is introduced.
- Run just validate-schema,just validate-strict,just validate-terms and just validate-references for each edited owner.

### A2

Reconcile exact CMC material identity before updating the preferred term or either identifier. Preserve generic-versus-recommended-sodium scope; use the maintained resolver and explicit primary evidence. Any upstream MIM label correction requires its own reviewed change and subsequent pinned dependency refresh.

- Verify CHEBI:85146 andCHEBI:234035 definitions against the chosen source scope, retaining high-viscosity wording without inferred polymer parameters.
- Use culturemech.ingredients.mim_label_index and just check-mim-label-index to verify the resulting publication identity.
- Do not apply mixture/polymer molarity from provider metadata.

### A3

Retain existing six DSM claim snippets and append-only history, reconcile or keep separate the two owner assertions, and regenerate through the current conservative merge pipeline. Do not require a two-record collapse.

- Exact compatible inputs preserve all evidence; incompatible preparation/provenance remains separate.
- Run just verify-merges and just audit-merge-freshness after the separately authorized regeneration.
- Check generated source attribution, material note and evidence against the maintained owners; retain permanent IDs.

### A4

Verify the exact historical KOMODO atmosphere assertion when source access is available and add an honest provenance note; preserve prior events and avoid supplying an unsupported atmosphere.

- Capture an exact accessible source/version or explicitly retain the unresolved condition.
- Append any future curation history with actual timezone-aware UTC; do not rewrite the two old events.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml; entire target | supports | Entire generated target, all eight ingredient quantities, seven primary and seven secondary identifiers, ancestry and embedded history. |
| komodo-owner | data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml; entire owner | supports | Entire maintained KOMODO contributor; exact accession and parent reference, eight quantities, no preparation or claim evidence. |
| dsm-owner | data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml; entire owner | supports | Entire maintained DSM contributor; six already attached claim snippets, source-material recommendation, reciprocal child and append-only evidence event. |
| dsm1111 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1111.pdf; page1, full table and final material note | supports | Official DSMZ1111 one-page recipe, eight gram inputs,1000ml water, separate phosphate sterilization and a recommended CMC material. Copyright2008 is printed; no publication date is inferred. |
| api1111 | https://mediadive.dsmz.de/rest/medium/1111; $.data; entire response | supports | Entire exact DSMZ database response: one medium, one main solution2232, nine source rows, volume1000 and one material recommendation. All eight g_l values are explicitly provider-declared. |
| komodo-current | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1111; HTTP403; challenge document | unknown | The exact historical detail route returns403 challenge; identity, atmosphere and historical-version equivalence cannot be independently rechecked from this response. |
| komodo-list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; HTTP403; challenge document | unknown | Exact historical MediaList route also returns403; the old mapping row remains historical report context. |
| chebi-131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:131527: dipotassium hydrogen phosphate; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-234035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_234035; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:234035: carboxymethylcellulose sodium salt; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:2509: agar; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-30808 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30808; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:30808: iron trichloride; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:31795: magnesium sulfate heptahydrate; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:62946: ammonium sulfate; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-85146 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_85146; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:85146: carboxymethylcellulose; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| chebi-86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | Current nonobsolete CHEBI:86158: calcium chloride dihydrate; exact label, synonyms and supplied-form definition inspected. This authority does not establish a recipe concentration or polymer viscosity. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; entire file | context_only | Entire pinned index loaded and integrity-checked through maintained resolver. Generic CMC label selects sodium-saltCHEBI:234035; source-grade wording must be retained separately. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; entire file | context_only | Exact immutable index hash, source commit and contract. |
| mediadive-writer | src/culturemech/import/mediadive_importer.py; entire file | context_only | Read _parse_api_composition, _get_api_medium_data, _is_api_stock_addition, _parse_preparation_steps and _classify_preparation_action. Current main parser omits solvent and item.attribute; source material prose defaults to MIX. |
| komodo-writer | src/culturemech/import/komodo_web_importer.py; entire file | context_only | Read _convert_to_culturemech. Aerobic boolean becomes source notes; timestamp formatter includes %f. This does not prove historical execution. |
| composition-resolver | src/culturemech/enrich/dsmz_resolver.py; entire file | context_only | Entire resolver read. merge_composition copies ingredients/solutions and selected metadata but not preparation; resolve_recipe skips already populated owners; old DSMZ_* indexing is not a current curator. |
| merge-formulation | src/culturemech/merge/formulation.py; entire file | context_only | Entire conservative projection and evidence union read. Preparation, notes and ancestry must match; evidence union is allowed only for compatible scientific assertions. |
| merge-writer | src/culturemech/merge/merger.py; entire file | context_only | Read merge_group: current runtime delegates to conservative merge_formulation_evidence and rejects this exact pair. |
| schema | src/culturemech/schema/culturemech.yaml; entire file | context_only | Relevant MediaRecipe, IngredientDescriptor, ConcentrationValue and PreparationStep definitions read; no new scientific fields proposed. |
| recipes | justfile; entire file | context_only | Record validation routes and standalone HistoryRecord validation reviewed; embedded history is assessed manually. |
| project-recipes | project.justfile; entire file | context_only | Maintained MIM dependency and merge regeneration/check entrypoints reviewed. |
| history-report-1 | reports/yaml_record_review/20260922T041539Z-CARBOXYMETHYL_CELLULOSE_MEDIUM.md; entire file | context_only | Full historical prose/table read. Reports are leads, not independent source authority. Current source joins distinguish their observations from current records. |
| history-report-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/carboxymethyl_cellulose_medium.yaml.md; entire file | context_only | Full historical prose/table read. Reports are leads, not independent source authority. Current source joins distinguish their observations from current records. |
| history-report-3 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml.md; entire file | context_only | Full historical prose/table read. Reports are leads, not independent source authority. Current source joins distinguish their observations from current records. |
| history-report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.md; entire file | context_only | Full historical prose/table read. Reports are leads, not independent source authority. Current source joins distinguish their observations from current records. |
| history-report-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.md; entire file | context_only | Full historical prose/table read. Reports are leads, not independent source authority. Current source joins distinguish their observations from current records. |
| history-report-6 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.md; entire file | context_only | Full historical prose/table read. Reports are leads, not independent source authority. Current source joins distinguish their observations from current records. |
| inspection | REVIEW_WORK/batch059/record10/inspection-addendum-dsmz-resolver/inspect.json; entire file | context_only | Native addendum contains all42 original inputs unchanged plus actual resolver implementation; exact target/owners unchanged. |
| inspection-delta | REVIEW_WORK/batch059/record10/inspection-addendum-dsmz-resolver/delta.json; entire file | context_only | One added context file,43 inputs; canonical target checks remain applicable. |
| diagnostics | REVIEW_WORK/batch059/record10/diagnostics.json; entire file | context_only | Eight maintained resolver decisions, eight OLS objects including candidate, six existing literal claims,28 historical source-object joins, exact owner fingerprints and in-memory writer previews. |
| ownership-search | REVIEW_WORK/batch059/record10/diagnostics.json; ownership_search.argv/stdout | context_only | Ignored/hidden-inclusive exact ID and source-slug search; existing local absence claims are confined to full inspected target and owners. |
| validate-schema | REVIEW_WORK/batch059/record10/validate-schema-result.json; entire result | supports | Complete original stdout/stderr and actual timing retained. |
| validate-strict | REVIEW_WORK/batch059/record10/validate-strict-result.json; entire result | supports | Complete original stdout/stderr and actual timing retained. |
| validate-terms | REVIEW_WORK/batch059/record10/validate-terms-result.json; entire result | supports | Complete original stdout/stderr and actual timing retained. |
| validate-references | REVIEW_WORK/batch059/record10/validate-references-result.json; entire result | supports | Complete original stdout/stderr and actual timing retained. |
| check-mim-label-index | REVIEW_WORK/batch059/record10/check-mim-label-index-result.json; entire result | supports | Complete original stdout/stderr and actual timing retained. |
| quantity-inventory | REVIEW_WORK/batch059/record10/quantity-inventory.json; entire file | context_only | Nine decisions cover all24 concentration fields across the target and two owners, plus the omitted source solvent; all nine API recipe rows are accounted for. |

## Limits And Additional Notes

- Current exact KOMODO detail and mapping routes return403; its atmosphere and historical-version equivalence remain unresolved, so this review is partial.
- Provider g_l values are supported as declared. Primary water input is not evidence of measured final volume; no stock, density, polymer mass, substitution, molarity or incubation condition is inferred.
- All seven asserted CHEBI IDs and the sodium-salt candidate were checked. Casitone MICRO resolver output is diagnostic only; it is not a new external grounding proposal.
- Four canonical checks apply to the selected generated record. Owners/context were read; the extra pinned-MIM check passed. No corpus ID/product/merge gates, scientific records or experiments were run or changed.
- Historical source objects and six literal claims match fresh bytes; old access times and original KOMODO HTML-capture provenance are not independently authenticated.
- No prior structured finding is closed; the six ad hoc historical reports remain contextual observations.
- The immutable original native inspection remains preserved. A single additive context inspection includes the actual composition resolver with all prior42 input hashes unchanged.
- All numeric quantities, source attributes, existing evidence and current importer safeguards were assessed separately; deterministic validation is not scientific approval.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T065902Z-carboxymethyl-cellulose-medium-batch059
kind: record
repository: CultureBotAI/CultureMech
title: 'Carboxymethyl cellulose medium: source preparation, evidence and material
  identity'
started_at: '2026-10-28T06:47:42.108335Z'
finished_at: '2026-10-28T06:59:02.701602Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the scientific records; source-grounded
    review without experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: DSM1111 amounts and six existing source claims are supported. Three major
  findings concern missing preparation, generated evidence loss and generic/sodium
  CMC identity divergence; one minor finding concerns KOMODO provenance. Exact current
  KOMODO sources remain inaccessible.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
    sha256: 6a863e8e4cd3ecb8107cee0f0dc7bb22badd5cba7dbed4c5eb749687ea26243e
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    sha256: fdc1e92caf8b36f3d1ffd83151f0a1a4976e488fe446d0fe893ff07130435145
    role: context
  - path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    sha256: 1db00413f19a52543d6a16bf61c274a00896028a38e8307b494a99039f9574f4
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
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/carboxymethyl_cellulose_medium.yaml.md
    sha256: 50f5c84051990a4bccff9fb38fd54543e8ab0065168f93c76bdc46a22ef86d52
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml.md
    sha256: ae088bc03950eb7cec3d0b73cc2ff92817def16d0b025873259cb9dbe1928b3b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.md
    sha256: 7946bd3b51a95c2b2aefc22c3f7a0d170db8158635c17399730ea3529de1c7ce
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.md
    sha256: b05102bf6b0c3785384788b0a16ecfcc902497189f32a998f0e5f81976da583f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.md
    sha256: e5365f6b6fc1fea50d0e1344075b9667f086e1b027e187e55cc3e1b02168ca5a
    role: context
  - path: reports/yaml_record_review/20260922T041539Z-CARBOXYMETHYL_CELLULOSE_MEDIUM.md
    sha256: 383f6d044feeb459fb574ca2a858b07d0cab4906ee45535e181709ca0685e22b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
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
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
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
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One entire generated record and both maintained contributors:24 local
    concentration fields, nine source recipe rows, exact chemical IDs, preparation,
    reciprocal references, history and current writers.
  selection: Batch059 item10 from Python-sorted uncovered paths in successful native
    lists;513 of6325 corpus paths covered at selection.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003813
  exclusions:
  - target: Other records, standalone solution2232 and organism-specific growth
    reason: Not referenced as a stock dependency by this selected record; historical
      leads do not expand target scope or support new growth assertions.
targets:
- target_id: CultureMech:003813
  path: data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
  label: carboxymethyl_cellulose_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
    --workers 1 --out REVIEW_WORK/batch059/record10/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch059/record10/strict.tsv"
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - validate-references
- check_id: check-mim-label-index
  name: check-mim-label-index
  command: just check-mim-label-index
  exit_code: 0
  required: true
  status: passed
  summary: 'MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9

    Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350


    uv run python scripts/check_mim_label_index.py'
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - check-mim-label-index
- check_id: embedded-history
  name: Manual embedded history and registry assessment
  required: false
  status: passed
  summary: Entire target and both owners read, including malformed historical KOMODO
    timestamp and later evidence event; exact registry routes checked. Standalone
    HistoryRecord validator is not an embedded-history checker.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - diagnostics
  - recipes
- check_id: komodo-live-source
  name: Current KOMODO detail and mapping source access
  required: true
  status: unavailable
  summary: Both exact source routes return403. Historical identity context remains
    explicit and this review is partial.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - komodo-current
  - komodo-list
- check_id: corpus-gates
  name: Full-corpus ID, product and merge gates
  required: false
  status: skipped
  summary: No corpus, schema, ID or generator was changed. Full-corpus assign-ids-check,validate-products,verify-merges
    and audit-merge-freshness were not run; no narrower substitute is claimed.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - project-recipes
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml
  locator: entire target
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Entire generated target, all eight ingredient quantities, seven primary
    and seven secondary identifiers, ancestry and embedded history.
  snapshot_sha256: 6a863e8e4cd3ecb8107cee0f0dc7bb22badd5cba7dbed4c5eb749687ea26243e
- evidence_id: komodo-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
  locator: entire owner
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Entire maintained KOMODO contributor; exact accession and parent reference,
    eight quantities, no preparation or claim evidence.
  snapshot_sha256: fdc1e92caf8b36f3d1ffd83151f0a1a4976e488fe446d0fe893ff07130435145
- evidence_id: dsm-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
  locator: entire owner
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Entire maintained DSM contributor; six already attached claim snippets,
    source-material recommendation, reciprocal child and append-only evidence event.
  snapshot_sha256: 1db00413f19a52543d6a16bf61c274a00896028a38e8307b494a99039f9574f4
- evidence_id: dsm1111
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1111.pdf
  locator: page1, full table and final material note
  accessed_at: '2026-10-28T06:48:05.461783Z'
  support: supports
  summary: Official DSMZ1111 one-page recipe, eight gram inputs,1000ml water, separate
    phosphate sterilization and a recommended CMC material. Copyright2008 is printed;
    no publication date is inferred.
  snapshot_sha256: 1cbd19aed4052d635cbb21a3304704365670e624cd277d0ebdaf80e26c26dadf
  quote: K2HPO4 (autoclaved separately)
- evidence_id: api1111
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1111
  locator: $.data; entire response
  accessed_at: '2026-10-28T06:48:05.116329Z'
  support: supports
  summary: 'Entire exact DSMZ database response: one medium, one main solution2232,
    nine source rows, volume1000 and one material recommendation. All eight g_l values
    are explicitly provider-declared.'
  snapshot_sha256: bc67e453fee21b5e0fb4a4f659ebd2b78be5d112d72c50af3bc9bdb6dcd388a8
- evidence_id: komodo-current
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1111
  locator: HTTP403; challenge document
  accessed_at: '2026-10-28T06:49:44.212302Z'
  support: unknown
  summary: The exact historical detail route returns403 challenge; identity, atmosphere
    and historical-version equivalence cannot be independently rechecked from this
    response.
  snapshot_sha256: b203769ceb120dd5aeec946627d1572e29b44655995d3e1c4dd85f6a6b2cb7e0
- evidence_id: komodo-list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: HTTP403; challenge document
  accessed_at: '2026-10-28T06:49:44.156830Z'
  support: unknown
  summary: Exact historical MediaList route also returns403; the old mapping row remains
    historical report context.
  snapshot_sha256: 5598531d15d586ec373383a6009f06e2e898ce6d06b84038ca3faf3328b47607
- evidence_id: chebi-131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.209917Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:131527: dipotassium hydrogen phosphate; exact
    label, synonyms and supplied-form definition inspected. This authority does not
    establish a recipe concentration or polymer viscosity.'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi-234035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_234035
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:49:44.834936Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:234035: carboxymethylcellulose sodium salt;
    exact label, synonyms and supplied-form definition inspected. This authority does
    not establish a recipe concentration or polymer viscosity.'
  snapshot_sha256: 5e2e2161547b3861c6695f6e1593d32f362c6ea16b6320cbb7d7ddec52d7991f
- evidence_id: chebi-2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.190105Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:2509: agar; exact label, synonyms and supplied-form
    definition inspected. This authority does not establish a recipe concentration
    or polymer viscosity.'
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi-30808
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30808
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.197322Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:30808: iron trichloride; exact label, synonyms
    and supplied-form definition inspected. This authority does not establish a recipe
    concentration or polymer viscosity.'
  snapshot_sha256: 3053606ef0cc9275ce2a4d374db1f6d2f61ceb59c93b3c69c5e0c437c121060c
- evidence_id: chebi-31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.231554Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:31795: magnesium sulfate heptahydrate; exact
    label, synonyms and supplied-form definition inspected. This authority does not
    establish a recipe concentration or polymer viscosity.'
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi-62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.721496Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:62946: ammonium sulfate; exact label, synonyms
    and supplied-form definition inspected. This authority does not establish a recipe
    concentration or polymer viscosity.'
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi-85146
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_85146
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.781812Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:85146: carboxymethylcellulose; exact label,
    synonyms and supplied-form definition inspected. This authority does not establish
    a recipe concentration or polymer viscosity.'
  snapshot_sha256: 6de00321284c118e5008f497bf181cb82a948ac88cf16af35e2270f7273e28f1
- evidence_id: chebi-86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T06:48:05.798300Z'
  support: supports
  summary: 'Current nonobsolete CHEBI:86158: calcium chloride dihydrate; exact label,
    synonyms and supplied-form definition inspected. This authority does not establish
    a recipe concentration or polymer viscosity.'
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: mim-index
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Entire pinned index loaded and integrity-checked through maintained resolver.
    Generic CMC label selects sodium-saltCHEBI:234035; source-grade wording must be
    retained separately.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-metadata
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Exact immutable index hash, source commit and contract.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: mediadive-writer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Read _parse_api_composition, _get_api_medium_data, _is_api_stock_addition,
    _parse_preparation_steps and _classify_preparation_action. Current main parser
    omits solvent and item.attribute; source material prose defaults to MIX.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: komodo-writer
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Read _convert_to_culturemech. Aerobic boolean becomes source notes; timestamp
    formatter includes %f. This does not prove historical execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: composition-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Entire resolver read. merge_composition copies ingredients/solutions and
    selected metadata but not preparation; resolve_recipe skips already populated
    owners; old DSMZ_* indexing is not a current curator.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: merge-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Entire conservative projection and evidence union read. Preparation, notes
    and ancestry must match; evidence union is allowed only for compatible scientific
    assertions.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: merge-writer
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: 'Read merge_group: current runtime delegates to conservative merge_formulation_evidence
    and rejects this exact pair.'
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: schema
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Relevant MediaRecipe, IngredientDescriptor, ConcentrationValue and PreparationStep
    definitions read; no new scientific fields proposed.
  snapshot_sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
- evidence_id: recipes
  kind: record_content
  reference: justfile
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Record validation routes and standalone HistoryRecord validation reviewed;
    embedded history is assessed manually.
  snapshot_sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
- evidence_id: project-recipes
  kind: record_content
  reference: project.justfile
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Maintained MIM dependency and merge regeneration/check entrypoints reviewed.
  snapshot_sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
- evidence_id: history-report-1
  kind: prior_review
  reference: reports/yaml_record_review/20260922T041539Z-CARBOXYMETHYL_CELLULOSE_MEDIUM.md
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Full historical prose/table read. Reports are leads, not independent source
    authority. Current source joins distinguish their observations from current records.
  snapshot_sha256: 383f6d044feeb459fb574ca2a858b07d0cab4906ee45535e181709ca0685e22b
- evidence_id: history-report-2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/carboxymethyl_cellulose_medium.yaml.md
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Full historical prose/table read. Reports are leads, not independent source
    authority. Current source joins distinguish their observations from current records.
  snapshot_sha256: 50f5c84051990a4bccff9fb38fd54543e8ab0065168f93c76bdc46a22ef86d52
- evidence_id: history-report-3
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml.md
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Full historical prose/table read. Reports are leads, not independent source
    authority. Current source joins distinguish their observations from current records.
  snapshot_sha256: ae088bc03950eb7cec3d0b73cc2ff92817def16d0b025873259cb9dbe1928b3b
- evidence_id: history-report-4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.md
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Full historical prose/table read. Reports are leads, not independent source
    authority. Current source joins distinguish their observations from current records.
  snapshot_sha256: e5365f6b6fc1fea50d0e1344075b9667f086e1b027e187e55cc3e1b02168ca5a
- evidence_id: history-report-5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.md
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Full historical prose/table read. Reports are leads, not independent source
    authority. Current source joins distinguish their observations from current records.
  snapshot_sha256: b05102bf6b0c3785384788b0a16ecfcc902497189f32a998f0e5f81976da583f
- evidence_id: history-report-6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.md
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Full historical prose/table read. Reports are leads, not independent source
    authority. Current source joins distinguish their observations from current records.
  snapshot_sha256: 7946bd3b51a95c2b2aefc22c3f7a0d170db8158635c17399730ea3529de1c7ce
- evidence_id: inspection
  kind: validation
  reference: REVIEW_WORK/batch059/record10/inspection-addendum-dsmz-resolver/inspect.json
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Native addendum contains all42 original inputs unchanged plus actual resolver
    implementation; exact target/owners unchanged.
  snapshot_sha256: acf0efbc394db4ead1ed6d753b70397b010f3595326e23e415d4c149c93e2b70
- evidence_id: inspection-delta
  kind: validation
  reference: REVIEW_WORK/batch059/record10/inspection-addendum-dsmz-resolver/delta.json
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: One added context file,43 inputs; canonical target checks remain applicable.
  snapshot_sha256: 11b1ce5192de02ea02a1b7b92e437fd1ca4cbc671046eeda5f87acaec82d518e
- evidence_id: diagnostics
  kind: validation
  reference: REVIEW_WORK/batch059/record10/diagnostics.json
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Eight maintained resolver decisions, eight OLS objects including candidate,
    six existing literal claims,28 historical source-object joins, exact owner fingerprints
    and in-memory writer previews.
  snapshot_sha256: db4d57a5f695a3c6f56aba76356fd19e9c1ede04ad0be7440e21ceb5c634e29b
- evidence_id: ownership-search
  kind: search
  reference: REVIEW_WORK/batch059/record10/diagnostics.json
  locator: ownership_search.argv/stdout
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Ignored/hidden-inclusive exact ID and source-slug search; existing local
    absence claims are confined to full inspected target and owners.
  snapshot_sha256: db4d57a5f695a3c6f56aba76356fd19e9c1ede04ad0be7440e21ceb5c634e29b
  search_scope: rg --no-ignore --hidden -n -l across data/normalized_yaml and reports
    for two exact IDs and both owner slugs; all matched paths retained in diagnostics.
    Unread global index/queue hits are not assessed.
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record10/validate-schema-result.json
  locator: entire result
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Complete original stdout/stderr and actual timing retained.
  snapshot_sha256: 8d1e3b9c444e5e2aeb513cfd51e86d6d1b64e658b3461e5105d42dd7fa05cba1
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record10/validate-strict-result.json
  locator: entire result
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Complete original stdout/stderr and actual timing retained.
  snapshot_sha256: 25bf67219cd3513c27fdb6a9ae668d8493edfb9effff9669c32a6b002c62f6d2
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record10/validate-terms-result.json
  locator: entire result
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Complete original stdout/stderr and actual timing retained.
  snapshot_sha256: 27c6df50adc0d0c90f1d4f03be719c509d8f3c6166c1be47a37eaec4376901e5
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch059/record10/validate-references-result.json
  locator: entire result
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Complete original stdout/stderr and actual timing retained.
  snapshot_sha256: ff3a4d627864b9c05eb04d848922f0a97ece569a1060609d17382dbeccf47ddb
- evidence_id: check-mim-label-index
  kind: validation
  reference: REVIEW_WORK/batch059/record10/check-mim-label-index-result.json
  locator: entire result
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: supports
  summary: Complete original stdout/stderr and actual timing retained.
  snapshot_sha256: f7ce9ff290b0d216fa6f094387a9109a1ab787ba57ec3aba40a25798b455038f
- evidence_id: quantity-inventory
  kind: validation
  reference: REVIEW_WORK/batch059/record10/quantity-inventory.json
  locator: entire file
  accessed_at: '2026-10-28T06:59:02.696587Z'
  support: context_only
  summary: Nine decisions cover all24 concentration fields across the target and two
    owners, plus the omitted source solvent; all nine API recipe rows are accounted
    for.
  snapshot_sha256: 215cdf72dfc2c7e4a9393c0736a047a52f4722e52869fc86b5bfe531b8671be6
assessments:
- assessment_id: identity
  area: identity
  topic: DSM1111 provenance and source-duplicate boundary
  outcome: concern
  summary: The exact DSM1111 primary and database support the intended medium; stable
    IDs and reciprocal maintained references resolve. Current KOMODO access and its
    atmosphere metadata remain unresolved.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - dsm1111
  - api1111
  - komodo-current
  - komodo-list
  - diagnostics
  details: Solid agar and complex/undefined composition are supported by agar and
    Casitone. No organism or growth claim is inferred. The same ingredient set does
    not prove identical preparation or historical source conditions; current notes,
    preparation and ancestry differ. iModulonDB is not applicable to this source-defined
    formulation without a gene, dataset or computational-module assertion.
- assessment_id: quantities
  area: quantity
  topic: Every local concentration and source-only solvent
  outcome: supported
  summary: All eight selected values agree with explicit database g_l; six existing
    DSM-owner evidence objects authenticate literally against identical fresh bytes.
    Missing evidence and preparation do not justify changing supported numeric values.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - dsm1111
  - api1111
  - quantity-inventory
  - diagnostics
  details: "[\n  {\n    \"decision_id\": \"q01\",\n    \"ingredient\": \"(NH4)2SO4\"\
    ,\n    \"local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[0].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[0].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[0].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"verified\",\n        \"proposed_value\": 1,\n        \"\
    proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n      }\n \
    \   ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\",\n \
    \   \"locator\": \"$.data.solutions[0].recipe[0]\",\n    \"source_snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 1,\\n                      \
    \  \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\
    \": 27,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"mmol_l\\\": 7.56773,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n    \"source_amount\": 1,\n    \"source_unit\"\
    : \"g\",\n    \"provider_g_l\": 1,\n    \"provider_volume_ml\": 1000,\n    \"\
    basis\": \"Explicit database normalization for main solution1111, with primary\
    \ batch amount independently compared.\",\n    \"calculation\": \"1 g / (1000\
    \ mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference\
    \ from water alone.\",\n    \"decision_notes\": \"Provider-declared main concentration\
    \ agrees with the local value. Primary gives batch mass and water input, not a\
    \ measured final-volume statement; no independent final-volume claim is added.\"\
    \n  },\n  {\n    \"decision_id\": \"q02\",\n    \"ingredient\": \"MgSO4 x 7 H2O\"\
    ,\n    \"local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[1].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[1].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[1].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"verified\",\n        \"proposed_value\": 1,\n        \"\
    proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n      }\n \
    \   ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\",\n \
    \   \"locator\": \"$.data.solutions[0].recipe[1]\",\n    \"source_snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 4.05719,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n    \"source_amount\": 1,\n    \"source_unit\"\
    : \"g\",\n    \"provider_g_l\": 1,\n    \"provider_volume_ml\": 1000,\n    \"\
    basis\": \"Explicit database normalization for main solution1111, with primary\
    \ batch amount independently compared.\",\n    \"calculation\": \"1 g / (1000\
    \ mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference\
    \ from water alone.\",\n    \"decision_notes\": \"Provider-declared main concentration\
    \ agrees with the local value. Primary gives batch mass and water input, not a\
    \ measured final-volume statement; no independent final-volume claim is added.\"\
    \n  },\n  {\n    \"decision_id\": \"q03\",\n    \"ingredient\": \"CaCl2 x 2 H2O\"\
    ,\n    \"local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[2].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[2].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[2].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"verified\",\n        \"proposed_value\": 1,\n        \"\
    proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n      }\n \
    \   ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\",\n \
    \   \"locator\": \"$.data.solutions[0].recipe[2]\",\n    \"source_snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 1,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n      \
    \                  \\\"mmol_l\\\": 6.80203,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n    \"source_amount\": 1,\n    \"source_unit\"\
    : \"g\",\n    \"provider_g_l\": 1,\n    \"provider_volume_ml\": 1000,\n    \"\
    basis\": \"Explicit database normalization for main solution1111, with primary\
    \ batch amount independently compared.\",\n    \"calculation\": \"1 g / (1000\
    \ mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference\
    \ from water alone.\",\n    \"decision_notes\": \"Provider-declared main concentration\
    \ agrees with the local value. Primary gives batch mass and water input, not a\
    \ measured final-volume statement; no independent final-volume claim is added.\"\
    \n  },\n  {\n    \"decision_id\": \"q04\",\n    \"ingredient\": \"FeCl3\",\n \
    \   \"local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[3].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 0.2,\n  \
    \      \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n \
    \     },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[3].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 0.2,\n  \
    \      \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n \
    \     },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[3].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"verified\",\n        \"proposed_value\": 0.2,\n       \
    \ \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n      }\n\
    \    ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\",\n\
    \    \"locator\": \"$.data.solutions[0].recipe[3]\",\n    \"source_snippet\":\
    \ \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"FeCl3\\\",\\n                        \\\"compound_id\\\
    \": 403,\\n                        \\\"amount\\\": 0.2,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 1.23305,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n    \"source_amount\": 0.2,\n  \
    \  \"source_unit\": \"g\",\n    \"provider_g_l\": 0.2,\n    \"provider_volume_ml\"\
    : 1000,\n    \"basis\": \"Explicit database normalization for main solution1111,\
    \ with primary batch amount independently compared.\",\n    \"calculation\": \"\
    0.2 g / (1000 mL / 1000 mL per L) = 0.2 g/L reproduces the provider declaration;\
    \ not an inference from water alone.\",\n    \"decision_notes\": \"Provider-declared\
    \ main concentration agrees with the local value. Primary gives batch mass and\
    \ water input, not a measured final-volume statement; no independent final-volume\
    \ claim is added.\"\n  },\n  {\n    \"decision_id\": \"q05\",\n    \"ingredient\"\
    : \"K2HPO4\",\n    \"local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[4].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[4].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[4].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 1,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   }\n    ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\"\
    ,\n    \"locator\": \"$.data.solutions[0].recipe[4]\",\n    \"source_snippet\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"attribute\\\": \\\"autoclaved separately\\\
    \",\\n                        \\\"amount\\\": 1,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n            \
    \            \\\"mmol_l\\\": 5.74132,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n    \"source_amount\": 1,\n    \"source_unit\"\
    : \"g\",\n    \"provider_g_l\": 1,\n    \"provider_volume_ml\": 1000,\n    \"\
    basis\": \"Explicit database normalization for main solution1111, with primary\
    \ batch amount independently compared.\",\n    \"calculation\": \"1 g / (1000\
    \ mL / 1000 mL per L) = 1 g/L reproduces the provider declaration; not an inference\
    \ from water alone.\",\n    \"decision_notes\": \"Provider-declared main concentration\
    \ agrees with the local value. Primary gives batch mass and water input, not a\
    \ measured final-volume statement; no independent final-volume claim is added.\
    \ The phosphate-specific separate-autoclaving instruction is essential context,\
    \ not a different amount or unspecified stock strength.\"\n  },\n  {\n    \"decision_id\"\
    : \"q06\",\n    \"ingredient\": \"Casitone\",\n    \"local_claims\": [\n     \
    \ {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[5].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 2,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[5].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 2,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[5].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 2,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   }\n    ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\"\
    ,\n    \"locator\": \"$.data.solutions[0].recipe[5]\",\n    \"source_snippet\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"Casitone\\\",\\n                        \\\"compound_id\\\
    \": 84,\\n                        \\\"attribute\\\": \\\"Difco\\\",\\n       \
    \                 \\\"amount\\\": 2,\\n                        \\\"unit\\\": \\\
    \"g\\\",\\n                        \\\"g_l\\\": 2,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n    \"source_amount\": 2,\n    \"\
    source_unit\": \"g\",\n    \"provider_g_l\": 2,\n    \"provider_volume_ml\": 1000,\n\
    \    \"basis\": \"Explicit database normalization for main solution1111, with\
    \ primary batch amount independently compared.\",\n    \"calculation\": \"2 g\
    \ / (1000 mL / 1000 mL per L) = 2 g/L reproduces the provider declaration; not\
    \ an inference from water alone.\",\n    \"decision_notes\": \"Provider-declared\
    \ main concentration agrees with the local value. Primary gives batch mass and\
    \ water input, not a measured final-volume statement; no independent final-volume\
    \ claim is added. Difco identifies the supplied Casitone product; this attribute\
    \ does not by itself make the explicitly stated amount unknown.\"\n  },\n  {\n\
    \    \"decision_id\": \"q07\",\n    \"ingredient\": \"Carboxymethyl cellulose\"\
    ,\n    \"local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[6].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 15,\n   \
    \     \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n  \
    \    },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[6].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 15,\n   \
    \     \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n  \
    \    },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[6].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"verified\",\n        \"proposed_value\": 15,\n        \"\
    proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n      }\n \
    \   ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\",\n \
    \   \"locator\": \"$.data.solutions[0].recipe[6]\",\n    \"source_snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 7,\\n                      \
    \  \\\"compound\\\": \\\"Carboxymethyl cellulose\\\",\\n                     \
    \   \\\"compound_id\\\": 989,\\n                        \\\"amount\\\": 15,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 15,\\n                        \\\"mmol_l\\\": 62.4454,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n    \"source_amount\"\
    : 15,\n    \"source_unit\": \"g\",\n    \"provider_g_l\": 15,\n    \"provider_volume_ml\"\
    : 1000,\n    \"basis\": \"Explicit database normalization for main solution1111,\
    \ with primary batch amount independently compared.\",\n    \"calculation\": \"\
    15 g / (1000 mL / 1000 mL per L) = 15 g/L reproduces the provider declaration;\
    \ not an inference from water alone.\",\n    \"decision_notes\": \"Provider-declared\
    \ main concentration agrees with the local value. Primary gives batch mass and\
    \ water input, not a measured final-volume statement; no independent final-volume\
    \ claim is added. The primary table names generic CMC and separately recommends\
    \ sodium salt of high viscosity. Its15g input is supported; chemical-form/grade\
    \ reconciliation is a separate finding. No polymer molarity is endorsed.\"\n \
    \ },\n  {\n    \"decision_id\": \"q08\",\n    \"ingredient\": \"Agar\",\n    \"\
    local_claims\": [\n      {\n        \"path\": \"data/merge_yaml/merged/CARBOXYMETHYL_CELLULOSE_MEDIUM.yaml\"\
    ,\n        \"field\": \"ingredients[7].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 6,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml\"\
    ,\n        \"field\": \"ingredients[7].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"evidence_only\",\n        \"proposed_value\": 6,\n    \
    \    \"proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n   \
    \   },\n      {\n        \"path\": \"data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml\"\
    ,\n        \"field\": \"ingredients[7].concentration\",\n        \"existing\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"status\": \"verified\",\n        \"proposed_value\": 6,\n        \"\
    proposed_unit\": \"G_PER_L\",\n        \"action_taken\": \"none\"\n      }\n \
    \   ],\n    \"reference\": \"https://mediadive.dsmz.de/rest/medium/1111\",\n \
    \   \"locator\": \"$.data.solutions[0].recipe[7]\",\n    \"source_snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 8,\\n                      \
    \  \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"amount\\\": 6,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 6,\\n      \
    \                  \\\"mmol_l\\\": 17.8396,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n    \"source_amount\": 6,\n    \"source_unit\"\
    : \"g\",\n    \"provider_g_l\": 6,\n    \"provider_volume_ml\": 1000,\n    \"\
    basis\": \"Explicit database normalization for main solution1111, with primary\
    \ batch amount independently compared.\",\n    \"calculation\": \"6 g / (1000\
    \ mL / 1000 mL per L) = 6 g/L reproduces the provider declaration; not an inference\
    \ from water alone.\",\n    \"decision_notes\": \"Provider-declared main concentration\
    \ agrees with the local value. Primary gives batch mass and water input, not a\
    \ measured final-volume statement; no independent final-volume claim is added.\"\
    \n  },\n  {\n    \"decision_id\": \"q09\",\n    \"ingredient\": \"Distilled water\"\
    ,\n    \"local_claims\": [],\n    \"status\": \"add\",\n    \"reference\": \"\
    https://mediadive.dsmz.de/rest/medium/1111\",\n    \"locator\": \"$.data.solutions[0].recipe[8]\"\
    ,\n    \"source_snippet\": \"{\\n                        \\\"recipe_order\\\"\
    : 9,\\n                        \\\"compound\\\": \\\"Distilled water\\\",\\n \
    \                       \\\"compound_id\\\": 4,\\n                        \\\"\
    amount\\\": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n    \"source_amount\"\
    : 1000,\n    \"source_unit\": \"ml\",\n    \"proposed_representation\": \"Preserve1000ml\
    \ solvent input in source-scoped preparation/evidence; no water mass, percentage\
    \ or final-volume concentration asserted.\",\n    \"decision_notes\": \"Absent\
    \ from target and both owners. Preserve as preparation solvent rather than assuming\
    \ water alone defines final volume.\",\n    \"action_taken\": \"none\"\n  }\n]"
- assessment_id: preparation
  area: completeness
  topic: Separate sterilization, source material and solvent context
  outcome: concern
  summary: Both owners omit phosphate separate-autoclaving and explicit preparation
    water; the generated target also omits the DSM-owner material recommendation.
    Neither source states pH, incubation, sterilization duration or temperature.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - dsm1111
  - api1111
  - mediadive-writer
  details: Preserve the Casitone manufacturer qualifier. The CMC sodium-salt/high-viscosity
    sentence is a recommended material, not an imperative mixing instruction or evidence
    that every generic CMC formulation requires that exact product. The existing DSM-owner
    MIX label derives from classifier fallback. No new pH, atmosphere, incubation,
    vessel, growth or sterilization parameters are supplied.
- assessment_id: grounding
  area: grounding
  topic: Chemical form and MIM publication identity
  outcome: concern
  summary: All seven asserted CHEBI IDs resolve with matching current labels; six
    of seven existing secondary IDs agree with the maintained MIM resolver. Generic
    CMC differs from the sodium-salt identity returned for that label.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - target
  - dsm1111
  - api1111
  - mim-index
  - mim-metadata
  - diagnostics
  - chebi-131527
  - chebi-234035
  - chebi-2509
  - chebi-30808
  - chebi-31795
  - chebi-62946
  - chebi-85146
  - chebi-86158
  details: '[{"field": "ingredients[0]", "ingredient": {"preferred_term": "(NH4)2SO4",
    "term": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value":
    "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:62946",
    "label": "ammonium sulfate"}}, "decision": {"query_label": "(NH4)2SO4", "identifier":
    "CHEBI:62946", "ontology_id": "CHEBI:62946", "mim_preferred_term": "(NH4)2SO4",
    "matched_label": "(NH4)2SO4", "match_type": "preferred_term", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:62946", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[1]", "ingredient": {"preferred_term": "MgSO4
    x 7 H2O", "term": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"},
    "concentration": {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term":
    {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}}, "decision":
    {"query_label": "MgSO4 x 7 H2O", "identifier": "CHEBI:31795", "ontology_id": "CHEBI:31795",
    "mim_preferred_term": "MgSO4 x 7 H2O", "matched_label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:31795", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[2]", "ingredient":
    {"preferred_term": "CaCl2 x 2 H2O", "term": {"id": "CHEBI:86158", "label": "calcium
    chloride dihydrate"}, "concentration": {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term":
    {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}}, "decision": {"query_label":
    "CaCl2 x 2 H2O", "identifier": "CHEBI:86158", "ontology_id": "CHEBI:86158", "mim_preferred_term":
    "CaCl2 x 2 H2O", "matched_label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact",
    "local_identifier": "CHEBI:86158", "source_compound_id": null, "reason": "trusted
    MIM label-index answer"}}, {"field": "ingredients[3]", "ingredient": {"preferred_term":
    "FeCl3", "term": {"id": "CHEBI:30808", "label": "iron trichloride"}, "concentration":
    {"value": "0.2", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id":
    "CHEBI:30808", "label": "iron trichloride"}}, "decision": {"query_label": "FeCl3",
    "identifier": "CHEBI:30808", "ontology_id": "CHEBI:30808", "mim_preferred_term":
    "FeCl3", "matched_label": "FeCl3", "match_type": "preferred_term", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:30808", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[4]", "ingredient": {"preferred_term": "K2HPO4",
    "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration":
    {"value": "1", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:131527",
    "label": "dipotassium hydrogen phosphate"}}, "decision": {"query_label": "K2HPO4",
    "identifier": "CHEBI:131527", "ontology_id": "CHEBI:131527", "mim_preferred_term":
    "K2HPO4", "matched_label": "K2HPO4", "match_type": "preferred_term", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:131527", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[5]", "ingredient": {"preferred_term": "Casitone",
    "concentration": {"value": "2", "unit": "G_PER_L"}}, "decision": {"query_label":
    "Casitone", "identifier": "MICRO:0000606", "ontology_id": "MICRO:0000606", "mim_preferred_term":
    "Casitone", "matched_label": "Casitone", "match_type": "preferred_term", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    null, "source_compound_id": null, "reason": "trusted MIM label-index answer"}},
    {"field": "ingredients[6]", "ingredient": {"preferred_term": "Carboxymethyl cellulose",
    "term": {"id": "CHEBI:85146", "label": "carboxymethylcellulose"}, "concentration":
    {"value": "15", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:85146",
    "label": "carboxymethylcellulose"}}, "decision": {"query_label": "Carboxymethyl
    cellulose", "identifier": "CHEBI:234035", "ontology_id": "CHEBI:234035", "mim_preferred_term":
    "Carboxymethyl cellulose", "matched_label": "Carboxymethyl cellulose", "match_type":
    "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:85146", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[7]", "ingredient":
    {"preferred_term": "Agar", "term": {"id": "CHEBI:2509", "label": "agar"}, "concentration":
    {"value": "6", "unit": "G_PER_L"}, "mediaingredientmech_chebi_term": {"id": "CHEBI:2509",
    "label": "agar"}}, "decision": {"query_label": "Agar", "identifier": "CHEBI:2509",
    "ontology_id": "CHEBI:2509", "mim_preferred_term": "Agar", "matched_label": "Agar",
    "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique",
    "resolution_source": "mim_exact", "local_identifier": "CHEBI:2509", "source_compound_id":
    null, "reason": "trusted MIM label-index answer"}}]

    The two hydrates are correct. CHEBI:85146 names generic CMC; CHEBI:234035 names
    its sodium salt. The source recommendation does not certify polymer degree, viscosity
    number, molar mass or substitution. Do not copy the API polymer mmol_l values
    or the candidate ontology mass into a conversion. Casitone is an undefined mixture;
    the MICRO resolver answer is a diagnostic observation, not a newly verified external
    ontology claim. Full source-grade text has no exact packaged-label answer, which
    does not imply that the material is absent.'
  metrics:
  - name: primary_coverage
    value: 87.5
    unit: percent
    denominator: 8
    minimum: 0
    maximum: 100
    definition: Seven of eight target ingredient descriptors have primary ontology
      identifiers; field coverage, not accuracy.
  - name: secondary_coverage
    value: 87.5
    unit: percent
    denominator: 8
    minimum: 0
    maximum: 100
    definition: Seven of eight target descriptors carry a CHEBI-keyed secondary identifier;
      linkage coverage only.
  - name: secondary_resolver_agreement
    value: 85.71428571428571
    unit: percent
    denominator: 7
    minimum: 0
    maximum: 100
    definition: Six of seven existing secondary IDs agree with the maintained resolver;
      chemical-form evidence assessed separately.
- assessment_id: writer-and-history
  area: provenance
  topic: Current writer behavior, existing evidence and historical reviews
  outcome: concern
  summary: The target lacks six evidence objects already in the DSM owner and preserves
    only the KOMODO history. Current conservative merger rejects this pair; current
    importer still drops ingredient attributes.
  target_ids:
  - CultureMech:003813
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - merge-formulation
  - merge-writer
  - mediadive-writer
  - composition-resolver
  - komodo-writer
  - inspection
  - inspection-delta
  - diagnostics
  - history-report-1
  - history-report-2
  - history-report-3
  - history-report-4
  - history-report-5
  - history-report-6
  details: All six historical reports were read. The two detailed curation reports
    contain28 API recipe/step objects, all matching current source objects, and their
    recorded source hash matches fresh bytes. This authenticates content, not historical
    retrieval time. The September report recommendation to retain a two-record merge
    is not applicable to current conservative compatibility. Its generated-MIX claim
    does not describe the current target. The October KOMODO report repeats the phosphate
    object for every amount and calls all eight conflicts; phosphate preparation and
    recommended CMC form do not refute unrelated numeric g_l values. The DSM report
    defers phosphate and Casitone based on attributes; current direct source inspection
    now supports their numeric values while preserving their attributes. No standalone
    main-solution record is assessed or copied; the historical solution2232 water
    allegation is outside the selected record. Current resolver only fills empty KOMODO
    recipes and skips this populated owner. Stored.fZ and naive timestamp strings
    remain historical; current formatting code is not proof of exact historical execution.
findings:
- finding_id: F1
  issue_key: cm003813-source-preparation-attributes
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and solvent context are incomplete
  description: Phosphate separate-autoclaving is absent from both owners and target;1000ml
    preparation water and the Casitone manufacturer are also omitted. Preserve the
    explicit source details without adding unstated final volume, time or temperature.
  target_ids:
  - CultureMech:003813
  field_paths:
  - ingredients[4]
  - ingredients[5]
  - preparation_steps
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - dsm1111
  - api1111
  - mediadive-writer
  rule_id: P3.4 / P3.5
  native_severity: P3
  normalization_reason: Elevated to major because the missing source-specific sterilization
    boundary changes how this formulation is prepared.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: maintained source transform
- finding_id: F2
  issue_key: cm003813-generated-evidence-preparation-staleness
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Generated record omits maintained source evidence
  description: Six scoped concentration evidence objects and the material recommendation
    already exist in the DSM owner but are absent from the target. Current exact-formulation
    checks reject merging the pair because notes, preparation and ancestry differ.
    Reconcile maintained provenance and regenerate without forcing the old ingredient-only
    collapse.
  target_ids:
  - CultureMech:003813
  field_paths:
  - merged_from
  - ingredients
  - preparation_steps
  - curation_history
  evidence_ids:
  - target
  - komodo-owner
  - dsm-owner
  - diagnostics
  - merge-formulation
  - merge-writer
  rule_id: review-yaml-record generated ownership
  native_severity: major
  normalization_reason: Material source-evidence and preparation loss in generated
    output; no claim that current merger still uses the old lossy behavior.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/formulation.py
    role: maintained compatibility and evidence union
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
- finding_id: F3
  issue_key: cm003813-cmc-generic-sodium-identity-divergence
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: CMC local and MIM identities diverge
  description: Local primary and secondary slots use genericCHEBI:85146, while the
    pinned MIM resolver returns sodium-saltCHEBI:234035 for the same preferred label.
    The source separately recommends sodium salt of high viscosity. Reconcile intended
    material scope and current publication identity; matching labels do not make these
    two identities equivalent, and no automatic primary-term replacement is justified.
  target_ids:
  - CultureMech:003813
  field_paths:
  - ingredients[6].preferred_term
  - ingredients[6].term
  - ingredients[6].mediaingredientmech_chebi_term
  evidence_ids:
  - target
  - dsm-owner
  - dsm1111
  - chebi-85146
  - chebi-234035
  - mim-index
  - diagnostics
  rule_id: P2.2
  native_severity: P2
  normalization_reason: Confirmed divergence between two chemical identity assertions
    is material; the generic term itself is valid and the intended broader-versus-sodium
    scope remains a curation decision.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
- finding_id: F4
  issue_key: cm003813-komodo-condition-history-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Imported atmosphere and historical timestamps need qualification
  description: The KOMODO-derived Aerobic:No note has no counterpart in the inspected
    DSM recipe/API and current KOMODO sources are inaccessible. This is unresolved
    provenance, not proof that the medium is aerobic. Retain the historical malformed.fZ
    and timezone-free events, documenting their limitations through a future append-only
    event.
  target_ids:
  - CultureMech:003813
  field_paths:
  - notes
  - curation_history
  evidence_ids:
  - target
  - komodo-owner
  - dsm1111
  - api1111
  - komodo-current
  - komodo-list
  - komodo-writer
  rule_id: P4.4
  native_severity: P4
  normalization_reason: Elevated to minor for a bounded provenance gap; no unsupported
    correction of the atmosphere is proposed.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: A1
  description: Preserve phosphate separate sterilization, source solvent input and
    Difco qualifier in the two maintained records and the MediaDive attribute path;
    retain the CMC material recommendation in a suitable source-scoped note rather
    than inferring a MIX instruction.
  finding_ids:
  - F1
  target_ids:
  - CultureMech:003813
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: maintained source transform
  acceptance_checks:
  - Compare all nine exact source rows and the phosphate attribute to the updated
    maintained fields.
  - All eight numeric g_l values stay unchanged unless a separately evidenced variant
    is introduced.
  - Run just validate-schema,just validate-strict,just validate-terms and just validate-references
    for each edited owner.
- action_id: A2
  description: Reconcile exact CMC material identity before updating the preferred
    term or either identifier. Preserve generic-versus-recommended-sodium scope; use
    the maintained resolver and explicit primary evidence. Any upstream MIM label
    correction requires its own reviewed change and subsequent pinned dependency refresh.
  finding_ids:
  - F3
  target_ids:
  - CultureMech:003813
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Verify CHEBI:85146 andCHEBI:234035 definitions against the chosen source scope,
    retaining high-viscosity wording without inferred polymer parameters.
  - Use culturemech.ingredients.mim_label_index and just check-mim-label-index to
    verify the resulting publication identity.
  - Do not apply mixture/polymer molarity from provider metadata.
- action_id: A3
  description: Retain existing six DSM claim snippets and append-only history, reconcile
    or keep separate the two owner assertions, and regenerate through the current
    conservative merge pipeline. Do not require a two-record collapse.
  finding_ids:
  - F2
  target_ids:
  - CultureMech:003813
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/formulation.py
    role: maintained compatibility and evidence union
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
  depends_on:
  - A1
  - A2
  generator: src/culturemech/merge/merge_recipes.py via just merge-recipes
  acceptance_checks:
  - Exact compatible inputs preserve all evidence; incompatible preparation/provenance
    remains separate.
  - Run just verify-merges and just audit-merge-freshness after the separately authorized
    regeneration.
  - Check generated source attribution, material note and evidence against the maintained
    owners; retain permanent IDs.
- action_id: A4
  description: Verify the exact historical KOMODO atmosphere assertion when source
    access is available and add an honest provenance note; preserve prior events and
    avoid supplying an unsupported atmosphere.
  finding_ids:
  - F4
  target_ids:
  - CultureMech:003813
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Capture an exact accessible source/version or explicitly retain the unresolved
    condition.
  - Append any future curation history with actual timezone-aware UTC; do not rewrite
    the two old events.
limitations:
- Current exact KOMODO detail and mapping routes return403; its atmosphere and historical-version
  equivalence remain unresolved, so this review is partial.
- Provider g_l values are supported as declared. Primary water input is not evidence
  of measured final volume; no stock, density, polymer mass, substitution, molarity
  or incubation condition is inferred.
- All seven asserted CHEBI IDs and the sodium-salt candidate were checked. Casitone
  MICRO resolver output is diagnostic only; it is not a new external grounding proposal.
- Four canonical checks apply to the selected generated record. Owners/context were
  read; the extra pinned-MIM check passed. No corpus ID/product/merge gates, scientific
  records or experiments were run or changed.
- Historical source objects and six literal claims match fresh bytes; old access times
  and original KOMODO HTML-capture provenance are not independently authenticated.
notes:
- No prior structured finding is closed; the six ad hoc historical reports remain
  contextual observations.
- The immutable original native inspection remains preserved. A single additive context
  inspection includes the actual composition resolver with all prior42 input hashes
  unchanged.
- All numeric quantities, source attributes, existing evidence and current importer
  safeguards were assessed separately; deterministic validation is not scientific
  approval.
tags:
- review-only
- batch059
- source-grounded
- quantity-inventory
```
