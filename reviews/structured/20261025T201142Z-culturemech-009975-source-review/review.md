# Source and formulation review: cellulose_agar (CultureMech:009975)

- Review: 20261025T201142Z-culturemech-009975-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-25T20:08:34Z
- Finished UTC: 2026-10-25T20:11:42Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M57 identifies the selected Cellulose Agar, but the local water and iron units differ from the provider rows. Other masses need an explicit final-volume basis and claim-level evidence; the original JCM65 endpoint returns no formulation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 524; batch 053 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifty-two task batches contain 520 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 523 of 6325 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 231e0ba71b41d45362168d539efebe7991823464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009975 | data/merge_yaml/merged/CELLULOSE_AGAR.yaml | generated | cellulose_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009975 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009975 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/524/strict.tsv |
| validate-terms | passed | True | CultureMech:009975 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009975 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009975 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm65 | unavailable | True | CultureMech:009975 | The exact JCM65 retrieval returned HTTP200 with Nothing found. The TOGO M57 payload remains available; direct current JCM formulation and version authentication is unavailable. |
| Exact source content access: togoM57Page | unavailable | False | CultureMech:009975 | The medium landing-page capture contains only TogoMedium; it provides no additional recipe text. The API payload is assessed separately. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009975.

The four documented recipes completed; interpret the scope of each separately.

### Exact source accession and maintained ownership

identity: supported. Targets: CultureMech:009975.

The selected target and one maintained TOGO owner resolve to M57 / JCM_M65. Their ingredient content agrees; generated merge metadata is not a second biological source. No independently authenticated sibling formula or growth evidence is inferred.

### Mixture and physical-state scope

scope: supported. Targets: CultureMech:009975.

The source identifies Cellulose Agar and includes agar, casein, yeast extract and Casamino acids. The complex/undefined and agar-medium descriptions are consistent. No strain, growth-rate, yield, temperature or incubation claim is supplied by this payload.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009975.

9 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 9/13 primary and 7/13 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 13: primary 69.23%; secondary 53.85%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009975.

19 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Historical reviews and exact source authentication

provenance: concern. Targets: CultureMech:009975.

All three exact historical report texts were read. The two October concentration reports explicitly performed zero source checks; the September review is derivative and assumes a final-litre basis and sibling equivalence not independently established here. Its claimed observations are separated from the newly inspected TOGO bytes. Current history retains the MgSO4 hydrate repair and mixture de-grounding credit; the historical Source: JCM, ID: M57 wording mixes TOGO and JCM accession namespaces. No old report is promoted to primary evidence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009975.

14 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The source lists 1 L distilled-water input, not 1 g/L. Preserve the volume as a batch/preparation fact; density and final-medium volume are not supplied.",
    "source_batch_amount": {
      "value": 1,
      "unit": "L",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q2",
    "subject": "MgSO4・7H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.3,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q3",
    "subject": "K2HPO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.2,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q4",
    "subject": "FeSO4・7H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The source reports 5 mg iron sulfate heptahydrate. 5 mg equals 0.005 g per stated batch, not 5 g/L. A final-volume rate still needs an explicit denominator; no universal g/L correction is asserted.",
    "source_batch_amount": {
      "value": 5,
      "unit": "mg",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q5",
    "subject": "CaCO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"CaCO3\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.2,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q6",
    "subject": "NH4NO3",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"NH4NO3\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.2,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q7",
    "subject": "Cellulose powder",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Cellulose powder\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 20,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q8",
    "subject": "Casein",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Casein\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.2,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q9",
    "subject": "L--Asparagine",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"L--Asparagine\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.25,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q10",
    "subject": "Agar",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 15,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q11",
    "subject": "Yeast extract (BD-Difco)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.1,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q12",
    "subject": "Urea",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Urea\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.1,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q13",
    "subject": "Casamino acids (BD-Difco)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Casamino acids (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "The named source mass is supported as a batch input, but the only volume statement is 1 L water. That is not an explicit final-volume makeup after solute addition. The whole local G_PER_L assertion therefore remains unsupported; retain the source amount separately and establish the denominator before assigning a final-medium rate.",
    "source_batch_amount": {
      "value": 0.1,
      "unit": "g",
      "basis": "TOGO M57 listed recipe input; final volume not explicitly established"
    }
  },
  {
    "decision_id": "q14",
    "subject": "Unadjusted pH instruction",
    "decision": "add",
    "local_fields": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM57",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "pH unadjusted.",
        "snapshot_sha256": "78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885"
      }
    ],
    "rationale": "Preserve the exact unadjusted-pH instruction in the maintained recipe. It is not a numerical pH and does not authorize a guessed pH range or sterilization cycle."
  }
]

