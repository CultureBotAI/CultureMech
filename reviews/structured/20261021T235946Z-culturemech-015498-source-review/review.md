# Source and formulation review: BHIS_PIPES (CultureMech:015498)

- Review: 20261021T235946Z-culturemech-015498-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:44:41Z
- Finished UTC: 2026-10-21T23:59:46Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact current FEBA BHIS_PIPES block supports eight printed g/L rates and 30 mM PIPES sesquisodium salt in both layers. None has attached claim-level quantity evidence. CHEBI:63055 instead denotes disodium PIPES, a confirmed supplied-form mismatch despite a correct canonical label. Original CultureBotHT authentication remains partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 419; batch 042 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-one task batches contain 410 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 413 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015498 | data/merge_yaml/merged/BHIS_PIPES.yaml | generated | BHIS_PIPES |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015498 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015498 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/419/strict.tsv |
| validate-terms | passed | True | CultureMech:015498 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015498 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015498 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: culturebothtRepository | unavailable | True | CultureMech:015498 | The exact CultureBotHT repository endpoint returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Its original formula bytes remain unavailable; the independently captured later FEBA revision supports current amounts but does not establish import-time equivalence. |
| Exact source content access: culturebothtExactBHIS_PIPES | unavailable | True | CultureMech:015498 | The exact named CultureBotHT media_yaml file returned HTTP 404 at 2026-10-21T23:23:21.603973+00:00. Its original formula bytes remain unavailable; the independently captured later FEBA revision supports current amounts but does not establish import-time equivalence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015498.

The four documented recipes completed; interpret the scope of each separately.

### Exact accession, contribution and variant boundary

identity: supported. Targets: CultureMech:015498.

The generated ID, source database_id and merged_from resolve to one exact maintained owner. Every ingredient and scientific field agrees between those two layers; only merge metadata and append-only merge history differ. Other BHIS products, agar formulations and glucose variants do not supply missing ingredients or conditions.

### Current source versus original imported bytes

provenance: unknown. Targets: CultureMech:015498.

Current FEBA and its compound catalogue are pinned to the named September revision. They provide direct present-day formula evidence; neither HTTP 404 response nor prior local review authenticates the March import. No historical raw digest or historical source equivalence is asserted.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015498.

33 per-layer and source-scope decisions cover all 18 concentration fields, all 14 ingredient-note fields and the explicitly unresolved preparation scope. All 18 numerical concentration matches are evidence_only because no matching attached concentration evidence exists. Chemical-form correspondence is evaluated separately.

