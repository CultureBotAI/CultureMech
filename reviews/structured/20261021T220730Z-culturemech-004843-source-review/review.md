# Source and formulation review: bacillus_thermoglucosidasius_medium (CultureMech:004843)

- Review: 20261021T220730Z-culturemech-004843-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T21:51:52Z
- Finished UTC: 2026-10-21T22:07:30.166864Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 305 primary supports six recipe mass numerals, soluble starch, 1000 mL water and final pH 7.0. All layers omit water and the soluble-starch qualifier; only the DSMZ owner retains the pH preparation instruction. Ten attached owner amount claims survive only as local derivative evidence because their cited historical API raw was not recovered. The generated target lacks those claims. This required historical authentication remains partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 386; batch 039 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-eight task batches contain 380 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 383 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004843 | data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml | generated | bacillus_thermoglucosidasius_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004843 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004843 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/386/strict.tsv |
| validate-terms | passed | True | CultureMech:004843 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004843 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:004843 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive305api | unavailable | False | CultureMech:004843 | The preserved mediadive305api request returned HTTP 503. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant. |
| Exact source content access: mediadive305api_retry | unavailable | False | CultureMech:004843 | The preserved mediadive305api_retry request returned HTTP 503. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant. |
| Exact source content access: komodo305detail | unavailable | False | CultureMech:004843 | The preserved komodo305detail request returned HTTP 403. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant. |
| Authenticate all ten owner amount claims against their original historical response | unavailable | True | CultureMech:004843 | The cited historical response ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2 is unrecovered within the bounded ignored-inclusive search. Current primary mass agreement and local report snippets do not authenticate its raw hash or provider normalization. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:004843.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:004843.

23 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Starch",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 1",
        "exact_source_quote": "Soluble starch 10.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The primary explicitly specifies soluble starch; the local generic name lacks that grade qualifier. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q2",
    "name": "Starch",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 1",
        "exact_source_quote": "Soluble starch 10.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The primary explicitly specifies soluble starch; the local generic name lacks that grade qualifier. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q3",
    "name": "Starch",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 1",
        "exact_source_quote": "Soluble starch 10.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The primary explicitly specifies soluble starch; the local generic name lacks that grade qualifier. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q4",
    "name": "Peptone",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 5,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 2",
        "exact_source_quote": "Peptone 5.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q5",
    "name": "Peptone",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 5,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 2",
        "exact_source_quote": "Peptone 5.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q6",
    "name": "Peptone",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 5,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 2",
        "exact_source_quote": "Peptone 5.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q7",
    "name": "Meat extract",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 3",
        "exact_source_quote": "Meat extract 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q8",
    "name": "Meat extract",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 3",
        "exact_source_quote": "Meat extract 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q9",
    "name": "Meat extract",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 3",
        "exact_source_quote": "Meat extract 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q10",
    "name": "Yeast extract",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 4",
        "exact_source_quote": "Yeast extract 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q11",
    "name": "Yeast extract",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 4",
        "exact_source_quote": "Yeast extract 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q12",
    "name": "Yeast extract",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 4",
        "exact_source_quote": "Yeast extract 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q13",
    "name": "KH2PO4",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 5",
        "exact_source_quote": "KH2PO4 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q14",
    "name": "KH2PO4",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 5",
        "exact_source_quote": "KH2PO4 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q15",
    "name": "KH2PO4",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 3,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 5",
        "exact_source_quote": "KH2PO4 3.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q16",
    "name": "Agar",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 30,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 6",
        "exact_source_quote": "Agar 30.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "There is no attached amount evidence at this field. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q17",
    "name": "Agar",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 30,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 6",
        "exact_source_quote": "Agar 30.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q18",
    "name": "Agar",
    "stage": "DSMZ 305 main recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_amount": 30,
      "source_unit": "g",
      "source_water_input_ml": 1000,
      "existing_unit": "G_PER_L",
      "normalization_status": "Preserve existing numeral pending exact denominator evidence; source batch grams are not a new measured final concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Composition table row 6",
        "exact_source_quote": "Agar 30.0 g",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The attached historical claim is preserved but not authenticated to its cited raw response. The source mass numeral agrees with the stored value. Its 1000 mL water input does not independently establish measured final volume or recover the missing historical provider denominator. No unsupported numerical correction is proposed."
  },
  {
    "decision_id": "q19",
    "name": "Distilled water",
    "stage": "Main recipe solvent input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Starch",
            "term": {
              "id": "CHEBI:28017",
              "label": "starch"
            },
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:28017",
              "label": "starch"
            }
          },
          {
            "preferred_term": "Peptone",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Meat extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Starch",
            "term": {
              "id": "CHEBI:28017",
              "label": "starch"
            },
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:28017",
              "label": "starch"
            }
          },
          {
            "preferred_term": "Peptone",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (Peptone) in MediaDive medium 305; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2. KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Meat extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Meat extract\",\n                        \"compound_id\": 2,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (Meat extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2. KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (Yeast extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2. KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
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
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.045,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 305; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2. KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 89.1981,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Agar) in MediaDive medium 305; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=30; check: 30 g * 1 g/g / (1000 ml / 1000 ml per L) = 30 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2. KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Starch",
            "term": {
              "id": "CHEBI:28017",
              "label": "starch"
            },
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:28017",
              "label": "starch"
            }
          },
          {
            "preferred_term": "Peptone",
            "concentration": {
              "value": "5",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (Peptone) in MediaDive medium 305; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2."
              }
            ]
          },
          {
            "preferred_term": "Meat extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Meat extract\",\n                        \"compound_id\": 2,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (Meat extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2."
              }
            ]
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "3",
              "unit": "G_PER_L"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (Yeast extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2."
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
              "value": "3",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.045,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 305; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2."
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/305",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 89.1981,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Agar) in MediaDive medium 305; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=30; check: 30 g * 1 g/g / (1000 ml / 1000 ml per L) = 30 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2."
              }
            ]
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 1000,
      "source_unit": "ml",
      "representation": "Preparation solvent input, not a water mass concentration"
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Final composition table row",
        "exact_source_quote": "Distilled water 1000.0 ml",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "Every layer omits this explicit source input. Preserve it with the recipe stage; do not convert it to grams or silently claim a measured final litre."
  },
  {
    "decision_id": "q20",
    "name": "Final pH",
    "stage": "Main medium adjustment",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0
      }
    ],
    "desired": {
      "value": 7.0
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Preparation sentence",
        "exact_source_quote": "Adjust final pH to 7.0.",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "All top-level values already agree. Ingredient amount evidence is not evidence for this distinct preparation field."
  },
  {
    "decision_id": "q21",
    "name": "Existing final pH instruction",
    "stage": "DSMZ owner preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust final pH to 7.0."
      }
    ],
    "desired": {
      "source_text": "Adjust final pH to 7.0."
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Preparation sentence",
        "exact_source_quote": "Adjust final pH to 7.0.",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "This exact instruction is already present in the DSMZ owner and must be retained; no missing-preparation finding applies to that owner."
  },
  {
    "decision_id": "q22",
    "name": "Missing final pH instruction",
    "stage": "Target and KOMODO owner preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "source_text": "Adjust final pH to 7.0."
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Preparation sentence",
        "exact_source_quote": "Adjust final pH to 7.0.",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The source instruction is absent in these two layers although both top-level pH values already exist. Do not infer titrant identity, concentration or volume."
  },
  {
    "decision_id": "q23",
    "name": "Unquantified preparation and cultivation conditions",
    "stage": "Source limits",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
        "field_path": "temperature_range",
        "stored": null
      }
    ],
    "desired": {
      "sterilization_temperature_or_duration": null,
      "incubation_temperature_or_duration": null,
      "pH_titrant_identity_strength_dose": null,
      "measured_final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Preparation sentence",
        "exact_source_quote": "Adjust final pH to 7.0.",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      },
      {
        "source_key": "dsmz305",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf",
        "source_locator": "Water input",
        "exact_source_quote": "Distilled water 1000.0 ml",
        "snapshot_sha256": "b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e",
        "parsed_text_sha256": "20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f"
      }
    ],
    "interpretation": "The exact primary provides no numerical sterilization cycle, growth temperature, titrant dose or independently measured final volume. The medium title and catalog oxygen field are not organism-specific evidence."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:004843.