## Findings

### f1: Water and iron units do not preserve the source

major / open / confirmed; issue key: cm009975-source-unit-dimensions.

Both layers store distilled water as 1 G_PER_L and iron sulfate heptahydrate as 5 G_PER_L. TOGO lists 1 L and 5 mg respectively. The iron batch mass converts to 0.005 g, while a final-medium denominator remains unestablished.

### f2: Batch quantities lack final-volume and claim-level evidence

major / open / confirmed; issue key: cm009975-batch-basis-and-evidence.

All thirteen local concentrations lack attached amount evidence. The twelve solid masses are recoverable from the TOGO payload, but its 1 L water row alone does not establish final-volume rates. The JCM endpoint supplies no current recipe. No typical-value or sibling-formula substitution resolves this gap.

### f3: The explicit pH instruction is missing

minor / open / confirmed; issue key: cm009975-unadjusted-ph.

TOGO states pH unadjusted, while neither selected layer has preparation_steps. Preserve that instruction without inventing a pH or a sterilization recipe.

### f4: Historical import note conflates source accession namespaces

minor / open / confirmed; issue key: cm009975-accession-history.

The history says Source: JCM, ID: M57. The record media_term and provider metadata correctly identify TOGO M57 and JCM_M65. Retain the old event and add a bounded clarification if separately curated.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained unit/stage representation from the exact TOGO rows, preserving source volume and mass before any separately justified final-volume normalization.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Attach source-specific amount, original unit and stage evidence; explicitly distinguish supported batch inputs from unresolved final-medium rates and preserve the failed JCM access.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Add the source-scoped unadjusted-pH instruction to the owner and retain exact evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Append an accession clarification distinguishing TOGO M57 from JCM65; preserve original history and access limitations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/CELLULOSE_AGAR.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/CELLULOSE_AGAR.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/CELLULOSE_AGAR.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch053/524/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/524/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/CELLULOSE_AGAR.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/CELLULOSE_AGAR.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/CELLULOSE_AGAR.yaml:1:id: CultureMech:009975<br>./data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml:1:id: CultureMech:009975<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/524/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 14 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| togo-recipe | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57; $.meta; $.components[0]; $.comments[0] | supports | Complete TOGO M57 payload read: JCM_M65 identity, thirteen source batch rows, and the unadjusted-pH instruction. Water is listed as an input, not an explicit final-volume makeup statement. |
| jcm65-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=65; Preserved exact public retrieval result | context_only | The exact JCM65 retrieval returned HTTP200 with Nothing found. The TOGO M57 payload remains available; direct current JCM formulation and version authentication is unavailable. |
| togoM57Page-attempt | https://togomedium.org/medium/M57; Preserved exact public retrieval result | context_only | The medium landing-page capture contains only TogoMedium; it provides no additional recipe text. The API payload is assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16199 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16199 resolves to urea. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17196 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17196; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17196 resolves to L-asparagine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3311 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3311 resolves to calcium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63038 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63038; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63038 resolves to ammonium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16199": [{"label": "Urea", "match_type": "preferred_term", "identifier": "CHEBI:16199", "preferred_term": "Urea", "ontology_id": "CHEBI:16199", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17196": [{"label": "L-Asparagine", "match_type": "preferred_term", "identifier": "CHEBI:17196", "preferred_term": "L-Asparagine", "ontology_id": "CHEBI:17196", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311": [{"label": "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311", "preferred_term": "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63038": [{"label": "(NH4)NO3", "match_type": "preferred_term", "identifier": "CHEBI:63038", "preferred_term": "(NH4)NO3", "ontology_id": "CHEBI:63038", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| historical-context | /private/tmp/culturemech-review-work-batch053/524/historical-evidence-review.json; Exact current history arrays, header-matched report texts, parent locators and raw-authentication outcomes | context_only | All three exact historical report texts were read. The two October concentration reports explicitly performed zero source checks; the September review is derivative and assumes a final-litre basis and sibling equivalence not independently established here. Its claimed observations are separated from the newly inspected TOGO bytes. Current history retains the MgSO4 hydrate repair and mixture de-grounding credit; the historical Source: JCM, ID: M57 wording mixes TOGO and JCM accession namespaces. No old report is promoted to primary evidence. |
| grounding-census | /private/tmp/culturemech-review-work-batch053/524/grounding-review.json; Every scoped asserted identifier and exact current CSV/catalog correspondence; excluded parent fields remain excluded | context_only | Bound independent census retains source/field membership and exact identifier matches. Current catalog presence does not authenticate historical use or a receiving-medium recipe. |
| field-census | /private/tmp/culturemech-review-work-batch053/524/local-field-census.json; Complete scalar census of the explicitly listed local documents | context_only | Exact values and locators retained for mechanical reconciliation; this census alone does not establish scientific support. |
| history-metadata | data/merge_yaml/merged/CELLULOSE_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml", "events": 9, "timestamp_issues": []}] |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _parse_unit, _extract_primary_components and _extract_preparation_steps | context_only | Current conversion distinguishes L, mg and mL, retains quantified source components, and can retain source comments. Bare mass mapping still requires source-specific final-volume review. These present guards do not retroactively repair the selected fields. Current code is not proof of the historical execution that produced these bytes. |
| writer-merge | src/culturemech/merge/merger.py; RecipeMerger.merge_group, single-owner and multi-owner branches | context_only | A single-owner group copies the owner and adds merge metadata. Multiple inputs are passed to merge_formulation_evidence, which checks compatibility; this method does not itself select matching groups. Current code is not proof of the historical execution that produced these bytes. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch053/524/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact JCM65 retrieval returned HTTP200 with Nothing found. The TOGO M57 payload remains available; direct current JCM formulation and version authentication is unavailable.
- The medium landing-page capture contains only TogoMedium; it provides no additional recipe text. The API payload is assessed separately.
- No current sibling medium, optional missing ontology link, or growth assertion was inferred. Earlier reports recommending a merge or final-litre concentration are retained as historical leads, not accepted without exact source/formulation evidence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201142Z-culturemech-009975-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: cellulose_agar (CultureMech:009975)'
started_at: '2026-10-25T20:08:34Z'
finished_at: '2026-10-25T20:11:42Z'
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
summary: TOGO M57 identifies the selected Cellulose Agar, but the local water and
  iron units differ from the provider rows. Other masses need an explicit final-volume
  basis and claim-level evidence; the original JCM65 endpoint returns no formulation.
