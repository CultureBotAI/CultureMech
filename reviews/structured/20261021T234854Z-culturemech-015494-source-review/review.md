# Source and formulation review: BHIS_CaCl2 (CultureMech:015494)

- Review: 20261021T234854Z-culturemech-015494-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T23:44:40Z
- Finished UTC: 2026-10-21T23:48:54Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The current versioned FEBA BHIS_CaCl2 block agrees with every stored concentration and unit in the generated target and its maintained owner. The calcium supplement is calcium chloride dihydrate at 1 mM, not an anhydrous salt or a stock dose. Neither layer attaches concentration evidence. Historical CultureBotHT correspondence remains unresolved because the exact requested file is unavailable; the later FEBA revision supplies current formulation support only.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 415; batch 042 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding forty-one task batches contain 410 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 413 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015494 | data/merge_yaml/merged/BHIS_CaCl2.yaml | generated | BHIS_CaCl2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015494 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015494 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/415/strict.tsv |
| validate-terms | passed | True | CultureMech:015494 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015494 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015494 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: culturebothtExactBHIS_CaCl2 | unavailable | True | CultureMech:015494 | The exact public CultureBotHT media_yaml/BHIS_CaCl2.yaml request returned HTTP 404. Its March import-time bytes and correspondence were not authenticated. The current FEBA comparison passed independently; the historical source check remains unavailable and makes this review partial. |
| Exact source content access: culturebothtRepository | unavailable | False | CultureMech:015494 | The public CultureBotHT repository API returned HTTP 404. This is an access-scoped outcome, not proof that the repository or historical source never existed. |
| Exact current FEBA variant and compound comparison | passed | True | CultureMech:015494 | All 9 direct concentration rows and exact compound metadata agree at their stated scope. No stock, water charge or growth result is supplied by this block. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015494.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015494.

All 9 distinct direct concentrations and 18 target/owner instances match the current exact source. Every decision is evidence_only because both layers lack attached evidence; no numeric correction is proposed. The block supplies no additional stock dose, batch water amount or preparation quantity.

[
  {
    "quantity_id": "q1",
    "topic": "Calf brains — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "7.7",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 7.7 g/L for Calf brains. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue equivalent or proof of tissue processing."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 7.7 g/L for Calf brains. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue equivalent or proof of tissue processing."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1423",
        "exact_source_quote": "Calf brains\t7.7\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 569; exact compound row",
        "exact_source_quote": "Calf brains\t\t\t\t\t\tUsed in BHIS_K3 media",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 7.7 g/L for Calf brains. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue equivalent or proof of tissue processing."
  },
  {
    "quantity_id": "q2",
    "topic": "Beef heart — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "9.8",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "9.8",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 9.8 g/L for Beef heart. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue equivalent or proof of tissue processing."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "9.8",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 9.8 g/L for Beef heart. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue equivalent or proof of tissue processing."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1424",
        "exact_source_quote": "Beef heart\t9.8\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 570; exact compound row",
        "exact_source_quote": "Beef heart\t\t\t\t\t\tUsed in BHIS_K3 media",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 9.8 g/L for Beef heart. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue equivalent or proof of tissue processing."
  },
  {
    "quantity_id": "q3",
    "topic": "Proteose Peptone — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 10 g/L for Proteose Peptone. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 10 g/L for Proteose Peptone. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1425",
        "exact_source_quote": "Proteose Peptone\t10\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 568; exact compound row",
        "exact_source_quote": "Proteose Peptone\t91079-38-8\tSigma\t82450",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 10 g/L for Proteose Peptone. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
  },
  {
    "quantity_id": "q4",
    "topic": "Sodium Chloride — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 5 g/L for Sodium Chloride. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 5 g/L for Sodium Chloride. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1426",
        "exact_source_quote": "Sodium Chloride\t5\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 375; exact compound row",
        "exact_source_quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 5 g/L for Sodium Chloride. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
  },
  {
    "quantity_id": "q5",
    "topic": "Disodium phosphate — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "2.5",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 2.5 g/L for Disodium phosphate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 2.5 g/L for Disodium phosphate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1427",
        "exact_source_quote": "Disodium phosphate\t2.5\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 171; exact compound row",
        "exact_source_quote": "Disodium phosphate\t7558-79-4\t\t\t141.96\tNa2HPO4, Sodium phosphate dibasic",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 2.5 g/L for Disodium phosphate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
  },
  {
    "quantity_id": "q6",
    "topic": "L-Cysteine — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 1 g/L for L-Cysteine. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 1 g/L for L-Cysteine. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1428",
        "exact_source_quote": "L-Cysteine\t1\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 519; exact compound row",
        "exact_source_quote": "L-Cysteine\t52-90-4\tsigmaaldrich\tW326305-100G\t121.16\t (R)-2-Amino-3-mercaptopropionic acid",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 1 g/L for L-Cysteine. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
  },
  {
    "quantity_id": "q7",
    "topic": "Sodium bicarbonate — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 2 g/L for Sodium bicarbonate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 2 g/L for Sodium bicarbonate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1429",
        "exact_source_quote": "Sodium bicarbonate\t2\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 369; exact compound row",
        "exact_source_quote": "Sodium bicarbonate\t144-55-8\t\t\t84.007\tNaHCO3\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 2 g/L for Sodium bicarbonate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
  },
  {
    "quantity_id": "q8",
    "topic": "Hemin — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "0.005",
      "unit": "G_PER_L"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 0.005 g/L for Hemin. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 0.005 g/L for Hemin. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1430",
        "exact_source_quote": "Hemin\t0.005\tg/L",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 520; exact compound row",
        "exact_source_quote": "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 0.005 g/L for Hemin. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source."
  },
  {
    "quantity_id": "q9",
    "topic": "Calcium chloride dihydrate — direct medium concentration",
    "decision": "evidence_only",
    "local": {
      "value": "1",
      "unit": "MILLIMOLAR"
    },
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "MILLIMOLAR"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 1 mM for Calcium chloride dihydrate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. Preserve the dihydrate: CAS 10035-04-8, FW 147.01 and CHEBI:86158 agree with the supplied source form; no conversion to anhydrous mass is needed."
      },
      {
        "input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1",
          "unit": "MILLIMOLAR"
        },
        "decision": "evidence_only",
        "rationale": "The exact current BHIS_CaCl2 block reports 1 mM for Calcium chloride dihydrate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. Preserve the dihydrate: CAS 10035-04-8, FW 147.01 and CHEBI:86158 agree with the supplied source form; no conversion to anhydrous mass is needed."
      }
    ],
    "source_snippets": [
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1431",
        "exact_source_quote": "Calcium chloride dihydrate\t1\tmM",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_media",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
        "source_locator": "BHIS_CaCl2, media line 1422",
        "exact_source_quote": "Controlled vocabulary\tConcentration\tUnits",
        "snapshot_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848"
      },
      {
        "source_key": "feba_compounds",
        "source_url": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
        "source_locator": "Compounds.tsv line 90; exact compound row",
        "exact_source_quote": "Calcium chloride dihydrate\t10035-04-8\tSigma\tC5080\t147.01\tCalcium Chloride Dihydrate, CaCl2*2H2O\t\t\tyes",
        "snapshot_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774"
      }
    ],
    "rationale": "The exact current BHIS_CaCl2 block reports 1 mM for Calcium chloride dihydrate. Both local layers retain that value and unit but attach no concentration evidence; add the exact source linkage without changing the amount. The printed concentration requires no assumed batch-volume arithmetic. The later FEBA revision does not authenticate the March CultureBotHT source. Preserve the dihydrate: CAS 10035-04-8, FW 147.01 and CHEBI:86158 agree with the supplied source form; no conversion to anhydrous mass is needed."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:015494.