3 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 3/6 primary and 3/6 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 6: primary 50.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:004843.

24 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accessions and relationship scope

identity: supported. Targets: CultureMech:004843.

KOMODO 305 maps directly to DSMZ 305, and both maintained paths and stable IDs resolve. This supports the base-source relationship independently of ingredient fingerprints; no historical raw equivalence or unobserved variant formulation is inferred.

### Source ingredient identity and grade

grounding: concern. Targets: CultureMech:004843.

CHEBI:63036 matches source KH2PO4. CHEBI:2509 represents agar as a mixture; no pure molecular formula or molar conversion is inferred. CHEBI:28017 matches the general starch class but does not preserve the source soluble-starch qualifier. Peptone, meat extract and yeast extract are complex mixtures without asserted single-chemical identifiers. Valid canonical labels and MIM membership are distinct from these source-form checks.

### Historical claims and generated lag

evidence: concern. Targets: CultureMech:004843.

The two owners each retain five amount claims; none is attached to starch. The target retains no ingredient evidence or source references. Catalog identity raw is authenticated, while all ten historical amount claims remain derivative-only and unverified against external raw. Current primary batch masses agree with their numerals but do not recover the historical per-litre declaration.

### Solvent and final pH instruction

completeness: concern. Targets: CultureMech:004843.

Every layer omits 1000 mL water; only the DSMZ owner retains the final pH instruction. All layers already store pH 7.0. Agar 30 g is printed without an optional qualification in this primary, supporting the existing solid formulation. No sterilization cycle or cultivation conditions are supplied.

### Classification and biological evidence

scope: supported. Targets: CultureMech:004843.

Peptone and extracts support an undefined complex medium. The explicit agar supports solid agar classification. No organism-specific growth, taxonomy or oxygen physiology is inferred from the title or the catalog Aerobic field.

## Findings

### f1: Water and preparation context are incomplete

major / open / confirmed; issue key: culturemech.004843.missing-water-and-preparation.

All layers omit the primary 1000 mL distilled water input. The target and KOMODO owner omit the final pH instruction retained by the DSMZ owner; top-level pH 7.0 is already present in every layer.

### f2: Historical amount claims cannot be raw-authenticated

major / open / confirmed; issue key: culturemech.004843.unrecovered-historical-amount-support.

