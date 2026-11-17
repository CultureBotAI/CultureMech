# Source and formulation review: ALP defined (CultureMech:015485)

- Review: 20261021T135907Z-culturemech-015485-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:52:38Z
- Finished UTC: 2026-10-21T13:59:07Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact public FEBA formulation supports all stored receiving-medium quantities, including the explicitly diluted Wolfe stocks. Sodium D,L-lactate is incorrectly narrowed to an L-specific ontology identity, and quantity/form evidence is unattached. The current public FEBA revision cannot authenticate the earlier CultureBotHT import, so historical provenance remains partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 235; batch 024 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-three task batches contain 230 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 233 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015485 | data/merge_yaml/merged/ALP_defined.yaml | generated | ALP defined |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015485 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015485 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch024/235/strict.tsv |
| validate-terms | passed | True | CultureMech:015485 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015485 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015485 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: culturebotht_public | unavailable | True | CultureMech:015485 | The exact asserted CultureBotHT repository was not accessible through the captured public API request (HTTP 404). This does not prove that it never existed or that access would fail through every authorized route. March import identity and bytes remain unverified. Current FEBA quantities are independently supported; the partial limit is historical provenance, not missing current recipe rows. |
| Exact source content access: supplier_l1375 | unavailable | False | CultureMech:015485 | The captured supplier_l1375 public product request timed out. Product-specific identity was not recovered; no supplier form, stereoisomer, density or concentration is inferred. The exact FEBA row and ontology metadata remain separate evidence. |
| Exact source content access: supplier_c8731 | unavailable | False | CultureMech:015485 | The captured supplier_c8731 public product request timed out. Product-specific identity was not recovered; no supplier form, stereoisomer, density or concentration is inferred. The exact FEBA row and ontology metadata remain separate evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015485.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:015485.

All 31 primary term instances in each local layer resolve to matching nonobsolete captured CHEBI labels. There are zero asserted current or legacy MIM slots in either layer; secondary membership is not claimed. Exact source-form correspondence is assessed separately, particularly the D,L versus L lactate distinction.

Instance coverage on a 0–100 percent scale, denominator 31: primary 100.00%; secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Current source identity and exact maintained owner

identity: concern. Targets: CultureMech:015485.

The merge event identifies one exact normalized contributor, whose ID, ingredient ordering, values and units agree with the target. FEBA provides the exact named current formulation. The asserted historical CultureBotHT import remains inaccessible and cannot be authenticated by the later FEBA commit or by filename agreement.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015485.