6 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 6/9 primary and 0/9 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 9: primary 66.67%; secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015494.

7 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact named variant and single maintained contributor

identity: supported. Targets: CultureMech:015494.

BHIS_CaCl2, source accession and CultureMech:015494 agree. The generated ingredient block exactly matches its sole maintained owner; only generated provenance/history keys differ. The calcium supplement is calcium chloride dihydrate at 1 mM, not an anhydrous salt or a stock dose. Keep similarly named BHIS variants separate.

### Maintained input and generated target

ownership: supported. Targets: CultureMech:015494.

The normalized CultureBotHT record is the curation owner. Its names, concentrations, notes, classification and source metadata are already retained in the generated target. There is no current owner quantity repair to reapply or missing generated scientific block to reconstruct. Any later source/evidence curation belongs in that owner or its actual importer, followed by separately authorized regeneration.

### Source form and unmapped-material boundaries

grounding: concern. Targets: CultureMech:015494.

The calcium supplement is calcium chloride dihydrate at 1 mM, not an anhydrous salt or a stock dose. All asserted CHEBI IDs have exact nonobsolete canonical labels and source-compatible CAS/form metadata. Calf brains, Beef heart and Proteose Peptone remain ungrounded complex materials; their printed masses must not be replaced by tissue equivalents. No asserted hydrate, stereochemistry or chemical identity mismatch was found in the inspected selected layers.

### Current source support and historical correspondence

evidence: concern. Targets: CultureMech:015494.

Both local layers contain zero attached concentration evidence objects across 18 concentration instances. Current FEBA rows support the numbers and variant identity; September 2026 source bytes do not authenticate the March import. Earlier reports provide historical observations and source leads only.

### Preparation, conditions and source-only quantity check

completeness: unknown. Targets: CultureMech:015494.

Neither local layer supplies preparation, sterilization, water charge, measured final batch volume, pH, atmosphere, incubation temperature, storage or shelf life. The exact source block also supplies none of those values and refers to no stock mix. This is an unresolved protocol boundary, not permission to add a typical BHIS method, assume one litre of water, or transfer a neighboring variant protocol. Empty optional organism/application fields alone are not defects.

### Complex broth classification and evidence limits

consistency: supported. Targets: CultureMech:015494.

The source describes brain heart infusion salt broth and Minimal FALSE; tissue-derived ingredients and peptone support the local COMPLEX/UNDEFINED classification. LIQUID agrees with broth, with no agar row. The specialized filing does not assert a taxon. The source table is a formulation description, not an observed-growth experiment.

### Stocks, variants, taxonomy and graph scope

scope: not_applicable. Targets: CultureMech:015494.

Neither selected layer asserts a solution reference, inline variant, organism taxon, growth measurement, legacy MIM identifier or KG-Microbe match. No stock or comparative organism evidence is transferred from other BHIS records. A micromediaparam_legacy mapping-method note on disodium phosphate is provenance text, not an asserted legacy MIM identifier.

### Complete current formulation review with historical source gap

completeness: concern. Targets: CultureMech:015494.

All 9 source concentrations and both local layers were assessed. Printed formula weights and CAS identifiers were examined as supplied-form metadata, not additional dosing instructions. No source-only preparation amount was found in the exact block. The current formulation comparison is complete; overall completion remains partial for the unavailable historical CultureBotHT source.

## Findings

### f1: Supported concentrations lack exact source links

minor / open / confirmed; issue key: culturemech.015494.concentration-evidence.

Both layers retain all 9 directly supported concentrations but attach no claim-level evidence. The generic CultureBotHT repository URL does not recover the exact formula/version, and current FEBA agreement cannot authenticate the March import.

### f2: Optional ingredient linkages remain incomplete

informational / open / confirmed; issue key: culturemech.015494.grounding-coverage.

Both layers have no secondary CHEBI-based MIM slots. Their complex-material rows remain ungrounded, with has_unmapped_ingredients retained. The asserted pure-reagent terms agree with the captured source forms.

## Recommended Actions And Acceptance Checks

### a1

