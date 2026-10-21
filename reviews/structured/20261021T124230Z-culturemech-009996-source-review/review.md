# Source and formulation review: alicycliphilus_denitrificans_medium (CultureMech:009996)

- Review: 20261021T124230Z-culturemech-009996-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:39:17Z
- Finished UTC: 2026-10-21T12:42:30Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM594/TOGO M599 identity resolves, but three named stock IDs identify unrelated formulations. Both layers flatten source-stage masses and volume doses, misground two explicit hydrates, omit the specified preparation and variant boundaries, and leave the directly cited stock recipes unrepresented.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 201; batch 021 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty task batches contain 200 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 203 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009996 | data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml | generated | alicycliphilus_denitrificans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009996 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009996 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/201/strict.tsv |
| validate-terms | passed | True | CultureMech:009996 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009996 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009996 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009996.

The four documented recipes completed; interpret the scope of each separately.

### Exact main identity and stock reference boundaries

identity: concern. Targets: CultureMech:009996.

CultureMech:009996 is JCM594 via TOGO M599 and one exact maintained owner. Main identity resolves. The stored 5342/5343/5312 Solution A/B/C references instead point to unrelated formulations; source-specific provider IDs are4440/4441/4442. A generic stock name or valid accession does not prove this association.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:009996.

12 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 12/12 primary and 7/12 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 12: primary 100.00%; secondary 58.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009996.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Classification and organism scope

scope: concern. Targets: CultureMech:009996.

LIQUID fits the base source. COMPLEX/UNDEFINED warrants reassessment after the wrong stock references are corrected: the exact base and cited stocks list defined chemicals rather than yeast/extract mixtures introduced by the unrelated stock IDs. Bacterial organization and generic cultivation do not establish strain growth. The source-specific JCM14587 comment is retained as a separate formulation statement, without independently verified strain/taxon or generalized growth claim.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009996.