66 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "Sodium phosphate monobasic monohydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.49",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.49",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Sodium phosphate monobasic monohydrate; line 5",
        "exact_source_quote": "Sodium phosphate monobasic monohydrate\t0.49\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "0.49",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q2",
    "claim": "Potassium phosphate dibasic receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.97",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.97",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Potassium phosphate dibasic; line 6",
        "exact_source_quote": "Potassium phosphate dibasic\t0.97\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "0.97",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q3",
    "claim": "Potassium Chloride receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Potassium Chloride; line 7",
        "exact_source_quote": "Potassium Chloride\t0.1\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "0.1",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q4",
    "claim": "Ammonium chloride receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Ammonium chloride; line 8",
        "exact_source_quote": "Ammonium chloride\t0.25\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "0.25",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q5",
    "claim": "Sodium D,L-Lactate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "40",
          "unit": "MILLIMOLAR"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "40",
          "unit": "MILLIMOLAR"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Sodium D,L-Lactate; line 9",
        "exact_source_quote": "Sodium D,L-Lactate\t40\tmM",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "40",
      "receiving_unit": "mM"
    }
  },
  {
    "decision_id": "q6",
    "claim": "Sodium pyruvate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Sodium pyruvate; line 10",
        "exact_source_quote": "Sodium pyruvate\t1.1\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "1.1",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q7",
    "claim": "Sodium acetate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.8203",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.8203",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined direct ingredient Sodium acetate; line 11",
        "exact_source_quote": "Sodium acetate\t0.8203\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The stored receiving-medium value and original unit match the exact direct source row. No attached claim evidence exists in either layer; preserve the amount and add source support.",
    "source_stage": "direct",
    "arithmetic_outside_quote": {
      "stock_divisor": "1",
      "expected_receiving_value": "0.8203",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q8",
    "claim": "Magnesium Sulfate Heptahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Magnesium Sulfate Heptahydrate; line 5",
        "exact_source_quote": "Magnesium Sulfate Heptahydrate\t3\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 3 g/L at 100X; its 1X receiving rate is 0.03 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.03",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q9",
    "claim": "Nitrilotriacetic acid receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.015",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.015",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Nitrilotriacetic acid; line 6",
        "exact_source_quote": "Nitrilotriacetic acid\t1.5\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 1.5 g/L at 100X; its 1X receiving rate is 0.015 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.015",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q10",
    "claim": "Sodium Chloride receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Sodium Chloride; line 7",
        "exact_source_quote": "Sodium Chloride\t1\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 1 g/L at 100X; its 1X receiving rate is 0.01 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.01",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q11",
    "claim": "Manganese (II) sulfate monohydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Manganese (II) sulfate monohydrate; line 8",
        "exact_source_quote": "Manganese (II) sulfate monohydrate\t0.5\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.5 g/L at 100X; its 1X receiving rate is 0.005 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.005",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q12",
    "claim": "Cobalt chloride hexahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Cobalt chloride hexahydrate; line 9",
        "exact_source_quote": "Cobalt chloride hexahydrate\t0.1\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.1 g/L at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q13",
    "claim": "Zinc sulfate heptahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Zinc sulfate heptahydrate; line 10",
        "exact_source_quote": "Zinc sulfate heptahydrate\t0.1\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.1 g/L at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q14",
    "claim": "Calcium Chloride Dihydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Calcium Chloride Dihydrate; line 11",
        "exact_source_quote": "Calcium Chloride Dihydrate\t0.1\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.1 g/L at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q15",
    "claim": "Iron (II) sulfate heptahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Iron (II) sulfate heptahydrate; line 12",
        "exact_source_quote": "Iron (II) sulfate heptahydrate\t0.1\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.1 g/L at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q16",
    "claim": "Nickel (II) chloride hexahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.00025",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.00025",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Nickel (II) chloride hexahydrate; line 13",
        "exact_source_quote": "Nickel (II) chloride hexahydrate\t0.025\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.025 g/L at 100X; its 1X receiving rate is 0.00025 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.00025",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q17",
    "claim": "Aluminum potassium sulfate dodecahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.0002",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.0002",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Aluminum potassium sulfate dodecahydrate; line 14",
        "exact_source_quote": "Aluminum potassium sulfate dodecahydrate\t0.02\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.02 g/L at 100X; its 1X receiving rate is 0.0002 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.0002",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q18",
    "claim": "Copper (II) sulfate pentahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Copper (II) sulfate pentahydrate; line 15",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t0.01\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.01 g/L at 100X; its 1X receiving rate is 0.0001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.0001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q19",
    "claim": "Boric Acid receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Boric Acid; line 16",
        "exact_source_quote": "Boric Acid\t0.01\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.01 g/L at 100X; its 1X receiving rate is 0.0001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.0001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q20",
    "claim": "Sodium Molybdate Dihydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Sodium Molybdate Dihydrate; line 17",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t0.01\tg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.01 g/L at 100X; its 1X receiving rate is 0.0001 g/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.0001",
      "receiving_unit": "g/L"
    }
  },
  {
    "decision_id": "q21",
    "claim": "Sodium selenite pentahydrate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock ingredient Sodium selenite pentahydrate; line 18",
        "exact_source_quote": "Sodium selenite pentahydrate\t0.3\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix stock strength; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's mineral mix; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.3 mg/L at 100X; its 1X receiving rate is 0.003 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's mineral mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.003",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q22",
    "claim": "pyridoxine HCl receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient pyridoxine HCl; line 42",
        "exact_source_quote": "pyridoxine HCl\t10\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 10 mg/L at 100X; its 1X receiving rate is 0.1 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.1",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q23",
    "claim": "4-Aminobenzoic acid receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient 4-Aminobenzoic acid; line 43",
        "exact_source_quote": "4-Aminobenzoic acid\t5\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 5 mg/L at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.05",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q24",
    "claim": "Lipoic acid receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient Lipoic acid; line 44",
        "exact_source_quote": "Lipoic acid\t5\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 5 mg/L at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.05",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q25",
    "claim": "Nicotinic Acid receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient Nicotinic Acid; line 45",
        "exact_source_quote": "Nicotinic Acid\t5\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 5 mg/L at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.05",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q26",
    "claim": "Riboflavin receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient Riboflavin; line 46",
        "exact_source_quote": "Riboflavin\t5\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 5 mg/L at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.05",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q27",
    "claim": "thiamine HCl receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient thiamine HCl; line 47",
        "exact_source_quote": "thiamine HCl\t5\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 5 mg/L at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.05",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q28",
    "claim": "calcium pantothenate receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient calcium pantothenate; line 48",
        "exact_source_quote": "calcium pantothenate\t5\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 5 mg/L at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.05",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q29",
    "claim": "biotin receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.02",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.02",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient biotin; line 49",
        "exact_source_quote": "biotin\t2\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 2 mg/L at 100X; its 1X receiving rate is 0.02 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.02",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q30",
    "claim": "Folic Acid receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.02",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.02",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient Folic Acid; line 50",
        "exact_source_quote": "Folic Acid\t2\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 2 mg/L at 100X; its 1X receiving rate is 0.02 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.02",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q31",
    "claim": "Cyanocobalamin receiving-medium concentration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.001",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.001",
          "unit": "MG_PER_L"
        },
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock ingredient Cyanocobalamin; line 51",
        "exact_source_quote": "Cyanocobalamin\t0.1\tmg/L",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix stock strength; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined receiving strength of Wolfe's vitamin mix; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact source stock contains 0.1 mg/L at 100X; its 1X receiving rate is 0.001 mg/L. Both layers already store that receiving rate. Preserve it and attach these scoped facts; do not multiply it back to stock strength or infer a dispensing volume.",
    "source_stage": "Wolfe's vitamin mix",
    "arithmetic_outside_quote": {
      "stock_divisor": "100",
      "expected_receiving_value": "0.001",
      "receiving_unit": "mg/L"
    }
  },
  {
    "decision_id": "q32",
    "claim": "Wolfe's mineral mix source stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's mineral mix strength header; line 3",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      }
    ],
    "conclusion": "The 100X source strength is context for the already-correct expanded receiving composition. Add explicit derivation/stage evidence if represented; this is not a claim that a normalized stock record must be invented."
  },
  {
    "decision_id": "q33",
    "claim": "Wolfe's mineral mix receiving strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined stock-use row; line 12",
        "exact_source_quote": "Wolfe's mineral mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The source uses this exact stock at 1X. Its liquid aliquot, solvent quantity and dispensing procedure are not specified by this row."
  },
  {
    "decision_id": "q34",
    "claim": "Wolfe's vitamin mix source stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_mixes",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
        "source_locator": "Wolfe's vitamin mix strength header; line 40",
        "exact_source_quote": "X\t100",
        "snapshot_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4"
      }
    ],
    "conclusion": "The 100X source strength is context for the already-correct expanded receiving composition. Add explicit derivation/stage evidence if represented; this is not a claim that a normalized stock record must be invented."
  },
  {
    "decision_id": "q35",
    "claim": "Wolfe's vitamin mix receiving strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined stock-use row; line 13",
        "exact_source_quote": "Wolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The source uses this exact stock at 1X. Its liquid aliquot, solvent quantity and dispensing procedure are not specified by this row."
  },
  {
    "decision_id": "q36",
    "claim": "Source-described pH target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "description",
        "stored": "Defined media for Dechlorosoma suillum PS, pH should be 7.2",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "description",
        "stored": "Defined media for Dechlorosoma suillum PS, pH should be 7.2",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined Description; line 2",
        "exact_source_quote": "Description\tDefined media for Dechlorosoma suillum PS, pH should be 7.2",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The existing description already says pH should be 7.2. This is a source target, not a measured pH, adjustment recipe or growth result."
  },
  {
    "decision_id": "q37",
    "claim": "Structured pH target",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined Description; line 2",
        "exact_source_quote": "Description\tDefined media for Dechlorosoma suillum PS, pH should be 7.2",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "A structured pH target could retain the source-described 7.2 with explicit evidence; preserve its descriptive rather than measured status."
  },
  {
    "decision_id": "q38",
    "claim": "Preparation, stock aliquots and sterilization parameters",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "not_quantified",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "ALP_defined complete exact block",
        "exact_source_quote": "Media\tALP_defined\t\nDescription\tDefined media for Dechlorosoma suillum PS, pH should be 7.2\t\nMinimal\tTRUE\t\nControlled vocabulary\tConcentration\tUnits\nSodium phosphate monobasic monohydrate\t0.49\tg/L\nPotassium phosphate dibasic\t0.97\tg/L\nPotassium Chloride\t0.1\tg/L\nAmmonium chloride\t0.25\tg/L\nSodium D,L-Lactate\t40\tmM\nSodium pyruvate\t1.1\tg/L\nSodium acetate\t0.8203\tg/L\nWolfe's mineral mix\t1\tX\nWolfe's vitamin mix\t1\tX",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      }
    ],
    "conclusion": "The exact metadata block provides composition, stock strength and a pH target, but no water batch, stock aliquot, sterilization temperature/time, atmosphere or incubation conditions. Do not infer these from typical use or from another medium."
  },
  {
    "decision_id": "q39",
    "claim": "Sodium phosphate monobasic monohydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "CAS: 10049-21-5; MW: 137.99; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "CAS: 10049-21-5; MW: 137.99; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium phosphate monobasic monohydrate row",
        "exact_source_quote": "Sodium phosphate monobasic monohydrate\t10049-21-5\tSigma\t\t137.99\tmonobasic sodium phosphate dihydrate\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:114249",
      "formula": [
        "H2O.H2O4P.Na"
      ],
      "mass": [
        "137.991"
      ]
    }
  },
  {
    "decision_id": "q40",
    "claim": "Potassium phosphate dibasic source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "CAS: 7758-11-4; MW: 174.18",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "CAS: 7758-11-4; MW: 174.18",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Potassium phosphate dibasic row",
        "exact_source_quote": "Potassium phosphate dibasic\t7758-11-4\tSigma\tP3786\t174.18\tK2HPO4, dibasic anhydrous sodium phosphate",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:131527",
      "formula": [
        "HO4P.2K"
      ],
      "mass": [
        "174.174"
      ]
    }
  },
  {
    "decision_id": "q41",
    "claim": "Potassium Chloride source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7447-40-7; MW: 74.55",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7447-40-7; MW: 74.55",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Potassium Chloride row",
        "exact_source_quote": "Potassium Chloride\t7447-40-7\tSigma\tP3911\t74.55\tKCl\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:32588",
      "formula": [
        "Cl.K"
      ],
      "mass": [
        "74.551"
      ]
    }
  },
  {
    "decision_id": "q42",
    "claim": "Ammonium chloride source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 12125-02-9; MW: 53.49",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 12125-02-9; MW: 53.49",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Ammonium chloride row",
        "exact_source_quote": "Ammonium chloride\t12125-02-9\tSigma\tA9434\t53.49\tNH4Cl\t\t\tyes\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:31206",
      "formula": [
        "Cl.H4N"
      ],
      "mass": [
        "53.492"
      ]
    }
  },
  {
    "decision_id": "q43",
    "claim": "Sodium D,L-Lactate source molecular-weight metadata",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 50-21-5; MW: 90.08",
        "decision": "conflict",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 50-21-5; MW: 90.08",
        "decision": "conflict",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium D,L-Lactate row",
        "exact_source_quote": "Sodium D,L-Lactate\t50-21-5\tSigma\tL1375\t90.08\tsodium lactate\t\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The source itself combines a sodium D,L-lactate name with CAS 50-21-5 and FW 90.08, while the asserted sodium L-lactate term has formula C3H5O3.Na and mass 112.06. Preserve the source-internal form/metadata conflict separately from the confirmed D,L-to-L narrowing. No mass conversion or replacement ID is inferred.",
    "ontology_metadata": {
      "id": "CHEBI:232798",
      "formula": [
        "C3H5O3.Na"
      ],
      "mass": [
        "112.06"
      ]
    }
  },
  {
    "decision_id": "q44",
    "claim": "Sodium pyruvate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 113-24-6; MW: 110.04",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 113-24-6; MW: 110.04",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium pyruvate row",
        "exact_source_quote": "Sodium pyruvate\t113-24-6\tSigma\tP2256\t110.04\t\t\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:50144",
      "formula": [
        "C3H3O3.Na"
      ],
      "mass": [
        "110.044"
      ]
    }
  },
  {
    "decision_id": "q45",
    "claim": "Sodium acetate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 127-09-3; MW: 82.03",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 127-09-3; MW: 82.03",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium acetate row",
        "exact_source_quote": "Sodium acetate\t127-09-3\tSigma\tS28889-250G\t82.03\tAcetic acid sodium salt\t\t\t\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:32954",
      "formula": [
        "C2H3O2.Na"
      ],
      "mass": [
        "82.034"
      ]
    }
  },
  {
    "decision_id": "q46",
    "claim": "Magnesium Sulfate Heptahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "CAS: 10034-99-8; MW: 246.47; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "CAS: 10034-99-8; MW: 246.47; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Magnesium Sulfate Heptahydrate row",
        "exact_source_quote": "Magnesium Sulfate Heptahydrate\t10034-99-8\tSigma\tM1880\t246.47\tEpsom salts, MgSO4 7H2O",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:31795",
      "formula": [
        "7H2O.Mg.O4S"
      ],
      "mass": [
        "246.473"
      ]
    }
  },
  {
    "decision_id": "q47",
    "claim": "Nitrilotriacetic acid source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 139-13-9; MW: 191.14; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 139-13-9; MW: 191.14; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Nitrilotriacetic acid row",
        "exact_source_quote": "Nitrilotriacetic acid\t139-13-9\tSigma\tN9877\t191.14\tN,N-Bis(carboxymethyl)glycine, NTA, Tris(carboxymethyl)amine\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:44557",
      "formula": [
        "C6H9NO6"
      ],
      "mass": [
        "191.139"
      ]
    }
  },
  {
    "decision_id": "q48",
    "claim": "Sodium Chloride source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "CAS: 7647-14-5; MW: 58.44; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "CAS: 7647-14-5; MW: 58.44; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium Chloride row",
        "exact_source_quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:26710",
      "formula": [
        "Cl.Na"
      ],
      "mass": [
        "58.443"
      ]
    }
  },
  {
    "decision_id": "q49",
    "claim": "Manganese (II) sulfate monohydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[10].notes",
        "stored": "CAS: 10034-96-5; MW: 169.02; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[10].notes",
        "stored": "CAS: 10034-96-5; MW: 169.02; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Manganese (II) sulfate monohydrate row",
        "exact_source_quote": "Manganese (II) sulfate monohydrate\t10034-96-5\tSigma\tM7634\t169.02\tMnSO4 H2O",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:86364",
      "formula": [
        "H2O.Mn.O4S"
      ],
      "mass": [
        "169.016"
      ]
    }
  },
  {
    "decision_id": "q50",
    "claim": "Cobalt chloride hexahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[11].notes",
        "stored": "CAS: 7791-13-1; MW: 237.93; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[11].notes",
        "stored": "CAS: 7791-13-1; MW: 237.93; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Cobalt chloride hexahydrate row",
        "exact_source_quote": "Cobalt chloride hexahydrate\t7791-13-1\tSigma\t255599\t237.93\tCobaltous chloride hexahydrate, CoCl2, CoCl2 6H2O, Cobalt Chloride\t\t\tyes\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:53503",
      "formula": [
        "2Cl.Co.6H2O"
      ],
      "mass": [
        "237.929"
      ]
    }
  },
  {
    "decision_id": "q51",
    "claim": "Zinc sulfate heptahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[12].notes",
        "stored": "CAS: 7446-20-0; MW: 287.56; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[12].notes",
        "stored": "CAS: 7446-20-0; MW: 287.56; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Zinc sulfate heptahydrate row",
        "exact_source_quote": "Zinc sulfate heptahydrate\t7446-20-0\tSigma\tZ0251\t287.56\tzinc sulfate, ZnSO4 7H2O\t\t\t\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:32312",
      "formula": [
        "7H2O.O4S.Zn"
      ],
      "mass": [
        "287.558"
      ]
    }
  },
  {
    "decision_id": "q52",
    "claim": "Iron (II) sulfate heptahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[14].notes",
        "stored": "CAS: 7782-63-0; MW: 278.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[14].notes",
        "stored": "CAS: 7782-63-0; MW: 278.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Iron (II) sulfate heptahydrate row",
        "exact_source_quote": "Iron (II) sulfate heptahydrate\t7782-63-0\tSigma\tF2387\t278.01\tFerrous sulfate heptahydrate, FeSO4 7H2O, Iron sulfate",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:75836",
      "formula": [
        "Fe.7H2O.O4S"
      ],
      "mass": [
        "278.013"
      ]
    }
  },
  {
    "decision_id": "q53",
    "claim": "Nickel (II) chloride hexahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[15].notes",
        "stored": "CAS: 7791-20-0; MW: 237.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[15].notes",
        "stored": "CAS: 7791-20-0; MW: 237.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Nickel (II) chloride hexahydrate row",
        "exact_source_quote": "Nickel (II) chloride hexahydrate\t7791-20-0\tSigma\tN6136\t237.69\tNiCl2 6H2O\t\t\tyes\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:53542",
      "formula": [
        "2Cl.6H2O.Ni"
      ],
      "mass": [
        "237.689"
      ]
    }
  },
  {
    "decision_id": "q54",
    "claim": "Aluminum potassium sulfate dodecahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[16].notes",
        "stored": "CAS: 7784-24-9; MW: 474.39; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[16].notes",
        "stored": "CAS: 7784-24-9; MW: 474.39; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Aluminum potassium sulfate dodecahydrate row",
        "exact_source_quote": "Aluminum potassium sulfate dodecahydrate\t7784-24-9\tSigma\tA7210\t474.39\tAlum, Potassium alum, Potassium aluminum sulfate dodecahydrate, AlK(SO4)2 12H2O",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:86465",
      "formula": [
        "Al.12H2O.K.2O4S"
      ],
      "mass": [
        "474.386"
      ]
    }
  },
  {
    "decision_id": "q55",
    "claim": "Copper (II) sulfate pentahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[17].notes",
        "stored": "CAS: 7758-99-8; MW: 249.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[17].notes",
        "stored": "CAS: 7758-99-8; MW: 249.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Copper (II) sulfate pentahydrate row",
        "exact_source_quote": "Copper (II) sulfate pentahydrate\t7758-99-8\tSigma\tC8027\t249.69\tBlue Vitriol, Cupric sulfate pentahydrate, Sulfuric acid, copper(II) salt (1:1) pentahydrate, CuSO4 5H2O, Cupric Sulfate",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:31440",
      "formula": [
        "Cu.5H2O.O4S"
      ],
      "mass": [
        "249.684"
      ]
    }
  },
  {
    "decision_id": "q56",
    "claim": "Boric Acid source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[18].notes",
        "stored": "CAS: 10043-35-3; MW: 61.83; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[18].notes",
        "stored": "CAS: 10043-35-3; MW: 61.83; From Wolfe's mineral mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Boric Acid row",
        "exact_source_quote": "Boric Acid\t10043-35-3\t\t0084-01 (JT*)\t61.83\tH3BO3\t\t\tno",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:33118",
      "formula": [
        "H3BO3"
      ],
      "mass": [
        "61.833"
      ]
    }
  },
  {
    "decision_id": "q57",
    "claim": "Sodium Molybdate Dihydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[19].notes",
        "stored": "CAS: 10102-40-6; MW: 241.95; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[19].notes",
        "stored": "CAS: 10102-40-6; MW: 241.95; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium Molybdate Dihydrate row",
        "exact_source_quote": "Sodium Molybdate Dihydrate\t10102-40-6\tSigma\t331058\t241.95\tNa2MoO4 2H2O, Na2MoO4-2H2O",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:75213",
      "formula": [
        "2H2O.MoO4.2Na"
      ],
      "mass": [
        "241.946"
      ]
    }
  },
  {
    "decision_id": "q58",
    "claim": "Sodium selenite pentahydrate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[20].notes",
        "stored": "CAS: 26970-82-1; MW: 263.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[20].notes",
        "stored": "CAS: 26970-82-1; MW: 263.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Sodium selenite pentahydrate row",
        "exact_source_quote": "Sodium selenite pentahydrate\t26970-82-1\tSigma\t163\t263.01\tNa2SeO3\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:131361",
      "formula": [
        "5H2O.2Na.O3Se"
      ],
      "mass": [
        "263.012"
      ]
    }
  },
  {
    "decision_id": "q59",
    "claim": "4-Aminobenzoic acid source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[22].notes",
        "stored": "CAS: 150-13-0; MW: 137.14; From Wolfe's vitamin mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[22].notes",
        "stored": "CAS: 150-13-0; MW: 137.14; From Wolfe's vitamin mix; Ontology enriched via CAS-RN lookup",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact 4-Aminobenzoic acid row",
        "exact_source_quote": "4-Aminobenzoic acid\t150-13-0\tSigma\tA9878\t137.14\tp-Aminobenzoic acid, para-aminobenzoic acid",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:30753",
      "formula": [
        "C7H7NO2"
      ],
      "mass": [
        "137.138"
      ]
    }
  },
  {
    "decision_id": "q60",
    "claim": "Lipoic acid source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[23].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 1077-28-7; MW: 206.33; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[23].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 1077-28-7; MW: 206.33; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Lipoic acid row",
        "exact_source_quote": "Lipoic acid\t1077-28-7\tSigma\t\t206.33\tThioctic acid, D,L-6,8-Thioctic Acid",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:16494",
      "formula": [
        "C8H14O2S2"
      ],
      "mass": [
        "206.332"
      ]
    }
  },
  {
    "decision_id": "q61",
    "claim": "Nicotinic Acid source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[24].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 59-67-6; MW: 123.11; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[24].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 59-67-6; MW: 123.11; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Nicotinic Acid row",
        "exact_source_quote": "Nicotinic Acid\t59-67-6\tSigma\tN4126\t123.11",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:15940",
      "formula": [
        "C6H5NO2"
      ],
      "mass": [
        "123.111"
      ]
    }
  },
  {
    "decision_id": "q62",
    "claim": "Riboflavin source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[25].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 83-88-5; MW: 376.36; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[25].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 83-88-5; MW: 376.36; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Riboflavin row",
        "exact_source_quote": "Riboflavin\t83-88-5\tSigma\tR4500\t376.36",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:17015",
      "formula": [
        "C17H20N4O6"
      ],
      "mass": [
        "376.369"
      ]
    }
  },
  {
    "decision_id": "q63",
    "claim": "calcium pantothenate source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[27].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 137-08-6; MW: 238.27; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[27].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 137-08-6; MW: 238.27; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact calcium pantothenate row",
        "exact_source_quote": "calcium pantothenate\t137-08-6\tSigma\tC8731\t238.27\t(R)-(+)-N-(2,4-Dihydroxy-3,3-dimethyl-1-oxobutyl)-_-alanine hemicalcium salt, Calcium D-pantothenate, Vitamin B5, pantothenic acid, Pantothenic acid dicalcium salt, Calcium D,L-pantothenate\t\t\tno",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The source FW 238.27 accompanies explicit hemicalcium-salt wording; the captured ontology mass 476.536 uses a full 2C9H16NO5.Ca formula. This half-formula convention is not evidence of a twofold recipe error. The source also mixes D and D,L synonyms; no unsupported stereoisomer is selected.",
    "ontology_metadata": {
      "id": "CHEBI:31345",
      "formula": [
        "2C9H16NO5.Ca"
      ],
      "mass": [
        "476.536"
      ]
    }
  },
  {
    "decision_id": "q64",
    "claim": "biotin source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[28].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 58-85-5; MW: 244.31; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[28].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 58-85-5; MW: 244.31; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact biotin row",
        "exact_source_quote": "biotin\t58-85-5\tSigma\tB4501\t244.31\tD-Biotin, Bios II, Biotin, Coenzyme R, Vitamin B7, Vitamin H\t\t\tno",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:15956",
      "formula": [
        "C10H16N2O3S"
      ],
      "mass": [
        "244.316"
      ]
    }
  },
  {
    "decision_id": "q65",
    "claim": "Folic Acid source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[29].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 59-30-3; MW: 441.4; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[29].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 59-30-3; MW: 441.4; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Folic Acid row",
        "exact_source_quote": "Folic Acid\t59-30-3\tSigma\tF7876\t441.4",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:27470",
      "formula": [
        "C19H19N7O6"
      ],
      "mass": [
        "441.404"
      ]
    }
  },
  {
    "decision_id": "q66",
    "claim": "Cyanocobalamin source molecular-weight metadata",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALP_defined.yaml",
        "field_path": "ingredients[30].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 68-19-9; MW: 1355.37; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      },
      {
        "input": "data/normalized_yaml/specialized/alp_defined.yaml",
        "field_path": "ingredients[30].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 68-19-9; MW: 1355.37; From Wolfe's vitamin mix",
        "decision": "evidence_only",
        "attached_matching_evidence": false
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv exact Cyanocobalamin row",
        "exact_source_quote": "Cyanocobalamin\t68-19-9\tSigma\tC3607\t1355.37\tVitamin B12, _-(5,6-Dimethylbenzimidazolyl)cyanocobamide, CN-Cbl, Cyanocob(III)alamin",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "conclusion": "The local MW/CAS text exactly reproduces this FEBA compound row; retain its source and formula convention rather than using rounded metadata to change recipe amounts.",
    "ontology_metadata": {
      "id": "CHEBI:17439",
      "formula": [
        "C63H88CoN14O14P"
      ],
      "mass": [
        "1355.388"
      ]
    }
  }
]