[
  {
    "decision_id": "q1",
    "name": "Calf brains",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "7.7",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1463 in BHIS_PIPES",
        "exact_source_quote": "Calf brains\t7.7\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q2",
    "name": "Beef heart",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "9.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "9.8",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1464 in BHIS_PIPES",
        "exact_source_quote": "Beef heart\t9.8\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q3",
    "name": "Proteose Peptone",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1465 in BHIS_PIPES",
        "exact_source_quote": "Proteose Peptone\t10\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q4",
    "name": "Sodium Chloride",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1466 in BHIS_PIPES",
        "exact_source_quote": "Sodium Chloride\t5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q5",
    "name": "Disodium phosphate",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1467 in BHIS_PIPES",
        "exact_source_quote": "Disodium phosphate\t2.5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q6",
    "name": "L-Cysteine",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1468 in BHIS_PIPES",
        "exact_source_quote": "L-Cysteine\t1\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q7",
    "name": "Sodium bicarbonate",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1469 in BHIS_PIPES",
        "exact_source_quote": "Sodium bicarbonate\t2\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q8",
    "name": "Hemin",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1470 in BHIS_PIPES",
        "exact_source_quote": "Hemin\t0.005\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q9",
    "name": "PIPES sesquisodium salt",
    "stage": "Direct named FEBA formulation; generated target",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "30",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "30",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1471 in BHIS_PIPES",
        "exact_source_quote": "PIPES sesquisodium salt\t30\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. The 30 mM rate belongs to the printed sesquisodium material; resolving the separate wrong disodium identifier is required before treating chemical identity as verified."
  },
  {
    "decision_id": "q10",
    "name": "Calf brains",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "7.7",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1463 in BHIS_PIPES",
        "exact_source_quote": "Calf brains\t7.7\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q11",
    "name": "Beef heart",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "9.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "9.8",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1464 in BHIS_PIPES",
        "exact_source_quote": "Beef heart\t9.8\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q12",
    "name": "Proteose Peptone",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1465 in BHIS_PIPES",
        "exact_source_quote": "Proteose Peptone\t10\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q13",
    "name": "Sodium Chloride",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1466 in BHIS_PIPES",
        "exact_source_quote": "Sodium Chloride\t5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q14",
    "name": "Disodium phosphate",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1467 in BHIS_PIPES",
        "exact_source_quote": "Disodium phosphate\t2.5\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q15",
    "name": "L-Cysteine",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1468 in BHIS_PIPES",
        "exact_source_quote": "L-Cysteine\t1\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q16",
    "name": "Sodium bicarbonate",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1469 in BHIS_PIPES",
        "exact_source_quote": "Sodium bicarbonate\t2\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q17",
    "name": "Hemin",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1470 in BHIS_PIPES",
        "exact_source_quote": "Hemin\t0.005\tg/L\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. This source row does not specify preparation volume or imply a tissue-equivalent raw-organ mass."
  },
  {
    "decision_id": "q18",
    "name": "PIPES sesquisodium salt",
    "stage": "Direct named FEBA formulation; maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "30",
          "unit": "MILLIMOLAR"
        }
      }
    ],
    "desired": {
      "value": "30",
      "unit": "MILLIMOLAR"
    },
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "media line 1471 in BHIS_PIPES",
        "exact_source_quote": "PIPES sesquisodium salt\t30\tmM\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "Printed value and unit match this existing concentration. Attach versioned claim-level evidence; no numerical change or stock dilution is justified. The 30 mM rate belongs to the printed sesquisodium material; resolving the separate wrong disodium identifier is required before treating chemical identity as verified."
  },
  {
    "decision_id": "q19",
    "name": "Proteose Peptone supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "CAS: 91079-38-8"
      }
    ],
    "desired": "CAS: 91079-38-8",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 568",
        "exact_source_quote": "Proteose Peptone\t91079-38-8\tSigma\t82450\t\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q20",
    "name": "Proteose Peptone supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "CAS: 91079-38-8"
      }
    ],
    "desired": "CAS: 91079-38-8",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 568",
        "exact_source_quote": "Proteose Peptone\t91079-38-8\tSigma\t82450\t\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q21",
    "name": "Sodium Chloride supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "CAS: 7647-14-5; MW: 58.44"
      }
    ],
    "desired": "CAS: 7647-14-5; MW: 58.44",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 375",
        "exact_source_quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q22",
    "name": "Sodium Chloride supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "CAS: 7647-14-5; MW: 58.44"
      }
    ],
    "desired": "CAS: 7647-14-5; MW: 58.44",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 375",
        "exact_source_quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q23",
    "name": "Disodium phosphate supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 171",
        "exact_source_quote": "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q24",
    "name": "Disodium phosphate supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 171",
        "exact_source_quote": "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q25",
    "name": "L-Cysteine supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 519",
        "exact_source_quote": "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic acid\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q26",
    "name": "L-Cysteine supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 519",
        "exact_source_quote": "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic acid\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q27",
    "name": "Sodium bicarbonate supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 369",
        "exact_source_quote": "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q28",
    "name": "Sodium bicarbonate supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 369",
        "exact_source_quote": "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q29",
    "name": "Hemin supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 520",
        "exact_source_quote": "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q30",
    "name": "Hemin supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94"
      }
    ],
    "desired": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 520",
        "exact_source_quote": "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. No new concentration is inferred from these metadata numbers."
  },
  {
    "decision_id": "q31",
    "name": "PIPES sesquisodium salt supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BHIS_PIPES.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "CAS: 100037-69-2; MW: 335.34"
      }
    ],
    "desired": "CAS: 100037-69-2; MW: 335.34",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 325",
        "exact_source_quote": "PIPES sesquisodium salt\t100037-69-2\tFisher\tBP304-500\t335.34\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. The retained sesquisodium metadata conflicts with its separate disodium term."
  },
  {
    "decision_id": "q32",
    "name": "PIPES sesquisodium salt supplier/mapping notes",
    "stage": "Material identity and metadata, not a medium dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "CAS: 100037-69-2; MW: 335.34"
      }
    ],
    "desired": "CAS: 100037-69-2; MW: 335.34",
    "source_snippets": [
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 325",
        "exact_source_quote": "PIPES sesquisodium salt\t100037-69-2\tFisher\tBP304-500\t335.34\t\t\t\t\t\t\t\t\n",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "CAS and any printed molecular/formula weight agree with the FEBA compound row. Retain source precision. A local mapping-confidence number or enrichment-method note is algorithm provenance, not a source measurement or identity proof. The retained sesquisodium metadata conflicts with its separate disodium term."
  },
  {
    "decision_id": "q33",
    "name": "Water, batch volume and preparation quantities",
    "stage": "Source completeness",
    "decision": "unsupported",
    "local_fields": [],
    "desired": null,
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "Complete media block lines 1459–1472",
        "exact_source_quote": "Media\tBHIS_PIPES\t\nDescription\tBrain heart infusion salt broth\t\nMinimal\tFALSE\t\nControlled vocabulary\tConcentration\tUnits\nCalf brains\t7.7\tg/L\nBeef heart\t9.8\tg/L\nProteose Peptone\t10\tg/L\nSodium Chloride\t5\tg/L\nDisodium phosphate\t2.5\tg/L\nL-Cysteine\t1\tg/L\nSodium bicarbonate\t2\tg/L\nHemin\t0.005\tg/L\nPIPES sesquisodium salt\t30\tmM\n\t\t\n",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848",
        "quote_representation": "Exact source text; line endings normalized to LF, tabs and trailing fields preserved."
      }
    ],
    "interpretation": "This complete block supplies no water amount, final batch volume, pH, temperature, gas, sterilization cycle, stock concentration or dose. No default 1 L batch or preparation protocol is added; the printed per-litre rates alone do not establish these quantities."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:015498.

6 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 6/9 primary and 0/9 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 9: primary 66.67%; secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source material, salt form and ontology specificity

grounding: concern. Targets: CultureMech:015498.

Five asserted chemicals match their source names/CAS; PIPES sesquisodium instead carries a disodium identifier. Calf brains, beef heart and proteose peptone remain complex materials with no invented pure-chemical mapping. No secondary CHEBI-based or legacy MediaIngredientMech slot is asserted in either layer.

### Preparation, stock scope and growth context

completeness: unknown. Targets: CultureMech:015498.

The direct FEBA block supplies no stock recipes or preparation instructions. Empty pH, temperature, gas, preparation and growth fields remain explicit source limitations, rather than confirmed loss of a protocol or a basis to import another BHIS variant. Complex/undefined broth classification is consistent with these material names and Minimal FALSE. There is no asserted organism, empirical growth metric, KG match, publication claim or assembly to verify for this target.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015498.

7 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Earlier exact-identity review reports

provenance: supported. Targets: CultureMech:015498.

The two October concentration reports explicitly performed zero of nine source checks and recorded missing evidence. The September exact-record report is derivative context. Current FEBA comparison now supports numerical values, without rewriting those earlier reports or treating their source-access statements as current proof.

## Findings

### f1: Sesquisodium PIPES is linked to disodium PIPES

major / open / confirmed; issue key: culturemech.015498.pipes-salt-form.

Both layers name PIPES sesquisodium salt and retain source CAS 100037-69-2 and FW 335.34, but assert CHEBI:63055 / disodium PIPES. The exact OLS definition, two-sodium formula and mass 346.338 establish a supplied-form mismatch; canonical-label validity does not resolve it.

### f2: Supported numerical rates lack attached versioned quantity evidence

minor / open / confirmed; issue key: culturemech.015498.amount-evidence.

All nine direct ingredient rates match the exact current FEBA block in both layers, but neither layer carries attached concentration evidence. The generic CultureBotHT repository link cannot preserve the exact FEBA revision, row and supplied-material basis.

## Recommended Actions And Acceptance Checks

### a1