source:
  git_revision: 231e0ba71b41d45362168d539efebe7991823464
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
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
  - path: data/merge_yaml/merged/CELLULOSE_AGAR.yaml
    sha256: 45b9e1a05e1ec8b4f4f5d63816991a3e7213d5048cdd8c900a8e1b64c2e2f1f0
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
    sha256: 4425e34b908d48c6d866486ccf0ad7f8a3f206e811f2c75df0bc7a2b636fa61f
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_650_CENTENUM_medium.yaml.md
    sha256: cea95c8bef224d7988c89e55916e6bfc1c85e40e1e04644c416ba76677bfaf5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_748_CENS_medium.yaml.md
    sha256: 013cdd23597b0f17ae16040cfcff4fa5612704583733ff2b59f4575da6a5ef4e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/medium_650_modified_for_dsm_8319.yaml.md
    sha256: bf8b812d7257fd833fe40a0c3d65ecca0d062d667e5d7ef32e8da45fdc400b8d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cellulosilyticum_medium.yaml.md
    sha256: 6fc71489fc62d3a8490420a79c8e85ef97b1bf00048f2b4a5f9cbde290926d95
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cens_medium.yaml.md
    sha256: 21cd5c7838ddcd4136764be9d06f0b560c3df459ffd3510ca5a9df7e1f34e292
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/centenum_medium.yaml.md
    sha256: 11adfae044a191efafa6569efa6dae001a26c2b4186bb1c4165f15ec06fb5aa7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cgm.yaml.md
    sha256: 00bc6814a1dfc5789c97728aa09b3959c842ce63a226744cc526ee36a88f826e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml.md
    sha256: 3338d620d73f8bd698294bbb4b0a267bb79d279ff8c96056cc4586cd8535f187
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5312_Solution_C.yaml.md
    sha256: e167b06340bce70ab77d6408c8f5e9cb6b1dbeef2c36e29ff20952990e3bfbd2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5342_Solution_A.yaml.md
    sha256: f68b7d85766061aa31ffef0f0172844d47d0aae036221dc66d608c86e8dce7a6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5343_Solution_B.yaml.md
    sha256: aca054ad3ae72ab8aee9908cb67ceac62a96adf84ff60a5141dda9b4f13ff6d8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
    sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-m258-m260-stocks/records/M258.md
    sha256: fda8033086b0627144eb23d2558e66134a597bfa67939fec2f18992de7845747
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CEJFB1T_MEDIUM.md
    sha256: 49ac2c7b79c5da4e7d56b164324afa763d1f8301cb1794aacecb55c381582cb6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.md
    sha256: a9112230e5f2b35a345d29058d2d06b1aec1b6c6e36d77e294ecbad9801f92ba
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: d71859ea710d11f601c3f0c34e1740f6d2afbae9b6516f296dccbe34c913d948
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSE_AGAR.md
    sha256: f90ca9219519b238b5b06d86a8ca2e84f6832a4ab67b0feabd05bdc3a9839381
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.md
    sha256: 3a3e74ac86eca9c6db45ec35f7ef0e6a76527941fffd6422ec02b9931c0c4212
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.md
    sha256: 63217cedf21217428eca34c2c1418b1982e2e1b435abc3a6130e2689216f9fb0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENS_MEDIUM.md
    sha256: 597cb6a7938f9cd459897adf69983dff16ed4d88f1a910366ad8abe4b3928222
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENTENUM_MEDIUM.md
    sha256: 64359ed6e4f323a585a64a19e0259164f4e54dd0e8d5c90443fca6183b6c91e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CGM.md
    sha256: a07bbba50f039aeb8d2aa1f811f38913a6651995e329748e80f180b9a3d57a3b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CGY_Medium.md
    sha256: 2d2435a40efa8bac48c6238994b420ea1f7022e9d1a615b67aa2734a79397302
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/cgm.md
    sha256: 306c1cacb9be80fb75cde15b3ccffd282c046df9f6cf08ef2ff32055f4886ee4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M1148_Halanaeroarchaeum_Medium.md
    sha256: edfdd0b0fb57e8f9d9c328c8326da947773576733a6c38f9ecda66e70fb8e1a9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.md
    sha256: 10dbfce058ee6e85485dcfdc15b611cc9e0b95cea52a03f631a3b54fe008fa04
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: 9a63092a34db92eb9ca60f2db910800f0034f5e7f0e6d1eb074e146061fa60d4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.md
    sha256: 9305c9cfd434cbb5f857fd99357fe9a811cb31a48a3d05d779959557c84250b2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_748_CENS_medium.md
    sha256: a9c41ec015e0f2f45bb92ed0065eb0ddc3f3852207c12751d1ce686377ba8326
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.md
    sha256: d3295a1ae91e3c543bac519713a5559b6da46ed2a5384def64ef0c9354ed6e4f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.md
    sha256: 59c8979a006d9b770dd6d2b0ecdbdfd4a81fa2339fff1d33afd41e65932df4fc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.md
    sha256: e43ae29a243274817a13192084b67ac0741248fff46309a4e2862aef08e1ef58
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.md
    sha256: 7a3396b4e01bffebe1a22b591ead29f62ecbfeaeeeb315bbcac5a84050435f83
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.md
    sha256: a1adca9a9911e57b4bd66fce0a5f4db9d2feea7b745195bf0c6e53238beeb2d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cellulosilyticum_medium.md
    sha256: da0b08c05cca15abca3721b4461c97a7cb8390a6cbb460045efe9dd04a956ec2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cens_medium.md
    sha256: 874c7e795a7cd6cb420776fb624326f85520f9879d26165de81a0638506b1de2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/centenum_medium.md
    sha256: fabcbe826c085e4f317e0f4dffb71c125ef8c93ca6d7c378eb5aa003bcbc9f94
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgm.md
    sha256: aed676ac8b2825a51883505bc77e41d3fd59a20a6facce044c7c62a638aa64d1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgy_medium.md
    sha256: 328084240301f3a0bd2140a55d72e331bb4d75dd7e40be3971155dff910193bc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5312_Solution_C.md
    sha256: 64ab17db61f41d71c9fab76cb8c0838b8cdcd81c4e35f7f240c71642196f0ff3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5342_Solution_A.md
    sha256: 31d821180b177a4395ac64cfe2eb443091729cb74309085beeb1b765ed2dd2f2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5343_Solution_B.md
    sha256: a1f8fb64c671e4aae298c328e3a93b1ad420e2d60c7400dbae6775f8081a0e33
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.md
    sha256: f8616b950028d94561a0c4a986c40d5fdcdfa14324af5f8fa130447d9f7d7bdb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
    role: context
  - path: reports/yaml_record_review/20260922T063517Z-CEJFB1T_MEDIUM.md
    sha256: 1c833062655743da5d43f5f05638efd1b7bad9147a054541027cb892ea737379
    role: context
  - path: reports/yaml_record_review/20260922T063654Z-CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.md
    sha256: 812641f1e5b20ca4a328fc409a8fd1f8cf18a1b8c740c904170097e764dd491a
    role: context
  - path: reports/yaml_record_review/20260922T063822Z-CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: cde23788b5a2bdfea2e67768ac9f27f0ad5200aeccb4c3e6fd8af84b3ac70c14
    role: context
  - path: reports/yaml_record_review/20260922T063942Z-CELLULOSE_AGAR.md
    sha256: 7d7df31cd5aa0b65511048a3ad7ea51ed128f3d111280455da6b27b77deeff3a
    role: context
  - path: reports/yaml_record_review/20260922T064115Z-CELLULOSILYTICUM_MEDIUM.md
    sha256: b3996678c78481e187be45d3a239865ef844eff74fcc663396ac72e9b986aaef
    role: context
  - path: reports/yaml_record_review/20260922T064238Z-CELLULOSILYTICUM_RUMINICOLA_MEDIUM.md
    sha256: 0b2275d6cbeebebbd700d25e120994c47e980a94f276e53b82544cbf4ab4ddff
    role: context
  - path: reports/yaml_record_review/20260922T064616Z-CENS_MEDIUM.md
    sha256: 6358d704259dc7ba50caf8263a8e95c81f311c9618f805c8f60587de73d37d16
    role: context
  - path: reports/yaml_record_review/20260922T064817Z-CENTENUM_MEDIUM.md
    sha256: 5a517b2db46fa7608fa93b1fd6f7ca36633e65d9e9187b38ed2f820fc9ff5c4c
    role: context
  - path: reports/yaml_record_review/20260922T064954Z-CGM.md
    sha256: b50dfb754feed998bcc620cfe9162a90071733ad665f78825ce24a6a870fe143
    role: context
  - path: reports/yaml_record_review/20260922T065133Z-CGY_Medium.md
    sha256: f24f1ad05b4a65ae735f976877698aed5a3ffa1df9130d14103914260882ae5a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/audit_mim_sssom_divergence.py
    sha256: ad3478a5aeb757f2ce503be1b4720c86f0c1d90f5549918e1341dc7ac2c0f445
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_dsmz650_752_762_preparations.py
    sha256: 0b955dd562a885fec75dd73bed1eaa00af707b3e2f9d35f7f16b066feb743e1a
    role: context
  - path: scripts/repair_komodo650_752_762_preparations.py
    sha256: 477e2e14b5ff6284e4e291986b333552215f44dca2473fc64cf1d60e0028c0bd
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_public_stock_concentrations.py
    sha256: 220dafdb1b826063f533a4b7e41dc3f2576adc433be92c65243605255fb97bb1
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
    role: context
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 524; batch 053 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fifty-two task batches
    contain 520 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 523 of 6325 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009975