### Direct rates and explicit stock dilution

quantity: supported. Targets: CultureMech:015485.

Every one of the 31 target concentrations and 31 owner concentrations matches the exact named FEBA block or its 100X-to-1X expansion, with units preserved. The 14 mineral and 10 vitamin rows are receiving concentrations, not an undiluted-stock flattening. Neither layer has attached quantity evidence. Source-only X strengths, pH and unspecified preparation parameters are individually inventoried.

### Hydrates, stereochemistry, CAS and molecular-weight notes

grounding: concern. Targets: CultureMech:015485.

The source explicitly names D,L-lactate, whereas CHEBI:232798 is sodium L-lactate. The source lactate dictionary also contains a sodium-name versus acid-scale CAS/FW tension. Calcium pantothenate hemicalcium wording explains the half-formula mass convention without a twofold dose correction. The source monobasic sodium-phosphate row has a contradictory dihydrate synonym despite its monohydrate name/CAS/formula, and its potassium-phosphate row contains a sodium synonym; these aliases are not alternative ingredient identities. Lipoic-acid source CAS 1077-28-7 is absent from the captured generic term cross-references, which does not prove an invalid ID or authorize a replacement. Explicit mineral hydrate forms and the other source-supported formula identities were compared individually.

### Preparation scope and evidence placement

completeness: concern. Targets: CultureMech:015485.

Current composition support is complete within the exact FEBA metadata scope. Preparation and experimental growth conditions are not supplied by that source; missing protocol values are not guessed. The existing descriptive pH is source-supported, but no claim-level evidence is attached to concentrations, pH or form decisions. Source references should distinguish current FEBA support from inaccessible historical CultureBotHT bytes.

### Medium classification and growth-description boundary

scope: supported. Targets: CultureMech:015485.

DEFINED/DEFINED and LIQUID agree with the named components and the lack of agar in this exact recipe. The generic specialized category is a current importer fallback, not biological growth evidence. The description names a strain and a pH target; taxonomy supplies identity only. No experiment, temperature, gas regime or organism growth assertion is added.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015485.

11 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Mapping annotations and stale presence flag

provenance: concern. Targets: CultureMech:015485.

All 31 ingredient rows in both layers now have primary term IDs, but has_unmapped_ingredients remains. The current importer definition checks slot presence, so this flag no longer describes that condition. Mapping confidence 0.90 is historical software metadata, not a calibrated scientific probability or MIM assertion; its original calculation is not recovered.

## Findings

### f1: A D,L source ingredient is narrowed to sodium L-lactate

major / open / confirmed; issue key: lactate-source-form.

The exact medium and compound rows name Sodium D,L-Lactate, while both local layers assert CHEBI:232798 sodium L-lactate. Canonical term-label validity does not establish that stereochemical substitution. The FEBA compound row also carries a sodium-name versus CAS/FW conflict; the local notes faithfully copy it, so it is not labeled a new local transcription error.

### f2: Current formulation evidence and historical import identity are not separated

major / open / confirmed; issue key: source-evidence-provenance.

All current receiving concentrations match the exact FEBA formulation, yet both local layers lack attached claim evidence and cite only CultureBotHT. The public September FEBA commit cannot authenticate March import bytes. The pH description and X-strength derivations also need their exact source scope.

### f3: The retained unmapped-ingredient flag no longer matches slot presence

minor / open / confirmed; issue key: unmapped-flag-stale.

Both local layers retain has_unmapped_ingredients even though all 31 primary term slots are present and their labels resolve. This is distinct from the confirmed lactate form error, which a presence flag cannot describe.

## Recommended Actions And Acceptance Checks

### a1

Resolve the exact supplied lactate form with source-specific evidence, retain the original 40 mM recipe claim, and correct or qualify unsupported stereochemical grounding and inconsistent metadata without inventing a replacement ID or mass conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Attach current exact FEBA recipe and stock evidence to each supported claim; preserve the historical CultureBotHT assertion as unresolved unless its actual bytes become available. Keep source versions and times separate and document preparation limits.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Reassess the stale presence flag under the current flag contract, retaining a specific source-form concern and an append-only explanation of any authorized change.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALP_defined.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/alp_defined.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALP_defined.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALP_defined.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch024/235/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch024/235/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALP_defined.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALP_defined.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/alp_defined.yaml:1:id: CultureMech:015485<br>./data/merge_yaml/merged/ALP_defined.yaml:1:id: CultureMech:015485<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch024/source-preflight-bound/235/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 44 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| feba-identity | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; Exact Media ALP_defined block, description and all direct/mix rows | supports | This exact named formulation is the source for the current numerical comparison; neighboring ALP variants are not substituted. |
| feba-stock-0 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes; Exact Wolfe's mineral mix block, X header and complete composition | supports | The stock is explicitly 100X and the exact medium calls for 1X. Composition rates divide by 100 with their original g/L or mg/L units; no dispensing volume is inferred. |
| feba-stock-1 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes; Exact Wolfe's vitamin mix block, X header and complete composition | supports | The stock is explicitly 100X and the exact medium calls for 1X. Composition rates divide by 100 with their original g/L or mg/L units; no dispensing volume is inferred. |
| compound-metadata | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact per-ingredient compound rows; CAS, FW, synonyms and product fields | supports | Each asserted local CAS/MW note is checked against the exact source row and captured ontology metadata. Source dictionaries may contain internally inconsistent synonyms; metadata agreement alone is not product or stereochemical verification. |
| feba-version | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b; Exact commit hash/date fields | supports | The public source revision is 803273865ea9e83fab770ec4f13670db80e1180b dated 2026-09-10T16:27:42+00:00. This September snapshot postdates the March CultureBotHT import; agreeing content is independent present-source support, not recovered historical bytes. |
| culturebotht_public-attempt | https://api.github.com/repos/CultureBotAI/CultureBotHT; Preserved exact public retrieval result | context_only | The exact asserted CultureBotHT repository was not accessible through the captured public API request (HTTP 404). This does not prove that it never existed or that access would fail through every authorized route. March import identity and bytes remain unverified. Current FEBA quantities are independently supported; the partial limit is historical provenance, not missing current recipe rows. |
| supplier_l1375-attempt | https://www.sigmaaldrich.com/US/en/product/sigma/l1375; Preserved exact public retrieval result | context_only | The captured supplier_l1375 public product request timed out. Product-specific identity was not recovered; no supplier form, stereoisomer, density or concentration is inferred. The exact FEBA row and ontology metadata remain separate evidence. |
| supplier_c8731-attempt | https://www.sigmaaldrich.com/US/en/product/sigma/c8731; Preserved exact public retrieval result | context_only | The captured supplier_c8731 public product request timed out. Product-specific identity was not recovered; no supplier form, stereoisomer, density or concentration is inferred. The exact FEBA row and ontology metadata remain separate evidence. |
| chebi114249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_114249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:114249 resolves to sodium dihydrogenphosphate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17439 resolves to cyanocob(III)alamin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi232798 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_232798; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:232798 resolves to sodium L-lactate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32954 resolves to sodium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53542 resolves to nickel chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}} |
| form-metadata | /private/tmp/culturemech-review-work-batch024/235/chemical-form-metadata.json; Every local ingredient, source compound row, notes and captured ontology formula/CAS/mass | context_only | Complete per-row metadata comparison, including exact raw source excerpts. CAS mismatch/absence is not automatically an invalid primary ID; full formula and stereochemical scope are assessed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch024/235/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| taxonomy-strain | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=640081&amp;retmode=xml; Taxon 640081: scientific name, synonym, parent and rank | supports | The description name Dechlorosoma suillum PS is a synonym of Azospira oryzae PS, rank strain, parent 146939. This establishes name correspondence only; it does not establish growth on this medium. |
| taxonomy-species | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=146939&amp;retmode=xml; Taxon 146939: scientific name/rank and historical synonym | supports | The species parent is Azospira oryzae; the strain record is the exact description-name correspondence. No species-wide cultivation assertion is inferred. |
| history-metadata | data/merge_yaml/merged/ALP_defined.yaml; data/normalized_yaml/specialized/alp_defined.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/alp_defined.yaml", "events": 5, "timestamp_issues": []}] |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer transformation copies source fields, appends source/import metadata and only appends an unmapped-ingredient flag when slots are missing; it does not prove March execution or source chemistry. Current formulation compatibility and any captured cleanup/regrounding sections were read as present code, not historical replay. |
| writer-1 | scripts/import_from_culturebotht.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer transformation copies source fields, appends source/import metadata and only appends an unmapped-ingredient flag when slots are missing; it does not prove March execution or source chemistry. Current formulation compatibility and any captured cleanup/regrounding sections were read as present code, not historical replay. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact asserted CultureBotHT repository was not accessible through the captured public API request (HTTP 404). This does not prove that it never existed or that access would fail through every authorized route. March import identity and bytes remain unverified. Current FEBA quantities are independently supported; the partial limit is historical provenance, not missing current recipe rows.
- The captured supplier_l1375 public product request timed out. Product-specific identity was not recovered; no supplier form, stereoisomer, density or concentration is inferred. The exact FEBA row and ontology metadata remain separate evidence.
- The captured supplier_c8731 public product request timed out. Product-specific identity was not recovered; no supplier form, stereoisomer, density or concentration is inferred. The exact FEBA row and ontology metadata remain separate evidence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135907Z-culturemech-015485-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: ALP defined (CultureMech:015485)'
started_at: '2026-10-21T13:52:38Z'
finished_at: '2026-10-21T13:59:07Z'
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
summary: The exact public FEBA formulation supports all stored receiving-medium quantities,
  including the explicitly diluted Wolfe stocks. Sodium D,L-lactate is incorrectly
  narrowed to an L-specific ontology identity, and quantity/form evidence is unattached.
  The current public FEBA revision cannot authenticate the earlier CultureBotHT import,
  so historical provenance remains partial.
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
  - path: data/merge_yaml/merged/ALP_defined.yaml
    sha256: bbce96948cc241c5930b8bbb249c18193f858a0fc1a8e73e1e8ec93f46fe6b77
    role: target
  - path: data/normalized_yaml/specialized/alp_defined.yaml
    sha256: b0eddec75e01eaa5c5573ee18555ecf4ca651bdae5084f8cc2d93fa42b2dc840
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
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
  selection: Task review 235; batch 024 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-three task batches
    contain 230 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 233 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015485