In the maintained owner, resolve the exact sesquisodium material and correct or remove the incompatible term using verified resolver evidence. Preserve the printed 30 mM dose, source CAS/FW and source accession; do not substitute disodium material or invent a replacement identifier. Regenerate only after owner correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Attach exact versioned FEBA row evidence to the maintained concentration fields, retaining printed units and material scope. Record the later FEBA date explicitly; do not call it the authenticated original import source. Preserve owner identity and regenerate only after authorized evidence curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BHIS_PIPES.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/bhis_pipes.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BHIS_PIPES.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BHIS_PIPES.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch042/419/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/419/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BHIS_PIPES.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BHIS_PIPES.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/bhis_pipes.yaml:1:id: CultureMech:015498<br>./data/merge_yaml/merged/BHIS_PIPES.yaml:1:id: CultureMech:015498<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch042/source-preflight-bound/419/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 15 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| feba-main | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; Exact named accession block, lines 1459–1472 | supports | Complete direct formulation block. Printed g/L and mM are concentration bases, not an experimentally measured final batch volume or stock-addition recipe. |
| feba-version | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b; Exact commit date and hash | supports | FEBA revision 803273865ea9e83fab770ec4f13670db80e1180b is dated 2026-09-10T16:27:42+00:00, after the March 2026 import. Current formula agreement cannot authenticate import-time bytes. |
| culturebothtRepository-attempt | https://api.github.com/repos/CultureBotAI/CultureBotHT; Preserved exact public retrieval result | context_only | The exact CultureBotHT repository endpoint returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Its original formula bytes remain unavailable; the independently captured later FEBA revision supports current amounts but does not establish import-time equivalence. |
| culturebothtExactBHIS_PIPES-attempt | https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS_PIPES.yaml; Preserved exact public retrieval result | context_only | The exact named CultureBotHT media_yaml file returned HTTP 404 at 2026-10-21T23:23:21.603973+00:00. Its original formula bytes remain unavailable; the independently captured later FEBA revision supports current amounts but does not establish import-time equivalence. |
| compound-0 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 569 | supports | Exact compound metadata for Calf brains. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-1 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 570 | supports | Exact compound metadata for Beef heart. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-2 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 568 | supports | Exact compound metadata for Proteose Peptone. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-3 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 375 | supports | Exact compound metadata for Sodium Chloride. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-4 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 171 | supports | Exact compound metadata for Disodium phosphate. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-5 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 519 | supports | Exact compound metadata for L-Cysteine. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-6 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 369 | supports | Exact compound metadata for Sodium bicarbonate. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-7 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 520 | supports | Exact compound metadata for Hemin. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| compound-8 | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Compounds.tsv line 325 | supports | Exact compound metadata for PIPES sesquisodium salt. CAS and formula weight concern this supplied material; catalogue numbers and mapping-confidence notes are not growth or concentration evidence. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch042/419/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| forms | /private/tmp/culturemech-review-work-batch042/419/chemical-form-inventory.json; All nine ingredient instances, exact compound rows and complete OLS scientific properties | context_only | Source-to-chemical-form assessment, including the three complex ungrounded materials and six asserted chemicals. |
| chebi17561 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17561 resolves to L-cysteine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50385 resolves to hemin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63055 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63055; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63055 resolves to disodium PIPES. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}} |
| history-metadata | data/merge_yaml/merged/BHIS_PIPES.yaml; data/normalized_yaml/specialized/bhis_pipes.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bhis_pipes.yaml", "events": 3, "timestamp_issues": []}] |
| writer-0 | scripts/import_from_culturebotht.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current importer, unit/history/preparation migration and formulation-preserving merge functions were read. They are current mechanisms only. The single maintained owner and target agree scientifically; no historical mapping execution or universal merger-loss causation is inferred. |
| writer-1 | scripts/migrate_legacy_fields.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current importer, unit/history/preparation migration and formulation-preserving merge functions were read. They are current mechanisms only. The single maintained owner and target agree scientifically; no historical mapping execution or universal merger-loss causation is inferred. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current importer, unit/history/preparation migration and formulation-preserving merge functions were read. They are current mechanisms only. The single maintained owner and target agree scientifically; no historical mapping execution or universal merger-loss causation is inferred. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Relevant current importer, unit/history/preparation migration and formulation-preserving merge functions were read. They are current mechanisms only. The single maintained owner and target agree scientifically; no historical mapping execution or universal merger-loss causation is inferred. |
| prior-report-0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis_pipes.md; Complete exact target/owner report, matched record path and CultureMech ID | context_only | Derivative local review read in full. Its earlier unavailable-source or amount-triage conclusions are historical context, not authenticated upstream raw bytes or a substitute for current source comparison. |
| prior-report-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS_PIPES.md; Complete exact target/owner report, matched record path and CultureMech ID | context_only | Derivative local review read in full. Its earlier unavailable-source or amount-triage conclusions are historical context, not authenticated upstream raw bytes or a substitute for current source comparison. |
| prior-report-2 | reports/yaml_record_review/20260921T213339Z-BHIS_PIPES.md; Complete exact target/owner report, matched record path and CultureMech ID | context_only | Derivative local review read in full. Its earlier unavailable-source or amount-triage conclusions are historical context, not authenticated upstream raw bytes or a substitute for current source comparison. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact CultureBotHT repository endpoint returned HTTP 404 at 2026-10-21T22:53:13.557900Z. Its original formula bytes remain unavailable; the independently captured later FEBA revision supports current amounts but does not establish import-time equivalence.
- The exact named CultureBotHT media_yaml file returned HTTP 404 at 2026-10-21T23:23:21.603973+00:00. Its original formula bytes remain unavailable; the independently captured later FEBA revision supports current amounts but does not establish import-time equivalence.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T235946Z-culturemech-015498-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: BHIS_PIPES (CultureMech:015498)'
started_at: '2026-10-21T23:44:41Z'
finished_at: '2026-10-21T23:59:46Z'
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
summary: The exact current FEBA BHIS_PIPES block supports eight printed g/L rates
  and 30 mM PIPES sesquisodium salt in both layers. None has attached claim-level
  quantity evidence. CHEBI:63055 instead denotes disodium PIPES, a confirmed supplied-form
  mismatch despite a correct canonical label. Original CultureBotHT authentication
  remains partial.
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
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 2bd19d90afa3d37315c69a45cccad8b4a8e30b6bca8e992a45d7ea0c9cadfb84
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
  - path: data/merge_yaml/merged/BHIS_PIPES.yaml
    sha256: fb1c7b325ba6c616cd157bea1956701d78b0953a83214715ecba48aedad63ae2
    role: target
  - path: data/normalized_yaml/specialized/bhis_pipes.yaml
    sha256: 4deaf07a800a6890ad7fb33a84982a9ec956516486444f278299079565e1f16c
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS_PIPES.md
    sha256: 10cc06abb0de8564bbec3ad9684683a310dfbad2a7455abcc331791ebe540394
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis_pipes.md
    sha256: 6247713620c1872e7533f93b23ef2374f53a574862a351953cfda72e077a6fba
    role: context
  - path: reports/yaml_record_review/20260921T213339Z-BHIS_PIPES.md
    sha256: 27a0d95ffd8e8419a44a5bb1627c2b11e67017086803b7b43e5abe8c1c83f26e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  selection: Task review 419; batch 042 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding forty-one task batches
    contain 410 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 413 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015498