targets:
- target_id: CultureMech:009975
  path: data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  label: cellulose_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CELLULOSE_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/524/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/524/strict.tsv"
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009975
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
  - CultureMech:009975
- check_id: jcm65-source-access
  name: 'Exact source content access: jcm65'
  required: true
  status: unavailable
  summary: The exact JCM65 retrieval returned HTTP200 with Nothing found. The TOGO
    M57 payload remains available; direct current JCM formulation and version authentication
    is unavailable.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - jcm65-attempt
- check_id: togoM57Page-source-access
  name: 'Exact source content access: togoM57Page'
  required: false
  status: unavailable
  summary: The medium landing-page capture contains only TogoMedium; it provides no
    additional recipe text. The API payload is assessed separately.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - togoM57Page-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:50.430444Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/CELLULOSE_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/524/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:54.391335Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/524/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:09:59.496613Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/CELLULOSE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:02.048659Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-25T20:11:40Z'
  support: supports
  summary: './data/merge_yaml/merged/CELLULOSE_AGAR.yaml:1:id: CultureMech:009975

    ./data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml:1:id: CultureMech:009975

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/524/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-25T20:11:40Z'
  support: supports
  summary: 14 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 49e1c4f5053686a312ad9d82fdc006e032834ee7e28b15457a4fab7296f5bb3b