targets:
- target_id: CultureMech:015485
  path: data/merge_yaml/merged/ALP_defined.yaml
  label: ALP defined
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALP_defined.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALP_defined.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch024/235/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch024/235/strict.tsv"
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALP_defined.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALP_defined.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015485
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
  - CultureMech:015485
- check_id: culturebotht_public-source-access
  name: 'Exact source content access: culturebotht_public'
  required: true
  status: unavailable
  summary: The exact asserted CultureBotHT repository was not accessible through the
    captured public API request (HTTP 404). This does not prove that it never existed
    or that access would fail through every authorized route. March import identity
    and bytes remain unverified. Current FEBA quantities are independently supported;
    the partial limit is historical provenance, not missing current recipe rows.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - culturebotht_public-attempt
- check_id: supplier_l1375-source-access
  name: 'Exact source content access: supplier_l1375'
  required: false
  status: unavailable
  summary: The captured supplier_l1375 public product request timed out. Product-specific
    identity was not recovered; no supplier form, stereoisomer, density or concentration
    is inferred. The exact FEBA row and ontology metadata remain separate evidence.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - supplier_l1375-attempt
- check_id: supplier_c8731-source-access
  name: 'Exact source content access: supplier_c8731'
  required: false
  status: unavailable
  summary: The captured supplier_c8731 public product request timed out. Product-specific
    identity was not recovered; no supplier form, stereoisomer, density or concentration
    is inferred. The exact FEBA row and ontology metadata remain separate evidence.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - supplier_c8731-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALP_defined.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/alp_defined.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALP_defined.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:17.789595Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALP_defined.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch024/235/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:19.205474Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch024/235/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALP_defined.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:20.873887Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALP_defined.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:53:22.018996Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:59:06Z'
  support: supports
  summary: './data/normalized_yaml/specialized/alp_defined.yaml:1:id: CultureMech:015485

    ./data/merge_yaml/merged/ALP_defined.yaml:1:id: CultureMech:015485

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/source-preflight-bound/235/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:59:06Z'
  support: supports
  summary: 44 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a6f9444af4e578a161ac10c452c6d1b47f5d85a1ebbb496fe1fa49f3a2dd69a3
- evidence_id: feba-identity
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: Exact Media ALP_defined block, description and all direct/mix rows
  accessed_at: '2026-10-21T07:58:53.930003Z'
  support: supports
  summary: This exact named formulation is the source for the current numerical comparison;
    neighboring ALP variants are not substituted.
  quote: "Media\tALP_defined\t\r\nDescription\tDefined media for Dechlorosoma suillum\
    \ PS, pH should be 7.2\t\r\nMinimal\tTRUE\t\r\nControlled vocabulary\tConcentration\t\
    Units\r\nSodium phosphate monobasic monohydrate\t0.49\tg/L\r\nPotassium phosphate\
    \ dibasic\t0.97\tg/L\r\nPotassium Chloride\t0.1\tg/L\r\nAmmonium chloride\t0.25\t\
    g/L\r\nSodium D,L-Lactate\t40\tmM\r\nSodium pyruvate\t1.1\tg/L\r\nSodium acetate\t\
    0.8203\tg/L\r\nWolfe's mineral mix\t1\tX\r\nWolfe's vitamin mix\t1\tX"
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: feba-stock-0
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes
  locator: Exact Wolfe's mineral mix block, X header and complete composition
  accessed_at: '2026-10-21T07:58:53.930648Z'
  support: supports
  summary: The stock is explicitly 100X and the exact medium calls for 1X. Composition
    rates divide by 100 with their original g/L or mg/L units; no dispensing volume
    is inferred.
  quote: "Media\tWolfe's mineral mix\t\r\nDescription\tStandard 100X mineral solution\
    \ (based on Wolfe's formulation)\t\r\nX\t100\t\r\nControlled vocabulary\tConcentration\t\
    Units\r\nMagnesium Sulfate Heptahydrate\t3\tg/L\r\nNitrilotriacetic acid\t1.5\t\
    g/L\r\nSodium Chloride\t1\tg/L\r\nManganese (II) sulfate monohydrate\t0.5\tg/L\r\
    \nCobalt chloride hexahydrate\t0.1\tg/L\r\nZinc sulfate heptahydrate\t0.1\tg/L\r\
    \nCalcium Chloride Dihydrate\t0.1\tg/L\r\nIron (II) sulfate heptahydrate\t0.1\t\
    g/L\r\nNickel (II) chloride hexahydrate\t0.025\tg/L\r\nAluminum potassium sulfate\
    \ dodecahydrate\t0.02\tg/L\r\nCopper (II) sulfate pentahydrate\t0.01\tg/L\r\n\
    Boric Acid\t0.01\tg/L\r\nSodium Molybdate Dihydrate\t0.01\tg/L\r\nSodium selenite\
    \ pentahydrate\t0.3\tmg/L"
  snapshot_sha256: b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4
- evidence_id: feba-stock-1
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes
  locator: Exact Wolfe's vitamin mix block, X header and complete composition
  accessed_at: '2026-10-21T07:58:53.930648Z'
  support: supports
  summary: The stock is explicitly 100X and the exact medium calls for 1X. Composition
    rates divide by 100 with their original g/L or mg/L units; no dispensing volume
    is inferred.
  quote: "Media\tWolfe's vitamin mix\t\r\nDescription\tStandard 100X vitamin solution\
    \ (based on Wolfe's formulation)\t\r\nX\t100\t\r\nControlled vocabulary\tConcentration\t\
    Units\r\npyridoxine HCl\t10\tmg/L\r\n4-Aminobenzoic acid\t5\tmg/L\r\nLipoic acid\t\
    5\tmg/L\r\nNicotinic Acid\t5\tmg/L\r\nRiboflavin\t5\tmg/L\r\nthiamine HCl\t5\t\
    mg/L\r\ncalcium pantothenate\t5\tmg/L\r\nbiotin\t2\tmg/L\r\nFolic Acid\t2\tmg/L\r\
    \nCyanocobalamin\t0.1\tmg/L"
  snapshot_sha256: b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4
- evidence_id: compound-metadata
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact per-ingredient compound rows; CAS, FW, synonyms and product fields
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Each asserted local CAS/MW note is checked against the exact source row
    and captured ontology metadata. Source dictionaries may contain internally inconsistent
    synonyms; metadata agreement alone is not product or stereochemical verification.
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: feba-version
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b
  locator: Exact commit hash/date fields
  accessed_at: '2026-10-21T07:59:41.378955Z'
  support: supports
  summary: The public source revision is 803273865ea9e83fab770ec4f13670db80e1180b
    dated 2026-09-10T16:27:42+00:00. This September snapshot postdates the March CultureBotHT
    import; agreeing content is independent present-source support, not recovered
    historical bytes.
  snapshot_sha256: 0a4998d61b96db10c549512e2fe06718e04b687e6bbc6b2c1ea121c3c11a53ca
- evidence_id: culturebotht_public-attempt
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:39:29.686353Z'
  support: context_only
  summary: The exact asserted CultureBotHT repository was not accessible through the
    captured public API request (HTTP 404). This does not prove that it never existed
    or that access would fail through every authorized route. March import identity
    and bytes remain unverified. Current FEBA quantities are independently supported;
    the partial limit is historical provenance, not missing current recipe rows.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: supplier_l1375-attempt
  kind: database
  reference: https://www.sigmaaldrich.com/US/en/product/sigma/l1375
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:40:53.404727Z'
  support: context_only
  summary: The captured supplier_l1375 public product request timed out. Product-specific
    identity was not recovered; no supplier form, stereoisomer, density or concentration
    is inferred. The exact FEBA row and ontology metadata remain separate evidence.
- evidence_id: supplier_c8731-attempt
  kind: database
  reference: https://www.sigmaaldrich.com/US/en/product/sigma/c8731
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:41:23.453651Z'
  support: context_only
  summary: The captured supplier_c8731 public product request timed out. Product-specific
    identity was not recovered; no supplier form, stereoisomer, density or concentration
    is inferred. The exact FEBA row and ontology metadata remain separate evidence.
- evidence_id: chebi114249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_114249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:41:01.898803Z'
  support: supports
  summary: CHEBI:114249 resolves to sodium dihydrogenphosphate monohydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 95f1a21c34a9515cd8ea47ffd1cfc2f5788bd31203f6888efb22b05eb6eb4efa
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
- evidence_id: chebi17439
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:23.574834Z'
  support: supports
  summary: CHEBI:17439 resolves to cyanocob(III)alamin. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: chebi232798
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_232798
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:41:01.909796Z'
  support: supports
  summary: CHEBI:232798 resolves to sodium L-lactate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 9babe942a39eb91a513ec202dbae4289fda9f5586836aaee58192b4795ce7344
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
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
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
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
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
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
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
- evidence_id: chebi53542
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:31.075912Z'
  support: supports
  summary: CHEBI:53542 resolves to nickel chloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
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
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:59:06Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: form-metadata
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/235/chemical-form-metadata.json
  locator: Every local ingredient, source compound row, notes and captured ontology
    formula/CAS/mass
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: Complete per-row metadata comparison, including exact raw source excerpts.
    CAS mismatch/absence is not automatically an invalid primary ID; full formula
    and stereochemical scope are assessed.
  snapshot_sha256: ffda4cdf28499ff46c646747c5bba6db7769ae8559b09c4bdb02e37d913b605f
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/235/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: afcbbe5720629b46ae3d3cbb41c36b71c0efd25ac2d384d4d046add3952d4d01
- evidence_id: taxonomy-strain
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=640081&retmode=xml
  locator: 'Taxon 640081: scientific name, synonym, parent and rank'
  accessed_at: '2026-10-21T13:40:53.031961Z'
  support: supports
  summary: The description name Dechlorosoma suillum PS is a synonym of Azospira oryzae
    PS, rank strain, parent 146939. This establishes name correspondence only; it
    does not establish growth on this medium.
  quote: <Synonym>Dechlorosoma suillum PS</Synonym>
  snapshot_sha256: f515fa7b63cfb39966440202928aa34c992f9c68f3f227521253ff65d11c766d