targets:
- target_id: CultureMech:015498
  path: data/merge_yaml/merged/BHIS_PIPES.yaml
  label: BHIS_PIPES
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_pipes.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BHIS_PIPES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BHIS_PIPES.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch042/419/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/419/strict.tsv"
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BHIS_PIPES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BHIS_PIPES.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015498
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
  - CultureMech:015498
- check_id: culturebothtRepository-source-access
  name: 'Exact source content access: culturebothtRepository'
  required: true
  status: unavailable
  summary: The exact CultureBotHT repository endpoint returned HTTP 404 at 2026-10-21T22:53:13.557900Z.
    Its original formula bytes remain unavailable; the independently captured later
    FEBA revision supports current amounts but does not establish import-time equivalence.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - culturebothtRepository-attempt
- check_id: culturebothtExactBHIS_PIPES-source-access
  name: 'Exact source content access: culturebothtExactBHIS_PIPES'
  required: true
  status: unavailable
  summary: The exact named CultureBotHT media_yaml file returned HTTP 404 at 2026-10-21T23:23:21.603973+00:00.
    Its original formula bytes remain unavailable; the independently captured later
    FEBA revision supports current amounts but does not establish import-time equivalence.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - culturebothtExactBHIS_PIPES-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BHIS_PIPES.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/bhis_pipes.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BHIS_PIPES.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:23.107676Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BHIS_PIPES.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch042/419/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:24.107869Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/419/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BHIS_PIPES.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:25.185580Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHIS_PIPES.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:25.877854Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:49:22Z'
  support: supports
  summary: './data/normalized_yaml/specialized/bhis_pipes.yaml:1:id: CultureMech:015498

    ./data/merge_yaml/merged/BHIS_PIPES.yaml:1:id: CultureMech:015498

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/source-preflight-bound/419/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:49:22Z'
  support: supports
  summary: 15 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: dff759f55a60d8e15451b80fd44d1d7820116f1713b508ade8035c90e24a4c25
- evidence_id: feba-main
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: Exact named accession block, lines 1459–1472
  accessed_at: '2026-10-21T07:58:53.930003Z'
  support: supports
  summary: Complete direct formulation block. Printed g/L and mM are concentration
    bases, not an experimentally measured final batch volume or stock-addition recipe.
  quote: "Media\tBHIS_PIPES\t\r\nDescription\tBrain heart infusion salt broth\t\r\n\
    Minimal\tFALSE\t\r\nControlled vocabulary\tConcentration\tUnits\r\nCalf brains\t\
    7.7\tg/L\r\nBeef heart\t9.8\tg/L\r\nProteose Peptone\t10\tg/L\r\nSodium Chloride\t\
    5\tg/L\r\nDisodium phosphate\t2.5\tg/L\r\nL-Cysteine\t1\tg/L\r\nSodium bicarbonate\t\
    2\tg/L\r\nHemin\t0.005\tg/L\r\nPIPES sesquisodium salt\t30\tmM\r\n\t\t\r\n"
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: feba-version
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b
  locator: Exact commit date and hash
  accessed_at: '2026-10-21T07:59:41.378955Z'
  support: supports
  summary: FEBA revision 803273865ea9e83fab770ec4f13670db80e1180b is dated 2026-09-10T16:27:42+00:00,
    after the March 2026 import. Current formula agreement cannot authenticate import-time
    bytes.
  snapshot_sha256: 0a4998d61b96db10c549512e2fe06718e04b687e6bbc6b2c1ea121c3c11a53ca
- evidence_id: culturebothtRepository-attempt
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:53:13.557900Z'
  support: context_only
  summary: The exact CultureBotHT repository endpoint returned HTTP 404 at 2026-10-21T22:53:13.557900Z.
    Its original formula bytes remain unavailable; the independently captured later
    FEBA revision supports current amounts but does not establish import-time equivalence.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: culturebothtExactBHIS_PIPES-attempt
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS_PIPES.yaml
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T23:23:21.603973Z'
  support: context_only
  summary: The exact named CultureBotHT media_yaml file returned HTTP 404 at 2026-10-21T23:23:21.603973+00:00.
    Its original formula bytes remain unavailable; the independently captured later
    FEBA revision supports current amounts but does not establish import-time equivalence.
  snapshot_sha256: d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed
- evidence_id: compound-0
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 569
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Calf brains. CAS and formula weight concern
    this supplied material; catalogue numbers and mapping-confidence notes are not
    growth or concentration evidence.
  quote: "Calf brains\t\t\t\t\t\tUsed in BHIS_K3 media\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-1
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 570
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Beef heart. CAS and formula weight concern
    this supplied material; catalogue numbers and mapping-confidence notes are not
    growth or concentration evidence.
  quote: "Beef heart\t\t\t\t\t\tUsed in BHIS_K3 media\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-2
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 568
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Proteose Peptone. CAS and formula weight concern
    this supplied material; catalogue numbers and mapping-confidence notes are not
    growth or concentration evidence.
  quote: "Proteose Peptone\t91079-38-8\tSigma\t82450\t\t\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-3
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 375
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Sodium Chloride. CAS and formula weight concern
    this supplied material; catalogue numbers and mapping-confidence notes are not
    growth or concentration evidence.
  quote: "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t\
    \r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-4
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 171
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Disodium phosphate. CAS and formula weight
    concern this supplied material; catalogue numbers and mapping-confidence notes
    are not growth or concentration evidence.
  quote: "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic\t\
    \t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-5
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 519
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for L-Cysteine. CAS and formula weight concern
    this supplied material; catalogue numbers and mapping-confidence notes are not
    growth or concentration evidence.
  quote: "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic\
    \ acid\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-6
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 369
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Sodium bicarbonate. CAS and formula weight
    concern this supplied material; catalogue numbers and mapping-confidence notes
    are not growth or concentration evidence.
  quote: "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-7
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 520
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for Hemin. CAS and formula weight concern this
    supplied material; catalogue numbers and mapping-confidence notes are not growth
    or concentration evidence.
  quote: "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III),\
    \ Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,\
    \ Hemin(chloride)\t\t\t\t\t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: compound-8
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Compounds.tsv line 325
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: Exact compound metadata for PIPES sesquisodium salt. CAS and formula weight
    concern this supplied material; catalogue numbers and mapping-confidence notes
    are not growth or concentration evidence.
  quote: "PIPES sesquisodium salt\t100037-69-2\tFisher\tBP304-500\t335.34\t\t\t\t\t\
    \t\t\t\r\n"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/419/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 66e48d6eaa2330cd2e51559b3702b06a60c03997b8975b02cabbf37956c92523