- evidence_id: togo-recipe
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57
  locator: $.meta; $.components[0]; $.comments[0]
  accessed_at: '2026-10-22T09:27:11.869157Z'
  support: supports
  summary: 'Complete TOGO M57 payload read: JCM_M65 identity, thirteen source batch
    rows, and the unadjusted-pH instruction. Water is listed as an input, not an explicit
    final-volume makeup statement.'
  snapshot_sha256: 78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885
- evidence_id: jcm65-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=65
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:13.215264Z'
  support: context_only
  summary: The exact JCM65 retrieval returned HTTP200 with Nothing found. The TOGO
    M57 payload remains available; direct current JCM formulation and version authentication
    is unavailable.
  snapshot_sha256: e3397209936c97bef61ef5824983d947c01fb979e232a12ea3c437411249bc5c
- evidence_id: togoM57Page-attempt
  kind: database
  reference: https://togomedium.org/medium/M57
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:12.719721Z'
  support: context_only
  summary: The medium landing-page capture contains only TogoMedium; it provides no
    additional recipe text. The API payload is assessed separately.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:46.687620Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.346522Z'
  support: supports
  summary: CHEBI:15377 resolves to water. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi16199
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:39.323287Z'
  support: supports
  summary: CHEBI:16199 resolves to urea. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 5298ca6b7d402b8a6e2091f03adf139a2d777c9614d760976b3953bc88bd862e