- evidence_id: taxonomy-species
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=146939&retmode=xml
  locator: 'Taxon 146939: scientific name/rank and historical synonym'
  accessed_at: '2026-10-21T13:40:20.742913Z'
  support: supports
  summary: The species parent is Azospira oryzae; the strain record is the exact description-name
    correspondence. No species-wide cultivation assertion is inferred.
  snapshot_sha256: 694882a904790f1666d2648148eea9fed51490e957ef8c404a16f2a9481f2c35
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALP_defined.yaml; data/normalized_yaml/specialized/alp_defined.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: '[{"input": "target", "events": 6, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/alp_defined.yaml",
    "events": 5, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: Current importer transformation copies source fields, appends source/import
    metadata and only appends an unmapped-ingredient flag when slots are missing;
    it does not prove March execution or source chemistry. Current formulation compatibility
    and any captured cleanup/regrounding sections were read as present code, not historical
    replay.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:59:06Z'
  support: context_only
  summary: Current importer transformation copies source fields, appends source/import
    metadata and only appends an unmapped-ingredient flag when slots are missing;
    it does not prove March execution or source chemistry. Current formulation compatibility
    and any captured cleanup/regrounding sections were read as present code, not historical
    replay.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: All 31 primary term instances in each local layer resolve to matching nonobsolete
    captured CHEBI labels. There are zero asserted current or legacy MIM slots in
    either layer; secondary membership is not claimed. Exact source-form correspondence
    is assessed separately, particularly the D,L versus L lactate distinction.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi114249
  - chebi131361
  - chebi131527
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17439
  - chebi232798
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi32954
  - chebi33118
  - chebi44557
  - chebi49105
  - chebi50144
  - chebi53503
  - chebi53542
  - chebi75213
  - chebi75836
  - chebi86158
  - chebi86364
  - chebi86465
  details: 'Instance coverage on a 0–100 percent scale, denominator 31: primary 100.00%;
    secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Current source identity and exact maintained owner
  outcome: concern
  summary: The merge event identifies one exact normalized contributor, whose ID,
    ingredient ordering, values and units agree with the target. FEBA provides the
    exact named current formulation. The asserted historical CultureBotHT import remains
    inaccessible and cannot be authenticated by the later FEBA commit or by filename
    agreement.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - record
  - id-search
  - feba-identity
  - feba-version
  - culturebotht_public-attempt
  - owner-0
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 66 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"Sodium phosphate\
    \ monobasic monohydrate receiving-medium concentration\",\n    \"decision\": \"\
    evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Sodium phosphate\
    \ monobasic monohydrate; line 5\",\n        \"exact_source_quote\": \"Sodium phosphate\
    \ monobasic monohydrate\\t0.49\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"0.49\",\n     \
    \ \"receiving_unit\": \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q2\",\n\
    \    \"claim\": \"Potassium phosphate dibasic receiving-medium concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.97\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.97\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Potassium phosphate\
    \ dibasic; line 6\",\n        \"exact_source_quote\": \"Potassium phosphate dibasic\\\
    t0.97\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"0.97\",\n     \
    \ \"receiving_unit\": \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q3\",\n\
    \    \"claim\": \"Potassium Chloride receiving-medium concentration\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Potassium Chloride;\
    \ line 7\",\n        \"exact_source_quote\": \"Potassium Chloride\\t0.1\\tg/L\"\
    ,\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"0.1\",\n      \"\
    receiving_unit\": \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q4\",\n  \
    \  \"claim\": \"Ammonium chloride receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.25\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.25\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Ammonium chloride;\
    \ line 8\",\n        \"exact_source_quote\": \"Ammonium chloride\\t0.25\\tg/L\"\
    ,\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"0.25\",\n     \
    \ \"receiving_unit\": \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q5\",\n\
    \    \"claim\": \"Sodium D,L-Lactate receiving-medium concentration\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"40\",\n          \"unit\": \"\
    MILLIMOLAR\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"40\",\n          \"unit\": \"MILLIMOLAR\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Sodium D,L-Lactate;\
    \ line 9\",\n        \"exact_source_quote\": \"Sodium D,L-Lactate\\t40\\tmM\"\
    ,\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"40\",\n      \"\
    receiving_unit\": \"mM\"\n    }\n  },\n  {\n    \"decision_id\": \"q6\",\n   \
    \ \"claim\": \"Sodium pyruvate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Sodium pyruvate;\
    \ line 10\",\n        \"exact_source_quote\": \"Sodium pyruvate\\t1.1\\tg/L\"\
    ,\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"1.1\",\n      \"\
    receiving_unit\": \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q7\",\n  \
    \  \"claim\": \"Sodium acetate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.8203\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.8203\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined direct ingredient Sodium acetate;\
    \ line 11\",\n        \"exact_source_quote\": \"Sodium acetate\\t0.8203\\tg/L\"\
    ,\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The stored receiving-medium value and\
    \ original unit match the exact direct source row. No attached claim evidence\
    \ exists in either layer; preserve the amount and add source support.\",\n   \
    \ \"source_stage\": \"direct\",\n    \"arithmetic_outside_quote\": {\n      \"\
    stock_divisor\": \"1\",\n      \"expected_receiving_value\": \"0.8203\",\n   \
    \   \"receiving_unit\": \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q8\"\
    ,\n    \"claim\": \"Magnesium Sulfate Heptahydrate receiving-medium concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.03\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Magnesium\
    \ Sulfate Heptahydrate; line 5\",\n        \"exact_source_quote\": \"Magnesium\
    \ Sulfate Heptahydrate\\t3\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 3 g/L\
    \ at 100X; its 1X receiving rate is 0.03 g/L. Both layers already store that receiving\
    \ rate. Preserve it and attach these scoped facts; do not multiply it back to\
    \ stock strength or infer a dispensing volume.\",\n    \"source_stage\": \"Wolfe's\
    \ mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.03\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"claim\": \"Nitrilotriacetic\
    \ acid receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.015\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.015\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Nitrilotriacetic\
    \ acid; line 6\",\n        \"exact_source_quote\": \"Nitrilotriacetic acid\\t1.5\\\
    tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 1.5 g/L\
    \ at 100X; its 1X receiving rate is 0.015 g/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.015\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"claim\": \"\
    Sodium Chloride receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Sodium Chloride;\
    \ line 7\",\n        \"exact_source_quote\": \"Sodium Chloride\\t1\\tg/L\",\n\
    \        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 1 g/L\
    \ at 100X; its 1X receiving rate is 0.01 g/L. Both layers already store that receiving\
    \ rate. Preserve it and attach these scoped facts; do not multiply it back to\
    \ stock strength or infer a dispensing volume.\",\n    \"source_stage\": \"Wolfe's\
    \ mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.01\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"claim\": \"\
    Manganese (II) sulfate monohydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Manganese\
    \ (II) sulfate monohydrate; line 8\",\n        \"exact_source_quote\": \"Manganese\
    \ (II) sulfate monohydrate\\t0.5\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.5 g/L\
    \ at 100X; its 1X receiving rate is 0.005 g/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.005\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"claim\": \"\
    Cobalt chloride hexahydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Cobalt chloride\
    \ hexahydrate; line 9\",\n        \"exact_source_quote\": \"Cobalt chloride hexahydrate\\\
    t0.1\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.1 g/L\
    \ at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"claim\": \"\
    Zinc sulfate heptahydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Zinc sulfate\
    \ heptahydrate; line 10\",\n        \"exact_source_quote\": \"Zinc sulfate heptahydrate\\\
    t0.1\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.1 g/L\
    \ at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"claim\": \"\
    Calcium Chloride Dihydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Calcium\
    \ Chloride Dihydrate; line 11\",\n        \"exact_source_quote\": \"Calcium Chloride\
    \ Dihydrate\\t0.1\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.1 g/L\
    \ at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"claim\": \"\
    Iron (II) sulfate heptahydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Iron (II)\
    \ sulfate heptahydrate; line 12\",\n        \"exact_source_quote\": \"Iron (II)\
    \ sulfate heptahydrate\\t0.1\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.1 g/L\
    \ at 100X; its 1X receiving rate is 0.001 g/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"claim\": \"\
    Nickel (II) chloride hexahydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.00025\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.00025\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Nickel (II)\
    \ chloride hexahydrate; line 13\",\n        \"exact_source_quote\": \"Nickel (II)\
    \ chloride hexahydrate\\t0.025\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.025\
    \ g/L at 100X; its 1X receiving rate is 0.00025 g/L. Both layers already store\
    \ that receiving rate. Preserve it and attach these scoped facts; do not multiply\
    \ it back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.00025\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"claim\": \"\
    Aluminum potassium sulfate dodecahydrate receiving-medium concentration\",\n \
    \   \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0002\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Aluminum\
    \ potassium sulfate dodecahydrate; line 14\",\n        \"exact_source_quote\"\
    : \"Aluminum potassium sulfate dodecahydrate\\t0.02\\tg/L\",\n        \"snapshot_sha256\"\
    : \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.02\
    \ g/L at 100X; its 1X receiving rate is 0.0002 g/L. Both layers already store\
    \ that receiving rate. Preserve it and attach these scoped facts; do not multiply\
    \ it back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.0002\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"claim\": \"\
    Copper (II) sulfate pentahydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[17].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Copper (II)\
    \ sulfate pentahydrate; line 15\",\n        \"exact_source_quote\": \"Copper (II)\
    \ sulfate pentahydrate\\t0.01\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.01\
    \ g/L at 100X; its 1X receiving rate is 0.0001 g/L. Both layers already store\
    \ that receiving rate. Preserve it and attach these scoped facts; do not multiply\
    \ it back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.0001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"claim\": \"\
    Boric Acid receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Boric Acid;\
    \ line 16\",\n        \"exact_source_quote\": \"Boric Acid\\t0.01\\tg/L\",\n \
    \       \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.01\
    \ g/L at 100X; its 1X receiving rate is 0.0001 g/L. Both layers already store\
    \ that receiving rate. Preserve it and attach these scoped facts; do not multiply\
    \ it back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.0001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"claim\": \"\
    Sodium Molybdate Dihydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[19].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Sodium Molybdate\
    \ Dihydrate; line 17\",\n        \"exact_source_quote\": \"Sodium Molybdate Dihydrate\\\
    t0.01\\tg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.01\
    \ g/L at 100X; its 1X receiving rate is 0.0001 g/L. Both layers already store\
    \ that receiving rate. Preserve it and attach these scoped facts; do not multiply\
    \ it back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.0001\",\n      \"receiving_unit\"\
    : \"g/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"claim\": \"\
    Sodium selenite pentahydrate receiving-medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"ingredients[20].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.003\",\n          \"unit\"\
    : \"MG_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n       \
    \ \"attached_matching_evidence\": false\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.003\",\n          \"unit\": \"MG_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_mixes\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock ingredient Sodium selenite\
    \ pentahydrate; line 18\",\n        \"exact_source_quote\": \"Sodium selenite\
    \ pentahydrate\\t0.3\\tmg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix stock strength; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's mineral\
    \ mix; line 12\",\n        \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.3 mg/L\
    \ at 100X; its 1X receiving rate is 0.003 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's mineral mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.003\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"claim\": \"\
    pyridoxine HCl receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"MG_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"MG_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient pyridoxine\
    \ HCl; line 42\",\n        \"exact_source_quote\": \"pyridoxine HCl\\t10\\tmg/L\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 10 mg/L\
    \ at 100X; its 1X receiving rate is 0.1 mg/L. Both layers already store that receiving\
    \ rate. Preserve it and attach these scoped facts; do not multiply it back to\
    \ stock strength or infer a dispensing volume.\",\n    \"source_stage\": \"Wolfe's\
    \ vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.1\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q23\",\n    \"claim\": \"\
    4-Aminobenzoic acid receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient 4-Aminobenzoic\
    \ acid; line 43\",\n        \"exact_source_quote\": \"4-Aminobenzoic acid\\t5\\\
    tmg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 5 mg/L\
    \ at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.05\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"claim\": \"\
    Lipoic acid receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient Lipoic acid;\
    \ line 44\",\n        \"exact_source_quote\": \"Lipoic acid\\t5\\tmg/L\",\n  \
    \      \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 5 mg/L\
    \ at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.05\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"claim\": \"\
    Nicotinic Acid receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient Nicotinic\
    \ Acid; line 45\",\n        \"exact_source_quote\": \"Nicotinic Acid\\t5\\tmg/L\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 5 mg/L\
    \ at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.05\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"claim\": \"\
    Riboflavin receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient Riboflavin;\
    \ line 46\",\n        \"exact_source_quote\": \"Riboflavin\\t5\\tmg/L\",\n   \
    \     \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 5 mg/L\
    \ at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.05\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"claim\": \"\
    thiamine HCl receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient thiamine\
    \ HCl; line 47\",\n        \"exact_source_quote\": \"thiamine HCl\\t5\\tmg/L\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 5 mg/L\
    \ at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.05\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"claim\": \"\
    calcium pantothenate receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient calcium\
    \ pantothenate; line 48\",\n        \"exact_source_quote\": \"calcium pantothenate\\\
    t5\\tmg/L\",\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 5 mg/L\
    \ at 100X; its 1X receiving rate is 0.05 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.05\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"claim\": \"\
    biotin receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient biotin;\
    \ line 49\",\n        \"exact_source_quote\": \"biotin\\t2\\tmg/L\",\n       \
    \ \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 2 mg/L\
    \ at 100X; its 1X receiving rate is 0.02 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.02\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q30\",\n    \"claim\": \"\
    Folic Acid receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"MG_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient Folic Acid;\
    \ line 50\",\n        \"exact_source_quote\": \"Folic Acid\\t2\\tmg/L\",\n   \
    \     \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 2 mg/L\
    \ at 100X; its 1X receiving rate is 0.02 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.02\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"claim\": \"\
    Cyanocobalamin receiving-medium concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"MG_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"MG_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock ingredient Cyanocobalamin;\
    \ line 51\",\n        \"exact_source_quote\": \"Cyanocobalamin\\t0.1\\tmg/L\"\
    ,\n        \"snapshot_sha256\": \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\
    \n      },\n      {\n        \"source_key\": \"feba_mixes\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix stock strength; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined receiving strength of Wolfe's vitamin\
    \ mix; line 13\",\n        \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\\
    tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact source stock contains 0.1 mg/L\
    \ at 100X; its 1X receiving rate is 0.001 mg/L. Both layers already store that\
    \ receiving rate. Preserve it and attach these scoped facts; do not multiply it\
    \ back to stock strength or infer a dispensing volume.\",\n    \"source_stage\"\
    : \"Wolfe's vitamin mix\",\n    \"arithmetic_outside_quote\": {\n      \"stock_divisor\"\
    : \"100\",\n      \"expected_receiving_value\": \"0.001\",\n      \"receiving_unit\"\
    : \"mg/L\"\n    }\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"claim\": \"\
    Wolfe's mineral mix source stock strength\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's mineral mix strength header; line 3\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The 100X source strength is context for the\
    \ already-correct expanded receiving composition. Add explicit derivation/stage\
    \ evidence if represented; this is not a claim that a normalized stock record\
    \ must be invented.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"claim\"\
    : \"Wolfe's mineral mix receiving strength\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined stock-use row; line 12\",\n     \
    \   \"exact_source_quote\": \"Wolfe's mineral mix\\t1\\tX\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The source uses this exact stock at 1X. Its\
    \ liquid aliquot, solvent quantity and dispensing procedure are not specified\
    \ by this row.\"\n  },\n  {\n    \"decision_id\": \"q34\",\n    \"claim\": \"\
    Wolfe's vitamin mix source stock strength\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    feba_mixes\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes\"\
    ,\n        \"source_locator\": \"Wolfe's vitamin mix strength header; line 40\"\
    ,\n        \"exact_source_quote\": \"X\\t100\",\n        \"snapshot_sha256\":\
    \ \"b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The 100X source strength is context for the\
    \ already-correct expanded receiving composition. Add explicit derivation/stage\
    \ evidence if represented; this is not a claim that a normalized stock record\
    \ must be invented.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"claim\"\
    : \"Wolfe's vitamin mix receiving strength\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\",\n        \"attached_matching_evidence\": false\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined stock-use row; line 13\",\n     \
    \   \"exact_source_quote\": \"Wolfe's vitamin mix\\t1\\tX\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The source uses this exact stock at 1X. Its\
    \ liquid aliquot, solvent quantity and dispensing procedure are not specified\
    \ by this row.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n    \"claim\": \"\
    Source-described pH target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n\
    \        \"field_path\": \"description\",\n        \"stored\": \"Defined media\
    \ for Dechlorosoma suillum PS, pH should be 7.2\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"attached_matching_evidence\": false\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"description\",\n        \"stored\": \"Defined media for Dechlorosoma suillum\
    \ PS, pH should be 7.2\",\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined Description; line 2\",\n        \"\
    exact_source_quote\": \"Description\\tDefined media for Dechlorosoma suillum PS,\
    \ pH should be 7.2\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The existing description already says\
    \ pH should be 7.2. This is a source target, not a measured pH, adjustment recipe\
    \ or growth result.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"claim\"\
    : \"Structured pH target\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"attached_matching_evidence\": false\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined Description; line 2\",\n        \"\
    exact_source_quote\": \"Description\\tDefined media for Dechlorosoma suillum PS,\
    \ pH should be 7.2\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"A structured pH target could retain the\
    \ source-described 7.2 with explicit evidence; preserve its descriptive rather\
    \ than measured status.\"\n  },\n  {\n    \"decision_id\": \"q38\",\n    \"claim\"\
    : \"Preparation, stock aliquots and sterilization parameters\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"not_quantified\",\n    \
    \    \"attached_matching_evidence\": false\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    not_quantified\",\n        \"attached_matching_evidence\": false\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"ALP_defined complete exact block\",\n       \
    \ \"exact_source_quote\": \"Media\\tALP_defined\\t\\nDescription\\tDefined media\
    \ for Dechlorosoma suillum PS, pH should be 7.2\\t\\nMinimal\\tTRUE\\t\\nControlled\
    \ vocabulary\\tConcentration\\tUnits\\nSodium phosphate monobasic monohydrate\\\
    t0.49\\tg/L\\nPotassium phosphate dibasic\\t0.97\\tg/L\\nPotassium Chloride\\\
    t0.1\\tg/L\\nAmmonium chloride\\t0.25\\tg/L\\nSodium D,L-Lactate\\t40\\tmM\\nSodium\
    \ pyruvate\\t1.1\\tg/L\\nSodium acetate\\t0.8203\\tg/L\\nWolfe's mineral mix\\\
    t1\\tX\\nWolfe's vitamin mix\\t1\\tX\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      }\n    ],\n    \"conclusion\": \"The exact metadata block provides composition,\
    \ stock strength and a pH target, but no water batch, stock aliquot, sterilization\
    \ temperature/time, atmosphere or incubation conditions. Do not infer these from\
    \ typical use or from another medium.\"\n  },\n  {\n    \"decision_id\": \"q39\"\
    ,\n    \"claim\": \"Sodium phosphate monobasic monohydrate source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"CAS: 10049-21-5;\
    \ MW: 137.99; Ontology enriched via CAS-RN lookup\",\n        \"decision\": \"\
    evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"CAS:\
    \ 10049-21-5; MW: 137.99; Ontology enriched via CAS-RN lookup\",\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium phosphate monobasic\
    \ monohydrate row\",\n        \"exact_source_quote\": \"Sodium phosphate monobasic\
    \ monohydrate\\t10049-21-5\\tSigma\\t\\t137.99\\tmonobasic sodium phosphate dihydrate\\\
    t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:114249\",\n      \"formula\": [\n        \"H2O.H2O4P.Na\"\
    \n      ],\n      \"mass\": [\n        \"137.991\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q40\",\n    \"claim\": \"Potassium phosphate dibasic source\
    \ molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n\
    \        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"CAS:\
    \ 7758-11-4; MW: 174.18\",\n        \"decision\": \"evidence_only\",\n       \
    \ \"attached_matching_evidence\": false\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[1].notes\",\n        \"stored\": \"CAS: 7758-11-4; MW: 174.18\"\
    ,\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Potassium phosphate dibasic\
    \ row\",\n        \"exact_source_quote\": \"Potassium phosphate dibasic\\t7758-11-4\\\
    tSigma\\tP3786\\t174.18\\tK2HPO4, dibasic anhydrous sodium phosphate\",\n    \
    \    \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:131527\",\n      \"formula\": [\n        \"HO4P.2K\"\
    \n      ],\n      \"mass\": [\n        \"174.174\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q41\",\n    \"claim\": \"Potassium Chloride source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7447-40-7; MW: 74.55\",\n  \
    \      \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7447-40-7; MW: 74.55\",\n  \
    \      \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Potassium Chloride row\"\
    ,\n        \"exact_source_quote\": \"Potassium Chloride\\t7447-40-7\\tSigma\\\
    tP3911\\t74.55\\tKCl\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:32588\",\n      \"formula\": [\n        \"Cl.K\"\n\
    \      ],\n      \"mass\": [\n        \"74.551\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q42\",\n    \"claim\": \"Ammonium chloride source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 12125-02-9; MW: 53.49\",\n \
    \       \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 12125-02-9; MW: 53.49\",\n \
    \       \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Ammonium chloride row\",\n\
    \        \"exact_source_quote\": \"Ammonium chloride\\t12125-02-9\\tSigma\\tA9434\\\
    t53.49\\tNH4Cl\\t\\t\\tyes\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:31206\",\n      \"formula\": [\n        \"Cl.H4N\"\n\
    \      ],\n      \"mass\": [\n        \"53.492\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q43\",\n    \"claim\": \"Sodium D,L-Lactate source molecular-weight\
    \ metadata\",\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n      \
    \  \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 50-21-5; MW: 90.08\",\n        \"decision\": \"conflict\"\
    ,\n        \"attached_matching_evidence\": false\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[4].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 50-21-5; MW: 90.08\",\n        \"decision\": \"conflict\"\
    ,\n        \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium D,L-Lactate row\"\
    ,\n        \"exact_source_quote\": \"Sodium D,L-Lactate\\t50-21-5\\tSigma\\tL1375\\\
    t90.08\\tsodium lactate\\t\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The source itself combines a sodium D,L-lactate\
    \ name with CAS 50-21-5 and FW 90.08, while the asserted sodium L-lactate term\
    \ has formula C3H5O3.Na and mass 112.06. Preserve the source-internal form/metadata\
    \ conflict separately from the confirmed D,L-to-L narrowing. No mass conversion\
    \ or replacement ID is inferred.\",\n    \"ontology_metadata\": {\n      \"id\"\
    : \"CHEBI:232798\",\n      \"formula\": [\n        \"C3H5O3.Na\"\n      ],\n \
    \     \"mass\": [\n        \"112.06\"\n      ]\n    }\n  },\n  {\n    \"decision_id\"\
    : \"q44\",\n    \"claim\": \"Sodium pyruvate source molecular-weight metadata\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[5].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 113-24-6; MW: 110.04\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"attached_matching_evidence\": false\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[5].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 113-24-6; MW: 110.04\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium pyruvate row\",\n\
    \        \"exact_source_quote\": \"Sodium pyruvate\\t113-24-6\\tSigma\\tP2256\\\
    t110.04\\t\\t\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:50144\",\n      \"formula\": [\n        \"C3H3O3.Na\"\
    \n      ],\n      \"mass\": [\n        \"110.044\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q45\",\n    \"claim\": \"Sodium acetate source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 127-09-3; MW: 82.03\",\n   \
    \     \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 127-09-3; MW: 82.03\",\n   \
    \     \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium acetate row\",\n \
    \       \"exact_source_quote\": \"Sodium acetate\\t127-09-3\\tSigma\\tS28889-250G\\\
    t82.03\\tAcetic acid sodium salt\\t\\t\\t\\t\\t\\tyes\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this\
    \ FEBA compound row; retain its source and formula convention rather than using\
    \ rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n\
    \      \"id\": \"CHEBI:32954\",\n      \"formula\": [\n        \"C2H3O2.Na\"\n\
    \      ],\n      \"mass\": [\n        \"82.034\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q46\",\n    \"claim\": \"Magnesium Sulfate Heptahydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"CAS:\
    \ 10034-99-8; MW: 246.47; From Wolfe's mineral mix\",\n        \"decision\": \"\
    evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"CAS:\
    \ 10034-99-8; MW: 246.47; From Wolfe's mineral mix\",\n        \"decision\": \"\
    evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n   \
    \ ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Magnesium Sulfate Heptahydrate\
    \ row\",\n        \"exact_source_quote\": \"Magnesium Sulfate Heptahydrate\\t10034-99-8\\\
    tSigma\\tM1880\\t246.47\\tEpsom salts, MgSO4 7H2O\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this\
    \ FEBA compound row; retain its source and formula convention rather than using\
    \ rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n\
    \      \"id\": \"CHEBI:31795\",\n      \"formula\": [\n        \"7H2O.Mg.O4S\"\
    \n      ],\n      \"mass\": [\n        \"246.473\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q47\",\n    \"claim\": \"Nitrilotriacetic acid source\
    \ molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n\
    \        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 139-13-9; MW: 191.14; From Wolfe's\
    \ mineral mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 139-13-9; MW: 191.14; From Wolfe's\
    \ mineral mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Nitrilotriacetic acid row\"\
    ,\n        \"exact_source_quote\": \"Nitrilotriacetic acid\\t139-13-9\\tSigma\\\
    tN9877\\t191.14\\tN,N-Bis(carboxymethyl)glycine, NTA, Tris(carboxymethyl)amine\\\
    t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:44557\",\n      \"formula\": [\n        \"C6H9NO6\"\
    \n      ],\n      \"mass\": [\n        \"191.139\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q48\",\n    \"claim\": \"Sodium Chloride source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[9].notes\",\n        \"stored\": \"CAS: 7647-14-5;\
    \ MW: 58.44; From Wolfe's mineral mix\",\n        \"decision\": \"evidence_only\"\
    ,\n        \"attached_matching_evidence\": false\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[9].notes\",\n        \"stored\": \"CAS: 7647-14-5; MW: 58.44;\
    \ From Wolfe's mineral mix\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium Chloride row\",\n\
    \        \"exact_source_quote\": \"Sodium Chloride\\t7647-14-5\\tSigma\\tS3014\\\
    t58.44\\tNaCl\\t\\t\\tyes\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:26710\",\n      \"formula\": [\n        \"Cl.Na\"\n\
    \      ],\n      \"mass\": [\n        \"58.443\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q49\",\n    \"claim\": \"Manganese (II) sulfate monohydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].notes\",\n        \"stored\": \"\
    CAS: 10034-96-5; MW: 169.02; From Wolfe's mineral mix\",\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].notes\",\n        \"stored\": \"\
    CAS: 10034-96-5; MW: 169.02; From Wolfe's mineral mix\",\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Manganese (II) sulfate monohydrate\
    \ row\",\n        \"exact_source_quote\": \"Manganese (II) sulfate monohydrate\\\
    t10034-96-5\\tSigma\\tM7634\\t169.02\\tMnSO4 H2O\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this\
    \ FEBA compound row; retain its source and formula convention rather than using\
    \ rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n\
    \      \"id\": \"CHEBI:86364\",\n      \"formula\": [\n        \"H2O.Mn.O4S\"\n\
    \      ],\n      \"mass\": [\n        \"169.016\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q50\",\n    \"claim\": \"Cobalt chloride hexahydrate source\
    \ molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n\
    \        \"field_path\": \"ingredients[11].notes\",\n        \"stored\": \"CAS:\
    \ 7791-13-1; MW: 237.93; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].notes\",\n        \"stored\": \"\
    CAS: 7791-13-1; MW: 237.93; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Cobalt chloride hexahydrate\
    \ row\",\n        \"exact_source_quote\": \"Cobalt chloride hexahydrate\\t7791-13-1\\\
    tSigma\\t255599\\t237.93\\tCobaltous chloride hexahydrate, CoCl2, CoCl2 6H2O,\
    \ Cobalt Chloride\\t\\t\\tyes\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n      }\n\
    \    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this FEBA\
    \ compound row; retain its source and formula convention rather than using rounded\
    \ metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n      \"\
    id\": \"CHEBI:53503\",\n      \"formula\": [\n        \"2Cl.Co.6H2O\"\n      ],\n\
    \      \"mass\": [\n        \"237.929\"\n      ]\n    }\n  },\n  {\n    \"decision_id\"\
    : \"q51\",\n    \"claim\": \"Zinc sulfate heptahydrate source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[12].notes\",\n        \"stored\": \"CAS:\
    \ 7446-20-0; MW: 287.56; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].notes\",\n        \"stored\": \"\
    CAS: 7446-20-0; MW: 287.56; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Zinc sulfate heptahydrate\
    \ row\",\n        \"exact_source_quote\": \"Zinc sulfate heptahydrate\\t7446-20-0\\\
    tSigma\\tZ0251\\t287.56\\tzinc sulfate, ZnSO4 7H2O\\t\\t\\t\\t\\t\\tyes\",\n \
    \       \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:32312\",\n      \"formula\": [\n        \"7H2O.O4S.Zn\"\
    \n      ],\n      \"mass\": [\n        \"287.558\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q52\",\n    \"claim\": \"Iron (II) sulfate heptahydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].notes\",\n        \"stored\": \"\
    CAS: 7782-63-0; MW: 278.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].notes\",\n        \"stored\": \"\
    CAS: 7782-63-0; MW: 278.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Iron (II) sulfate heptahydrate\
    \ row\",\n        \"exact_source_quote\": \"Iron (II) sulfate heptahydrate\\t7782-63-0\\\
    tSigma\\tF2387\\t278.01\\tFerrous sulfate heptahydrate, FeSO4 7H2O, Iron sulfate\"\
    ,\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:75836\",\n      \"formula\": [\n        \"Fe.7H2O.O4S\"\
    \n      ],\n      \"mass\": [\n        \"278.013\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q53\",\n    \"claim\": \"Nickel (II) chloride hexahydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].notes\",\n        \"stored\": \"\
    CAS: 7791-20-0; MW: 237.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].notes\",\n        \"stored\": \"\
    CAS: 7791-20-0; MW: 237.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Nickel (II) chloride hexahydrate\
    \ row\",\n        \"exact_source_quote\": \"Nickel (II) chloride hexahydrate\\\
    t7791-20-0\\tSigma\\tN6136\\t237.69\\tNiCl2 6H2O\\t\\t\\tyes\\t\\t\\tyes\",\n\
    \        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:53542\",\n      \"formula\": [\n        \"2Cl.6H2O.Ni\"\
    \n      ],\n      \"mass\": [\n        \"237.689\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q54\",\n    \"claim\": \"Aluminum potassium sulfate dodecahydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].notes\",\n        \"stored\": \"\
    CAS: 7784-24-9; MW: 474.39; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].notes\",\n        \"stored\": \"\
    CAS: 7784-24-9; MW: 474.39; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Aluminum potassium sulfate\
    \ dodecahydrate row\",\n        \"exact_source_quote\": \"Aluminum potassium sulfate\
    \ dodecahydrate\\t7784-24-9\\tSigma\\tA7210\\t474.39\\tAlum, Potassium alum, Potassium\
    \ aluminum sulfate dodecahydrate, AlK(SO4)2 12H2O\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this\
    \ FEBA compound row; retain its source and formula convention rather than using\
    \ rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n\
    \      \"id\": \"CHEBI:86465\",\n      \"formula\": [\n        \"Al.12H2O.K.2O4S\"\
    \n      ],\n      \"mass\": [\n        \"474.386\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q55\",\n    \"claim\": \"Copper (II) sulfate pentahydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].notes\",\n        \"stored\": \"\
    CAS: 7758-99-8; MW: 249.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].notes\",\n        \"stored\": \"\
    CAS: 7758-99-8; MW: 249.69; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Copper (II) sulfate pentahydrate\
    \ row\",\n        \"exact_source_quote\": \"Copper (II) sulfate pentahydrate\\\
    t7758-99-8\\tSigma\\tC8027\\t249.69\\tBlue Vitriol, Cupric sulfate pentahydrate,\
    \ Sulfuric acid, copper(II) salt (1:1) pentahydrate, CuSO4 5H2O, Cupric Sulfate\"\
    ,\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:31440\",\n      \"formula\": [\n        \"Cu.5H2O.O4S\"\
    \n      ],\n      \"mass\": [\n        \"249.684\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q56\",\n    \"claim\": \"Boric Acid source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[18].notes\",\n        \"stored\": \"CAS:\
    \ 10043-35-3; MW: 61.83; From Wolfe's mineral mix\",\n        \"decision\": \"\
    evidence_only\",\n        \"attached_matching_evidence\": false\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].notes\",\n        \"stored\": \"\
    CAS: 10043-35-3; MW: 61.83; From Wolfe's mineral mix\",\n        \"decision\"\
    : \"evidence_only\",\n        \"attached_matching_evidence\": false\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Boric Acid row\",\n     \
    \   \"exact_source_quote\": \"Boric Acid\\t10043-35-3\\t\\t0084-01 (JT*)\\t61.83\\\
    tH3BO3\\t\\t\\tno\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:33118\",\n      \"formula\": [\n        \"H3BO3\"\n\
    \      ],\n      \"mass\": [\n        \"61.833\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q57\",\n    \"claim\": \"Sodium Molybdate Dihydrate source\
    \ molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n\
    \        \"field_path\": \"ingredients[19].notes\",\n        \"stored\": \"CAS:\
    \ 10102-40-6; MW: 241.95; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].notes\",\n        \"stored\": \"\
    CAS: 10102-40-6; MW: 241.95; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium Molybdate Dihydrate\
    \ row\",\n        \"exact_source_quote\": \"Sodium Molybdate Dihydrate\\t10102-40-6\\\
    tSigma\\t331058\\t241.95\\tNa2MoO4 2H2O, Na2MoO4-2H2O\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this\
    \ FEBA compound row; retain its source and formula convention rather than using\
    \ rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n\
    \      \"id\": \"CHEBI:75213\",\n      \"formula\": [\n        \"2H2O.MoO4.2Na\"\
    \n      ],\n      \"mass\": [\n        \"241.946\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q58\",\n    \"claim\": \"Sodium selenite pentahydrate\
    \ source molecular-weight metadata\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].notes\",\n        \"stored\": \"\
    CAS: 26970-82-1; MW: 263.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].notes\",\n        \"stored\": \"\
    CAS: 26970-82-1; MW: 263.01; From Wolfe's mineral mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Sodium selenite pentahydrate\
    \ row\",\n        \"exact_source_quote\": \"Sodium selenite pentahydrate\\t26970-82-1\\\
    tSigma\\t163\\t263.01\\tNa2SeO3\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n      }\n\
    \    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this FEBA\
    \ compound row; retain its source and formula convention rather than using rounded\
    \ metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n      \"\
    id\": \"CHEBI:131361\",\n      \"formula\": [\n        \"5H2O.2Na.O3Se\"\n   \
    \   ],\n      \"mass\": [\n        \"263.012\"\n      ]\n    }\n  },\n  {\n  \
    \  \"decision_id\": \"q59\",\n    \"claim\": \"4-Aminobenzoic acid source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[22].notes\",\n        \"stored\": \"CAS:\
    \ 150-13-0; MW: 137.14; From Wolfe's vitamin mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].notes\",\n        \"stored\": \"\
    CAS: 150-13-0; MW: 137.14; From Wolfe's vitamin mix; Ontology enriched via CAS-RN\
    \ lookup\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact 4-Aminobenzoic acid row\"\
    ,\n        \"exact_source_quote\": \"4-Aminobenzoic acid\\t150-13-0\\tSigma\\\
    tA9878\\t137.14\\tp-Aminobenzoic acid, para-aminobenzoic acid\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces this\
    \ FEBA compound row; retain its source and formula convention rather than using\
    \ rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\": {\n\
    \      \"id\": \"CHEBI:30753\",\n      \"formula\": [\n        \"C7H7NO2\"\n \
    \     ],\n      \"mass\": [\n        \"137.138\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q60\",\n    \"claim\": \"Lipoic acid source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[23].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 1077-28-7; MW: 206.33; From\
    \ Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\":\
    \ \"ingredients[23].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 1077-28-7; MW: 206.33; From Wolfe's vitamin mix\",\n\
    \        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Lipoic acid row\",\n    \
    \    \"exact_source_quote\": \"Lipoic acid\\t1077-28-7\\tSigma\\t\\t206.33\\tThioctic\
    \ acid, D,L-6,8-Thioctic Acid\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:16494\",\n      \"formula\": [\n        \"C8H14O2S2\"\
    \n      ],\n      \"mass\": [\n        \"206.332\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q61\",\n    \"claim\": \"Nicotinic Acid source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[24].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 59-67-6; MW: 123.11; From Wolfe's\
    \ vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].notes\",\n        \"stored\": \"\
    Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 59-67-6; MW: 123.11;\
    \ From Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Nicotinic Acid row\",\n \
    \       \"exact_source_quote\": \"Nicotinic Acid\\t59-67-6\\tSigma\\tN4126\\t123.11\"\
    ,\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:15940\",\n      \"formula\": [\n        \"C6H5NO2\"\
    \n      ],\n      \"mass\": [\n        \"123.111\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q62\",\n    \"claim\": \"Riboflavin source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[25].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 83-88-5; MW: 376.36; From Wolfe's\
    \ vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].notes\",\n        \"stored\": \"\
    Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 83-88-5; MW: 376.36;\
    \ From Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Riboflavin row\",\n     \
    \   \"exact_source_quote\": \"Riboflavin\\t83-88-5\\tSigma\\tR4500\\t376.36\"\
    ,\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:17015\",\n      \"formula\": [\n        \"C17H20N4O6\"\
    \n      ],\n      \"mass\": [\n        \"376.369\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q63\",\n    \"claim\": \"calcium pantothenate source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[27].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 137-08-6; MW: 238.27; From Wolfe's\
    \ vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].notes\",\n        \"stored\": \"\
    Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 137-08-6; MW: 238.27;\
    \ From Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact calcium pantothenate row\"\
    ,\n        \"exact_source_quote\": \"calcium pantothenate\\t137-08-6\\tSigma\\\
    tC8731\\t238.27\\t(R)-(+)-N-(2,4-Dihydroxy-3,3-dimethyl-1-oxobutyl)-_-alanine\
    \ hemicalcium salt, Calcium D-pantothenate, Vitamin B5, pantothenic acid, Pantothenic\
    \ acid dicalcium salt, Calcium D,L-pantothenate\\t\\t\\tno\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"conclusion\": \"The source FW 238.27 accompanies explicit hemicalcium-salt\
    \ wording; the captured ontology mass 476.536 uses a full 2C9H16NO5.Ca formula.\
    \ This half-formula convention is not evidence of a twofold recipe error. The\
    \ source also mixes D and D,L synonyms; no unsupported stereoisomer is selected.\"\
    ,\n    \"ontology_metadata\": {\n      \"id\": \"CHEBI:31345\",\n      \"formula\"\
    : [\n        \"2C9H16NO5.Ca\"\n      ],\n      \"mass\": [\n        \"476.536\"\
    \n      ]\n    }\n  },\n  {\n    \"decision_id\": \"q64\",\n    \"claim\": \"\
    biotin source molecular-weight metadata\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].notes\",\n        \"stored\": \"\
    Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 58-85-5; MW: 244.31;\
    \ From Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"attached_matching_evidence\": false\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/alp_defined.yaml\",\n        \"field_path\"\
    : \"ingredients[28].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 58-85-5; MW: 244.31; From Wolfe's vitamin mix\",\n\
    \        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact biotin row\",\n        \"\
    exact_source_quote\": \"biotin\\t58-85-5\\tSigma\\tB4501\\t244.31\\tD-Biotin,\
    \ Bios II, Biotin, Coenzyme R, Vitamin B7, Vitamin H\\t\\t\\tno\",\n        \"\
    snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:15956\",\n      \"formula\": [\n        \"C10H16N2O3S\"\
    \n      ],\n      \"mass\": [\n        \"244.316\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q65\",\n    \"claim\": \"Folic Acid source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[29].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 59-30-3; MW: 441.4; From Wolfe's\
    \ vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].notes\",\n        \"stored\": \"\
    Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 59-30-3; MW: 441.4; From\
    \ Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"\
    attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Folic Acid row\",\n     \
    \   \"exact_source_quote\": \"Folic Acid\\t59-30-3\\tSigma\\tF7876\\t441.4\",\n\
    \        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:27470\",\n      \"formula\": [\n        \"C19H19N7O6\"\
    \n      ],\n      \"mass\": [\n        \"441.404\"\n      ]\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q66\",\n    \"claim\": \"Cyanocobalamin source molecular-weight\
    \ metadata\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALP_defined.yaml\",\n  \
    \      \"field_path\": \"ingredients[30].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 68-19-9; MW: 1355.37; From Wolfe's\
    \ vitamin mix\",\n        \"decision\": \"evidence_only\",\n        \"attached_matching_evidence\"\
    : false\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/alp_defined.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].notes\",\n        \"stored\": \"\
    Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 68-19-9; MW: 1355.37;\
    \ From Wolfe's vitamin mix\",\n        \"decision\": \"evidence_only\",\n    \
    \    \"attached_matching_evidence\": false\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv exact Cyanocobalamin row\",\n \
    \       \"exact_source_quote\": \"Cyanocobalamin\\t68-19-9\\tSigma\\tC3607\\t1355.37\\\
    tVitamin B12, _-(5,6-Dimethylbenzimidazolyl)cyanocobamide, CN-Cbl, Cyanocob(III)alamin\"\
    ,\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"conclusion\": \"The local MW/CAS text exactly reproduces\
    \ this FEBA compound row; retain its source and formula convention rather than\
    \ using rounded metadata to change recipe amounts.\",\n    \"ontology_metadata\"\
    : {\n      \"id\": \"CHEBI:17439\",\n      \"formula\": [\n        \"C63H88CoN14O14P\"\
    \n      ],\n      \"mass\": [\n        \"1355.388\"\n      ]\n    }\n  }\n]"