- evidence_id: forms
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/419/chemical-form-inventory.json
  locator: All nine ingredient instances, exact compound rows and complete OLS scientific
    properties
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Source-to-chemical-form assessment, including the three complex ungrounded
    materials and six asserted chemicals.
  snapshot_sha256: 6fdad085da4fd8b5f345a2acb6cce98da1f02456a89f731ee44bad56e186b7e3
- evidence_id: chebi17561
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.213329Z'
  support: supports
  summary: CHEBI:17561 resolves to L-cysteine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea82f62413bdf5b5575ec20c8bd9e19bb3f41efb6f1efa500401656e6c186292
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
- evidence_id: chebi50385
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:40.648821Z'
  support: supports
  summary: CHEBI:50385 resolves to hemin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b989203634707b89526a8664c8fa65cb4976c4cdd791427218cf01b37d17356e
- evidence_id: chebi63055
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63055
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T23:23:21.914041Z'
  support: supports
  summary: CHEBI:63055 resolves to disodium PIPES. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 88c9111607c99ca4c9a180b5c6506a9bddd8eea7bdbb31f90745e8405b42901d
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T23:49:22Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BHIS_PIPES.yaml; data/normalized_yaml/specialized/bhis_pipes.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: '[{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bhis_pipes.yaml",
    "events": 3, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Relevant current importer, unit/history/preparation migration and formulation-preserving
    merge functions were read. They are current mechanisms only. The single maintained
    owner and target agree scientifically; no historical mapping execution or universal
    merger-loss causation is inferred.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_legacy_fields.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Relevant current importer, unit/history/preparation migration and formulation-preserving
    merge functions were read. They are current mechanisms only. The single maintained
    owner and target agree scientifically; no historical mapping execution or universal
    merger-loss causation is inferred.
  snapshot_sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Relevant current importer, unit/history/preparation migration and formulation-preserving
    merge functions were read. They are current mechanisms only. The single maintained
    owner and target agree scientifically; no historical mapping execution or universal
    merger-loss causation is inferred.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Relevant current importer, unit/history/preparation migration and formulation-preserving
    merge functions were read. They are current mechanisms only. The single maintained
    owner and target agree scientifically; no historical mapping execution or universal
    merger-loss causation is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: prior-report-0
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis_pipes.md
  locator: Complete exact target/owner report, matched record path and CultureMech
    ID
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Derivative local review read in full. Its earlier unavailable-source or
    amount-triage conclusions are historical context, not authenticated upstream raw
    bytes or a substitute for current source comparison.
  snapshot_sha256: 6247713620c1872e7533f93b23ef2374f53a574862a351953cfda72e077a6fba
- evidence_id: prior-report-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS_PIPES.md
  locator: Complete exact target/owner report, matched record path and CultureMech
    ID
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Derivative local review read in full. Its earlier unavailable-source or
    amount-triage conclusions are historical context, not authenticated upstream raw
    bytes or a substitute for current source comparison.
  snapshot_sha256: 10cc06abb0de8564bbec3ad9684683a310dfbad2a7455abcc331791ebe540394
- evidence_id: prior-report-2
  kind: record_content
  reference: reports/yaml_record_review/20260921T213339Z-BHIS_PIPES.md
  locator: Complete exact target/owner report, matched record path and CultureMech
    ID
  accessed_at: '2026-10-21T23:49:22Z'
  support: context_only
  summary: Derivative local review read in full. Its earlier unavailable-source or
    amount-triage conclusions are historical context, not authenticated upstream raw
    bytes or a substitute for current source comparison.
  snapshot_sha256: 27a0d95ffd8e8419a44a5bb1627c2b11e67017086803b7b43e5abe8c1c83f26e
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact accession, contribution and variant boundary
  outcome: supported
  summary: The generated ID, source database_id and merged_from resolve to one exact
    maintained owner. Every ingredient and scientific field agrees between those two
    layers; only merge metadata and append-only merge history differ. Other BHIS products,
    agar formulations and glucose variants do not supply missing ingredients or conditions.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - record
  - owner-0
  - id-search
  - feba-main