- evidence_id: chebi17196
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17196
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T19:02:24.508520Z'
  support: supports
  summary: CHEBI:17196 resolves to L-asparagine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 5e546def4d69297d487ef85c54167891ab8505aa4b59957410bcc05722f4b8a2
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:37.629610Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
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
- evidence_id: chebi3311
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.903210Z'
  support: supports
  summary: CHEBI:3311 resolves to calcium carbonate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5413cec912ec253d62ba7a3f4ce7f0a9312ba8d1cb756713003f77a6e849d4b2
- evidence_id: chebi63038
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63038
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T12:23:44.217684Z'
  support: supports
  summary: CHEBI:63038 resolves to ammonium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3e84a6e44c936aaa0dd03b53fbb9592dccb6de0f8331244a80e4f2292296b2c4
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:48.784931Z'
  support: supports
  summary: CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-25T20:11:40Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:16199": [{"label": "Urea", "match_type": "preferred_term", "identifier":
    "CHEBI:16199", "preferred_term": "Urea", "ontology_id": "CHEBI:16199", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17196": [{"label": "L-Asparagine", "match_type":
    "preferred_term", "identifier": "CHEBI:17196", "preferred_term": "L-Asparagine",
    "ontology_id": "CHEBI:17196", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:3311": [{"label": "CaCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:3311", "preferred_term": "CaCO3", "ontology_id":
    "CHEBI:3311", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63038":
    [{"label": "(NH4)NO3", "match_type": "preferred_term", "identifier": "CHEBI:63038",
    "preferred_term": "(NH4)NO3", "ontology_id": "CHEBI:63038", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: historical-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/524/historical-evidence-review.json
  locator: Exact current history arrays, header-matched report texts, parent locators
    and raw-authentication outcomes
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: 'All three exact historical report texts were read. The two October concentration
    reports explicitly performed zero source checks; the September review is derivative
    and assumes a final-litre basis and sibling equivalence not independently established
    here. Its claimed observations are separated from the newly inspected TOGO bytes.
    Current history retains the MgSO4 hydrate repair and mixture de-grounding credit;
    the historical Source: JCM, ID: M57 wording mixes TOGO and JCM accession namespaces.
    No old report is promoted to primary evidence.'
  snapshot_sha256: bac4930d6b3221137e42de40ffb947bc5acf4d86f26e2a5f8fa59282f2a77c2d
- evidence_id: grounding-census
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/524/grounding-review.json
  locator: Every scoped asserted identifier and exact current CSV/catalog correspondence;
    excluded parent fields remain excluded
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: Bound independent census retains source/field membership and exact identifier
    matches. Current catalog presence does not authenticate historical use or a receiving-medium
    recipe.
  snapshot_sha256: f02df631c7d2a3bf14fcaac4191a063bb84044cca98fc102c3615078594a8bdb
- evidence_id: field-census
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/524/local-field-census.json
  locator: Complete scalar census of the explicitly listed local documents
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: Exact values and locators retained for mechanical reconciliation; this
    census alone does not establish scientific support.
  snapshot_sha256: baf78ba411c6a686e894b0f28039c40aa8df8ad389ce4c4278103ab2dc738c33
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/CELLULOSE_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml", "events": 9, "timestamp_issues":
    []}]'
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _parse_unit, _extract_primary_components and _extract_preparation_steps
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: Current conversion distinguishes L, mg and mL, retains quantified source
    components, and can retain source comments. Bare mass mapping still requires source-specific
    final-volume review. These present guards do not retroactively repair the selected
    fields. Current code is not proof of the historical execution that produced these
    bytes.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group, single-owner and multi-owner branches
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: A single-owner group copies the owner and adds merge metadata. Multiple
    inputs are passed to merge_formulation_evidence, which checks compatibility; this
    method does not itself select matching groups. Current code is not proof of the
    historical execution that produced these bytes.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/524/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-25T20:11:40Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ec98c742e63d9afd2948bdb930a2ec1727c23e7c2715eaeefb9f88886c73ee69
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source accession and maintained ownership
  outcome: supported
  summary: The selected target and one maintained TOGO owner resolve to M57 / JCM_M65.
    Their ingredient content agrees; generated merge metadata is not a second biological
    source. No independently authenticated sibling formula or growth evidence is inferred.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - record
  - owner-0
  - togo-recipe