Attach the exact named FEBA rows, printed units and compound-form evidence in the maintained owner while retaining the current-versus-historical version distinction. Preserve every amount. Keep original CultureBotHT authentication explicitly unresolved until an exact historical source is recovered.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Consider exact supplied-material linkage in a separate curation task. Preserve unresolved mixtures and the unmapped flag; add only independently verified identifiers, without substituting a pure molecule or anatomy term for an ingredient product.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BHIS_CaCl2.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/bhis_cacl2.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BHIS_CaCl2.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BHIS_CaCl2.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch042/415/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch042/415/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BHIS_CaCl2.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BHIS_CaCl2.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/bhis_cacl2.yaml:1:id: CultureMech:015494<br>./data/merge_yaml/merged/BHIS_CaCl2.yaml:1:id: CultureMech:015494<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch042/source-preflight-bound/415/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 15 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| feba-main | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; Exact BHIS_CaCl2 block, lines 1419–1432 | supports | The exact named block gives 9 direct ingredient concentrations. These printed units establish concentrations without assuming a final batch volume. |
| feba-header | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; Line 1422, exact named block | supports | The table explicitly labels concentration and units; these are not unqualified batch masses. |
| feba-compounds | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact compound-name rows; CAS, formula weight and supplied form | supports | All selected compound rows were compared with local names, notes and asserted chemical forms. Complex tissue and peptone materials remain mixtures; no tissue-equivalent masses were inferred. |
| feba-version | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b; $.hash and $.date | supports | The pinned FEBA revision 803273865ea9e83fab770ec4f13670db80e1180b is dated September 10, 2026, after the March 18 import. Current agreement is not historical import-time authentication. |
| culturebothtExactBHIS_CaCl2-attempt | https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS_CaCl2.yaml; Preserved exact public retrieval result | context_only | The exact public CultureBotHT media_yaml/BHIS_CaCl2.yaml request returned HTTP 404. Its March import-time bytes and correspondence were not authenticated. The current FEBA comparison passed independently; the historical source check remains unavailable and makes this review partial. |
| culturebothtRepository-attempt | https://api.github.com/repos/CultureBotAI/CultureBotHT; Preserved exact public retrieval result | context_only | The public CultureBotHT repository API returned HTTP 404. This is an access-scoped outcome, not proof that the repository or historical source never existed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch042/415/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi17561 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17561; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17561 resolves to L-cysteine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34683; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34683 resolves to disodium hydrogenphosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50385; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50385 resolves to hemin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}} |
| history-metadata | data/merge_yaml/merged/BHIS_CaCl2.yaml; data/normalized_yaml/specialized/bhis_cacl2.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bhis_cacl2.yaml", "events": 3, "timestamp_issues": []}] |
| prior-0 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis_cacl2.md; Entire record-specific historical report; exact present bytes | context_only | Historical review context only. October reports explicitly performed zero source checks; September review observations and prior command outcomes do not replace the present source assessment. No structured prior finding is closed or superseded. |
| prior-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS_CaCl2.md; Entire record-specific historical report; exact present bytes | context_only | Historical review context only. October reports explicitly performed zero source checks; September review observations and prior command outcomes do not replace the present source assessment. No structured prior finding is closed or superseded. |
| prior-2 | reports/yaml_record_review/20260921T212834Z-BHIS_CaCl2.md; Entire record-specific historical report; exact present bytes | context_only | Historical review context only. October reports explicitly performed zero source checks; September review observations and prior command outcomes do not replace the present source assessment. No structured prior finding is closed or superseded. |
| grounding-detail | /private/tmp/culturemech-review-work-batch042/415/grounding-inventory.json; Complete local per-layer fields and exact captured scientific context | context_only | Each local ingredient/form or history entry is retained with its actual input path and source boundary. |
| history-detail | /private/tmp/culturemech-review-work-batch042/415/history-inventory.json; Complete local per-layer fields and exact captured scientific context | context_only | Each local ingredient/form or history entry is retained with its actual input path and source boundary. |
| writer-0 | scripts/import_from_culturebotht.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CultureBotHT import_file reads YAML; transform_medium copies source content and adds source/history/flags without source authentication. Current migration handles metadata/units/preparation aliases; this record documents category normalization. Current merger preserves one-input content and requires full formulation compatibility for multi-input merges. These current functions do not prove a historical invocation or cause of stored content. |
| writer-1 | scripts/migrate_legacy_fields.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CultureBotHT import_file reads YAML; transform_medium copies source content and adds source/history/flags without source authentication. Current migration handles metadata/units/preparation aliases; this record documents category normalization. Current merger preserves one-input content and requires full formulation compatibility for multi-input merges. These current functions do not prove a historical invocation or cause of stored content. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CultureBotHT import_file reads YAML; transform_medium copies source content and adds source/history/flags without source authentication. Current migration handles metadata/units/preparation aliases; this record documents category normalization. Current merger preserves one-input content and requires full formulation compatibility for multi-input merges. These current functions do not prove a historical invocation or cause of stored content. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current CultureBotHT import_file reads YAML; transform_medium copies source content and adds source/history/flags without source authentication. Current migration handles metadata/units/preparation aliases; this record documents category normalization. Current merger preserves one-input content and requires full formulation compatibility for multi-input merges. These current functions do not prove a historical invocation or cause of stored content. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact public CultureBotHT media_yaml/BHIS_CaCl2.yaml request returned HTTP 404. Its March import-time bytes and correspondence were not authenticated. The current FEBA comparison passed independently; the historical source check remains unavailable and makes this review partial.
- The public CultureBotHT repository API returned HTTP 404. This is an access-scoped outcome, not proof that the repository or historical source never existed.
- The FEBA block is direct composition only. No dose, stock strength, density, final volume, pH or cultivation condition was inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T234854Z-culturemech-015494-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: BHIS_CaCl2 (CultureMech:015494)'
started_at: '2026-10-21T23:44:40Z'
finished_at: '2026-10-21T23:48:54Z'
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
summary: The current versioned FEBA BHIS_CaCl2 block agrees with every stored concentration
  and unit in the generated target and its maintained owner. The calcium supplement
  is calcium chloride dihydrate at 1 mM, not an anhydrous salt or a stock dose. Neither
  layer attaches concentration evidence. Historical CultureBotHT correspondence remains
  unresolved because the exact requested file is unavailable; the later FEBA revision
  supplies current formulation support only.
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
  - path: data/merge_yaml/merged/BHIS_CaCl2.yaml
    sha256: 5d20fc5ae6f7043dcceb7ee52e5717de957fa828d9721043ba01937bf8231052
    role: target
  - path: data/normalized_yaml/specialized/bhis_cacl2.yaml
    sha256: 687d3790d60e40d21abd6a05bfd7ae0eff6feeabdaa90051abb7f4595e44f3ba
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS_CaCl2.md
    sha256: e5cd738b514ffbdbeb8e5da91fb70754def60bfeabeb0131c0ed1ea274899a40
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis_cacl2.md
    sha256: 2603ddc38a1df4bfe4c5cda9eeef956c087190cb1cd566921e4db2ee65a68a70
    role: context
  - path: reports/yaml_record_review/20260921T212834Z-BHIS_CaCl2.md
    sha256: ef16bbe5ca1ad7f77da1d5dc7747b1b436ea5681ce06ed1fd6583dc67d467ac1
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
  selection: Task review 415; batch 042 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:015494