- assessment_id: source-version
  area: provenance
  topic: Current source versus original imported bytes
  outcome: unknown
  summary: Current FEBA and its compound catalogue are pinned to the named September
    revision. They provide direct present-day formula evidence; neither HTTP 404 response
    nor prior local review authenticates the March import. No historical raw digest
    or historical source equivalence is asserted.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - feba-main
  - feba-version
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 33 per-layer and source-scope decisions cover all 18 concentration fields,
    all 14 ingredient-note fields and the explicitly unresolved preparation scope.
    All 18 numerical concentration matches are evidence_only because no matching attached
    concentration evidence exists. Chemical-form correspondence is evaluated separately.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Calf brains\",\n\
    \    \"stage\": \"Direct named FEBA formulation; generated target\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.7\",\n          \"unit\": \"\
    G_PER_L\"\n        }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"\
    7.7\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1463 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Calf brains\\t7.7\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"name\": \"\
    Beef heart\",\n    \"stage\": \"Direct named FEBA formulation; generated target\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"9.8\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"value\": \"9.8\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\",\n\
    \        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1464 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Beef heart\\t9.8\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"name\": \"\
    Proteose Peptone\",\n    \"stage\": \"Direct named FEBA formulation; generated\
    \ target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    }\n    ],\n    \"desired\": {\n      \"value\": \"10\",\n      \"unit\":\
    \ \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1465 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Proteose Peptone\\t10\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\": \"\
    Sodium Chloride\",\n    \"stage\": \"Direct named FEBA formulation; generated\
    \ target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n    \
    \    \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   }\n    ],\n    \"desired\": {\n      \"value\": \"5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1466 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Sodium Chloride\\t5\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"name\": \"\
    Disodium phosphate\",\n    \"stage\": \"Direct named FEBA formulation; generated\
    \ target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     }\n    ],\n    \"desired\": {\n      \"value\": \"2.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1467 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Disodium phosphate\\t2.5\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"name\": \"\
    L-Cysteine\",\n    \"stage\": \"Direct named FEBA formulation; generated target\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\",\n\
    \        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1468 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"L-Cysteine\\t1\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"name\": \"\
    Sodium bicarbonate\",\n    \"stage\": \"Direct named FEBA formulation; generated\
    \ target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n    \
    \    \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   }\n    ],\n    \"desired\": {\n      \"value\": \"2\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1469 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Sodium bicarbonate\\t2\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\": \"\
    Hemin\",\n    \"stage\": \"Direct named FEBA formulation; generated target\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n  \
    \  \"desired\": {\n      \"value\": \"0.005\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1470 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Hemin\\t0.005\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"name\": \"\
    PIPES sesquisodium salt\",\n    \"stage\": \"Direct named FEBA formulation; generated\
    \ target\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n    \
    \    \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"30\",\n          \"unit\": \"MILLIMOLAR\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"30\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1471 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"PIPES sesquisodium salt\\t30\\tmM\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. The\
    \ 30 mM rate belongs to the printed sesquisodium material; resolving the separate\
    \ wrong disodium identifier is required before treating chemical identity as verified.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"name\": \"Calf brains\",\n \
    \   \"stage\": \"Direct named FEBA formulation; maintained owner\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/specialized/bhis_pipes.yaml\",\n        \"field_path\": \"\
    ingredients[0].concentration\",\n        \"stored\": {\n          \"value\": \"\
    7.7\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"desired\"\
    : {\n      \"value\": \"7.7\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1463 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Calf brains\\t7.7\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"name\": \"\
    Beef heart\",\n    \"stage\": \"Direct named FEBA formulation; maintained owner\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n    \
    \    \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"9.8\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     }\n    ],\n    \"desired\": {\n      \"value\": \"9.8\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1464 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Beef heart\\t9.8\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"name\": \"\
    Proteose Peptone\",\n    \"stage\": \"Direct named FEBA formulation; maintained\
    \ owner\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1465 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Proteose Peptone\\t10\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"name\": \"\
    Sodium Chloride\",\n    \"stage\": \"Direct named FEBA formulation; maintained\
    \ owner\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1466 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Sodium Chloride\\t5\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"name\": \"\
    Disodium phosphate\",\n    \"stage\": \"Direct named FEBA formulation; maintained\
    \ owner\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"2.5\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1467 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Disodium phosphate\\t2.5\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"name\": \"\
    L-Cysteine\",\n    \"stage\": \"Direct named FEBA formulation; maintained owner\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n    \
    \    \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   }\n    ],\n    \"desired\": {\n      \"value\": \"1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1468 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"L-Cysteine\\t1\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"name\": \"\
    Sodium bicarbonate\",\n    \"stage\": \"Direct named FEBA formulation; maintained\
    \ owner\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"2\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1469 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Sodium bicarbonate\\t2\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"name\": \"\
    Hemin\",\n    \"stage\": \"Direct named FEBA formulation; maintained owner\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n      \
    \  \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.005\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1470 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"Hemin\\t0.005\\tg/L\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. This\
    \ source row does not specify preparation volume or imply a tissue-equivalent\
    \ raw-organ mass.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"name\": \"\
    PIPES sesquisodium salt\",\n    \"stage\": \"Direct named FEBA formulation; maintained\
    \ owner\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"MILLIMOLAR\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"30\",\n      \"\
    unit\": \"MILLIMOLAR\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"media line 1471 in BHIS_PIPES\",\n        \"\
    exact_source_quote\": \"PIPES sesquisodium salt\\t30\\tmM\\n\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\",\n    \
    \    \"quote_representation\": \"Exact source text; line endings normalized to\
    \ LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"Printed value and unit match this existing concentration. Attach versioned\
    \ claim-level evidence; no numerical change or stock dilution is justified. The\
    \ 30 mM rate belongs to the printed sesquisodium material; resolving the separate\
    \ wrong disodium identifier is required before treating chemical identity as verified.\"\
    \n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"Proteose Peptone supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[2].notes\",\n        \"stored\": \"CAS: 91079-38-8\"\n      }\n\
    \    ],\n    \"desired\": \"CAS: 91079-38-8\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\":\
    \ \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 568\",\n        \"exact_source_quote\"\
    : \"Proteose Peptone\\t91079-38-8\\tSigma\\t82450\\t\\t\\t\\t\\t\\t\\t\\t\\t\\\
    n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q20\",\n    \"name\": \"Proteose Peptone supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"CAS: 91079-38-8\"\
    \n      }\n    ],\n    \"desired\": \"CAS: 91079-38-8\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 568\",\n        \"exact_source_quote\"\
    : \"Proteose Peptone\\t91079-38-8\\tSigma\\t82450\\t\\t\\t\\t\\t\\t\\t\\t\\t\\\
    n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q21\",\n    \"name\": \"Sodium Chloride supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[3].notes\",\n        \"stored\": \"CAS: 7647-14-5; MW: 58.44\"\
    \n      }\n    ],\n    \"desired\": \"CAS: 7647-14-5; MW: 58.44\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 375\",\n        \"exact_source_quote\"\
    : \"Sodium Chloride\\t7647-14-5\\tSigma\\tS3014\\t58.44\\tNaCl\\t\\t\\tyes\\t\\\
    t\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q22\",\n    \"name\": \"Sodium Chloride supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n    \
    \    \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"CAS: 7647-14-5;\
    \ MW: 58.44\"\n      }\n    ],\n    \"desired\": \"CAS: 7647-14-5; MW: 58.44\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 375\",\n        \"exact_source_quote\"\
    : \"Sodium Chloride\\t7647-14-5\\tSigma\\tS3014\\t58.44\\tNaCl\\t\\t\\tyes\\t\\\
    t\\tyes\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q23\",\n    \"name\": \"Disodium phosphate supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[4].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 7558-79-4; MW: 141.96\"\n      }\n    ],\n    \"desired\"\
    : \"Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 171\",\n        \"exact_source_quote\"\
    : \"Disodium phosphate\\t7558-79-4\\t\\t\\t141.96\\tNa2HPO4, Sodium phosphate\
    \ dibasic\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q24\",\n    \"name\": \"Disodium phosphate supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 7558-79-4; MW: 141.96\"\n  \
    \    }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 7558-79-4; MW: 141.96\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 171\",\n        \"exact_source_quote\"\
    : \"Disodium phosphate\\t7558-79-4\\t\\t\\t141.96\\tNa2HPO4, Sodium phosphate\
    \ dibasic\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q25\",\n    \"name\": \"L-Cysteine supplier/mapping notes\"\
    ,\n    \"stage\": \"Material identity and metadata, not a medium dose\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[5].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 52-90-4; MW: 121.16\"\n      }\n    ],\n    \"desired\"\
    : \"Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 519\",\n        \"exact_source_quote\"\
    : \"L-Cysteine\\t52-90-4\\tsigmaaldrich\\tW326305-100G\\t121.16\\t (R)-2-Amino-3-mercaptopropionic\
    \ acid\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q26\",\n    \"name\": \"L-Cysteine supplier/mapping notes\"\
    ,\n    \"stage\": \"Material identity and metadata, not a medium dose\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n        \"\
    field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 52-90-4; MW: 121.16\"\n      }\n    ],\n    \"desired\"\
    : \"Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 52-90-4; MW: 121.16\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 519\",\n        \"exact_source_quote\"\
    : \"L-Cysteine\\t52-90-4\\tsigmaaldrich\\tW326305-100G\\t121.16\\t (R)-2-Amino-3-mercaptopropionic\
    \ acid\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q27\",\n    \"name\": \"Sodium bicarbonate supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[6].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 144-55-8; MW: 84.007\"\n      }\n    ],\n    \"desired\"\
    : \"Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 369\",\n        \"exact_source_quote\"\
    : \"Sodium bicarbonate\\t144-55-8\\t\\t\\t84.007\\tNaHCO3\\t\\t\\tyes\\t\\t\\\
    t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q28\",\n    \"name\": \"Sodium bicarbonate supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n    \
    \    \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Mapping:\
    \ micromediaparam_legacy (confidence: 0.90); CAS: 144-55-8; MW: 84.007\"\n   \
    \   }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy (confidence:\
    \ 0.90); CAS: 144-55-8; MW: 84.007\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 369\",\n        \"exact_source_quote\"\
    : \"Sodium bicarbonate\\t144-55-8\\t\\t\\t84.007\\tNaHCO3\\t\\t\\tyes\\t\\t\\\
    t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q29\",\n    \"name\": \"Hemin supplier/mapping notes\",\n\
    \    \"stage\": \"Material identity and metadata, not a medium dose\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\": \"ingredients[7].notes\"\
    ,\n        \"stored\": \"Mapping: micromediaparam_legacy (confidence: 0.90); CAS:\
    \ 16009-13-5; MW: 651.94\"\n      }\n    ],\n    \"desired\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 16009-13-5; MW: 651.94\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 520\",\n        \"exact_source_quote\"\
    : \"Hemin\\t16009-13-5\\tsigmaaldrich\\tH9039-10G\\t651.94\\tChloro(protoporphyrinato)iron(III),\
    \ Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,\
    \ Hemin(chloride)\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n        \"\
    quote_representation\": \"Exact source text; line endings normalized to LF, tabs\
    \ and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\": \"\
    CAS and any printed molecular/formula weight agree with the FEBA compound row.\
    \ Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q30\",\n    \"name\": \"Hemin supplier/mapping notes\",\n\
    \    \"stage\": \"Material identity and metadata, not a medium dose\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/bhis_pipes.yaml\",\n        \"field_path\"\
    : \"ingredients[7].notes\",\n        \"stored\": \"Mapping: micromediaparam_legacy\
    \ (confidence: 0.90); CAS: 16009-13-5; MW: 651.94\"\n      }\n    ],\n    \"desired\"\
    : \"Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 520\",\n        \"exact_source_quote\"\
    : \"Hemin\\t16009-13-5\\tsigmaaldrich\\tH9039-10G\\t651.94\\tChloro(protoporphyrinato)iron(III),\
    \ Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,\
    \ Hemin(chloride)\\t\\t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"\
    25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\",\n        \"\
    quote_representation\": \"Exact source text; line endings normalized to LF, tabs\
    \ and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\": \"\
    CAS and any printed molecular/formula weight agree with the FEBA compound row.\
    \ Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. No\
    \ new concentration is inferred from these metadata numbers.\"\n  },\n  {\n  \
    \  \"decision_id\": \"q31\",\n    \"name\": \"PIPES sesquisodium salt supplier/mapping\
    \ notes\",\n    \"stage\": \"Material identity and metadata, not a medium dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BHIS_PIPES.yaml\",\n        \"field_path\"\
    : \"ingredients[8].notes\",\n        \"stored\": \"CAS: 100037-69-2; MW: 335.34\"\
    \n      }\n    ],\n    \"desired\": \"CAS: 100037-69-2; MW: 335.34\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"feba_compounds\",\n \
    \       \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 325\",\n        \"exact_source_quote\"\
    : \"PIPES sesquisodium salt\\t100037-69-2\\tFisher\\tBP304-500\\t335.34\\t\\t\\\
    t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. The\
    \ retained sesquisodium metadata conflicts with its separate disodium term.\"\n\
    \  },\n  {\n    \"decision_id\": \"q32\",\n    \"name\": \"PIPES sesquisodium\
    \ salt supplier/mapping notes\",\n    \"stage\": \"Material identity and metadata,\
    \ not a medium dose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_pipes.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"CAS:\
    \ 100037-69-2; MW: 335.34\"\n      }\n    ],\n    \"desired\": \"CAS: 100037-69-2;\
    \ MW: 335.34\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"feba_compounds\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 325\",\n        \"exact_source_quote\"\
    : \"PIPES sesquisodium salt\\t100037-69-2\\tFisher\\tBP304-500\\t335.34\\t\\t\\\
    t\\t\\t\\t\\t\\t\\n\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"CAS and any printed molecular/formula weight agree with the FEBA compound\
    \ row. Retain source precision. A local mapping-confidence number or enrichment-method\
    \ note is algorithm provenance, not a source measurement or identity proof. The\
    \ retained sesquisodium metadata conflicts with its separate disodium term.\"\n\
    \  },\n  {\n    \"decision_id\": \"q33\",\n    \"name\": \"Water, batch volume\
    \ and preparation quantities\",\n    \"stage\": \"Source completeness\",\n   \
    \ \"decision\": \"unsupported\",\n    \"local_fields\": [],\n    \"desired\":\
    \ null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"Complete media block lines 1459–1472\",\n   \
    \     \"exact_source_quote\": \"Media\\tBHIS_PIPES\\t\\nDescription\\tBrain heart\
    \ infusion salt broth\\t\\nMinimal\\tFALSE\\t\\nControlled vocabulary\\tConcentration\\\
    tUnits\\nCalf brains\\t7.7\\tg/L\\nBeef heart\\t9.8\\tg/L\\nProteose Peptone\\\
    t10\\tg/L\\nSodium Chloride\\t5\\tg/L\\nDisodium phosphate\\t2.5\\tg/L\\nL-Cysteine\\\
    t1\\tg/L\\nSodium bicarbonate\\t2\\tg/L\\nHemin\\t0.005\\tg/L\\nPIPES sesquisodium\
    \ salt\\t30\\tmM\\n\\t\\t\\n\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    ,\n        \"quote_representation\": \"Exact source text; line endings normalized\
    \ to LF, tabs and trailing fields preserved.\"\n      }\n    ],\n    \"interpretation\"\
    : \"This complete block supplies no water amount, final batch volume, pH, temperature,\
    \ gas, sterilization cycle, stock concentration or dose. No default 1 L batch\
    \ or preparation protocol is added; the printed per-litre rates alone do not establish\
    \ these quantities.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '6 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 6/9 primary
    and 0/9 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17561
  - chebi26710
  - chebi32139
  - chebi34683
  - chebi50385
  - chebi63055
  details: 'Instance coverage on a 0–100 percent scale, denominator 9: primary 66.67%;
    secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: source-forms
  area: grounding
  topic: Source material, salt form and ontology specificity
  outcome: concern
  summary: Five asserted chemicals match their source names/CAS; PIPES sesquisodium
    instead carries a disodium identifier. Calf brains, beef heart and proteose peptone
    remain complex materials with no invented pure-chemical mapping. No secondary
    CHEBI-based or legacy MediaIngredientMech slot is asserted in either layer.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - forms
  - feba-main
  - compound-0
  - compound-1
  - compound-2
  - compound-3
  - compound-4
  - compound-5
  - compound-6
  - compound-7
  - compound-8
  - chebi17561
  - chebi26710
  - chebi32139
  - chebi34683
  - chebi50385
  - chebi63055