Ten owner amount claims cite one historical response that remains unrecovered; their local report copies do not authenticate its source hash or denominator. The generated target omits those claims entirely. Current primary mass agreement supports scoped follow-up but not a verified historical-raw claim.

### f3: Starch grade qualifier is missing

minor / open / confirmed; issue key: culturemech.004843.lost-soluble-starch-qualifier.

Every layer uses the generic preferred name Starch, while the primary specifies Soluble starch. The general starch identifier is not proven wrong; it does not encode the source grade.

### f4: KOMODO history has malformed and timezone-naive timestamps

minor / open / confirmed; issue key: culturemech.004843.malformed-import-timestamps.

The target and KOMODO owner retain one malformed .fZ and one timezone-naive timestamp each. The DSMZ owner history is parseable.

## Recommended Actions And Acceptance Checks

### a1

Preserve the water input as preparation context and the exact pH instruction at the missing layers without inventing a measured final volume or titrant, then regenerate only after owner review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain original claims and recover the exact cited response or append accurately scoped new primary support. Keep historical normalization unresolved until directly supported, and assess propagation to the generated target without fabricating retrieval provenance.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the soluble qualifier in the maintained ingredient description with exact source evidence; retain the supported general class unless a more specific supported identifier is established.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve original events and append only independently supported timestamp clarification; do not invent precise times.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch039/386/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch039/386/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml:1:id: CultureMech:004843<br>./data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml:1:id: CultureMech:004843<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch039/source-preflight-bound/386/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 8 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf; Complete composition table and final pH instruction | supports | Six gram amounts and 1000 mL distilled water are recipe inputs, followed by final pH 7.0. Water is not a measured final-volume declaration. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 305 row, identity and DSMZ source URL only | supports | The exact accession maps to DSMZ 305. Catalog identity is authenticated separately from ingredient amounts, source-version equality and physiological oxygen requirements. |
| mediadive305api-attempt | https://mediadive.dsmz.de/rest/medium/305; Preserved exact public retrieval result | context_only | The preserved mediadive305api request returned HTTP 503. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant. |
| mediadive305api_retry-attempt | https://mediadive.dsmz.de/rest/medium/305; Preserved exact public retrieval result | context_only | The preserved mediadive305api_retry request returned HTTP 503. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant. |
| komodo305detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=305; Preserved exact public retrieval result | context_only | The preserved komodo305detail request returned HTTP 403. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch039/386/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:28017 resolves to starch. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28017": [{"label": "Starch", "match_type": "preferred_term", "identifier": "CHEBI:28017", "preferred_term": "Starch", "ontology_id": "CHEBI:28017", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml; data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.163264"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.163264"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml", "events": 7, "timestamp_issues": []}] |
| history-inventory | /private/tmp/culturemech-review-work-batch039/386/history-inventory.json; Ten exact owner amount claims, two scoped full historical reports and bounded raw-search provenance | context_only | The original response hash ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2 was not recovered in the recorded ignored-inclusive owned-checkout search. Local snippets and plans remain derivative. No universal absence claim is made. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current importer treats solvent rows separately and consumes provider normalization when supplied. The current merger checks encoded formulation compatibility and unions compatible scoped evidence. These mechanisms are context only; they do not establish the historical cause of these layer differences or authenticate missing API bytes. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current importer treats solvent rows separately and consumes provider normalization when supplied. The current merger checks encoded formulation compatibility and unions compatible scoped evidence. These mechanisms are context only; they do not establish the historical cause of these layer differences or authenticate missing API bytes. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current importer treats solvent rows separately and consumes provider normalization when supplied. The current merger checks encoded formulation compatibility and unions compatible scoped evidence. These mechanisms are context only; they do not establish the historical cause of these layer differences or authenticate missing API bytes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved mediadive305api request returned HTTP 503. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant.
- The preserved mediadive305api_retry request returned HTTP 503. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant.
- The preserved komodo305detail request returned HTTP 403. Current primary composition remains available. These optional live access attempts are separate from the required unavailable historical raw authentication; they establish no formula absence or unseen variant.
- Required historical amount authentication remains unavailable, so completion and coverage are partial. The bounded ignored-inclusive search did not recover the cited raw; it does not prove universal historical absence.
- Current primary mass numerals, catalog identity, historical derivative snippets and measured final concentrations are separate evidence claims. No source oxygen physiology, growth temperature, sterilization cycle or final volume is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T220730Z-culturemech-004843-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bacillus_thermoglucosidasius_medium (CultureMech:004843)'
started_at: '2026-10-21T21:51:52Z'
finished_at: '2026-10-21T22:07:30.166864Z'
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
summary: The exact DSMZ 305 primary supports six recipe mass numerals, soluble starch,
  1000 mL water and final pH 7.0. All layers omit water and the soluble-starch qualifier;
  only the DSMZ owner retains the pH preparation instruction. Ten attached owner amount
  claims survive only as local derivative evidence because their cited historical
  API raw was not recovered. The generated target lacks those claims. This required
  historical authentication remains partial.
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
  - path: data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
    sha256: d46c15bd7aa8d710a4b8f02cdf279ab88675e4aba30d91ddb5f910aac20da634
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    sha256: 29bc5283ec71ba403f856270b67fcc7bada5830cfd9257bcbddafafb2f6a8411
    role: context
  - path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
    sha256: b15fd95ca20cf646c278327caa83979be6bf615d5df0751bea43fd24a08b8fe7
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/inspected-candidate-context.json
    sha256: bea184ce1f011e5714cef082c0341aaf001d16024ef7935d004cbc8899f74fd5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/plan.json
    sha256: 5a48b07490ce656e22f5742a30b6c1bdae479f575388bea6551bad9ccdd051c0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml.md
    sha256: eb4b736de7ccf34b63e1991dc8eb3d3af14fdc356e47683ea25a6f82802782df
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/bacillus_thermoglucosidasius_medium.yaml.md
    sha256: 2be1cd570396c85c598e4ed1a8e064d18361d105d7558d750b004d748df9f818
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
  selection: Task review 386; batch 039 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-eight task batches
    contain 380 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 383 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004843