targets:
- target_id: CultureMech:015494
  path: data/merge_yaml/merged/BHIS_CaCl2.yaml
  label: BHIS_CaCl2
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_cacl2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BHIS_CaCl2.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BHIS_CaCl2.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch042/415/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/415/strict.tsv"
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BHIS_CaCl2.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BHIS_CaCl2.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015494
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
  - CultureMech:015494
- check_id: culturebothtExactBHIS_CaCl2-source-access
  name: 'Exact source content access: culturebothtExactBHIS_CaCl2'
  required: true
  status: unavailable
  summary: The exact public CultureBotHT media_yaml/BHIS_CaCl2.yaml request returned
    HTTP 404. Its March import-time bytes and correspondence were not authenticated.
    The current FEBA comparison passed independently; the historical source check
    remains unavailable and makes this review partial.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - culturebothtExactBHIS_CaCl2-attempt
- check_id: culturebothtRepository-source-access
  name: 'Exact source content access: culturebothtRepository'
  required: false
  status: unavailable
  summary: The public CultureBotHT repository API returned HTTP 404. This is an access-scoped
    outcome, not proof that the repository or historical source never existed.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - culturebothtRepository-attempt
- check_id: current-feba-formulation
  name: Exact current FEBA variant and compound comparison
  required: true
  status: passed
  summary: All 9 direct concentration rows and exact compound metadata agree at their
    stated scope. No stock, water charge or growth result is supplied by this block.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - feba-main
  - feba-header
  - feba-compounds
  - feba-version
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BHIS_CaCl2.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/bhis_cacl2.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BHIS_CaCl2.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:08.883941Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BHIS_CaCl2.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch042/415/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:09.887713Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-042/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch042/415/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BHIS_CaCl2.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:10.994781Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BHIS_CaCl2.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T23:45:11.730910Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T23:48:53Z'
  support: supports
  summary: './data/normalized_yaml/specialized/bhis_cacl2.yaml:1:id: CultureMech:015494

    ./data/merge_yaml/merged/BHIS_CaCl2.yaml:1:id: CultureMech:015494

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/source-preflight-bound/415/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T23:48:53Z'
  support: supports
  summary: 15 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a603bab0d9c984f712b408d718aad27cdf71dbb6c9233e6272baefa9c2ec684b
- evidence_id: feba-main
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: Exact BHIS_CaCl2 block, lines 1419–1432
  accessed_at: '2026-10-21T07:58:53.930003Z'
  support: supports
  summary: The exact named block gives 9 direct ingredient concentrations. These printed
    units establish concentrations without assuming a final batch volume.
  quote: "Media\tBHIS_CaCl2"
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: feba-header
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: Line 1422, exact named block
  accessed_at: '2026-10-21T07:58:53.930003Z'
  support: supports
  summary: The table explicitly labels concentration and units; these are not unqualified
    batch masses.
  quote: "Controlled vocabulary\tConcentration\tUnits"
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: feba-compounds
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact compound-name rows; CAS, formula weight and supplied form
  accessed_at: '2026-10-21T13:40:20.285295Z'
  support: supports
  summary: All selected compound rows were compared with local names, notes and asserted
    chemical forms. Complex tissue and peptone materials remain mixtures; no tissue-equivalent
    masses were inferred.
  quote: "Compound\tCAS\tCompany\tCatalogNumber\tFW"
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: feba-version
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commit/803273865ea9e83fab770ec4f13670db80e1180b
  locator: $.hash and $.date
  accessed_at: '2026-10-21T07:59:41.378955Z'
  support: supports
  summary: The pinned FEBA revision 803273865ea9e83fab770ec4f13670db80e1180b is dated
    September 10, 2026, after the March 18 import. Current agreement is not historical
    import-time authentication.
  quote: '"date": "2026-09-10T16:27:42+00:00"'
  snapshot_sha256: 0a4998d61b96db10c549512e2fe06718e04b687e6bbc6b2c1ea121c3c11a53ca
- evidence_id: culturebothtExactBHIS_CaCl2-attempt
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/BHIS_CaCl2.yaml
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T23:23:20.936960Z'
  support: context_only
  summary: The exact public CultureBotHT media_yaml/BHIS_CaCl2.yaml request returned
    HTTP 404. Its March import-time bytes and correspondence were not authenticated.
    The current FEBA comparison passed independently; the historical source check
    remains unavailable and makes this review partial.
  snapshot_sha256: d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed
- evidence_id: culturebothtRepository-attempt
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:53:13.557900Z'
  support: context_only
  summary: The public CultureBotHT repository API returned HTTP 404. This is an access-scoped
    outcome, not proof that the repository or historical source never existed.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/415/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 09c15281292b40bbad7acb4dd1b96725b5ff5c97a32b34497ce799d287f04c18
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T23:48:53Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BHIS_CaCl2.yaml; data/normalized_yaml/specialized/bhis_cacl2.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: '[{"input": "target", "events": 4, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/bhis_cacl2.yaml",
    "events": 3, "timestamp_issues": []}]'