- assessment_id: protocol
  area: completeness
  topic: Preparation, stock scope and growth context
  outcome: unknown
  summary: The direct FEBA block supplies no stock recipes or preparation instructions.
    Empty pH, temperature, gas, preparation and growth fields remain explicit source
    limitations, rather than confirmed loss of a protocol or a basis to import another
    BHIS variant. Complex/undefined broth classification is consistent with these
    material names and Minimal FALSE. There is no asserted organism, empirical growth
    metric, KG match, publication claim or assembly to verify for this target.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - record
  - owner-0
  - feba-main
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 7 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: prior-reviews
  area: provenance
  topic: Earlier exact-identity review reports
  outcome: supported
  summary: The two October concentration reports explicitly performed zero of nine
    source checks and recorded missing evidence. The September exact-record report
    is derivative context. Current FEBA comparison now supports numerical values,
    without rewriting those earlier reports or treating their source-access statements
    as current proof.
  target_ids:
  - CultureMech:015498
  evidence_ids:
  - prior-report-0
  - prior-report-1
  - prior-report-2
  - feba-main
findings:
- finding_id: f1
  issue_key: culturemech.015498.pipes-salt-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sesquisodium PIPES is linked to disodium PIPES
  description: Both layers name PIPES sesquisodium salt and retain source CAS 100037-69-2
    and FW 335.34, but assert CHEBI:63055 / disodium PIPES. The exact OLS definition,
    two-sodium formula and mass 346.338 establish a supplied-form mismatch; canonical-label
    validity does not resolve it.
  target_ids:
  - CultureMech:015498
  field_paths:
  - ingredients[8].term
  - ingredients[8].notes
  evidence_ids:
  - feba-main
  - compound-8
  - forms
  - chebi63055
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_pipes.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.2
  native_severity: P2
  normalization_reason: P2.2 maps to major because the asserted ion stoichiometry
    is chemically incompatible with the specified source material, affecting identity
    and any mass conversion independently of the correct numeric 30 mM rate.