- assessment_id: quantitative-scope
  area: quantity
  topic: Direct rates and explicit stock dilution
  outcome: supported
  summary: Every one of the 31 target concentrations and 31 owner concentrations matches
    the exact named FEBA block or its 100X-to-1X expansion, with units preserved.
    The 14 mineral and 10 vitamin rows are receiving concentrations, not an undiluted-stock
    flattening. Neither layer has attached quantity evidence. Source-only X strengths,
    pH and unspecified preparation parameters are individually inventoried.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - feba-identity
  - feba-stock-0
  - feba-stock-1
  - quantity-inventory
- assessment_id: chemical-forms
  area: grounding
  topic: Hydrates, stereochemistry, CAS and molecular-weight notes
  outcome: concern
  summary: The source explicitly names D,L-lactate, whereas CHEBI:232798 is sodium
    L-lactate. The source lactate dictionary also contains a sodium-name versus acid-scale
    CAS/FW tension. Calcium pantothenate hemicalcium wording explains the half-formula
    mass convention without a twofold dose correction. The source monobasic sodium-phosphate
    row has a contradictory dihydrate synonym despite its monohydrate name/CAS/formula,
    and its potassium-phosphate row contains a sodium synonym; these aliases are not
    alternative ingredient identities. Lipoic-acid source CAS 1077-28-7 is absent
    from the captured generic term cross-references, which does not prove an invalid
    ID or authorize a replacement. Explicit mineral hydrate forms and the other source-supported
    formula identities were compared individually.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - compound-metadata
  - form-metadata
  - chebi232798
  - chebi31345
  - chebi16494
  - chebi114249
  - chebi131527