- evidence_id: prior-0
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/bhis_cacl2.md
  locator: Entire record-specific historical report; exact present bytes
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Historical review context only. October reports explicitly performed zero
    source checks; September review observations and prior command outcomes do not
    replace the present source assessment. No structured prior finding is closed or
    superseded.
  snapshot_sha256: 2603ddc38a1df4bfe4c5cda9eeef956c087190cb1cd566921e4db2ee65a68a70
- evidence_id: prior-1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BHIS_CaCl2.md
  locator: Entire record-specific historical report; exact present bytes
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Historical review context only. October reports explicitly performed zero
    source checks; September review observations and prior command outcomes do not
    replace the present source assessment. No structured prior finding is closed or
    superseded.
  snapshot_sha256: e5cd738b514ffbdbeb8e5da91fb70754def60bfeabeb0131c0ed1ea274899a40
- evidence_id: prior-2
  kind: prior_review
  reference: reports/yaml_record_review/20260921T212834Z-BHIS_CaCl2.md
  locator: Entire record-specific historical report; exact present bytes
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Historical review context only. October reports explicitly performed zero
    source checks; September review observations and prior command outcomes do not
    replace the present source assessment. No structured prior finding is closed or
    superseded.
  snapshot_sha256: ef16bbe5ca1ad7f77da1d5dc7747b1b436ea5681ce06ed1fd6583dc67d467ac1
- evidence_id: grounding-detail
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/415/grounding-inventory.json
  locator: Complete local per-layer fields and exact captured scientific context
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Each local ingredient/form or history entry is retained with its actual
    input path and source boundary.
  snapshot_sha256: 5b6b256010382f8be2437a5af78dc2e0bf3355d2378a6de20f04773c10a94a8a
- evidence_id: history-detail
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch042/415/history-inventory.json
  locator: Complete local per-layer fields and exact captured scientific context
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Each local ingredient/form or history entry is retained with its actual
    input path and source boundary.
  snapshot_sha256: 105eaaf8a5592801def02c7a5d1e3579abb9e7b6606e52e38347d7470d0e764c