targets:
- target_id: CultureMech:004843
  path: data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  label: bacillus_thermoglucosidasius_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/386/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/386/strict.tsv"
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:004843
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
  - CultureMech:004843
- check_id: mediadive305api-source-access
  name: 'Exact source content access: mediadive305api'
  required: false
  status: unavailable
  summary: The preserved mediadive305api request returned HTTP 503. Current primary
    composition remains available. These optional live access attempts are separate
    from the required unavailable historical raw authentication; they establish no
    formula absence or unseen variant.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - mediadive305api-attempt
- check_id: mediadive305api_retry-source-access
  name: 'Exact source content access: mediadive305api_retry'
  required: false
  status: unavailable
  summary: The preserved mediadive305api_retry request returned HTTP 503. Current
    primary composition remains available. These optional live access attempts are
    separate from the required unavailable historical raw authentication; they establish
    no formula absence or unseen variant.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - mediadive305api_retry-attempt
- check_id: komodo305detail-source-access
  name: 'Exact source content access: komodo305detail'
  required: false
  status: unavailable
  summary: The preserved komodo305detail request returned HTTP 403. Current primary
    composition remains available. These optional live access attempts are separate
    from the required unavailable historical raw authentication; they establish no
    formula absence or unseen variant.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - komodo305detail-attempt