- assessment_id: classification
  area: scope
  topic: Mixture and physical-state scope
  outcome: supported
  summary: The source identifies Cellulose Agar and includes agar, casein, yeast extract
    and Casamino acids. The complex/undefined and agar-medium descriptions are consistent.
    No strain, growth-rate, yield, temperature or incubation claim is supplied by
    this payload.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - record
  - togo-recipe
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '9 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 9/13 primary
    and 7/13 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi16199
  - chebi17196
  - chebi2509
  - chebi31795
  - chebi3311
  - chebi63038
  - chebi75836
  details: 'Instance coverage on a 0–100 percent scale, denominator 13: primary 69.23%;
    secondary 53.85%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 19 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: historical-scope
  area: provenance
  topic: Historical reviews and exact source authentication
  outcome: concern
  summary: 'All three exact historical report texts were read. The two October concentration
    reports explicitly performed zero source checks; the September review is derivative
    and assumes a final-litre basis and sibling equivalence not independently established
    here. Its claimed observations are separated from the newly inspected TOGO bytes.
    Current history retains the MgSO4 hydrate repair and mixture de-grounding credit;
    the historical Source: JCM, ID: M57 wording mixes TOGO and JCM accession namespaces.
    No old report is promoted to primary evidence.'
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - historical-context
  - record
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 14 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009975
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The source lists 1 L distilled-water input,\
    \ not 1 g/L. Preserve the volume as a batch/preparation fact; density and final-medium\
    \ volume are not supplied.\",\n    \"source_batch_amount\": {\n      \"value\"\
    : 1,\n      \"unit\": \"L\",\n      \"basis\": \"TOGO M57 listed recipe input;\
    \ final volume not explicitly established\"\n    }\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"subject\": \"MgSO4・7H2O\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 0.3,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q3\",\n    \"subject\": \"K2HPO4\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 0.2,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q4\",\n    \"subject\": \"FeSO4・7H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The source reports 5 mg iron sulfate heptahydrate.\
    \ 5 mg equals 0.005 g per stated batch, not 5 g/L. A final-volume rate still needs\
    \ an explicit denominator; no universal g/L correction is asserted.\",\n    \"\
    source_batch_amount\": {\n      \"value\": 5,\n      \"unit\": \"mg\",\n     \
    \ \"basis\": \"TOGO M57 listed recipe input; final volume not explicitly established\"\
    \n    }\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"subject\": \"CaCO3\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCO3\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 0.2,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q6\",\n    \"subject\": \"NH4NO3\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4NO3\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 0.2,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q7\",\n    \"subject\": \"Cellulose powder\",\n \
    \   \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Cellulose powder\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\n      }\n\
    \    ],\n    \"rationale\": \"The named source mass is supported as a batch input,\
    \ but the only volume statement is 1 L water. That is not an explicit final-volume\
    \ makeup after solute addition. The whole local G_PER_L assertion therefore remains\
    \ unsupported; retain the source amount separately and establish the denominator\
    \ before assigning a final-medium rate.\",\n    \"source_batch_amount\": {\n \
    \     \"value\": 20,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57 listed\
    \ recipe input; final volume not explicitly established\"\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q8\",\n    \"subject\": \"Casein\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Casein\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 0.2,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q9\",\n    \"subject\": \"L--Asparagine\",\n    \"\
    decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[8].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L--Asparagine\\\",\\n          \\\"volume\\\"\
    : 0.25,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\n      }\n\
    \    ],\n    \"rationale\": \"The named source mass is supported as a batch input,\
    \ but the only volume statement is 1 L water. That is not an explicit final-volume\
    \ makeup after solute addition. The whole local G_PER_L assertion therefore remains\
    \ unsupported; retain the source amount separately and establish the denominator\
    \ before assigning a final-medium rate.\",\n    \"source_batch_amount\": {\n \
    \     \"value\": 0.25,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57 listed\
    \ recipe input; final volume not explicitly established\"\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q10\",\n    \"subject\": \"Agar\",\n    \"decision\":\
    \ \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 15,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 15,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q11\",\n    \"subject\": \"Yeast extract (BD-Difco)\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\n     \
    \ }\n    ],\n    \"rationale\": \"The named source mass is supported as a batch\
    \ input, but the only volume statement is 1 L water. That is not an explicit final-volume\
    \ makeup after solute addition. The whole local G_PER_L assertion therefore remains\
    \ unsupported; retain the source amount separately and establish the denominator\
    \ before assigning a final-medium rate.\",\n    \"source_batch_amount\": {\n \
    \     \"value\": 0.1,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57 listed\
    \ recipe input; final volume not explicitly established\"\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q12\",\n    \"subject\": \"Urea\",\n    \"decision\":\
    \ \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Urea\\\",\\n          \\\"volume\\\": 0.1,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"The named source mass is supported as\
    \ a batch input, but the only volume statement is 1 L water. That is not an explicit\
    \ final-volume makeup after solute addition. The whole local G_PER_L assertion\
    \ therefore remains unsupported; retain the source amount separately and establish\
    \ the denominator before assigning a final-medium rate.\",\n    \"source_batch_amount\"\
    : {\n      \"value\": 0.1,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57\
    \ listed recipe input; final volume not explicitly established\"\n    }\n  },\n\
    \  {\n    \"decision_id\": \"q13\",\n    \"subject\": \"Casamino acids (BD-Difco)\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Casamino acids (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\n     \
    \ }\n    ],\n    \"rationale\": \"The named source mass is supported as a batch\
    \ input, but the only volume statement is 1 L water. That is not an explicit final-volume\
    \ makeup after solute addition. The whole local G_PER_L assertion therefore remains\
    \ unsupported; retain the source amount separately and establish the denominator\
    \ before assigning a final-medium rate.\",\n    \"source_batch_amount\": {\n \
    \     \"value\": 0.1,\n      \"unit\": \"g\",\n      \"basis\": \"TOGO M57 listed\
    \ recipe input; final volume not explicitly established\"\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q14\",\n    \"subject\": \"Unadjusted pH instruction\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM57\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M57\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"pH unadjusted.\",\n        \"snapshot_sha256\": \"78fdb0eeca05868a87e322bb5a9c366f8bf6a504f1a70bae77c04f6ee2139885\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the exact unadjusted-pH instruction\
    \ in the maintained recipe. It is not a numerical pH and does not authorize a\
    \ guessed pH range or sterilization cycle.\"\n  }\n]"