- evidence_id: writer-0
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Current CultureBotHT import_file reads YAML; transform_medium copies source
    content and adds source/history/flags without source authentication. Current migration
    handles metadata/units/preparation aliases; this record documents category normalization.
    Current merger preserves one-input content and requires full formulation compatibility
    for multi-input merges. These current functions do not prove a historical invocation
    or cause of stored content.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_legacy_fields.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Current CultureBotHT import_file reads YAML; transform_medium copies source
    content and adds source/history/flags without source authentication. Current migration
    handles metadata/units/preparation aliases; this record documents category normalization.
    Current merger preserves one-input content and requires full formulation compatibility
    for multi-input merges. These current functions do not prove a historical invocation
    or cause of stored content.
  snapshot_sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Current CultureBotHT import_file reads YAML; transform_medium copies source
    content and adds source/history/flags without source authentication. Current migration
    handles metadata/units/preparation aliases; this record documents category normalization.
    Current merger preserves one-input content and requires full formulation compatibility
    for multi-input merges. These current functions do not prove a historical invocation
    or cause of stored content.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T23:48:53Z'
  support: context_only
  summary: Current CultureBotHT import_file reads YAML; transform_medium copies source
    content and adds source/history/flags without source authentication. Current migration
    handles metadata/units/preparation aliases; this record documents category normalization.
    Current merger preserves one-input content and requires full formulation compatibility
    for multi-input merges. These current functions do not prove a historical invocation
    or cause of stored content.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: All 9 distinct direct concentrations and 18 target/owner instances match
    the current exact source. Every decision is evidence_only because both layers
    lack attached evidence; no numeric correction is proposed. The block supplies
    no additional stock dose, batch water amount or preparation quantity.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"topic\": \"Calf brains — direct\
    \ medium concentration\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"7.7\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.7\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The exact current BHIS_CaCl2 block reports 7.7 g/L for Calf brains. Both local\
    \ layers retain that value and unit but attach no concentration evidence; add\
    \ the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source. This is the printed complex-material\
    \ addition, not a fresh-tissue equivalent or proof of tissue processing.\"\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.7\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 7.7 g/L for Calf brains. Both local layers\
    \ retain that value and unit but attach no concentration evidence; add the exact\
    \ source linkage without changing the amount. The printed concentration requires\
    \ no assumed batch-volume arithmetic. The later FEBA revision does not authenticate\
    \ the March CultureBotHT source. This is the printed complex-material addition,\
    \ not a fresh-tissue equivalent or proof of tissue processing.\"\n      }\n  \
    \  ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"feba_media\"\
    ,\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1423\",\n        \"exact_source_quote\"\
    : \"Calf brains\\t7.7\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 569; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Calf brains\\t\\t\\t\\t\\t\\tUsed in BHIS_K3\
    \ media\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 7.7 g/L for Calf brains. Both local layers retain that value and unit but attach\
    \ no concentration evidence; add the exact source linkage without changing the\
    \ amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\
    \ This is the printed complex-material addition, not a fresh-tissue equivalent\
    \ or proof of tissue processing.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n\
    \    \"topic\": \"Beef heart — direct medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": {\n      \"value\": \"9.8\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[1].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"9.8\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The exact current BHIS_CaCl2 block reports 9.8 g/L for Beef heart. Both local\
    \ layers retain that value and unit but attach no concentration evidence; add\
    \ the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source. This is the printed complex-material\
    \ addition, not a fresh-tissue equivalent or proof of tissue processing.\"\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 9.8 g/L for Beef heart. Both local layers retain\
    \ that value and unit but attach no concentration evidence; add the exact source\
    \ linkage without changing the amount. The printed concentration requires no assumed\
    \ batch-volume arithmetic. The later FEBA revision does not authenticate the March\
    \ CultureBotHT source. This is the printed complex-material addition, not a fresh-tissue\
    \ equivalent or proof of tissue processing.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1424\",\n        \"exact_source_quote\"\
    : \"Beef heart\\t9.8\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 570; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Beef heart\\t\\t\\t\\t\\t\\tUsed in BHIS_K3\
    \ media\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 9.8 g/L for Beef heart. Both local layers retain that value and unit but attach\
    \ no concentration evidence; add the exact source linkage without changing the\
    \ amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\
    \ This is the printed complex-material addition, not a fresh-tissue equivalent\
    \ or proof of tissue processing.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n\
    \    \"topic\": \"Proteose Peptone — direct medium concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": {\n      \"value\": \"10\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"ingredients[2].concentration\",\n   \
    \     \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The exact current BHIS_CaCl2 block reports 10 g/L for Proteose Peptone. Both\
    \ local layers retain that value and unit but attach no concentration evidence;\
    \ add the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\":\
    \ \"evidence_only\",\n        \"rationale\": \"The exact current BHIS_CaCl2 block\
    \ reports 10 g/L for Proteose Peptone. Both local layers retain that value and\
    \ unit but attach no concentration evidence; add the exact source linkage without\
    \ changing the amount. The printed concentration requires no assumed batch-volume\
    \ arithmetic. The later FEBA revision does not authenticate the March CultureBotHT\
    \ source.\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1425\",\n        \"exact_source_quote\"\
    : \"Proteose Peptone\\t10\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 568; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Proteose Peptone\\t91079-38-8\\tSigma\\t82450\"\
    ,\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 10 g/L for Proteose Peptone. Both local layers retain that value and unit but\
    \ attach no concentration evidence; add the exact source linkage without changing\
    \ the amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"topic\": \"Sodium Chloride —\
    \ direct medium concentration\",\n    \"decision\": \"evidence_only\",\n    \"\
    local\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n    },\n   \
    \ \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact current\
    \ BHIS_CaCl2 block reports 5 g/L for Sodium Chloride. Both local layers retain\
    \ that value and unit but attach no concentration evidence; add the exact source\
    \ linkage without changing the amount. The printed concentration requires no assumed\
    \ batch-volume arithmetic. The later FEBA revision does not authenticate the March\
    \ CultureBotHT source.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 5 g/L for Sodium Chloride. Both local layers\
    \ retain that value and unit but attach no concentration evidence; add the exact\
    \ source linkage without changing the amount. The printed concentration requires\
    \ no assumed batch-volume arithmetic. The later FEBA revision does not authenticate\
    \ the March CultureBotHT source.\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1426\",\n        \"exact_source_quote\"\
    : \"Sodium Chloride\\t5\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 375; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Sodium Chloride\\t7647-14-5\\tSigma\\tS3014\\\
    t58.44\\tNaCl\\t\\t\\tyes\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 5 g/L for Sodium Chloride. Both local layers retain that value and unit but\
    \ attach no concentration evidence; add the exact source linkage without changing\
    \ the amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"topic\": \"Disodium phosphate\
    \ — direct medium concentration\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local\": {\n      \"value\": \"2.5\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact current\
    \ BHIS_CaCl2 block reports 2.5 g/L for Disodium phosphate. Both local layers retain\
    \ that value and unit but attach no concentration evidence; add the exact source\
    \ linkage without changing the amount. The printed concentration requires no assumed\
    \ batch-volume arithmetic. The later FEBA revision does not authenticate the March\
    \ CultureBotHT source.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 2.5 g/L for Disodium phosphate. Both local\
    \ layers retain that value and unit but attach no concentration evidence; add\
    \ the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1427\",\n        \"exact_source_quote\"\
    : \"Disodium phosphate\\t2.5\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 171; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Disodium phosphate\\t7558-79-4\\t\\t\\t141.96\\\
    tNa2HPO4, Sodium phosphate dibasic\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 2.5 g/L for Disodium phosphate. Both local layers retain that value and unit\
    \ but attach no concentration evidence; add the exact source linkage without changing\
    \ the amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"topic\": \"L-Cysteine — direct\
    \ medium concentration\",\n    \"decision\": \"evidence_only\",\n    \"local\"\
    : {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The exact current BHIS_CaCl2 block reports 1 g/L for L-Cysteine. Both local\
    \ layers retain that value and unit but attach no concentration evidence; add\
    \ the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    evidence_only\",\n        \"rationale\": \"The exact current BHIS_CaCl2 block\
    \ reports 1 g/L for L-Cysteine. Both local layers retain that value and unit but\
    \ attach no concentration evidence; add the exact source linkage without changing\
    \ the amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1428\",\n        \"exact_source_quote\"\
    : \"L-Cysteine\\t1\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 519; exact compound row\"\
    ,\n        \"exact_source_quote\": \"L-Cysteine\\t52-90-4\\tsigmaaldrich\\tW326305-100G\\\
    t121.16\\t (R)-2-Amino-3-mercaptopropionic acid\",\n        \"snapshot_sha256\"\
    : \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\n     \
    \ }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports 1\
    \ g/L for L-Cysteine. Both local layers retain that value and unit but attach\
    \ no concentration evidence; add the exact source linkage without changing the\
    \ amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"topic\": \"Sodium bicarbonate\
    \ — direct medium concentration\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local\": {\n      \"value\": \"2\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact current\
    \ BHIS_CaCl2 block reports 2 g/L for Sodium bicarbonate. Both local layers retain\
    \ that value and unit but attach no concentration evidence; add the exact source\
    \ linkage without changing the amount. The printed concentration requires no assumed\
    \ batch-volume arithmetic. The later FEBA revision does not authenticate the March\
    \ CultureBotHT source.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 2 g/L for Sodium bicarbonate. Both local layers\
    \ retain that value and unit but attach no concentration evidence; add the exact\
    \ source linkage without changing the amount. The printed concentration requires\
    \ no assumed batch-volume arithmetic. The later FEBA revision does not authenticate\
    \ the March CultureBotHT source.\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1429\",\n        \"exact_source_quote\"\
    : \"Sodium bicarbonate\\t2\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 369; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Sodium bicarbonate\\t144-55-8\\t\\t\\t84.007\\\
    tNaHCO3\\t\\t\\tyes\",\n        \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 2 g/L for Sodium bicarbonate. Both local layers retain that value and unit but\
    \ attach no concentration evidence; add the exact source linkage without changing\
    \ the amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"topic\": \"Hemin — direct medium\
    \ concentration\",\n    \"decision\": \"evidence_only\",\n    \"local\": {\n \
    \     \"value\": \"0.005\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.005\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The exact current BHIS_CaCl2 block reports 0.005 g/L for Hemin.\
    \ Both local layers retain that value and unit but attach no concentration evidence;\
    \ add the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source.\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.005\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\",\n        \"rationale\": \"The exact current BHIS_CaCl2 block\
    \ reports 0.005 g/L for Hemin. Both local layers retain that value and unit but\
    \ attach no concentration evidence; add the exact source linkage without changing\
    \ the amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"feba_media\",\n        \"source_url\": \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1430\",\n        \"exact_source_quote\"\
    : \"Hemin\\t0.005\\tg/L\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 520; exact compound row\"\
    ,\n        \"exact_source_quote\": \"Hemin\\t16009-13-5\\tsigmaaldrich\\tH9039-10G\\\
    t651.94\\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin\
    \ IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)\",\n        \"\
    snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 0.005 g/L for Hemin. Both local layers retain that value and unit but attach\
    \ no concentration evidence; add the exact source linkage without changing the\
    \ amount. The printed concentration requires no assumed batch-volume arithmetic.\
    \ The later FEBA revision does not authenticate the March CultureBotHT source.\"\
    \n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"topic\": \"Calcium chloride dihydrate\
    \ — direct medium concentration\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"MILLIMOLAR\"\n    },\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1\",\n          \"unit\": \"MILLIMOLAR\"\n        },\n\
    \        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 1 mM for Calcium chloride dihydrate. Both local\
    \ layers retain that value and unit but attach no concentration evidence; add\
    \ the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source. Preserve the dihydrate: CAS 10035-04-8,\
    \ FW 147.01 and CHEBI:86158 agree with the supplied source form; no conversion\
    \ to anhydrous mass is needed.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/bhis_cacl2.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"MILLIMOLAR\"\n       \
    \ },\n        \"decision\": \"evidence_only\",\n        \"rationale\": \"The exact\
    \ current BHIS_CaCl2 block reports 1 mM for Calcium chloride dihydrate. Both local\
    \ layers retain that value and unit but attach no concentration evidence; add\
    \ the exact source linkage without changing the amount. The printed concentration\
    \ requires no assumed batch-volume arithmetic. The later FEBA revision does not\
    \ authenticate the March CultureBotHT source. Preserve the dihydrate: CAS 10035-04-8,\
    \ FW 147.01 and CHEBI:86158 agree with the supplied source form; no conversion\
    \ to anhydrous mass is needed.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"feba_media\",\n        \"source_url\": \"\
    https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1431\",\n        \"exact_source_quote\"\
    : \"Calcium chloride dihydrate\\t1\\tmM\",\n        \"snapshot_sha256\": \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\
    \n      },\n      {\n        \"source_key\": \"feba_media\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media\"\
    ,\n        \"source_locator\": \"BHIS_CaCl2, media line 1422\",\n        \"exact_source_quote\"\
    : \"Controlled vocabulary\\tConcentration\\tUnits\",\n        \"snapshot_sha256\"\
    : \"a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848\"\n     \
    \ },\n      {\n        \"source_key\": \"feba_compounds\",\n        \"source_url\"\
    : \"https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv\"\
    ,\n        \"source_locator\": \"Compounds.tsv line 90; exact compound row\",\n\
    \        \"exact_source_quote\": \"Calcium chloride dihydrate\\t10035-04-8\\tSigma\\\
    tC5080\\t147.01\\tCalcium Chloride Dihydrate, CaCl2*2H2O\\t\\t\\tyes\",\n    \
    \    \"snapshot_sha256\": \"25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774\"\
    \n      }\n    ],\n    \"rationale\": \"The exact current BHIS_CaCl2 block reports\
    \ 1 mM for Calcium chloride dihydrate. Both local layers retain that value and\
    \ unit but attach no concentration evidence; add the exact source linkage without\
    \ changing the amount. The printed concentration requires no assumed batch-volume\
    \ arithmetic. The later FEBA revision does not authenticate the March CultureBotHT\
    \ source. Preserve the dihydrate: CAS 10035-04-8, FW 147.01 and CHEBI:86158 agree\
    \ with the supplied source form; no conversion to anhydrous mass is needed.\"\n\
    \  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '6 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 6/9 primary
    and 0/9 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17561
  - chebi26710
  - chebi32139
  - chebi34683
  - chebi50385
  - chebi86158
  details: 'Instance coverage on a 0–100 percent scale, denominator 9: primary 66.67%;
    secondary 0.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 7 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact named variant and single maintained contributor
  outcome: supported
  summary: BHIS_CaCl2, source accession and CultureMech:015494 agree. The generated
    ingredient block exactly matches its sole maintained owner; only generated provenance/history
    keys differ. The calcium supplement is calcium chloride dihydrate at 1 mM, not
    an anhydrous salt or a stock dose. Keep similarly named BHIS variants separate.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - owner-0
  - id-search
  - feba-main
  - history-detail
- assessment_id: ownership
  area: ownership
  topic: Maintained input and generated target
  outcome: supported
  summary: The normalized CultureBotHT record is the curation owner. Its names, concentrations,
    notes, classification and source metadata are already retained in the generated
    target. There is no current owner quantity repair to reapply or missing generated
    scientific block to reconstruct. Any later source/evidence curation belongs in
    that owner or its actual importer, followed by separately authorized regeneration.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - owner-0
  - history-detail
  - writer-0
  - writer-2
  - writer-3
- assessment_id: supplied-forms
  area: grounding
  topic: Source form and unmapped-material boundaries
  outcome: concern
  summary: The calcium supplement is calcium chloride dihydrate at 1 mM, not an anhydrous
    salt or a stock dose. All asserted CHEBI IDs have exact nonobsolete canonical
    labels and source-compatible CAS/form metadata. Calf brains, Beef heart and Proteose
    Peptone remain ungrounded complex materials; their printed masses must not be
    replaced by tissue equivalents. No asserted hydrate, stereochemistry or chemical
    identity mismatch was found in the inspected selected layers.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - feba-compounds
  - grounding-detail
  - chebi17561
  - chebi26710
  - chebi32139
  - chebi34683
  - chebi50385
  - chebi86158
- assessment_id: evidence
  area: evidence
  topic: Current source support and historical correspondence
  outcome: concern
  summary: Both local layers contain zero attached concentration evidence objects
    across 18 concentration instances. Current FEBA rows support the numbers and variant
    identity; September 2026 source bytes do not authenticate the March import. Earlier
    reports provide historical observations and source leads only.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - feba-main
  - feba-version
  - history-detail
  - culturebothtExactBHIS_CaCl2-attempt
- assessment_id: preparation
  area: completeness
  topic: Preparation, conditions and source-only quantity check
  outcome: unknown
  summary: Neither local layer supplies preparation, sterilization, water charge,
    measured final batch volume, pH, atmosphere, incubation temperature, storage or
    shelf life. The exact source block also supplies none of those values and refers
    to no stock mix. This is an unresolved protocol boundary, not permission to add
    a typical BHIS method, assume one litre of water, or transfer a neighboring variant
    protocol. Empty optional organism/application fields alone are not defects.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - owner-0
  - feba-main
  - quantity-inventory
- assessment_id: classification
  area: consistency
  topic: Complex broth classification and evidence limits
  outcome: supported
  summary: The source describes brain heart infusion salt broth and Minimal FALSE;
    tissue-derived ingredients and peptone support the local COMPLEX/UNDEFINED classification.
    LIQUID agrees with broth, with no agar row. The specialized filing does not assert
    a taxon. The source table is a formulation description, not an observed-growth
    experiment.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - owner-0
  - feba-main
  - feba-compounds
- assessment_id: relationships
  area: scope
  topic: Stocks, variants, taxonomy and graph scope
  outcome: not_applicable
  summary: Neither selected layer asserts a solution reference, inline variant, organism
    taxon, growth measurement, legacy MIM identifier or KG-Microbe match. No stock
    or comparative organism evidence is transferred from other BHIS records. A micromediaparam_legacy
    mapping-method note on disodium phosphate is provenance text, not an asserted
    legacy MIM identifier.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - record
  - owner-0
  - history-detail
  - grounding-detail
- assessment_id: completion
  area: completeness
  topic: Complete current formulation review with historical source gap
  outcome: concern
  summary: All 9 source concentrations and both local layers were assessed. Printed
    formula weights and CAS identifiers were examined as supplied-form metadata, not
    additional dosing instructions. No source-only preparation amount was found in
    the exact block. The current formulation comparison is complete; overall completion
    remains partial for the unavailable historical CultureBotHT source.
  target_ids:
  - CultureMech:015494
  evidence_ids:
  - quantity-inventory
  - grounding-detail
  - history-detail
  - culturebothtExactBHIS_CaCl2-attempt
findings:
- finding_id: f1
  issue_key: culturemech.015494.concentration-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported concentrations lack exact source links
  description: Both layers retain all 9 directly supported concentrations but attach
    no claim-level evidence. The generic CultureBotHT repository URL does not recover
    the exact formula/version, and current FEBA agreement cannot authenticate the
    March import.
  target_ids:
  - CultureMech:015494
  field_paths:
  - ingredients[*].concentration
  - references
  - sources
  evidence_ids:
  - feba-main
  - feba-header
  - feba-version
  - quantity-inventory
  - history-detail
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_cacl2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4.3 is normalized to minor because all 9 numerical values
    are supported by the exact current variant, but 18 local concentration instances
    lack claim-level provenance needed to reproduce that support. No wrong concentration
    is alleged. Historical import-time authentication is a separate unavailable check.
- finding_id: f2
  issue_key: culturemech.015494.grounding-coverage
  category: grounding
  severity: informational
  status: open
  certainty: confirmed
  title: Optional ingredient linkages remain incomplete
  description: Both layers have no secondary CHEBI-based MIM slots. Their complex-material
    rows remain ungrounded, with has_unmapped_ingredients retained. The asserted pure-reagent
    terms agree with the captured source forms.
  target_ids:
  - CultureMech:015494
  field_paths:
  - ingredients[*].term
  - ingredients[*].mediaingredientmech_chebi_term
  - data_quality_flags
  evidence_ids:
  - grounding-detail
  - mim
  - feba-compounds
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_cacl2.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.1
  native_severity: P4
  normalization_reason: 'P4.1 remains informational: zero optional secondary links
    reduces lookup coverage but does not invalidate an asserted identifier or contradict
    a supported source concentration. Missing primary identifiers are recorded explicitly
    rather than filled with guesses.'
actions:
- action_id: a1
  description: Attach the exact named FEBA rows, printed units and compound-form evidence
    in the maintained owner while retaining the current-versus-historical version
    distinction. Preserve every amount. Keep original CultureBotHT authentication
    explicitly unresolved until an exact historical source is recovered.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015494
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_cacl2.yaml
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
  description: Consider exact supplied-material linkage in a separate curation task.
    Preserve unresolved mixtures and the unmapped flag; add only independently verified
    identifiers, without substituting a pure molecule or anatomy term for an ingredient
    product.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015494
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/bhis_cacl2.yaml
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
- The exact public CultureBotHT media_yaml/BHIS_CaCl2.yaml request returned HTTP 404.
  Its March import-time bytes and correspondence were not authenticated. The current
  FEBA comparison passed independently; the historical source check remains unavailable
  and makes this review partial.
- The public CultureBotHT repository API returned HTTP 404. This is an access-scoped
  outcome, not proof that the repository or historical source never existed.
- The FEBA block is direct composition only. No dose, stock strength, density, final
  volume, pH or cultivation condition was inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-042
- generated-medium
```