58 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "KH2PO4",
    "decision": "correct",
    "stage": "Base solution A batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.41",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.41",
      "solution": "A",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution A, exact ingredient row",
        "exact_source_quote": "KH 2 PO 4 0.41 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.41,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q2",
    "claim": "NaNO3",
    "decision": "correct",
    "stage": "Base solution A batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.85",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.85",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.85",
      "solution": "A",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution A, exact ingredient row",
        "exact_source_quote": "NaNO3 0.85 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"NaNO3\",\n          \"volume\": 0.85,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q3",
    "claim": "Na2HPO4・2H2O",
    "decision": "correct",
    "stage": "Base solution A batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.53",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.53",
      "solution": "A",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution A, exact ingredient row",
        "exact_source_quote": "Na 2 HPO 4 ·2H 2 O 0.53 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Na2HPO4・2H2O\",\n          \"volume\": 0.53,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q4",
    "claim": "Sodium acetate・3H2O",
    "decision": "correct",
    "stage": "Base solution A batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.136",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.136",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.136",
      "solution": "A",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution A, exact ingredient row",
        "exact_source_quote": "Sodium acetate·3H 2 O 0.136 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Sodium acetate・3H2O\",\n          \"volume\": 0.136,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q5",
    "claim": "CaCl2 x 2 H2O",
    "decision": "correct",
    "stage": "Base solution B batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.11",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.11",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.11",
      "solution": "B",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution B, exact ingredient row",
        "exact_source_quote": "CaCl 2 2H 2 O 0.11 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"CaCl22H2O\",\n          \"volume\": 0.11,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q6",
    "claim": "MgCl2・6H2O",
    "decision": "correct",
    "stage": "Base solution B batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.1",
      "solution": "B",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution B, exact ingredient row",
        "exact_source_quote": "MgCl 2 ·6H 2 O 0.1 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q7",
    "claim": "NaHCO3",
    "decision": "correct",
    "stage": "Base solution C batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3.73",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3.73",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "3.73",
      "solution": "C",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution C, exact ingredient row",
        "exact_source_quote": "NaHCO 3 3.73 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 3.73,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q8",
    "claim": "Na2SO4",
    "decision": "correct",
    "stage": "Base solution C batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.2",
      "solution": "C",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution C, exact ingredient row",
        "exact_source_quote": "Na 2 SO 4 0.2 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2SO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q9",
    "claim": "NH4HCO3",
    "decision": "correct",
    "stage": "Base solution C batch mass, before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.44",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.44",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "literal_mass_g": "0.44",
      "solution": "C",
      "basis": "original batch; no measured final-medium denominator"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution C, exact ingredient row",
        "exact_source_quote": "NH 4 HCO 3 0.44 g",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4HCO3\",\n          \"volume\": 0.44,\n          \"unit\": \"g\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The numerical source mass has been stored as G_PER_L in the flat medium. Restore its source-stage amount and basis; do not substitute provider stock-normalized g_l or infer that the water sum is a final one-litre denominator."
  },
  {
    "decision_id": "q10",
    "claim": "Carbon dioxide gas",
    "decision": "not_quantified",
    "stage": "Initial nitrogen atmosphere and later N2/CO2 gas phase",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": {
      "absolute_dose": null,
      "ratio_separate": true
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 preparation",
        "exact_source_quote": "Prepare all solutions and autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 post-combination gas replacement",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "VARIABLE correctly avoids an invented absolute amount; source gas ratio is a separate preparation claim. Neither total flow nor pressure is supplied."
  },
  {
    "decision_id": "q11",
    "claim": "N2",
    "decision": "not_quantified",
    "stage": "Initial nitrogen atmosphere and later N2/CO2 gas phase",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": {
      "absolute_dose": null,
      "ratio_separate": true
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 preparation",
        "exact_source_quote": "Prepare all solutions and autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 post-combination gas replacement",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "VARIABLE correctly avoids an invented absolute amount; source gas ratio is a separate preparation claim. Neither total flow nor pressure is supplied."
  },
  {
    "decision_id": "q12",
    "claim": "Water in solution 1",
    "decision": "correct",
    "stage": "Base source solution A",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 900,
      "unit": "mL",
      "basis": "listed water addition"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution A water row",
        "exact_source_quote": "Distilled water 900.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The single1000.0 G_PER_L aggregate is a sum of three volume inputs, not a mass concentration or a measured final volume. Preserve all three stages."
  },
  {
    "decision_id": "q13",
    "claim": "Water in solution 2",
    "decision": "correct",
    "stage": "Base source solution B",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 50,
      "unit": "mL",
      "basis": "listed water addition"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution B water row",
        "exact_source_quote": "Distilled water 50.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 50,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The single1000.0 G_PER_L aggregate is a sum of three volume inputs, not a mass concentration or a measured final volume. Preserve all three stages."
  },
  {
    "decision_id": "q14",
    "claim": "Water in solution 3",
    "decision": "correct",
    "stage": "Base source solution C",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 50,
      "unit": "mL",
      "basis": "listed water addition"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 Solution C water row",
        "exact_source_quote": "Distilled water 50.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 50,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "The single1000.0 G_PER_L aggregate is a sum of three volume inputs, not a mass concentration or a measured final volume. Preserve all three stages."
  },
  {
    "decision_id": "q15",
    "claim": "Solution A",
    "decision": "correct",
    "stage": "Base A; TOGO addition includes900mL water and three1mL stocks",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "903",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "903",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 903,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Solution A:",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 903,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q16",
    "claim": "Solution B",
    "decision": "correct",
    "stage": "Base B",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 50,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Solution B:",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 50,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q17",
    "claim": "Solution C",
    "decision": "correct",
    "stage": "Base C before later additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 50,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Solution C:",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Solution C\",\n          \"volume\": 50,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q18",
    "claim": "FeCl2 solution (see Medium [M180])",
    "decision": "correct",
    "stage": "FeCl2 stock addition into A",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "FeCl 2 solution (see Medium No. 187 ) 1.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q19",
    "claim": "Trace element solution (see Medium [M180])",
    "decision": "correct",
    "stage": "Trace-element stock addition into A",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Trace element solution (see Medium No. 187 ) 1.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q20",
    "claim": "Selenite--tungstate solution (see Medium [M431])",
    "decision": "correct",
    "stage": "Selenite/tungstate stock addition into A",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Selenite-tungstate solution (see Medium No. 431 ) 1.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q21",
    "claim": "1.0 M Sodium acetate solution",
    "decision": "correct",
    "stage": "Base post-combination acetate addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 10,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "1.0 M Sodium acetate solution 10.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"1.0 M Sodium acetate solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q22",
    "claim": "Vitamin solution (see Medium [M401])",
    "decision": "correct",
    "stage": "Base post-combination vitamin addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Vitamin solution* (see Medium No. 403 ) 1.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"Vitamin solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q23",
    "claim": "Thiamine solution (see Medium [M401])",
    "decision": "correct",
    "stage": "Base post-combination thiamine addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[8].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Thiamine solution* (see Medium No. 403 ) 1.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[4].items[2]",
        "exact_source_quote": "\"component_name\": \"Thiamine solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q24",
    "claim": "Vitamin B12 solution (see Medium [M401])",
    "decision": "correct",
    "stage": "Base post-combination B12 addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[9].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": {
      "value": 1,
      "unit": "mL",
      "basis": "source-specific addition, not g/L"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact section/addition row",
        "exact_source_quote": "Vitamin B 1 2 solution* (see Medium No. 403 ) 1.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      },
      {
        "source_key": "togoM599",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599",
        "source_locator": "$.components[4].items[3]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12 solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba"
      }
    ],
    "explanation": "Both local layers replace volume with G_PER_L. A/B/C require source-specific identities. Preserve primary timing; C50mL is the original component-stage water/TOGO addition, whereas provider C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither is proof of measured final volume."
  },
  {
    "decision_id": "q25",
    "claim": "Acetate stock strength",
    "decision": "evidence_only",
    "stage": "Base post-combination acetate stock, separate from receiving dose",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[6].preferred_term",
        "stored": "1.0 M Sodium acetate solution"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[6].preferred_term",
        "stored": "1.0 M Sodium acetate solution"
      }
    ],
    "source_amount": {
      "value": 1.0,
      "unit": "M"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 later-addition row",
        "exact_source_quote": "1.0 M Sodium acetate solution 10.0 ml",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "The strength is already named but lacks attached evidence and structured stage linkage; its ten-millilitre receiving dose is separate. No hydrate or density is assumed."
  },
  {
    "decision_id": "q26",
    "claim": "FeCl2 solution: HCl",
    "decision": "add",
    "stage": "Directly referenced FeCl2 solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 10,
      "primary_unit": "ml",
      "primary_literal_quantity": "25% HCl (7.7 M) 10.0 ml",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 2.5,
      "source_attribute": "7.7 M, 25%"
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact FeCl2 solution subsection; ingredient/solvent row",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[4].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"7.7 M, 25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q27",
    "claim": "FeCl2 solution: FeCl2 x 4 H2O",
    "decision": "add",
    "stage": "Directly referenced FeCl2 solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 1.5,
      "primary_unit": "g",
      "primary_literal_quantity": "FeCl 2 ·4H 2 O 1.5 g",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 1.5,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact FeCl2 solution subsection; ingredient/solvent row",
        "exact_source_quote": "FeCl 2 ·4H 2 O 1.5 g",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[4].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q28",
    "claim": "FeCl2 solution: Distilled water",
    "decision": "add",
    "stage": "Directly referenced FeCl2 solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 990,
      "primary_unit": "ml",
      "primary_literal_quantity": "Distilled water 990.0 ml",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": null,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact FeCl2 solution subsection; ingredient/solvent row",
        "exact_source_quote": "Distilled water 990.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[4].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q29",
    "claim": "Trace element solution: ZnCl2",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 70,
      "primary_unit": "mg",
      "primary_literal_quantity": "ZnCl 2 70.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.07,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "ZnCl 2 70.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q30",
    "claim": "Trace element solution: MnCl2 x 4 H2O",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 100,
      "primary_unit": "mg",
      "primary_literal_quantity": "MnCl 2 ·4H 2 O 100.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.1,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "MnCl 2 ·4H 2 O 100.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q31",
    "claim": "Trace element solution: H3BO3",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 6,
      "primary_unit": "mg",
      "primary_literal_quantity": "H 3 BO 3 6.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.006,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "H 3 BO 3 6.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q32",
    "claim": "Trace element solution: CoCl2 x 6 H2O",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 190,
      "primary_unit": "mg",
      "primary_literal_quantity": "CoCl 2 ·6H 2 O 190.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.19,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "CoCl 2 ·6H 2 O 190.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q33",
    "claim": "Trace element solution: CuCl2 x 2 H2O",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 2,
      "primary_unit": "mg",
      "primary_literal_quantity": "CuCl 2 ·2H 2 O 2.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.002,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "CuCl 2 ·2H 2 O 2.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q34",
    "claim": "Trace element solution: NiCl2 x 6 H2O",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 24,
      "primary_unit": "mg",
      "primary_literal_quantity": "NiCl 2 ·6H 2 O 24.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.024,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "NiCl 2 ·6H 2 O 24.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q35",
    "claim": "Trace element solution: Na2MoO4 x 2 H2O",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 36,
      "primary_unit": "mg",
      "primary_literal_quantity": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.036,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q36",
    "claim": "Trace element solution: Distilled water",
    "decision": "add",
    "stage": "Directly referenced Trace element solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 1.0,
      "primary_unit": "L",
      "primary_literal_quantity": "Distilled water 1.0 L",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": null,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "jcm187 exact Trace element solution subsection; ingredient/solvent row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[5].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q37",
    "claim": "Selenite-tungstate solution: NaOH",
    "decision": "add",
    "stage": "Directly referenced Selenite-tungstate solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 0.4,
      "primary_unit": "g",
      "primary_literal_quantity": "NaOH 0.4 g",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.4,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "jcm431 exact Selenite-tungstate solution subsection; ingredient/solvent row",
        "exact_source_quote": "NaOH 0.4 g",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[6].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 10.0007,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q38",
    "claim": "Selenite-tungstate solution: Na2SeO3 x 5 H2O",
    "decision": "add",
    "stage": "Directly referenced Selenite-tungstate solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 6,
      "primary_unit": "mg",
      "primary_literal_quantity": "Na 2 SeO 3 ·5H 2 O 6.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.006,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "jcm431 exact Selenite-tungstate solution subsection; ingredient/solvent row",
        "exact_source_quote": "Na 2 SeO 3 ·5H 2 O 6.0 mg",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[6].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0228125,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q39",
    "claim": "Selenite-tungstate solution: Na2WO4 x 2 H2O",
    "decision": "add",
    "stage": "Directly referenced Selenite-tungstate solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 8,
      "primary_unit": "mg",
      "primary_literal_quantity": "Na 2 WO 4 ·2H 2 O 8.0 mg",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": 0.008,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "jcm431 exact Selenite-tungstate solution subsection; ingredient/solvent row",
        "exact_source_quote": "Na 2 WO 4 ·2H 2 O 8.0 mg",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[6].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 8,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.008,\n                        \"mmol_l\": 0.0242534,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q40",
    "claim": "Selenite-tungstate solution: Distilled water",
    "decision": "add",
    "stage": "Directly referenced Selenite-tungstate solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[5].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 1.0,
      "primary_unit": "L",
      "primary_literal_quantity": "Distilled water 1.0 L",
      "provider_declared_stock_volume_ml": 1000,
      "provider_g_l_context_only": null,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "jcm431 exact Selenite-tungstate solution subsection; ingredient/solvent row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[6].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q41",
    "claim": "Vitamin solution: p-Aminobenzoic acid",
    "decision": "add",
    "stage": "Directly referenced Vitamin solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 4,
      "primary_unit": "mg",
      "primary_literal_quantity": "p -Aminobenzoic acid 4.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.04,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin solution subsection; ingredient/solvent row",
        "exact_source_quote": "p -Aminobenzoic acid 4.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[7].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\": 0.291673,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q42",
    "claim": "Vitamin solution: Biotin",
    "decision": "add",
    "stage": "Directly referenced Vitamin solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 1,
      "primary_unit": "mg",
      "primary_literal_quantity": "Biotin 1.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.01,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin solution subsection; ingredient/solvent row",
        "exact_source_quote": "Biotin 1.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[7].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0409316,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q43",
    "claim": "Vitamin solution: Nicotinic acid",
    "decision": "add",
    "stage": "Directly referenced Vitamin solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 10,
      "primary_unit": "mg",
      "primary_literal_quantity": "Nicotinic acid 10.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.1,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin solution subsection; ingredient/solvent row",
        "exact_source_quote": "Nicotinic acid 10.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[7].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.812282,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q44",
    "claim": "Vitamin solution: DL-Calcium pantothenate",
    "decision": "add",
    "stage": "Directly referenced Vitamin solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 5,
      "primary_unit": "mg",
      "primary_literal_quantity": "DL-Calcium pantothenate 5.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.05,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin solution subsection; ingredient/solvent row",
        "exact_source_quote": "DL-Calcium pantothenate 5.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[7].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"DL-Calcium pantothenate\",\n                        \"compound_id\": 1720,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.104932,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q45",
    "claim": "Vitamin solution: Pyridoxine hydrochloride",
    "decision": "add",
    "stage": "Directly referenced Vitamin solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 10,
      "primary_unit": "mg",
      "primary_literal_quantity": "Pyridoxine·HCl 10.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.1,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin solution subsection; ingredient/solvent row",
        "exact_source_quote": "Pyridoxine·HCl 10.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[7].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q46",
    "claim": "Vitamin solution: Sodium phosphate buffer",
    "decision": "add",
    "stage": "Directly referenced Vitamin solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[7].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 100,
      "primary_unit": "ml",
      "primary_literal_quantity": "Sodium phosphate buffer (10 mM, pH 7.1) 100.0 ml",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": null,
      "source_attribute": "10 mM, pH 7.1"
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin solution subsection; ingredient/solvent row",
        "exact_source_quote": "Sodium phosphate buffer (10 mM, pH 7.1) 100.0 ml",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[7].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Sodium phosphate buffer\",\n                        \"compound_id\": 1753,\n                        \"attribute\": \"10 mM, pH 7.1\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q47",
    "claim": "Thiamine solution: Thiamine HCl",
    "decision": "add",
    "stage": "Directly referenced Thiamine solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[8].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[8].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 10,
      "primary_unit": "mg",
      "primary_literal_quantity": "Thiamine·HCl 10.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.1,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Thiamine solution subsection; ingredient/solvent row",
        "exact_source_quote": "Thiamine·HCl 10.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[8].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q48",
    "claim": "Thiamine solution: Sodium phosphate buffer",
    "decision": "add",
    "stage": "Directly referenced Thiamine solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[8].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[8].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 100,
      "primary_unit": "ml",
      "primary_literal_quantity": "Sodium phosphate buffer (25 mM, pH 3.4) 100.0 ml",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": null,
      "source_attribute": "25 mM, pH 3.4"
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Thiamine solution subsection; ingredient/solvent row",
        "exact_source_quote": "Sodium phosphate buffer (25 mM, pH 3.4) 100.0 ml",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[8].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium phosphate buffer\",\n                        \"compound_id\": 1753,\n                        \"attribute\": \"25 mM, pH 3.4\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q49",
    "claim": "Vitamin B12 solution: Vitamin B12",
    "decision": "add",
    "stage": "Directly referenced Vitamin B12 solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[9].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[9].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 5,
      "primary_unit": "mg",
      "primary_literal_quantity": "Vitamin B 1 2 5.0 mg",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": 0.05,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin B12 solution subsection; ingredient/solvent row",
        "exact_source_quote": "Vitamin B 1 2 5.0 mg",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[9].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.0368895,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q50",
    "claim": "Vitamin B12 solution: Distilled water",
    "decision": "add",
    "stage": "Directly referenced Vitamin B12 solution composition only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "solutions[9].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "solutions[9].composition",
        "stored": []
      }
    ],
    "source_amount": {
      "primary_batch_amount": 100,
      "primary_unit": "ml",
      "primary_literal_quantity": "Distilled water 100.0 ml",
      "provider_declared_stock_volume_ml": 100,
      "provider_g_l_context_only": null,
      "source_attribute": null
    },
    "source_snippets": [
      {
        "source_key": "jcm403",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403",
        "source_locator": "jcm403 exact Vitamin B12 solution subsection; ingredient/solvent row",
        "exact_source_quote": "Distilled water 100.0 ml",
        "snapshot_sha256": "b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61",
        "parsed_text_sha256": "c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1"
      },
      {
        "source_key": "mediadiveJ594api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J594",
        "source_locator": "$.data.solutions[9].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c"
      }
    ],
    "explanation": "The target and owner retain an empty composition. Add or reference the exact scoped stock definition with original mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M separately and do not adopt provider2.5g/L as a justified conversion."
  },
  {
    "decision_id": "q51",
    "claim": "N2:CO2 gas ratio",
    "decision": "add",
    "stage": "Base after combining cooled A/B/C",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": {
      "ratio": "4:1",
      "basis": "v/v"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q52",
    "claim": "Final base pH",
    "decision": "add",
    "stage": "Base after later additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_amount": {
      "value": 7.3,
      "qualifier": "around"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "Check the final pH of the medium to be around 7.3.",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q53",
    "claim": "Autoclave temperature",
    "decision": "add",
    "stage": "JCM594 default unless overridden",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_amount": {
      "value": 121,
      "unit": "degree Celsius"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q54",
    "claim": "Autoclave duration",
    "decision": "add",
    "stage": "JCM594 default unless overridden",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_amount": {
      "value": 15,
      "unit": "min"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q55",
    "claim": "Variant nitrate replacement",
    "decision": "add",
    "stage": "JCM14587 chlorate/benzene branch, A only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "variants",
        "stored": null
      }
    ],
    "source_amount": {
      "mass_g": 1.06,
      "solution_A_ml": 900,
      "replaces": "NaNO3"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "replace NaNO 3 with 1.06 g NaClO 3 (in 900 ml solution A)",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q56",
    "claim": "Variant acetate dose and strength",
    "decision": "add",
    "stage": "JCM14587 branch after A/B/C combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "variants",
        "stored": null
      }
    ],
    "source_amount": {
      "dose_mL_per_L": 1.0,
      "stock_M": 1.0
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "1.0 ml/L of 1.0 M sodium acetate solution",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q57",
    "claim": "Variant benzene dose and strength",
    "decision": "add",
    "stage": "JCM14587 branch after A/B/C combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "variants",
        "stored": null
      }
    ],
    "source_amount": {
      "dose_mL_per_L": 25,
      "stock_mM": 20,
      "qualification": "water-saturated, autoclaved"
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "25 ml/L of 20 mM benzene (water-saturated, autoclaved)",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  },
  {
    "decision_id": "q58",
    "claim": "Variant vitamin dose",
    "decision": "add",
    "stage": "JCM14587 branch only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
        "field_path": "variants",
        "stored": null
      }
    ],
    "source_amount": {
      "dose_mL_per_L_each": 1,
      "separate_stocks": [
        "vitamin",
        "thiamine",
        "B12"
      ]
    },
    "source_snippets": [
      {
        "source_key": "jcm594",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594",
        "source_locator": "JCM594 exact preparation/default or Comment variant sentence",
        "exact_source_quote": "1 ml/L of each of vitamin solution (see Medium No. 403 , filter-sterilized), thiamine solution (see Medium No. 403 , filter-sterilized) and vitamin B 12 solution (see Medium No. 403 , filter-sterilized)",
        "snapshot_sha256": "eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca",
        "parsed_text_sha256": "684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836"
      }
    ],
    "explanation": "This source assertion is absent in both local layers. Preserve its stage and conditional branch. Do not promote the source strain mention to independently verified taxonomy or apply variant quantities to the base recipe."
  }
]