- check_id: historical-amount-raw-authentication
  name: Authenticate all ten owner amount claims against their original historical
    response
  required: true
  status: unavailable
  summary: The cited historical response ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2
    is unrecovered within the bounded ignored-inclusive search. Current primary mass
    agreement and local report snippets do not authenticate its raw hash or provider
    normalization.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - history-inventory
  - primary
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:28.244619Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch039/386/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:29.270701Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-039/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch039/386/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:30.546049Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T21:52:31.274853Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T21:58:11Z'
  support: supports
  summary: './data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml:1:id:
    CultureMech:004843

    ./data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml:1:id:
    CultureMech:004843

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/source-preflight-bound/386/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T21:58:11Z'
  support: supports
  summary: 8 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 093d995c4035ef9dd277775bd31dbf5a65df81dba004224e897b5f50f661b828
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf
  locator: Complete composition table and final pH instruction
  accessed_at: '2026-10-21T21:13:30.369067Z'
  support: supports
  summary: Six gram amounts and 1000 mL distilled water are recipe inputs, followed
    by final pH 7.0. Water is not a measured final-volume declaration.
  quote: 305. BACILLUS THERMOGLUCOSIDASIUS MEDIUM
  snapshot_sha256: b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 305 row, identity and DSMZ source URL only
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact accession maps to DSMZ 305. Catalog identity is authenticated
    separately from ingredient amounts, source-version equality and physiological
    oxygen requirements.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=305'\
    \ >305</a></TD>\n\t\t\t\t\t<TD>BACILLUS THERMOGLUCOSIDASIUS medium</TD>\n\t\t\t\
    \t\t<TD> 7.0</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\
    \t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive305api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/305
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:13:29.819219Z'
  support: context_only
  summary: The preserved mediadive305api request returned HTTP 503. Current primary
    composition remains available. These optional live access attempts are separate
    from the required unavailable historical raw authentication; they establish no
    formula absence or unseen variant.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive305api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/305
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:14:38.788843Z'
  support: context_only
  summary: The preserved mediadive305api_retry request returned HTTP 503. Current
    primary composition remains available. These optional live access attempts are
    separate from the required unavailable historical raw authentication; they establish
    no formula absence or unseen variant.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo305detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=305
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T21:13:29.547781Z'
  support: context_only
  summary: The preserved komodo305detail request returned HTTP 403. Current primary
    composition remains available. These optional live access attempts are separate
    from the required unavailable historical raw authentication; they establish no
    formula absence or unseen variant.
  snapshot_sha256: 92c874f3e50e1272cb3869855004a1996e48eb017d4aaa29c3149bc785bc7dc2
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/386/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 456c8c7f67eb23b4c9567ebc92a25b042f015ca7ffc4bbcb21076125feb31d65
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi28017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:42.748724Z'
  support: supports
  summary: CHEBI:28017 resolves to starch. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T21:58:11Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:2509":
    [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:28017": [{"label": "Starch", "match_type": "preferred_term",
    "identifier": "CHEBI:28017", "preferred_term": "Starch", "ontology_id": "CHEBI:28017",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml;
    data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:04.163264"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:04.163264"}]}, {"input": "data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch039/386/history-inventory.json
  locator: Ten exact owner amount claims, two scoped full historical reports and bounded
    raw-search provenance
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: The original response hash ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2
    was not recovered in the recorded ignored-inclusive owned-checkout search. Local
    snippets and plans remain derivative. No universal absence claim is made.
  snapshot_sha256: f3ef7324b51f7819686be7341178b07d4908162446606560a8e3936462fb0682
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: The current importer treats solvent rows separately and consumes provider
    normalization when supplied. The current merger checks encoded formulation compatibility
    and unions compatible scoped evidence. These mechanisms are context only; they
    do not establish the historical cause of these layer differences or authenticate
    missing API bytes.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: The current importer treats solvent rows separately and consumes provider
    normalization when supplied. The current merger checks encoded formulation compatibility
    and unions compatible scoped evidence. These mechanisms are context only; they
    do not establish the historical cause of these layer differences or authenticate
    missing API bytes.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T21:58:11Z'
  support: context_only
  summary: The current importer treats solvent rows separately and consumes provider
    normalization when supplied. The current merger checks encoded formulation compatibility
    and unions compatible scoped evidence. These mechanisms are context only; they
    do not establish the historical cause of these layer differences or authenticate
    missing API bytes.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 23 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Starch\",\n    \"\
    stage\": \"DSMZ 305 main recipe\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 10,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 1\",\n        \"exact_source_quote\"\
    : \"Soluble starch 10.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The primary explicitly specifies soluble starch; the local generic\
    \ name lacks that grade qualifier. The source mass numeral agrees with the stored\
    \ value. Its 1000 mL water input does not independently establish measured final\
    \ volume or recover the missing historical provider denominator. No unsupported\
    \ numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\": \"q2\"\
    ,\n    \"name\": \"Starch\",\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 10,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 1\",\n        \"exact_source_quote\"\
    : \"Soluble starch 10.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The primary explicitly specifies soluble starch; the local generic\
    \ name lacks that grade qualifier. The source mass numeral agrees with the stored\
    \ value. Its 1000 mL water input does not independently establish measured final\
    \ volume or recover the missing historical provider denominator. No unsupported\
    \ numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\": \"q3\"\
    ,\n    \"name\": \"Starch\",\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 10,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 1\",\n        \"exact_source_quote\"\
    : \"Soluble starch 10.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The primary explicitly specifies soluble starch; the local generic\
    \ name lacks that grade qualifier. The source mass numeral agrees with the stored\
    \ value. Its 1000 mL water input does not independently establish measured final\
    \ volume or recover the missing historical provider denominator. No unsupported\
    \ numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\": \"q4\"\
    ,\n    \"name\": \"Peptone\",\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"\
    decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   }\n    ],\n    \"desired\": {\n      \"source_amount\": 5,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 2\",\n        \"exact_source_quote\"\
    : \"Peptone 5.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The source mass numeral agrees with the stored value. Its 1000\
    \ mL water input does not independently establish measured final volume or recover\
    \ the missing historical provider denominator. No unsupported numerical correction\
    \ is proposed.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"name\": \"Peptone\"\
    ,\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 5,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 2\",\n        \"exact_source_quote\"\
    : \"Peptone 5.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"name\": \"Peptone\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 5,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 2\",\n        \"exact_source_quote\"\
    : \"Peptone 5.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"name\": \"Meat extract\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 3\",\n        \"exact_source_quote\"\
    : \"Meat extract 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The source mass numeral agrees with the stored value. Its 1000\
    \ mL water input does not independently establish measured final volume or recover\
    \ the missing historical provider denominator. No unsupported numerical correction\
    \ is proposed.\"\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"name\": \"Meat\
    \ extract\",\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 3\",\n        \"exact_source_quote\"\
    : \"Meat extract 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"name\": \"Meat extract\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 3\",\n        \"exact_source_quote\"\
    : \"Meat extract 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 4\",\n        \"exact_source_quote\"\
    : \"Yeast extract 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The source mass numeral agrees with the stored value. Its 1000\
    \ mL water input does not independently establish measured final volume or recover\
    \ the missing historical provider denominator. No unsupported numerical correction\
    \ is proposed.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"name\": \"Yeast\
    \ extract\",\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 4\",\n        \"exact_source_quote\"\
    : \"Yeast extract 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 4\",\n        \"exact_source_quote\"\
    : \"Yeast extract 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 5\",\n        \"exact_source_quote\"\
    : \"KH2PO4 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The source mass numeral agrees with the stored value. Its 1000\
    \ mL water input does not independently establish measured final volume or recover\
    \ the missing historical provider denominator. No unsupported numerical correction\
    \ is proposed.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"name\": \"KH2PO4\"\
    ,\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 5\",\n        \"exact_source_quote\"\
    : \"KH2PO4 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"DSMZ 305 main recipe\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 3,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 5\",\n        \"exact_source_quote\"\
    : \"KH2PO4 3.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"name\": \"Agar\",\n    \"stage\": \"DSMZ 305 main recipe\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 30,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 6\",\n        \"exact_source_quote\"\
    : \"Agar 30.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"There is no attached amount evidence\
    \ at this field. The source mass numeral agrees with the stored value. Its 1000\
    \ mL water input does not independently establish measured final volume or recover\
    \ the missing historical provider denominator. No unsupported numerical correction\
    \ is proposed.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"name\": \"Agar\"\
    ,\n    \"stage\": \"DSMZ 305 main recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 30,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 6\",\n        \"exact_source_quote\"\
    : \"Agar 30.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"name\": \"Agar\",\n    \"stage\": \"DSMZ 305 main recipe\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_amount\": 30,\n      \"source_unit\"\
    : \"g\",\n      \"source_water_input_ml\": 1000,\n      \"existing_unit\": \"\
    G_PER_L\",\n      \"normalization_status\": \"Preserve existing numeral pending\
    \ exact denominator evidence; source batch grams are not a new measured final\
    \ concentration\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Composition table row 6\",\n        \"exact_source_quote\"\
    : \"Agar 30.0 g\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The attached historical claim is\
    \ preserved but not authenticated to its cited raw response. The source mass numeral\
    \ agrees with the stored value. Its 1000 mL water input does not independently\
    \ establish measured final volume or recover the missing historical provider denominator.\
    \ No unsupported numerical correction is proposed.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"name\": \"Distilled water\",\n    \"stage\": \"Main recipe solvent\
    \ input\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Starch\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:28017\",\n              \"label\": \"starch\"\n \
    \           },\n            \"concentration\": {\n              \"value\": \"\
    10\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:28017\",\n              \"label\": \"starch\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Peptone\",\n            \"concentration\": {\n              \"value\": \"5\",\n\
    \              \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"Meat extract\",\n            \"concentration\"\
    : {\n              \"value\": \"3\",\n              \"unit\": \"G_PER_L\"\n  \
    \          }\n          },\n          {\n            \"preferred_term\": \"Yeast\
    \ extract\",\n            \"concentration\": {\n              \"value\": \"3\"\
    ,\n              \"unit\": \"G_PER_L\"\n            }\n          },\n        \
    \  {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"3\",\n              \"unit\": \"G_PER_L\"\n            },\n  \
    \          \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            }\n\
    \          },\n          {\n            \"preferred_term\": \"Agar\",\n      \
    \      \"term\": {\n              \"id\": \"CHEBI:2509\",\n              \"label\"\
    : \"agar\"\n            },\n            \"concentration\": {\n              \"\
    value\": \"30\",\n              \"unit\": \"G_PER_L\"\n            },\n      \
    \      \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\"\
    ,\n              \"label\": \"agar\"\n            }\n          }\n        ]\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Starch\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:28017\",\n              \"label\": \"starch\"\n \
    \           },\n            \"concentration\": {\n              \"value\": \"\
    10\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:28017\",\n              \"label\": \"starch\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Peptone\",\n            \"concentration\": {\n              \"value\": \"5\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"evidence\"\
    : [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"Peptone\\\",\\n                        \\\"compound_id\\\
    \": 1,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n          \
    \      \"explanation\": \"Concentration evidence for ingredients[1].concentration\
    \ (Peptone) in MediaDive medium 305; locator=$.data.solutions[0].recipe[1]. Provider\
    \ explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00;\
    \ response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\
    \ KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Meat extract\",\n            \"concentration\": {\n              \"value\"\
    : \"3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"Meat extract\\\",\\n                        \\\"compound_id\\\
    \": 2,\\n                        \\\"amount\\\": 3,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n          \
    \      \"explanation\": \"Concentration evidence for ingredients[2].concentration\
    \ (Meat extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[2].\
    \ Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 3 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\
    \ KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n         \
    \       \"explanation\": \"Concentration evidence for ingredients[3].concentration\
    \ (Yeast extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[3].\
    \ Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 3 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\
    \ KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"3\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 22.045,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 305;\
    \ locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=3; check:\
    \ 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\
    \ KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"30\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/305\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 6,\\n                        \\\"compound\\\": \\\"Agar\\\"\
    ,\\n                        \\\"compound_id\\\": 3,\\n                       \
    \ \\\"amount\\\": 30,\\n                        \\\"unit\\\": \\\"g\\\",\\n  \
    \                      \\\"g_l\\\": 30,\\n                        \\\"mmol_l\\\
    \": 89.1981,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[5].concentration\
    \ (Agar) in MediaDive medium 305; locator=$.data.solutions[0].recipe[5]. Provider\
    \ explicitly reports g_l=30; check: 30 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 30 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\
    \ KOMODO accession 305 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Starch\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:28017\",\n              \"label\": \"starch\"\n \
    \           },\n            \"concentration\": {\n              \"value\": \"\
    10\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:28017\",\n              \"label\": \"starch\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Peptone\",\n            \"concentration\": {\n              \"value\": \"5\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"evidence\"\
    : [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"Peptone\\\",\\n                        \\\"compound_id\\\
    \": 1,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n          \
    \      \"explanation\": \"Concentration evidence for ingredients[1].concentration\
    \ (Peptone) in MediaDive medium 305; locator=$.data.solutions[0].recipe[1]. Provider\
    \ explicitly reports g_l=5; check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00;\
    \ response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Meat extract\",\n            \"concentration\": {\n              \"value\"\
    : \"3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"Meat extract\\\",\\n                        \\\"compound_id\\\
    \": 2,\\n                        \\\"amount\\\": 3,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n          \
    \      \"explanation\": \"Concentration evidence for ingredients[2].concentration\
    \ (Meat extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[2].\
    \ Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 3 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"3\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    evidence\": [\n              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n         \
    \       \"explanation\": \"Concentration evidence for ingredients[3].concentration\
    \ (Yeast extract) in MediaDive medium 305; locator=$.data.solutions[0].recipe[3].\
    \ Provider explicitly reports g_l=3; check: 3 g * 1 g/g / (1000 ml / 1000 ml per\
    \ L) = 3 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"3\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/305\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 22.045,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n                \"explanation\": \"Concentration\
    \ evidence for ingredients[4].concentration (KH2PO4) in MediaDive medium 305;\
    \ locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=3; check:\
    \ 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L. This supports the provider-declared\
    \ main-recipe concentration, not an independently measured final volume, a stock\
    \ composition, or a downstream assay dilution. Water alone does not establish\
    \ final volume. Exact source ingredient labels/forms are matched; secondary ontology\
    \ mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume\
    \ (ml): 1000. Retrieved 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"30\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/305\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 6,\\n                        \\\"compound\\\": \\\"Agar\\\"\
    ,\\n                        \\\"compound_id\\\": 3,\\n                       \
    \ \\\"amount\\\": 30,\\n                        \\\"unit\\\": \\\"g\\\",\\n  \
    \                      \\\"g_l\\\": 30,\\n                        \\\"mmol_l\\\
    \": 89.1981,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[5].concentration\
    \ (Agar) in MediaDive medium 305; locator=$.data.solutions[0].recipe[5]. Provider\
    \ explicitly reports g_l=30; check: 30 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 30 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T10:45:05.165391+00:00; response SHA256=ff4b9cd48f0fe635bea9539bfffc3deab0ad83a20fc6ddd4f4c45490f4711ab2.\"\
    \n              }\n            ]\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 1000,\n      \"source_unit\": \"ml\"\
    ,\n      \"representation\": \"Preparation solvent input, not a water mass concentration\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz305\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Final composition table row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.0 ml\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"Every layer omits this explicit source\
    \ input. Preserve it with the recipe stage; do not convert it to grams or silently\
    \ claim a measured final litre.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n\
    \    \"name\": \"Final pH\",\n    \"stage\": \"Main medium adjustment\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0\n      }\n \
    \   ],\n    \"desired\": {\n      \"value\": 7.0\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz305\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\",\n        \"\
    source_locator\": \"Preparation sentence\",\n        \"exact_source_quote\": \"\
    Adjust final pH to 7.0.\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"All top-level values already agree.\
    \ Ingredient amount evidence is not evidence for this distinct preparation field.\"\
    \n  },\n  {\n    \"decision_id\": \"q21\",\n    \"name\": \"Existing final pH\
    \ instruction\",\n    \"stage\": \"DSMZ owner preparation\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\",\n \
    \       \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust final pH to 7.0.\"\n      }\n    ],\n    \"desired\": {\n      \"source_text\"\
    : \"Adjust final pH to 7.0.\"\n    },\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust final pH to 7.0.\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact instruction is already\
    \ present in the DSMZ owner and must be retained; no missing-preparation finding\
    \ applies to that owner.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"name\"\
    : \"Missing final pH instruction\",\n    \"stage\": \"Target and KOMODO owner\
    \ preparation\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_text\": \"Adjust final pH\
    \ to 7.0.\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz305\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\"\
    ,\n        \"source_locator\": \"Preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust final pH to 7.0.\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The source instruction is absent\
    \ in these two layers although both top-level pH values already exist. Do not\
    \ infer titrant identity, concentration or volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"name\": \"Unquantified preparation and cultivation conditions\"\
    ,\n    \"stage\": \"Source limits\",\n    \"decision\": \"not_quantified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BACILLUS_THERMOGLUCOSIDASIUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"sterilization_temperature_or_duration\"\
    : null,\n      \"incubation_temperature_or_duration\": null,\n      \"pH_titrant_identity_strength_dose\"\
    : null,\n      \"measured_final_volume\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz305\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\",\n        \"\
    source_locator\": \"Preparation sentence\",\n        \"exact_source_quote\": \"\
    Adjust final pH to 7.0.\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      },\n      {\n        \"source_key\": \"dsmz305\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium305.pdf\",\n    \
    \    \"source_locator\": \"Water input\",\n        \"exact_source_quote\": \"\
    Distilled water 1000.0 ml\",\n        \"snapshot_sha256\": \"b0122dc636a22ba7a88b77cd4d75100ba9f30428ffcf47b89e1eddf1c060509e\"\
    ,\n        \"parsed_text_sha256\": \"20242db62d5a4de31f7827b7ae84e3b7d2cde8d091dbad1d0d01f4ee7933769f\"\
    \n      }\n    ],\n    \"interpretation\": \"The exact primary provides no numerical\
    \ sterilization cycle, growth temperature, titrant dose or independently measured\
    \ final volume. The medium title and catalog oxygen field are not organism-specific\
    \ evidence.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '3 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 3/6 primary
    and 3/6 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi2509
  - chebi28017
  - chebi63036
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 50.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
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
  - CultureMech:004843
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Exact accessions and relationship scope
  outcome: supported
  summary: KOMODO 305 maps directly to DSMZ 305, and both maintained paths and stable
    IDs resolve. This supports the base-source relationship independently of ingredient
    fingerprints; no historical raw equivalence or unobserved variant formulation
    is inferred.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - primary
  - catalog
  - record
  - owner-0
  - owner-1