- assessment_id: preparation
  area: completeness
  topic: Preparation scope and evidence placement
  outcome: concern
  summary: Current composition support is complete within the exact FEBA metadata
    scope. Preparation and experimental growth conditions are not supplied by that
    source; missing protocol values are not guessed. The existing descriptive pH is
    source-supported, but no claim-level evidence is attached to concentrations, pH
    or form decisions. Source references should distinguish current FEBA support from
    inaccessible historical CultureBotHT bytes.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - feba-identity
  - quantity-inventory
  - feba-version
  - culturebotht_public-attempt
- assessment_id: classification
  area: scope
  topic: Medium classification and growth-description boundary
  outcome: supported
  summary: DEFINED/DEFINED and LIQUID agree with the named components and the lack
    of agar in this exact recipe. The generic specialized category is a current importer
    fallback, not biological growth evidence. The description names a strain and a
    pH target; taxonomy supplies identity only. No experiment, temperature, gas regime
    or organism growth assertion is added.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - record
  - feba-identity
  - taxonomy-strain
  - taxonomy-species
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 11 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: flag-and-mapping-notes
  area: provenance
  topic: Mapping annotations and stale presence flag
  outcome: concern
  summary: All 31 ingredient rows in both layers now have primary term IDs, but has_unmapped_ingredients
    remains. The current importer definition checks slot presence, so this flag no
    longer describes that condition. Mapping confidence 0.90 is historical software
    metadata, not a calibrated scientific probability or MIM assertion; its original
    calculation is not recovered.
  target_ids:
  - CultureMech:015485
  evidence_ids:
  - record
  - form-metadata
  - history-metadata