### Source support and nested dependency limits

evidence: concern. Targets: CultureMech:009996.

Main identity, source stages, all stored direct/stock-addition quantities and the six directly transferred stock recipes are supported by exact primary/provider comparisons. Neither local main layer has attached quantity evidence. Legacy MIM000926/001072 occur only on context parent records and are absent from the target and maintained owner. M401 DL-calcium pantothenate is within the transferred vitamin stock and is independently supported by JCM403/provider evidence; its parent legacy MIM000926 does not authenticate stock identity or proposed grounding. Current catalog/index misses do not establish historical validity or invalidity. Unrelated M180/M431 basal, sulfur and vitamin content is outside the transfer.

## Findings

### f1: Three generic stock names point to different formulations

blocker / open / confirmed; issue key: JCM594-wrong-stock-ids.

The asserted mediadive.solution5342/5343/5312 IDs resolve but their recipes are unrelated to JCM594 A/B/C. The correct source-specific provider identities are4440/4441/4442; source content, not label equality, establishes this distinction.

### f2: Batch masses and volume additions are flattened into g/L

major / open / confirmed; issue key: JCM594-stage-unit-collapse.

Both layers store nine source-stage masses as final-looking G_PER_L values, sum three water inputs as1000 G_PER_L, and encode ten stock additions as mass concentrations. A903mL and C63mL provider layouts differ in bookkeeping from the primary separate-stage instructions; no measured final volume is supplied.

### f3: Two explicitly named hydrates use anhydrous structures

major / open / confirmed; issue key: JCM594-hydrate-grounding.

Na2HPO4 dihydrate is assigned CHEBI34683 without hydrate water, and sodium acetate trihydrate is assigned CHEBI32954 without hydrate water. The primary explicitly names both hydrates. Existing canonical-label passes do not establish source-form correspondence.

### f4: Cited stocks and required preparation stages are missing

major / open / confirmed; issue key: JCM594-preparation-stock-context.

Six directly cited stock definitions remain empty, while the owner omits gas-phase change, source default sterilization, post-cooling sterile additions and final pH context. Parent-stock content outside the specifically cited subsections must not be transferred.

### f5: The explicitly separate chlorate/benzene branch is unrepresented

major / open / confirmed; issue key: JCM594-source-variant-omitted.

JCM594 specifies a JCM14587 modified branch with nitrate replacement and different acetate/benzene additions. Neither layer retains that conditional formulation. The base must not inherit variant quantities, and the source comment alone is not an independent taxonomy or broad growth assertion.

## Recommended Actions And Acceptance Checks

### a1