- finding_id: f2
  issue_key: culturemech.015498.amount-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported numerical rates lack attached versioned quantity evidence
  description: All nine direct ingredient rates match the exact current FEBA block
    in both layers, but neither layer carries attached concentration evidence. The
    generic CultureBotHT repository link cannot preserve the exact FEBA revision,
    row and supplied-material basis.
  target_ids:
  - CultureMech:015498
  field_paths:
  - ingredients
  - sources
  - references
  evidence_ids:
  - feba-main
  - feba-version
  - quantity-inventory
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_pipes.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: 'P4.3 is a concrete minor traceability exception: the current
    exact variant supports every numerical rate, so this finding alleges no wrong
    amount. The missing attached source version, row and claim linkage prevent reproducible
    verification and require evidence-only curation.'
actions:
- action_id: a1
  description: In the maintained owner, resolve the exact sesquisodium material and
    correct or remove the incompatible term using verified resolver evidence. Preserve
    the printed 30 mM dose, source CAS/FW and source accession; do not substitute
    disodium material or invent a replacement identifier. Regenerate only after owner
    correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015498
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_pipes.yaml
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
  description: Attach exact versioned FEBA row evidence to the maintained concentration
    fields, retaining printed units and material scope. Record the later FEBA date
    explicitly; do not call it the authenticated original import source. Preserve
    owner identity and regenerate only after authorized evidence curation.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015498
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_pipes.yaml
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
- The exact CultureBotHT repository endpoint returned HTTP 404 at 2026-10-21T22:53:13.557900Z.
  Its original formula bytes remain unavailable; the independently captured later
  FEBA revision supports current amounts but does not establish import-time equivalence.
- The exact named CultureBotHT media_yaml file returned HTTP 404 at 2026-10-21T23:23:21.603973+00:00.
  Its original formula bytes remain unavailable; the independently captured later
  FEBA revision supports current amounts but does not establish import-time equivalence.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-042
- generated-medium
```