- assessment_id: forms
  area: grounding
  topic: Source ingredient identity and grade
  outcome: concern
  summary: CHEBI:63036 matches source KH2PO4. CHEBI:2509 represents agar as a mixture;
    no pure molecular formula or molar conversion is inferred. CHEBI:28017 matches
    the general starch class but does not preserve the source soluble-starch qualifier.
    Peptone, meat extract and yeast extract are complex mixtures without asserted
    single-chemical identifiers. Valid canonical labels and MIM membership are distinct
    from these source-form checks.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - primary
  - chebi63036
  - chebi2509
  - chebi28017
  - record
- assessment_id: historical-evidence
  area: evidence
  topic: Historical claims and generated lag
  outcome: concern
  summary: The two owners each retain five amount claims; none is attached to starch.
    The target retains no ingredient evidence or source references. Catalog identity
    raw is authenticated, while all ten historical amount claims remain derivative-only
    and unverified against external raw. Current primary batch masses agree with their
    numerals but do not recover the historical per-litre declaration.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - history-inventory
  - catalog
  - primary
  - record
  - owner-0
  - owner-1
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Solvent and final pH instruction
  outcome: concern
  summary: Every layer omits 1000 mL water; only the DSMZ owner retains the final
    pH instruction. All layers already store pH 7.0. Agar 30 g is printed without
    an optional qualification in this primary, supporting the existing solid formulation.
    No sterilization cycle or cultivation conditions are supplied.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - primary
  - quantity-inventory
  - owner-1