Correct the normalized owner stock associations only after exact source-stage verification; regenerate the target and prove all linked stock formulations and locators are source-specific.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent exact original mass and volume units at their own source stage, attach literal amount and denominator evidence, and preserve provider stage normalization separately. Do not infer a final1L denominator or overwrite C50mL with63mL without stage context.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve exact supplied hydrate terms from authoritative ontology metadata and source identity before altering maintained grounding. Preserve masses and do not compensate by silently converting to anhydrous-equivalent quantities.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain or reference each exact stock subsection with ingredient/solvent/strength/pH evidence, and preserve the primary preparation order including differentiated filtration versus autoclaving. Reassess classification from the corrected source formulation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve the source variant as a separate evidence-linked conditional formulation description; verify strain identity before adding any independently curated organism assertion, and keep base and variant quantitative inventories distinct.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch021/201/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/201/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml:1:id: CultureMech:009996<br>./data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml:1:id: CultureMech:009996<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch021/source-preflight-bound/201/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 77 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch021/source-preflight-bound/201/evidence-context-original.json; Complete frozen source context compared with fresh native input hashes | context_only | Every contextual input hash matches the fresh inspection at the same base. Preflight remains provisional provenance; this review supplies its own single-target judgment. |
| jcm594 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| togoM599 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| mediadiveJ594api | https://mediadive.dsmz.de/rest/medium/J594; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| jcm403 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| solution5342 | https://mediadive.dsmz.de/rest/solution/5342; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| solution5343 | https://mediadive.dsmz.de/rest/solution/5343; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| solution5312 | https://mediadive.dsmz.de/rest/solution/5312; Exact accession; whole main source or explicitly cited stock subsection only | supports | Main JCM594 and independent provider structure compared. Parent187 contributes only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three named vitamin stocks. Unrelated declared stock identities are comparison evidence only. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi184335 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_184335; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:184335 resolves to Ammonium bicarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32149 resolves to sodium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32954 resolves to sodium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63005; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63005 resolves to sodium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:184335": [{"label": "NH4HCO3", "match_type": "preferred_term", "identifier": "CHEBI:184335", "preferred_term": "NH4HCO3", "ontology_id": "CHEBI:184335", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63005": [{"label": "NaNO3", "match_type": "preferred_term", "identifier": "CHEBI:63005", "preferred_term": "NaNO3", "ontology_id": "CHEBI:63005", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch021/201/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read only and pinned in the inspection. Name-based references and historical cleanup notes do not prove chemical identity or current historical causation; source-specific stock IDs and stage-aware quantities must control follow-up. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read only and pinned in the inspection. Name-based references and historical cleanup notes do not prove chemical identity or current historical causation; source-specific stock IDs and stage-aware quantities must control follow-up. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current code was read only and pinned in the inspection. Name-based references and historical cleanup notes do not prove chemical identity or current historical causation; source-specific stock IDs and stage-aware quantities must control follow-up. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Parent dependency records are context for the exact cited stock sections and identity comparisons. Legacy MIM000926/001072 are absent from the reviewed target and maintained owner and do not authenticate stock identity or proposed grounding. M401 DL-calcium pantothenate belongs to the transferred vitamin recipe and is independently verified against JCM403/provider content; no historical legacy-key equivalence is inferred from a current index miss. Unrelated M180/M431 basal, sulfur, vitamin, gas and organism content does not transfer. Provider normalized stock g_l values do not prove final-medium concentrations.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124230Z-culturemech-009996-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alicycliphilus_denitrificans_medium (CultureMech:009996)'
started_at: '2026-10-21T12:39:17Z'
finished_at: '2026-10-21T12:42:30Z'
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
summary: JCM594/TOGO M599 identity resolves, but three named stock IDs identify unrelated
  formulations. Both layers flatten source-stage masses and volume doses, misground
  two explicit hydrates, omit the specified preparation and variant boundaries, and
  leave the directly cited stock recipes unrepresented.
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
  - path: data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
    sha256: 64f89ba44ad39c45e6cfe0ac66e7d7ab0f12cf12b357a08e9d6df92ed400fd73
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
    sha256: 44c6a48673b45ee13b3ce423ebf8ad7bcd0eea3b028568e3b4bd6216016e71da
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3846_FeCl2_solution.yaml
    sha256: b2e4c8ae5f0ec6756471724d2280bce9385e9928b686cc8e74f4ee7f946961b6
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3847_Trace_element_solution.yaml
    sha256: e5e1e4c877006ddb55ed1495e22dd88c4a1c352828d5b1d7c3ad4934c90f2cde
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4132_Vitamin_solution.yaml
    sha256: f5a7a0740201e8459bc35413469432990965fba495e6e5a8914a897796f28f69
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4133_Thiamine_solution.yaml
    sha256: a60a1fe269eb040835377b94c19c79971d6db3f57d4a1ae361cbe9dd1c2411d2
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4134_Vitamin_B12_solution_0_05_g_L.yaml
    sha256: 346ecedd035e71615b7947ab80bd8efa81fc0bbd79cdf4929e794d6cdb2ded80
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4172_Selenite-tungstate_solution.yaml
    sha256: 550d2d55fa756a0e4b44b5b8731dcb3629781e609fc153554bc2a06adf9d5bd9
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4440_Solution_A.yaml
    sha256: 92112a832669153f84639f20cb761239d4a93cfe0204a43f4faefda88bf9b62b
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4441_Solution_B.yaml
    sha256: 00e62ef932cd5f2dccc111c71049293b558b473da8f7602d838e72a347e5d97a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4442_Solution_C.yaml
    sha256: 9c95589e199cfbd570777f9369b28778e2f25e7c2e06faa1e605775f6950efdd
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5312_Solution_C.yaml
    sha256: b62be1d475240198979f708052c230a10a5d650e51572aef8af89354e9da54d6
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
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
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
    role: context
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
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
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
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
  selection: Task review 201; batch 021 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty task batches contain
    200 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 203 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009996
targets:
- target_id: CultureMech:009996
  path: data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  label: alicycliphilus_denitrificans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/201/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/201/strict.tsv"
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009996
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
  - CultureMech:009996
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:39:48.468601Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/201/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:39:50.233217Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/201/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:39:52.946268Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:39:54.260244Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:42:29Z'
  support: supports
  summary: './data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml:1:id:
    CultureMech:009996

    ./data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml:1:id:
    CultureMech:009996

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/source-preflight-bound/201/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:42:29Z'
  support: supports
  summary: 77 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: c3c98d0a211b4f7b971e1a5fbd72265b8f8645dfa3b5b28233287ee896b29af0
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/source-preflight-bound/201/evidence-context-original.json
  locator: Complete frozen source context compared with fresh native input hashes
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Every contextual input hash matches the fresh inspection at the same base.
    Preflight remains provisional provenance; this review supplies its own single-target
    judgment.
  snapshot_sha256: 9ab4cecf710e80e783fddbf7ab919c2b428e5cc28fad102469c14495dea6d623