findings:
- finding_id: f1
  issue_key: cm009975-source-unit-dimensions
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and iron units do not preserve the source
  description: Both layers store distilled water as 1 G_PER_L and iron sulfate heptahydrate
    as 5 G_PER_L. TOGO lists 1 L and 5 mg respectively. The iron batch mass converts
    to 0.005 g, while a final-medium denominator remains unestablished.
  target_ids:
  - CultureMech:009975
  field_paths:
  - ingredients[0].concentration
  - ingredients[3].concentration
  evidence_ids:
  - record
  - owner-0
  - togo-recipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: concentration-source-units
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: cm009975-batch-basis-and-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Batch quantities lack final-volume and claim-level evidence
  description: All thirteen local concentrations lack attached amount evidence. The
    twelve solid masses are recoverable from the TOGO payload, but its 1 L water row
    alone does not establish final-volume rates. The JCM endpoint supplies no current
    recipe. No typical-value or sibling-formula substitution resolves this gap.
  target_ids:
  - CultureMech:009975
  field_paths:
  - ingredients
  - notes
  evidence_ids:
  - record
  - togo-recipe
  - jcm65-attempt
  - historical-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: concentration-evidence-basis
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: cm009975-unadjusted-ph
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The explicit pH instruction is missing
  description: TOGO states pH unadjusted, while neither selected layer has preparation_steps.
    Preserve that instruction without inventing a pH or a sterilization recipe.
  target_ids:
  - CultureMech:009975
  field_paths:
  - notes
  evidence_ids:
  - record
  - owner-0
  - togo-recipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: preparation-source-completeness
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm009975-accession-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical import note conflates source accession namespaces
  description: 'The history says Source: JCM, ID: M57. The record media_term and provider
    metadata correctly identify TOGO M57 and JCM_M65. Retain the old event and add
    a bounded clarification if separately curated.'
  target_ids:
  - CultureMech:009975
  field_paths:
  - curation_history
  - media_term
  - notes
  evidence_ids:
  - history-metadata
  - togo-recipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: source-accession-provenance
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Correct the maintained unit/stage representation from the exact TOGO
    rows, preserving source volume and mass before any separately justified final-volume
    normalization.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
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
  description: Attach source-specific amount, original unit and stage evidence; explicitly
    distinguish supported batch inputs from unresolved final-medium rates and preserve
    the failed JCM access.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
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
  description: Add the source-scoped unadjusted-pH instruction to the owner and retain
    exact evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
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
  description: Append an accession clarification distinguishing TOGO M57 from JCM65;
    preserve original history and access limitations.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009975
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.yaml
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
- The exact JCM65 retrieval returned HTTP200 with Nothing found. The TOGO M57 payload
  remains available; direct current JCM formulation and version authentication is
  unavailable.
- The medium landing-page capture contains only TogoMedium; it provides no additional
  recipe text. The API payload is assessed separately.
- No current sibling medium, optional missing ontology link, or growth assertion was
  inferred. Earlier reports recommending a merge or final-litre concentration are
  retained as historical leads, not accepted without exact source/formulation evidence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-053
- generated-medium
```