findings:
- finding_id: f1
  issue_key: lactate-source-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: A D,L source ingredient is narrowed to sodium L-lactate
  description: The exact medium and compound rows name Sodium D,L-Lactate, while both
    local layers assert CHEBI:232798 sodium L-lactate. Canonical term-label validity
    does not establish that stereochemical substitution. The FEBA compound row also
    carries a sodium-name versus CAS/FW conflict; the local notes faithfully copy
    it, so it is not labeled a new local transcription error.
  target_ids:
  - CultureMech:015485
  field_paths:
  - ingredients
  - ingredients.term
  - ingredients.notes
  evidence_ids:
  - feba-identity
  - compound-metadata
  - form-metadata
  - chebi232798
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
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
  issue_key: source-evidence-provenance
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Current formulation evidence and historical import identity are not separated
  description: All current receiving concentrations match the exact FEBA formulation,
    yet both local layers lack attached claim evidence and cite only CultureBotHT.
    The public September FEBA commit cannot authenticate March import bytes. The pH
    description and X-strength derivations also need their exact source scope.
  target_ids:
  - CultureMech:015485
  field_paths:
  - ingredients.concentration
  - description
  - sources
  - curation_history
  evidence_ids:
  - feba-identity
  - feba-stock-0
  - feba-stock-1
  - feba-version
  - quantity-inventory
  - culturebotht_public-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
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
  issue_key: unmapped-flag-stale
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The retained unmapped-ingredient flag no longer matches slot presence
  description: Both local layers retain has_unmapped_ingredients even though all 31
    primary term slots are present and their labels resolve. This is distinct from
    the confirmed lactate form error, which a presence flag cannot describe.
  target_ids:
  - CultureMech:015485
  field_paths:
  - data_quality_flags
  evidence_ids:
  - record
  - form-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
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
  description: Resolve the exact supplied lactate form with source-specific evidence,
    retain the original 40 mM recipe claim, and correct or qualify unsupported stereochemical
    grounding and inconsistent metadata without inventing a replacement ID or mass
    conversion.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
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
  description: Attach current exact FEBA recipe and stock evidence to each supported
    claim; preserve the historical CultureBotHT assertion as unresolved unless its
    actual bytes become available. Keep source versions and times separate and document
    preparation limits.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
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
  description: Reassess the stale presence flag under the current flag contract, retaining
    a specific source-form concern and an append-only explanation of any authorized
    change.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015485
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/alp_defined.yaml
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
- The exact asserted CultureBotHT repository was not accessible through the captured
  public API request (HTTP 404). This does not prove that it never existed or that
  access would fail through every authorized route. March import identity and bytes
  remain unverified. Current FEBA quantities are independently supported; the partial
  limit is historical provenance, not missing current recipe rows.
- The captured supplier_l1375 public product request timed out. Product-specific identity
  was not recovered; no supplier form, stereoisomer, density or concentration is inferred.
  The exact FEBA row and ontology metadata remain separate evidence.
- The captured supplier_c8731 public product request timed out. Product-specific identity
  was not recovered; no supplier form, stereoisomer, density or concentration is inferred.
  The exact FEBA row and ontology metadata remain separate evidence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-024
- generated-medium
```