- evidence_id: jcm594
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T12:23:19.286237Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca
- evidence_id: togoM599
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T12:23:17.826649Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: 48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba
- evidence_id: mediadiveJ594api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J594
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T12:23:16.981936Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: 7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm403
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T09:49:56.169277Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T12:23:19.260180Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: solution5342
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: 4bf262e02d0a83f9d1a24a52d2a14383aa8c6f27384e446d7da6274a05319240
- evidence_id: solution5343
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- evidence_id: solution5312
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5312
  locator: Exact accession; whole main source or explicitly cited stock subsection
    only
  accessed_at: '2026-10-21T10:35:27.466550Z'
  support: supports
  summary: Main JCM594 and independent provider structure compared. Parent187 contributes
    only FeCl2 and trace-element stocks;431 only selenite/tungstate;403 only the three
    named vitamin stocks. Unrelated declared stock identities are comparison evidence
    only.
  snapshot_sha256: 6766811e685137e51045e0a5a2c301954772fa34dd3ed711eb541ef862e480b9
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
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi184335
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_184335
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T12:23:18.805766Z'
  support: supports
  summary: CHEBI:184335 resolves to Ammonium bicarbonate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 827e022c826822b8d6f2492dc034a78afc6ba2cdc22f7dafa8b42d6c5ac2af27
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:42:29Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:184335": [{"label": "NH4HCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:184335", "preferred_term": "NH4HCO3", "ontology_id":
    "CHEBI:184335", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63005": [{"label":
    "NaNO3", "match_type": "preferred_term", "identifier": "CHEBI:63005", "preferred_term":
    "NaNO3", "ontology_id": "CHEBI:63005", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label":
    "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml",
    "events": 12, "timestamp_issues": []}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/201/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 03b8a1674dfe28ba2a52601b3af5e35bf075361c9d0f0faf9eba7a162bbcd4f5
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Current code was read only and pinned in the inspection. Name-based references
    and historical cleanup notes do not prove chemical identity or current historical
    causation; source-specific stock IDs and stage-aware quantities must control follow-up.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Current code was read only and pinned in the inspection. Name-based references
    and historical cleanup notes do not prove chemical identity or current historical
    causation; source-specific stock IDs and stage-aware quantities must control follow-up.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:42:29Z'
  support: context_only
  summary: Current code was read only and pinned in the inspection. Name-based references
    and historical cleanup notes do not prove chemical identity or current historical
    causation; source-specific stock IDs and stage-aware quantities must control follow-up.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact main identity and stock reference boundaries
  outcome: concern
  summary: CultureMech:009996 is JCM594 via TOGO M599 and one exact maintained owner.
    Main identity resolves. The stored 5342/5343/5312 Solution A/B/C references instead
    point to unrelated formulations; source-specific provider IDs are4440/4441/4442.
    A generic stock name or valid accession does not prove this association.
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - record
  - jcm594
  - togoM599
  - mediadiveJ594api
  - solution5342
  - solution5343
  - solution5312
  - owner-0
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '12 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 12/12 primary and 7/12 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi184335
  - chebi32139
  - chebi32149
  - chebi32954
  - chebi34683
  - chebi63005
  - chebi63036
  - chebi86158
  - chebi86345
  details: 'Instance coverage on a 0–100 percent scale, denominator 12: primary 100.00%;
    secondary 58.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: classification
  area: scope
  topic: Classification and organism scope
  outcome: concern
  summary: 'LIQUID fits the base source. COMPLEX/UNDEFINED warrants reassessment after
    the wrong stock references are corrected: the exact base and cited stocks list
    defined chemicals rather than yeast/extract mixtures introduced by the unrelated
    stock IDs. Bacterial organization and generic cultivation do not establish strain
    growth. The source-specific JCM14587 comment is retained as a separate formulation
    statement, without independently verified strain/taxon or generalized growth claim.'
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - record
  - jcm594
  - jcm187
  - jcm403
  - jcm431
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 58 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"KH2PO4\",\n   \
    \ \"decision\": \"correct\",\n    \"stage\": \"Base solution A batch mass, before\
    \ combination\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.41\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.41\"\
    ,\n      \"solution\": \"A\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution A, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"KH 2 PO 4 0.41 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.41,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n\
    \    \"claim\": \"NaNO3\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Base solution A batch mass, before combination\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.85\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.85\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.85\"\
    ,\n      \"solution\": \"A\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution A, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"NaNO3 0.85 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaNO3\\\",\\n          \\\"volume\\\": 0.85,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n\
    \    \"claim\": \"Na2HPO4・2H2O\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"Base solution A batch mass, before combination\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.53\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.53\"\
    ,\n      \"solution\": \"A\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution A, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Na 2 HPO 4 ·2H 2 O 0.53 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2HPO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.53,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\n      }\n\
    \    ],\n    \"explanation\": \"The numerical source mass has been stored as G_PER_L\
    \ in the flat medium. Restore its source-stage amount and basis; do not substitute\
    \ provider stock-normalized g_l or infer that the water sum is a final one-litre\
    \ denominator.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"claim\": \"Sodium\
    \ acetate・3H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Base solution\
    \ A batch mass, before combination\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.136\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.136\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"\
    0.136\",\n      \"solution\": \"A\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution A, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Sodium acetate·3H 2 O 0.136 g\",\n        \"\
    snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sodium acetate・3H2O\\\",\\n          \\\"volume\\\
    \": 0.136,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\n     \
    \ }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n\
    \    \"claim\": \"CaCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"Base solution B batch mass, before combination\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.11\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.11\"\
    ,\n      \"solution\": \"B\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution B, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"CaCl 2 2H 2 O 0.11 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl22H2O\\\",\\n          \\\"volume\\\": 0.11,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n\
    \    \"claim\": \"MgCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"Base solution B batch mass, before combination\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.1\"\
    ,\n      \"solution\": \"B\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution B, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"MgCl 2 ·6H 2 O 0.1 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n\
    \    \"claim\": \"NaHCO3\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Base solution C batch mass, before combination\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.73\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.73\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"3.73\"\
    ,\n      \"solution\": \"C\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution C, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"NaHCO 3 3.73 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 3.73,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n\
    \    \"claim\": \"Na2SO4\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Base solution C batch mass, before combination\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.2\"\
    ,\n      \"solution\": \"C\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution C, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"Na 2 SO 4 0.2 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n\
    \    \"claim\": \"NH4HCO3\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Base solution C batch mass, before combination\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.44\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.44\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": {\n      \"literal_mass_g\": \"0.44\"\
    ,\n      \"solution\": \"C\",\n      \"basis\": \"original batch; no measured\
    \ final-medium denominator\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution C, exact ingredient row\",\n\
    \        \"exact_source_quote\": \"NH 4 HCO 3 0.44 g\",\n        \"snapshot_sha256\"\
    : \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n    \
    \    \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4HCO3\\\",\\n          \\\"volume\\\": 0.44,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"The numerical source mass has been stored\
    \ as G_PER_L in the flat medium. Restore its source-stage amount and basis; do\
    \ not substitute provider stock-normalized g_l or infer that the water sum is\
    \ a final one-litre denominator.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n\
    \    \"claim\": \"Carbon dioxide gas\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"stage\": \"Initial nitrogen atmosphere and later N2/CO2 gas phase\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": {\n      \"absolute_dose\":\
    \ null,\n      \"ratio_separate\": true\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 preparation\",\n        \"exact_source_quote\"\
    : \"Prepare all solutions and autoclave under a N 2 atmosphere.\",\n        \"\
    snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"jcm594\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\",\n        \"source_locator\"\
    : \"JCM594 post-combination gas replacement\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"VARIABLE correctly avoids an invented\
    \ absolute amount; source gas ratio is a separate preparation claim. Neither total\
    \ flow nor pressure is supplied.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n\
    \    \"claim\": \"N2\",\n    \"decision\": \"not_quantified\",\n    \"stage\"\
    : \"Initial nitrogen atmosphere and later N2/CO2 gas phase\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": {\n      \"absolute_dose\":\
    \ null,\n      \"ratio_separate\": true\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 preparation\",\n        \"exact_source_quote\"\
    : \"Prepare all solutions and autoclave under a N 2 atmosphere.\",\n        \"\
    snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"jcm594\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\",\n        \"source_locator\"\
    : \"JCM594 post-combination gas replacement\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"VARIABLE correctly avoids an invented\
    \ absolute amount; source gas ratio is a separate preparation claim. Neither total\
    \ flow nor pressure is supplied.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n\
    \    \"claim\": \"Water in solution 1\",\n    \"decision\": \"correct\",\n   \
    \ \"stage\": \"Base source solution A\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": {\n      \"value\": 900,\n    \
    \  \"unit\": \"mL\",\n      \"basis\": \"listed water addition\"\n    },\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 Solution A water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 900.0 ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\n      }\n\
    \    ],\n    \"explanation\": \"The single1000.0 G_PER_L aggregate is a sum of\
    \ three volume inputs, not a mass concentration or a measured final volume. Preserve\
    \ all three stages.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"claim\"\
    : \"Water in solution 2\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Base source solution B\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": {\n      \"value\": 50,\n     \
    \ \"unit\": \"mL\",\n      \"basis\": \"listed water addition\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\",\n  \
    \      \"source_locator\": \"JCM594 Solution B water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 50.0 ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 50,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\n      }\n\
    \    ],\n    \"explanation\": \"The single1000.0 G_PER_L aggregate is a sum of\
    \ three volume inputs, not a mass concentration or a measured final volume. Preserve\
    \ all three stages.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"claim\"\
    : \"Water in solution 3\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Base source solution C\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": {\n      \"value\": 50,\n     \
    \ \"unit\": \"mL\",\n      \"basis\": \"listed water addition\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\",\n  \
    \      \"source_locator\": \"JCM594 Solution C water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 50.0 ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 50,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\n      }\n\
    \    ],\n    \"explanation\": \"The single1000.0 G_PER_L aggregate is a sum of\
    \ three volume inputs, not a mass concentration or a measured final volume. Preserve\
    \ all three stages.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"claim\"\
    : \"Solution A\",\n    \"decision\": \"correct\",\n    \"stage\": \"Base A; TOGO\
    \ addition includes900mL water and three1mL stocks\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"903\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"903\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 903,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Solution A:\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 903,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q16\"\
    ,\n    \"claim\": \"Solution B\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"Base B\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 50,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Solution B:\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 50,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q17\"\
    ,\n    \"claim\": \"Solution C\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"Base C before later additions\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 50,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Solution C:\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution C\\\",\\n          \\\"volume\\\": 50,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q18\"\
    ,\n    \"claim\": \"FeCl2 solution (see Medium [M180])\",\n    \"decision\": \"\
    correct\",\n    \"stage\": \"FeCl2 stock addition into A\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"FeCl 2 solution (see Medium No. 187 ) 1.0 ml\",\n\
    \        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2 solution (see Medium [M180])\\\",\\n   \
    \       \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q19\"\
    ,\n    \"claim\": \"Trace element solution (see Medium [M180])\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Trace-element stock addition into A\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Trace element solution (see Medium No. 187 ) 1.0\
    \ ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M180])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q20\"\
    ,\n    \"claim\": \"Selenite--tungstate solution (see Medium [M431])\",\n    \"\
    decision\": \"correct\",\n    \"stage\": \"Selenite/tungstate stock addition into\
    \ A\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Selenite-tungstate solution (see Medium No. 431 )\
    \ 1.0 ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Selenite--tungstate solution (see Medium [M431])\\\
    \",\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n \
    \       \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q21\"\
    ,\n    \"claim\": \"1.0 M Sodium acetate solution\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Base post-combination acetate addition\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 10,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"1.0 M Sodium acetate solution 10.0 ml\",\n      \
    \  \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1.0 M Sodium acetate solution\\\",\\n        \
    \  \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"\
    conc_value\\\": 1,\\n          \\\"conc_unit\\\": \\\"M\\\"\",\n        \"snapshot_sha256\"\
    : \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\n     \
    \ }\n    ],\n    \"explanation\": \"Both local layers replace volume with G_PER_L.\
    \ A/B/C require source-specific identities. Preserve primary timing; C50mL is\
    \ the original component-stage water/TOGO addition, whereas provider C63mL aggregates\
    \ the later10mL acetate and three1mL vitamin additions. Neither is proof of measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"claim\": \"\
    Vitamin solution (see Medium [M401])\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Base post-combination vitamin addition\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Vitamin solution* (see Medium No. 403 ) 1.0 ml\"\
    ,\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin solution (see Medium [M401])\\\",\\n \
    \         \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n       \
    \ \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q23\"\
    ,\n    \"claim\": \"Thiamine solution (see Medium [M401])\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Base post-combination thiamine addition\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Thiamine solution* (see Medium No. 403 ) 1.0 ml\"\
    ,\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[4].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine solution (see Medium [M401])\\\",\\n\
    \          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n      \
    \  \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q24\"\
    ,\n    \"claim\": \"Vitamin B12 solution (see Medium [M401])\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Base post-combination B12 addition\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"value\": 1,\n      \"unit\"\
    : \"mL\",\n      \"basis\": \"source-specific addition, not g/L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact section/addition row\",\n      \
    \  \"exact_source_quote\": \"Vitamin B 1 2 solution* (see Medium No. 403 ) 1.0\
    \ ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      },\n      {\n        \"source_key\": \"togoM599\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M599\",\n \
    \       \"source_locator\": \"$.components[4].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12 solution (see Medium [M401])\\\",\\\
    n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n      \
    \  \"snapshot_sha256\": \"48c99d733176708eeb5a908cfeb9f0fbb77577b52322799cb50f31c74bc5f7ba\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers replace volume with\
    \ G_PER_L. A/B/C require source-specific identities. Preserve primary timing;\
    \ C50mL is the original component-stage water/TOGO addition, whereas provider\
    \ C63mL aggregates the later10mL acetate and three1mL vitamin additions. Neither\
    \ is proof of measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q25\"\
    ,\n    \"claim\": \"Acetate stock strength\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Base post-combination acetate stock, separate from receiving\
    \ dose\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[6].preferred_term\",\n        \"stored\"\
    : \"1.0 M Sodium acetate solution\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[6].preferred_term\",\n        \"stored\"\
    : \"1.0 M Sodium acetate solution\"\n      }\n    ],\n    \"source_amount\": {\n\
    \      \"value\": 1.0,\n      \"unit\": \"M\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm594\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\",\n        \"source_locator\"\
    : \"JCM594 later-addition row\",\n        \"exact_source_quote\": \"1.0 M Sodium\
    \ acetate solution 10.0 ml\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"The strength is already named but lacks\
    \ attached evidence and structured stage linkage; its ten-millilitre receiving\
    \ dose is separate. No hydrate or density is assumed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q26\",\n    \"claim\": \"FeCl2 solution: HCl\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"Directly referenced FeCl2 solution composition only\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 10,\n      \"primary_unit\": \"ml\",\n      \"primary_literal_quantity\": \"\
    25% HCl (7.7 M) 10.0 ml\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 2.5,\n      \"source_attribute\": \"7.7\
    \ M, 25%\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact FeCl2 solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"25% HCl (7.7 M) 10.0 ml\",\n     \
    \   \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"7.7 M, 25%\\\",\\n           \
    \             \\\"amount\\\": 10,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"g_l\\\": 2.5,\\n                       \
    \ \\\"mmol_l\\\": 68.5683,\\n                        \\\"optional\\\": 0\\n  \
    \                  }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q27\",\n    \"claim\": \"FeCl2 solution: FeCl2 x\
    \ 4 H2O\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced FeCl2\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[3].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 1.5,\n      \"primary_unit\": \"g\",\n      \"primary_literal_quantity\": \"\
    FeCl 2 ·4H 2 O 1.5 g\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 1.5,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact FeCl2 solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"FeCl 2 ·4H 2 O 1.5 g\",\n        \"\
    snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"FeCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 260,\\n                        \\\"amount\\\": 1.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n\
    \                        \\\"mmol_l\\\": 7.54482,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q28\",\n    \"claim\": \"FeCl2 solution: Distilled water\",\n\
    \    \"decision\": \"add\",\n    \"stage\": \"Directly referenced FeCl2 solution\
    \ composition only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[3].composition\",\n        \"stored\": []\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 990,\n      \"primary_unit\": \"ml\",\n      \"primary_literal_quantity\": \"\
    Distilled water 990.0 ml\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": null,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact FeCl2 solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Distilled water 990.0 ml\",\n    \
    \    \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 990,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q29\",\n    \"claim\": \"Trace element solution:\
    \ ZnCl2\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Trace\
    \ element solution composition only\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 70,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    ZnCl 2 70.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n      \"\
    provider_g_l_context_only\": 0.07,\n      \"source_attribute\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"ZnCl 2 70.0 mg\"\
    ,\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"ZnCl2\\\",\\n                        \\\"compound_id\\\": 64,\\\
    n                        \\\"amount\\\": 70,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.07,\\n              \
    \          \\\"mmol_l\\\": 0.513573,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q30\",\n    \"claim\": \"Trace element solution:\
    \ MnCl2 x 4 H2O\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced\
    \ Trace element solution composition only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 100,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    MnCl 2 ·4H 2 O 100.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.1,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O\
    \ 100.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.505293,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q31\",\n    \"claim\": \"Trace element solution: H3BO3\",\n \
    \   \"decision\": \"add\",\n    \"stage\": \"Directly referenced Trace element\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[4].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 6,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    H 3 BO 3 6.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n     \
    \ \"provider_g_l_context_only\": 0.006,\n      \"source_attribute\": null\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"H 3 BO 3 6.0 mg\"\
    ,\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 6,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.006,\\n             \
    \           \\\"mmol_l\\\": 0.0970246,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q32\",\n    \"claim\": \"Trace element solution:\
    \ CoCl2 x 6 H2O\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced\
    \ Trace element solution composition only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 190,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    CoCl 2 ·6H 2 O 190.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.19,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"CoCl 2 ·6H 2 O\
    \ 190.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 190,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.19,\\\
    n                        \\\"mmol_l\\\": 1.46335,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q33\",\n    \"claim\": \"Trace element solution: CuCl2 x 2 H2O\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Trace element\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[4].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 2,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    CuCl 2 ·2H 2 O 2.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.002,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"CuCl 2 ·2H 2 O\
    \ 2.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n\
    \                        \\\"mmol_l\\\": 0.0117314,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n     \
    \ }\n    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q34\",\n    \"claim\": \"Trace element solution: NiCl2 x 6 H2O\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Trace element\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[4].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 24,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    NiCl 2 ·6H 2 O 24.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.024,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"NiCl 2 ·6H 2 O\
    \ 24.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 24,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.024,\\\
    n                        \\\"mmol_l\\\": 0.185187,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q35\",\n    \"claim\": \"Trace element solution: Na2MoO4 x 2\
    \ H2O\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Trace\
    \ element solution composition only\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 36,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Na 2 MoO 4 ·2H 2 O 36.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.036,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H\
    \ 2 O 36.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 36,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.036,\\n\
    \                        \\\"mmol_l\\\": 0.148791,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q36\",\n    \"claim\": \"Trace element solution: Distilled water\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Trace element\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[4].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 1.0,\n      \"primary_unit\": \"L\",\n      \"primary_literal_quantity\": \"\
    Distilled water 1.0 L\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": null,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"jcm187 exact Trace element solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Distilled water\
    \ 1.0 L\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q37\",\n    \"claim\": \"Selenite-tungstate solution:\
    \ NaOH\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Selenite-tungstate\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[5].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 0.4,\n      \"primary_unit\": \"g\",\n      \"primary_literal_quantity\": \"\
    NaOH 0.4 g\",\n      \"provider_declared_stock_volume_ml\": 1000,\n      \"provider_g_l_context_only\"\
    : 0.4,\n      \"source_attribute\": null\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"jcm431 exact Selenite-tungstate solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"NaOH 0.4 g\",\n\
    \        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaOH\\\",\\n                        \\\"compound_id\\\": 256,\\\
    n                        \\\"amount\\\": 0.4,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n                \
    \        \\\"mmol_l\\\": 10.0007,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q38\",\n    \"claim\": \"Selenite-tungstate solution:\
    \ Na2SeO3 x 5 H2O\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced\
    \ Selenite-tungstate solution composition only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 6,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Na 2 SeO 3 ·5H 2 O 6.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.006,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"jcm431 exact Selenite-tungstate solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Na 2 SeO 3 ·5H\
    \ 2 O 6.0 mg\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 107,\\n                        \\\"amount\\\": 6,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.006,\\\
    n                        \\\"mmol_l\\\": 0.0228125,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n     \
    \ }\n    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q39\",\n    \"claim\": \"Selenite-tungstate solution: Na2WO4\
    \ x 2 H2O\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced\
    \ Selenite-tungstate solution composition only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 8,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Na 2 WO 4 ·2H 2 O 8.0 mg\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": 0.008,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"jcm431 exact Selenite-tungstate solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Na 2 WO 4 ·2H 2\
    \ O 8.0 mg\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 8,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.008,\\\
    n                        \\\"mmol_l\\\": 0.0242534,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n     \
    \ }\n    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q40\",\n    \"claim\": \"Selenite-tungstate solution: Distilled\
    \ water\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Selenite-tungstate\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[5].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 1.0,\n      \"primary_unit\": \"L\",\n      \"primary_literal_quantity\": \"\
    Distilled water 1.0 L\",\n      \"provider_declared_stock_volume_ml\": 1000,\n\
    \      \"provider_g_l_context_only\": null,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm431\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"jcm431 exact Selenite-tungstate solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Distilled water\
    \ 1.0 L\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q41\",\n    \"claim\": \"Vitamin solution: p-Aminobenzoic\
    \ acid\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[7].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 4,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    p -Aminobenzoic acid 4.0 mg\",\n      \"provider_declared_stock_volume_ml\": 100,\n\
    \      \"provider_g_l_context_only\": 0.04,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"p -Aminobenzoic acid 4.0 mg\",\n \
    \       \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                        \\\"compound_id\\\
    \": 47,\\n                        \\\"amount\\\": 4,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.04,\\n \
    \                       \\\"mmol_l\\\": 0.291673,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q42\",\n    \"claim\": \"Vitamin solution: Biotin\",\n    \"\
    decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin solution composition\
    \ only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 1,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Biotin 1.0 mg\",\n      \"provider_declared_stock_volume_ml\": 100,\n      \"\
    provider_g_l_context_only\": 0.01,\n      \"source_attribute\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Biotin 1.0 mg\",\n        \"snapshot_sha256\"\
    : \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\",\n    \
    \    \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n              \
    \          \\\"mmol_l\\\": 0.0409316,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q43\",\n    \"claim\": \"Vitamin solution: Nicotinic\
    \ acid\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[7].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 10,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Nicotinic acid 10.0 mg\",\n      \"provider_declared_stock_volume_ml\": 100,\n\
    \      \"provider_g_l_context_only\": 0.1,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Nicotinic acid 10.0 mg\",\n      \
    \  \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"compound_id\\\
    \": 139,\\n                        \\\"amount\\\": 10,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.812282,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q44\",\n    \"claim\": \"Vitamin solution: DL-Calcium pantothenate\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin solution\
    \ composition only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[7].composition\",\n        \"stored\": []\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 5,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    DL-Calcium pantothenate 5.0 mg\",\n      \"provider_declared_stock_volume_ml\"\
    : 100,\n      \"provider_g_l_context_only\": 0.05,\n      \"source_attribute\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm403\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"DL-Calcium pantothenate 5.0 mg\",\n\
    \        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"DL-Calcium pantothenate\\\",\\n                        \\\"\
    compound_id\\\": 1720,\\n                        \\\"amount\\\": 5,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.05,\\n                        \\\"mmol_l\\\": 0.104932,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n     \
    \ }\n    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q45\",\n    \"claim\": \"Vitamin solution: Pyridoxine hydrochloride\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin solution\
    \ composition only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[7].composition\",\n        \"stored\": []\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 10,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Pyridoxine·HCl 10.0 mg\",\n      \"provider_declared_stock_volume_ml\": 100,\n\
    \      \"provider_g_l_context_only\": 0.1,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Pyridoxine·HCl 10.0 mg\",\n      \
    \  \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                        \\\"\
    compound_id\\\": 519,\\n                        \\\"amount\\\": 10,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q46\",\n    \"claim\": \"Vitamin solution: Sodium\
    \ phosphate buffer\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced\
    \ Vitamin solution composition only\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[7].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 100,\n      \"primary_unit\": \"ml\",\n      \"primary_literal_quantity\": \"\
    Sodium phosphate buffer (10 mM, pH 7.1) 100.0 ml\",\n      \"provider_declared_stock_volume_ml\"\
    : 100,\n      \"provider_g_l_context_only\": null,\n      \"source_attribute\"\
    : \"10 mM, pH 7.1\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm403\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Sodium phosphate buffer (10 mM, pH\
    \ 7.1) 100.0 ml\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[7].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Sodium phosphate buffer\\\",\\n                        \\\"\
    compound_id\\\": 1753,\\n                        \\\"attribute\\\": \\\"10 mM,\
    \ pH 7.1\\\",\\n                        \\\"amount\\\": 100,\\n              \
    \          \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q47\",\n    \"claim\": \"Thiamine solution: Thiamine\
    \ HCl\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Thiamine\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[8].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 10,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Thiamine·HCl 10.0 mg\",\n      \"provider_declared_stock_volume_ml\": 100,\n \
    \     \"provider_g_l_context_only\": 0.1,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Thiamine solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Thiamine·HCl 10.0 mg\",\n        \"\
    snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[8].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Thiamine HCl\\\",\\n                        \\\"compound_id\\\
    \": 1207,\\n                        \\\"amount\\\": 10,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q48\",\n    \"claim\": \"Thiamine solution: Sodium\
    \ phosphate buffer\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced\
    \ Thiamine solution composition only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[8].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 100,\n      \"primary_unit\": \"ml\",\n      \"primary_literal_quantity\": \"\
    Sodium phosphate buffer (25 mM, pH 3.4) 100.0 ml\",\n      \"provider_declared_stock_volume_ml\"\
    : 100,\n      \"provider_g_l_context_only\": null,\n      \"source_attribute\"\
    : \"25 mM, pH 3.4\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm403\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Thiamine solution subsection; ingredient/solvent\
    \ row\",\n        \"exact_source_quote\": \"Sodium phosphate buffer (25 mM, pH\
    \ 3.4) 100.0 ml\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[8].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Sodium phosphate buffer\\\",\\n                        \\\"\
    compound_id\\\": 1753,\\n                        \\\"attribute\\\": \\\"25 mM,\
    \ pH 3.4\\\",\\n                        \\\"amount\\\": 100,\\n              \
    \          \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q49\",\n    \"claim\": \"Vitamin B12 solution: Vitamin\
    \ B12\",\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin\
    \ B12 solution composition only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[9].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[9].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 5,\n      \"primary_unit\": \"mg\",\n      \"primary_literal_quantity\": \"\
    Vitamin B 1 2 5.0 mg\",\n      \"provider_declared_stock_volume_ml\": 100,\n \
    \     \"provider_g_l_context_only\": 0.05,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin B12 solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Vitamin B 1 2 5.0\
    \ mg\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\n \
    \                       \\\"mmol_l\\\": 0.0368895,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\n      }\n\
    \    ],\n    \"explanation\": \"The target and owner retain an empty composition.\
    \ Add or reference the exact scoped stock definition with original mass/volume\
    \ and supplied form. Provider g_l is stock-stage context, never final-medium concentration.\
    \ In the HCl row,25% has no explicit percentage basis; retain7.7M separately and\
    \ do not adopt provider2.5g/L as a justified conversion.\"\n  },\n  {\n    \"\
    decision_id\": \"q50\",\n    \"claim\": \"Vitamin B12 solution: Distilled water\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Directly referenced Vitamin B12\
    \ solution composition only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[9].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[9].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": {\n      \"primary_batch_amount\"\
    : 100,\n      \"primary_unit\": \"ml\",\n      \"primary_literal_quantity\": \"\
    Distilled water 100.0 ml\",\n      \"provider_declared_stock_volume_ml\": 100,\n\
    \      \"provider_g_l_context_only\": null,\n      \"source_attribute\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm403\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403\"\
    ,\n        \"source_locator\": \"jcm403 exact Vitamin B12 solution subsection;\
    \ ingredient/solvent row\",\n        \"exact_source_quote\": \"Distilled water\
    \ 100.0 ml\",\n        \"snapshot_sha256\": \"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61\"\
    ,\n        \"parsed_text_sha256\": \"c065cdb99c5fa0703169502db2b68dfda5127d9731695a0b1bd075e0869922a1\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ594api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J594\",\n        \"source_locator\"\
    : \"$.data.solutions[9].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 100,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7f04ef9cc50833c0aa7e60e5eff9d2c6e8afbef41c30daaf43e513aa647e489c\"\
    \n      }\n    ],\n    \"explanation\": \"The target and owner retain an empty\
    \ composition. Add or reference the exact scoped stock definition with original\
    \ mass/volume and supplied form. Provider g_l is stock-stage context, never final-medium\
    \ concentration. In the HCl row,25% has no explicit percentage basis; retain7.7M\
    \ separately and do not adopt provider2.5g/L as a justified conversion.\"\n  },\n\
    \  {\n    \"decision_id\": \"q51\",\n    \"claim\": \"N2:CO2 gas ratio\",\n  \
    \  \"decision\": \"add\",\n    \"stage\": \"Base after combining cooled A/B/C\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": {\n      \"ratio\": \"4:1\",\n      \"\
    basis\": \"v/v\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"N 2 -CO 2 (4:1, v/v) gas mixture\"\
    ,\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q52\",\n    \"claim\"\
    : \"Final base pH\",\n    \"decision\": \"add\",\n    \"stage\": \"Base after\
    \ later additions\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ph_value\",\n        \"stored\": null\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"value\": 7.3,\n      \"qualifier\"\
    : \"around\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"Check the final pH of the medium\
    \ to be around 7.3.\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q53\",\n    \"claim\"\
    : \"Autoclave temperature\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM594\
    \ default unless overridden\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"sterilization\",\n        \"stored\": null\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_amount\": {\n      \"value\": 121,\n      \"unit\"\
    : \"degree Celsius\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n        \"\
    parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q54\",\n    \"claim\"\
    : \"Autoclave duration\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM594\
    \ default unless overridden\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"sterilization\",\n        \"stored\": null\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_amount\": {\n      \"value\": 15,\n      \"unit\":\
    \ \"min\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize\
    \ media by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"\
    eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\",\n        \"\
    parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q55\",\n    \"claim\"\
    : \"Variant nitrate replacement\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"JCM14587 chlorate/benzene branch, A only\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"mass_g\": 1.06,\n      \"solution_A_ml\"\
    : 900,\n      \"replaces\": \"NaNO3\"\n    },\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"replace NaNO 3 with 1.06 g NaClO\
    \ 3 (in 900 ml solution A)\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"claim\"\
    : \"Variant acetate dose and strength\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"JCM14587 branch after A/B/C combination\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"dose_mL_per_L\": 1.0,\n      \"stock_M\"\
    : 1.0\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"1.0 ml/L of 1.0 M sodium acetate\
    \ solution\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q57\",\n    \"claim\"\
    : \"Variant benzene dose and strength\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"JCM14587 branch after A/B/C combination\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"dose_mL_per_L\": 25,\n      \"stock_mM\"\
    : 20,\n      \"qualification\": \"water-saturated, autoclaved\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm594\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\",\n  \
    \      \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"25 ml/L of 20 mM benzene (water-saturated,\
    \ autoclaved)\",\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  },\n  {\n    \"decision_id\": \"q58\",\n    \"claim\"\
    : \"Variant vitamin dose\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM14587\
    \ branch only\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALICYCLIPHILUS_DENITRIFICANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": {\n      \"dose_mL_per_L_each\": 1,\n      \"\
    separate_stocks\": [\n        \"vitamin\",\n        \"thiamine\",\n        \"\
    B12\"\n      ]\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm594\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=594\"\
    ,\n        \"source_locator\": \"JCM594 exact preparation/default or Comment variant\
    \ sentence\",\n        \"exact_source_quote\": \"1 ml/L of each of vitamin solution\
    \ (see Medium No. 403 , filter-sterilized), thiamine solution (see Medium No.\
    \ 403 , filter-sterilized) and vitamin B 12 solution (see Medium No. 403 , filter-sterilized)\"\
    ,\n        \"snapshot_sha256\": \"eb1c1122f50939f2d5344be667d7f85f0aeb2873101a023df7cdbcd23884c3ca\"\
    ,\n        \"parsed_text_sha256\": \"684dd8cbb2003f7767827ffa3e490d232509532e6ece1c0691f7425fad032836\"\
    \n      }\n    ],\n    \"explanation\": \"This source assertion is absent in both\
    \ local layers. Preserve its stage and conditional branch. Do not promote the\
    \ source strain mention to independently verified taxonomy or apply variant quantities\
    \ to the base recipe.\"\n  }\n]"
- assessment_id: evidence
  area: evidence
  topic: Source support and nested dependency limits
  outcome: concern
  summary: Main identity, source stages, all stored direct/stock-addition quantities
    and the six directly transferred stock recipes are supported by exact primary/provider
    comparisons. Neither local main layer has attached quantity evidence. Legacy MIM000926/001072
    occur only on context parent records and are absent from the target and maintained
    owner. M401 DL-calcium pantothenate is within the transferred vitamin stock and
    is independently supported by JCM403/provider evidence; its parent legacy MIM000926
    does not authenticate stock identity or proposed grounding. Current catalog/index
    misses do not establish historical validity or invalidity. Unrelated M180/M431
    basal, sulfur and vitamin content is outside the transfer.
  target_ids:
  - CultureMech:009996
  evidence_ids:
  - bound-context
  - quantity-inventory
  - jcm594
  - jcm187
  - jcm403
  - jcm431
findings:
- finding_id: f1
  issue_key: JCM594-wrong-stock-ids
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Three generic stock names point to different formulations
  description: The asserted mediadive.solution5342/5343/5312 IDs resolve but their
    recipes are unrelated to JCM594 A/B/C. The correct source-specific provider identities
    are4440/4441/4442; source content, not label equality, establishes this distinction.
  target_ids:
  - CultureMech:009996
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[2].term
  evidence_ids:
  - record
  - jcm594
  - mediadiveJ594api
  - solution5342
  - solution5343
  - solution5312
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  issue_key: JCM594-stage-unit-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Batch masses and volume additions are flattened into g/L
  description: Both layers store nine source-stage masses as final-looking G_PER_L
    values, sum three water inputs as1000 G_PER_L, and encode ten stock additions
    as mass concentrations. A903mL and C63mL provider layouts differ in bookkeeping
    from the primary separate-stage instructions; no measured final volume is supplied.
  target_ids:
  - CultureMech:009996
  field_paths:
  - ingredients[*].concentration
  - solutions[*].concentration
  evidence_ids:
  - quantity-inventory
  - jcm594
  - togoM599
  - mediadiveJ594api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  issue_key: JCM594-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two explicitly named hydrates use anhydrous structures
  description: Na2HPO4 dihydrate is assigned CHEBI34683 without hydrate water, and
    sodium acetate trihydrate is assigned CHEBI32954 without hydrate water. The primary
    explicitly names both hydrates. Existing canonical-label passes do not establish
    source-form correspondence.
  target_ids:
  - CultureMech:009996
  field_paths:
  - ingredients[5].term
  - ingredients[6].term
  evidence_ids:
  - record
  - jcm594
  - chebi34683
  - chebi32954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  issue_key: JCM594-preparation-stock-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Cited stocks and required preparation stages are missing
  description: Six directly cited stock definitions remain empty, while the owner
    omits gas-phase change, source default sterilization, post-cooling sterile additions
    and final pH context. Parent-stock content outside the specifically cited subsections
    must not be transferred.
  target_ids:
  - CultureMech:009996
  field_paths:
  - solutions[3:6].composition
  - solutions[7:10].composition
  - preparation_steps
  - sterilization
  - ph_value
  evidence_ids:
  - quantity-inventory
  - jcm594
  - jcm187
  - jcm403
  - jcm431
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  issue_key: JCM594-source-variant-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The explicitly separate chlorate/benzene branch is unrepresented
  description: JCM594 specifies a JCM14587 modified branch with nitrate replacement
    and different acetate/benzene additions. Neither layer retains that conditional
    formulation. The base must not inherit variant quantities, and the source comment
    alone is not an independent taxonomy or broad growth assertion.
  target_ids:
  - CultureMech:009996
  field_paths:
  - variants
  - notes
  evidence_ids:
  - jcm594
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  description: Correct the normalized owner stock associations only after exact source-stage
    verification; regenerate the target and prove all linked stock formulations and
    locators are source-specific.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009996
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  description: Represent exact original mass and volume units at their own source
    stage, attach literal amount and denominator evidence, and preserve provider stage
    normalization separately. Do not infer a final1L denominator or overwrite C50mL
    with63mL without stage context.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009996
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  description: Resolve exact supplied hydrate terms from authoritative ontology metadata
    and source identity before altering maintained grounding. Preserve masses and
    do not compensate by silently converting to anhydrous-equivalent quantities.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009996
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  description: Retain or reference each exact stock subsection with ingredient/solvent/strength/pH
    evidence, and preserve the primary preparation order including differentiated
    filtration versus autoclaving. Reassess classification from the corrected source
    formulation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009996
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
  description: Preserve the source variant as a separate evidence-linked conditional
    formulation description; verify strain identity before adding any independently
    curated organism assertion, and keep base and variant quantitative inventories
    distinct.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009996
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M599_Alicycliphilus_Denitrificans_Medium.yaml
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
- Parent dependency records are context for the exact cited stock sections and identity
  comparisons. Legacy MIM000926/001072 are absent from the reviewed target and maintained
  owner and do not authenticate stock identity or proposed grounding. M401 DL-calcium
  pantothenate belongs to the transferred vitamin recipe and is independently verified
  against JCM403/provider content; no historical legacy-key equivalence is inferred
  from a current index miss. Unrelated M180/M431 basal, sulfur, vitamin, gas and organism
  content does not transfer. Provider normalized stock g_l values do not prove final-medium
  concentrations.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-021
- generated-medium
```