- assessment_id: biological-scope
  area: scope
  topic: Classification and biological evidence
  outcome: supported
  summary: Peptone and extracts support an undefined complex medium. The explicit
    agar supports solid agar classification. No organism-specific growth, taxonomy
    or oxygen physiology is inferred from the title or the catalog Aerobic field.
  target_ids:
  - CultureMech:004843
  evidence_ids:
  - primary
  - catalog
  - record
findings:
- finding_id: f1
  issue_key: culturemech.004843.missing-water-and-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Water and preparation context are incomplete
  description: All layers omit the primary 1000 mL distilled water input. The target
    and KOMODO owner omit the final pH instruction retained by the DSMZ owner; top-level
    pH 7.0 is already present in every layer.
  target_ids:
  - CultureMech:004843
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
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
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
  issue_key: culturemech.004843.unrecovered-historical-amount-support
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Historical amount claims cannot be raw-authenticated
  description: Ten owner amount claims cite one historical response that remains unrecovered;
    their local report copies do not authenticate its source hash or denominator.
    The generated target omits those claims entirely. Current primary mass agreement
    supports scoped follow-up but not a verified historical-raw claim.
  target_ids:
  - CultureMech:004843
  field_paths:
  - ingredients[*].evidence
  - references
  - curation_history
  evidence_ids:
  - primary
  - history-inventory
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
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
  issue_key: culturemech.004843.lost-soluble-starch-qualifier
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Starch grade qualifier is missing
  description: Every layer uses the generic preferred name Starch, while the primary
    specifies Soluble starch. The general starch identifier is not proven wrong; it
    does not encode the source grade.
  target_ids:
  - CultureMech:004843
  field_paths:
  - ingredients[0].preferred_term
  - ingredients[0].notes
  evidence_ids:
  - primary
  - chebi28017
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.004843.malformed-import-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO history has malformed and timezone-naive timestamps
  description: The target and KOMODO owner retain one malformed .fZ and one timezone-naive
    timestamp each. The DSMZ owner history is parseable.
  target_ids:
  - CultureMech:004843
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
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
  description: Preserve the water input as preparation context and the exact pH instruction
    at the missing layers without inventing a measured final volume or titrant, then
    regenerate only after owner review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004843
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
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
  description: Retain original claims and recover the exact cited response or append
    accurately scoped new primary support. Keep historical normalization unresolved
    until directly supported, and assess propagation to the generated target without
    fabricating retrieval provenance.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004843
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
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
  description: Preserve the soluble qualifier in the maintained ingredient description
    with exact source evidence; retain the supported general class unless a more specific
    supported identifier is established.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004843
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml
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
  description: Preserve original events and append only independently supported timestamp
    clarification; do not invent precise times.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004843
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml
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
- The preserved mediadive305api request returned HTTP 503. Current primary composition
  remains available. These optional live access attempts are separate from the required
  unavailable historical raw authentication; they establish no formula absence or
  unseen variant.
- The preserved mediadive305api_retry request returned HTTP 503. Current primary composition
  remains available. These optional live access attempts are separate from the required
  unavailable historical raw authentication; they establish no formula absence or
  unseen variant.
- The preserved komodo305detail request returned HTTP 403. Current primary composition
  remains available. These optional live access attempts are separate from the required
  unavailable historical raw authentication; they establish no formula absence or
  unseen variant.
- Required historical amount authentication remains unavailable, so completion and
  coverage are partial. The bounded ignored-inclusive search did not recover the cited
  raw; it does not prove universal historical absence.
- Current primary mass numerals, catalog identity, historical derivative snippets
  and measured final concentrations are separate evidence claims. No source oxygen
  physiology, growth temperature, sterilization cycle or final volume is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-039
- generated-medium
```
